import argparse
import json
import os
import sys
from collections import defaultdict
from typing import Dict, Iterable, List, Optional, Tuple

try:
    from clang.cindex import Config, CursorKind, Index, StorageClass, TranslationUnit
except Exception as exc:  # pragma: no cover - runtime dependency check
    print("ERROR: clang Python bindings are required. Try: pip install clang", file=sys.stderr)
    print(f"Details: {exc}", file=sys.stderr)
    sys.exit(1)


TARGET_DIRS = ["db", "table", "util", "include"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect testable C++ methods/functions using libclang AST."
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Project root. Defaults to repository root (parent of this script).",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Output directory. Defaults to collection/ next to this script.",
    )
    parser.add_argument(
        "--compile-commands",
        default=None,
        help="Path to compile_commands.json. Auto-detected if omitted.",
    )
    return parser.parse_args()


def repo_root(script_path: str, override: Optional[str]) -> str:
    if override:
        return os.path.abspath(override)
    return os.path.abspath(os.path.join(os.path.dirname(script_path), ".."))


def output_dir(script_path: str, override: Optional[str]) -> str:
    if override:
        return os.path.abspath(override)
    return os.path.abspath(os.path.dirname(script_path))


def find_compile_commands(root: str, override: Optional[str]) -> Optional[str]:
    if override:
        if os.path.isfile(override):
            return os.path.abspath(override)
        return None

    candidates = [
        os.path.join(root, "build", "compile_commands.json"),
        os.path.join(root, "build-cov", "compile_commands.json"),
        os.path.join(root, "cmake-build-debug", "compile_commands.json"),
        os.path.join(root, "cmake-build-release", "compile_commands.json"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return os.path.abspath(path)
    return None


def load_compile_commands(path: Optional[str]) -> Tuple[Dict[str, List[str]], List[str]]:
    if not path:
        return {}, []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    file_args: Dict[str, List[str]] = {}
    common_args: List[str] = []

    for entry in data:
        file_path = os.path.abspath(entry.get("file", ""))
        args = entry.get("arguments")
        if not args:
            command = entry.get("command", "")
            args = command.split()
        if not args:
            continue
        cleaned = sanitize_args(args)
        if file_path:
            file_args[file_path] = cleaned
        if not common_args:
            common_args = cleaned[:]

    return file_args, common_args


def sanitize_args(args: Iterable[str]) -> List[str]:
    cleaned: List[str] = []
    skip_next = False
    for arg in args:
        if skip_next:
            skip_next = False
            continue
        if arg in {"-c", "-o"}:
            skip_next = True
            continue
        if arg.startswith("-o"):
            continue
        if arg == "-Winvalid-pch":
            continue
        cleaned.append(arg)
    return cleaned


def ensure_libclang_configured() -> None:
    libclang_path = os.environ.get("LIBCLANG_PATH")
    libclang_file = os.environ.get("LIBCLANG_FILE")
    if libclang_file:
        Config.set_library_file(libclang_file)
    elif libclang_path:
        Config.set_library_path(libclang_path)


def discover_files(root: str) -> List[str]:
    files: List[str] = []
    for target_dir in TARGET_DIRS:
        abs_dir = os.path.join(root, target_dir)
        if not os.path.isdir(abs_dir):
            continue
        for dirpath, _, filenames in os.walk(abs_dir):
            for filename in filenames:
                if filename.endswith(".cc") or filename.endswith(".h"):
                    files.append(os.path.join(dirpath, filename))
    return sorted(files)


def is_function_cursor(cursor_kind: CursorKind) -> bool:
    return cursor_kind in {
        CursorKind.FUNCTION_DECL,
        CursorKind.FUNCTION_TEMPLATE,
        CursorKind.CXX_METHOD,
        CursorKind.CONVERSION_FUNCTION,
    }


def is_constructor_or_destructor(cursor_kind: CursorKind) -> bool:
    return cursor_kind in {
        CursorKind.CONSTRUCTOR,
        CursorKind.DESTRUCTOR,
    }


def namespace_chain(cursor) -> List[str]:
    names: List[str] = []
    parent = cursor.semantic_parent
    while parent is not None:
        if parent.kind == CursorKind.NAMESPACE:
            if parent.spelling:
                names.append(parent.spelling)
        parent = parent.semantic_parent
    return list(reversed(names))


def class_chain(cursor) -> List[str]:
    names: List[str] = []
    parent = cursor.semantic_parent
    while parent is not None:
        if parent.kind in {CursorKind.CLASS_DECL, CursorKind.STRUCT_DECL}:
            if parent.spelling:
                names.append(parent.spelling)
        parent = parent.semantic_parent
    return list(reversed(names))


def is_in_anonymous_namespace(cursor) -> bool:
    parent = cursor.semantic_parent
    while parent is not None:
        if parent.kind == CursorKind.NAMESPACE and parent.spelling == "":
            return True
        parent = parent.semantic_parent
    return False


def build_signature(return_type: str, qualified_name: str, params: str) -> str:
    return f"{return_type} {qualified_name}({params})"


def calculate_complexity(param_count: int) -> str:
    if param_count <= 2:
        return "simple"
    if param_count <= 4:
        return "medium"
    return "complex"


def categorize(cursor, has_namespace: bool, is_file_scope: bool) -> str:
    if cursor.kind == CursorKind.CXX_METHOD:
        return "类方法"
    if is_file_scope:
        return "文件作用域函数（静态函数/匿名命名空间）"
    if has_namespace:
        return "命名空间函数"
    return "全局函数（无命名空间）"


def cursor_params(cursor) -> Tuple[str, int]:
    params: List[str] = []
    for arg in cursor.get_arguments():
        param = arg.type.spelling
        if arg.spelling:
            param = f"{param} {arg.spelling}"
        params.append(param)
    if not params:
        return "无参数", 0
    return ", ".join(params), len(params)


def parse_translation_unit(index: Index, file_path: str, args: List[str]) -> TranslationUnit:
    return index.parse(
        file_path,
        args=args,
        options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
    )


def collect_functions(
    index: Index,
    file_path: str,
    args: List[str],
    root: str,
) -> List[Dict[str, object]]:
    tu = parse_translation_unit(index, file_path, args)
    functions: List[Dict[str, object]] = []
    seen = set()

    for cursor in tu.cursor.walk_preorder():
        if not cursor.location.file:
            continue
        if os.path.abspath(cursor.location.file.name) != os.path.abspath(file_path):
            continue
        if is_constructor_or_destructor(cursor.kind):
            continue
        if not is_function_cursor(cursor.kind):
            continue
        if not cursor.is_definition():
            continue

        ns_chain = namespace_chain(cursor)
        class_names = class_chain(cursor)
        qualified_parts = ns_chain + class_names + [cursor.spelling]
        qualified_name = "::".join([p for p in qualified_parts if p])
        return_type = cursor.result_type.spelling
        params_str, param_count = cursor_params(cursor)
        signature = build_signature(return_type, qualified_name, params_str)
        location = cursor.location
        is_static = cursor.storage_class == StorageClass.STATIC
        is_file_scope = is_static or is_in_anonymous_namespace(cursor)
        category = categorize(cursor, bool(ns_chain), is_file_scope)

        unique_key = (qualified_name, location.line, location.column)
        if unique_key in seen:
            continue
        seen.add(unique_key)

        functions.append(
            {
                "name": cursor.spelling,
                "qualified_name": qualified_name,
                "return_type": return_type,
                "params": params_str,
                "signature": signature,
                "complexity": calculate_complexity(param_count),
                "category": category,
                "class": "::".join(class_names) if class_names else "",
                "namespace": "::".join(ns_chain) if ns_chain else "",
                "is_member_method": cursor.kind == CursorKind.CXX_METHOD,
                "is_static": is_static,
                "is_file_scope": is_file_scope,
                "line": location.line,
                "column": location.column,
                "file_path": os.path.relpath(file_path, root),
            }
        )

    return functions


def ensure_args_for_header(args: List[str]) -> List[str]:
    args = list(args)
    if "-x" not in args:
        args = ["-x", "c++"] + args
    if not any(arg.startswith("-std=") for arg in args):
        args.append("-std=c++11")
    return args


def write_jsonl(records: List[Dict[str, object]], out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        for index, record in enumerate(records, 1):
            namespace = record["namespace"]
            class_name = record["class"]
            method_name = record["name"]

            # Normalize for downstream C++ generator:
            # - Member methods need fully-qualified class names (namespace::Class).
            # - Free functions should include namespace in the method name.
            qualified_class = class_name
            if class_name and namespace:
                qualified_class = f"{namespace}::{class_name}"

            qualified_method = method_name
            if not class_name and namespace:
                qualified_method = f"{namespace}::{method_name}"

            line = {
                "index": index,
                "category": record["category"],
                "class": qualified_class,
                "namespace": namespace,
                "method": qualified_method,
                "full_signature": record["signature"],
                "return_type": record["return_type"],
                "params": record["params"],
                "is_member_method": record["is_member_method"],
                "is_static": record["is_static"],
                "is_file_scope": record["is_file_scope"],
                "file_path": record["file_path"],
                "line": record["line"],
            }
            f.write(json.dumps(line, ensure_ascii=False) + "\n")


def write_markdown(file_path: str, funcs: List[Dict[str, object]], out_dir: str) -> None:
    if not funcs:
        return

    total_funcs = len(funcs)
    complexity_counts = {"simple": 0, "medium": 0, "complex": 0}
    for func in funcs:
        complexity_counts[func["complexity"]] += 1

    safe_name = file_path.replace("/", "_").replace(".", "_")
    md_path = os.path.join(out_dir, f"{safe_name}_methods.md")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# leveldb 项目 - `{file_path}` 可测试方法列表\n\n")
        f.write("## 🔍 收集规则\n\n")
        f.write(f"本报告收集了 `{file_path}` 文件中所有公共方法、命名空间函数及文件作用域函数。\n\n")

        f.write("## 统计概览\n\n")
        f.write("| 指标 | 数值 |\n")
        f.write("|------|------|\n")
        f.write(f"| **总方法 (不含构造器/析构器)** | {total_funcs} |\n\n")

        f.write("### 复杂度分布\n\n")
        f.write("| 复杂度 | 数量 | 占比 |\n")
        f.write("|--------|------|------|\n")
        for comp, count in complexity_counts.items():
            pct = (count / total_funcs * 100) if total_funcs > 0 else 0
            f.write(f"| {comp} | {count} | {pct:.1f}% |\n")
        f.write("\n---\n\n")

        by_category: Dict[str, List[Dict[str, object]]] = defaultdict(list)
        for func in funcs:
            by_category[func["category"]].append(func)

        for category in [
            "类方法",
            "命名空间函数",
            "全局函数（无命名空间）",
            "文件作用域函数（静态函数/匿名命名空间）",
        ]:
            cat_funcs = by_category.get(category)
            if not cat_funcs:
                continue
            f.write(f"## 📦 {category}\n\n")
            f.write(f"**包含方法数**: {len(cat_funcs)}\n\n")
            f.write("| # | 方法名 | 返回类型 | 参数 | 完整签名 | 复杂度 | 特征 |\n")
            f.write("|---|--------|----------|------|----------|--------|------|\n")

            for idx, func in enumerate(cat_funcs, 1):
                sig = func["signature"].replace("|", "\\|")
                ret = func["return_type"].replace("|", "\\|")
                params = func["params"].replace("|", "\\|")
                name = func["name"]
                f.write(
                    f"| {idx} | `{name}` | `{ret}` | `{params}` | `{sig}` | {func['complexity']} | 有逻辑 |\n"
                )
            f.write("\n---\n\n")


def write_summary(report_path: str, all_funcs: List[Dict[str, object]]) -> None:
    total_funcs = len(all_funcs)
    complexity_counts = {"simple": 0, "medium": 0, "complex": 0}
    for func in all_funcs:
        complexity_counts[func["complexity"]] += 1

    by_file: Dict[str, int] = defaultdict(int)
    for func in all_funcs:
        by_file[func["file_path"]] += 1

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# leveldb 项目-可测试方法列表（libclang AST）\n\n")
        f.write("## 🔍 收集规则\n\n")
        f.write("本报告收集了项目中所有公共方法、命名空间函数及文件作用域函数。\n\n")

        f.write("## 统计概览\n\n")
        f.write("| 指标 | 数值 |\n")
        f.write("|------|------|\n")
        f.write(f"| **总方法 (不含构造器/析构器)** | {total_funcs} |\n")
        f.write(f"| **总文件数** | {len(by_file)} |\n\n")

        f.write("### 复杂度分布\n\n")
        f.write("| 复杂度 | 数量 | 占比 |\n")
        f.write("|--------|------|------|\n")
        for comp, count in complexity_counts.items():
            pct = (count / total_funcs * 100) if total_funcs > 0 else 0
            f.write(f"| {comp} | {count} | {pct:.1f}% |\n")
        f.write("\n---\n\n")

        f.write("## 📦 文件统计\n\n")
        f.write("| 文件 | 方法数 |\n")
        f.write("|------|--------|\n")
        for file_path in sorted(by_file.keys()):
            f.write(f"| {file_path} | {by_file[file_path]} |\n")
        f.write("\n")


def main() -> None:
    args = parse_args()
    ensure_libclang_configured()

    root = repo_root(__file__, args.root)
    out_dir = output_dir(__file__, args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    compile_commands_path = find_compile_commands(root, args.compile_commands)
    file_args_map, common_args = load_compile_commands(compile_commands_path)

    files = discover_files(root)
    if not files:
        print("No source files found.")
        return

    index = Index.create()
    all_funcs: List[Dict[str, object]] = []
    per_file_out_dir = os.path.join(out_dir, "methods_reports")
    os.makedirs(per_file_out_dir, exist_ok=True)

    for file_path in files:
        args_for_file = file_args_map.get(os.path.abspath(file_path), common_args)
        if file_path.endswith(".h"):
            args_for_file = ensure_args_for_header(args_for_file)
        if not args_for_file:
            args_for_file = ensure_args_for_header([])

        try:
            funcs = collect_functions(index, file_path, args_for_file, root)
        except Exception as exc:
            print(f"WARN: failed to parse {file_path}: {exc}")
            continue

        for func in funcs:
            func["file_path"] = os.path.relpath(file_path, root)
        all_funcs.extend(funcs)
        write_markdown(os.path.relpath(file_path, root), funcs, per_file_out_dir)

    jsonl_path = os.path.join(out_dir, "testable_methods.jsonl")
    write_jsonl(all_funcs, jsonl_path)

    summary_path = os.path.join(out_dir, "leveldb_testable_methods_report.md")
    write_summary(summary_path, all_funcs)

    print(f"JSONL written to {jsonl_path}")
    print(f"Summary written to {summary_path}")
    print(f"Per-file reports in {per_file_out_dir}")


if __name__ == "__main__":
    main()
