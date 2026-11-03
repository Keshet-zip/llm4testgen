# llm4testgen

This repository contains the replication package for the paper
"Context-Aware Unit Test Generation and Error-Driven Iterative Repair with Locally Deployed Large Language Models" (under review).

> **Status:** This is a partial release. It currently includes the
> benchmark method lists and the scripts used to collect them. The full implementation
> of llm4testgen is being cleaned up and will be released in this
> repository by <date / upon acceptance>.

## Contents

| Directory     | Description                                         | Status      |
|---------------|-----------------------------------------------------|-------------|
| `benchmarks/` | Methods under test for each subject project         | Available   |
| `scripts/`    | Scripts used to extract and filter testable methods | Available   |
| `prompts/`    | Prompt templates used in the experiments            | Available   |
| `src/`        | Implementation of <Tool Name>                       | Coming soon |

## Subject Projects

| Project         | Language | Version / Commit | #Methods (all) | #Methods (used) |
|-----------------|----------|------------------|----------------|-----------------|
| JFreeChart      | Java     | 1.5.4            | 6656           | 200             |
| Commons CLI     | Java     | 1.6.0            | 202            | 202             |
| Commons CSV     | Java     | 1.10.0           | 161            | 161             |
| nlohmann/json   | C++      | 3.11.3           | 333            | 333             |
| google/leveldb  | C++      | 1.23             | 994            | 300             |
| scikit-learn    | Python   | 1.8.0            | 2561           | 300             |

Source code of the subject projects is not redistributed here.
Clone them from their official repositories at the listed versions.

## Method Selection

Starting from all public methods and constructors (including inner
classes and interface methods), we removed:

- simple getters and setters (`get*`, `set*`, `is*`) without logic
- standard methods: `toString`, `hashCode`, `equals`, `clone`
- `main` methods
- methods annotated with `@Deprecated`
- wrapper methods that only call `super.method()`

Each `benchmarks/<project>/` folder contains:
- `all_methods.md`/`all_methods.jsonl`: all collected methods
- `filtered_methods.md`/`filtered_methods.jsonl`: methods used in the experiments

To regenerate a method list (C++ projects only), run:

```bash
python scripts/collect_testable_methods_libclang.py <args>
```

## Experimental Configurations

| Name            | Description (map to paper terminology) |
|-----------------|----------------------------------------|
| `full`          | Full approach                          |
| `method-only`   | Only the focal method as context       |
| `dependency`    | Focal method + dependency context      |
| `core`          | <...>                                  |
| `no-repair`     | Without the repair stage               |
| `blind-retry`   | Retry without error feedback           |

LLMs: <model name> (14B), <model name> (20B), served via <Ollama/...>.

## License

MIT