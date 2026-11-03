# scikit-learn-1.8.0 - Python 方法列表

**生成时间**: 2026-01-21 12:02:33

## 🔍 收集规则

本报告收集了项目中**所有公共方法**（不包括私有方法，但包括魔术方法）。

## 📊 统计概览

| 指标 | 数值 |
|------|------|
| **总方法数** | 2561 |
| **类方法数** | 1624 |
| **模块函数数** | 937 |

### 复杂度分布

| 复杂度 | 数量 | 占比 |
|--------|------|------|
| simple | 839 | 32.8% |
| medium | 963 | 37.6% |
| complex | 759 | 29.6% |

### 方法类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| class | 27 | 1.1% |
| instance | 2433 | 95.0% |
| property | 98 | 3.8% |
| static | 3 | 0.1% |

---

## 🔹 `SKExampleTitleSortKey`

**完全限定名**: `doc.conf.SKExampleTitleSortKey`

**文件路径**: `doc/conf.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__call__` | instance | `self, filename` | `None` | `doc.conf.SKExampleTitleSortKey.__call__(self, filename)` | simple | 13 | 魔术方法, 有逻辑 |

---

## 🔹 `SubSectionTitleOrder`

**完全限定名**: `doc.conf.SubSectionTitleOrder`

**文件路径**: `doc/conf.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, src_dir` | `None` | `doc.conf.SubSectionTitleOrder.__init__(self, src_dir)` | simple | 3 | 魔术方法 |
| 2 | `__repr__` | instance | `self` | `None` | `doc.conf.SubSectionTitleOrder.__repr__(self)` | simple | 2 | 魔术方法 |
| 3 | `__call__` | instance | `self, directory` | `None` | `doc.conf.SubSectionTitleOrder.__call__(self, directory)` | medium | 19 | 魔术方法, 有逻辑 |

---

## 🔹 `AllowNanEstimators`

**完全限定名**: `doc.sphinxext.allow_nan_estimators.AllowNanEstimators`

**文件路径**: `doc/sphinxext/allow_nan_estimators.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_paragraph_for_estimator_type` | static | `estimator_type` | `None` | `doc.sphinxext.allow_nan_estimators.AllowNanEstimators.make_paragraph_for_estimator_type(estimator_type)` | medium | 28 | 有逻辑 |
| 2 | `run` | instance | `self` | `None` | `doc.sphinxext.allow_nan_estimators.AllowNanEstimators.run(self)` | simple | 7 | 有逻辑 |

---

## 🔹 `ShortSummaryDocumenter`

**完全限定名**: `doc.sphinxext.autoshortsummary.ShortSummaryDocumenter`

**文件路径**: `doc/sphinxext/autoshortsummary.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `can_document_member` | class | `cls, member, membername, isattr, parent` | `None` | `doc.sphinxext.autoshortsummary.ShortSummaryDocumenter.can_document_member(cls, member, membername, isattr, parent)` | simple | 3 | - |
| 2 | `get_object_members` | instance | `self, want_all` | `None` | `doc.sphinxext.autoshortsummary.ShortSummaryDocumenter.get_object_members(self, want_all)` | simple | 3 | - |
| 3 | `add_directive_header` | instance | `self, sig` | `None` | `doc.sphinxext.autoshortsummary.ShortSummaryDocumenter.add_directive_header(self, sig)` | simple | 3 | - |
| 4 | `add_content` | instance | `self, more_content` | `None` | `doc.sphinxext.autoshortsummary.ShortSummaryDocumenter.add_content(self, more_content)` | medium | 20 | 有逻辑 |

---

## 🔹 `DropdownAnchorAdder`

**完全限定名**: `doc.sphinxext.dropdown_anchors.DropdownAnchorAdder`

**文件路径**: `doc/sphinxext/dropdown_anchors.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `run` | instance | `self` | `None` | `doc.sphinxext.dropdown_anchors.DropdownAnchorAdder.run(self)` | medium | 33 | 有逻辑 |

---

## 🔹 `IssueRole`

**完全限定名**: `doc.sphinxext.sphinx_issues.IssueRole`

**文件路径**: `doc/sphinxext/sphinx_issues.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, uri_config_option, format_kwarg, github_u...` | `None` | `doc.sphinxext.sphinx_issues.IssueRole.__init__(self, uri_config_option, format_kwarg, github_uri_template, format_text = None)` | simple | 7 | 魔术方法 |
| 2 | `default_format_text` | static | `issue_no` | `None` | `doc.sphinxext.sphinx_issues.IssueRole.default_format_text(issue_no)` | simple | 2 | - |
| 3 | `make_node` | instance | `self, name, issue_no, config, options = None` | `None` | `doc.sphinxext.sphinx_issues.IssueRole.make_node(self, name, issue_no, config, options = None)` | complex | 38 | 抛异常, 有逻辑 |
| 4 | `__call__` | instance | `self, name, rawtext, text, lineno, inliner, opt...` | `None` | `doc.sphinxext.sphinx_issues.IssueRole.__call__(self, name, rawtext, text, lineno, inliner, options = None, content = None)` | medium | 15 | 魔术方法, 有逻辑 |

---

## 🔹 `ReutersParser`

**完全限定名**: `examples.applications.plot_out_of_core_classification.ReutersParser`

**文件路径**: `examples/applications/plot_out_of_core_classification.py`

**公共方法数**: 15

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, encoding = 'latin-1'` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.__init__(self, encoding = 'latin-1')` | simple | 4 | 魔术方法 |
| 2 | `handle_starttag` | instance | `self, tag, attrs` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.handle_starttag(self, tag, attrs)` | simple | 3 | - |
| 3 | `handle_endtag` | instance | `self, tag` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.handle_endtag(self, tag)` | simple | 3 | - |
| 4 | `parse` | instance | `self, fd` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.parse(self, fd)` | simple | 8 | 有逻辑 |
| 5 | `handle_data` | instance | `self, data` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.handle_data(self, data)` | simple | 7 | 有逻辑 |
| 6 | `start_reuters` | instance | `self, attributes` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.start_reuters(self, attributes)` | simple | 2 | - |
| 7 | `end_reuters` | instance | `self` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.end_reuters(self)` | simple | 6 | - |
| 8 | `start_title` | instance | `self, attributes` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.start_title(self, attributes)` | simple | 2 | - |
| 9 | `end_title` | instance | `self` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.end_title(self)` | simple | 2 | - |
| 10 | `start_body` | instance | `self, attributes` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.start_body(self, attributes)` | simple | 2 | - |
| 11 | `end_body` | instance | `self` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.end_body(self)` | simple | 2 | - |
| 12 | `start_topics` | instance | `self, attributes` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.start_topics(self, attributes)` | simple | 2 | - |
| 13 | `end_topics` | instance | `self` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.end_topics(self)` | simple | 2 | - |
| 14 | `start_d` | instance | `self, attributes` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.start_d(self, attributes)` | simple | 2 | - |
| 15 | `end_d` | instance | `self` | `None` | `examples.applications.plot_out_of_core_classification.ReutersParser.end_d(self)` | simple | 4 | - |

---

## 🔹 `NumberNormalizingVectorizer`

**完全限定名**: `examples.bicluster.plot_bicluster_newsgroups.NumberNormalizingVectorizer`

**文件路径**: `examples/bicluster/plot_bicluster_newsgroups.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `build_tokenizer` | instance | `self` | `None` | `examples.bicluster.plot_bicluster_newsgroups.NumberNormalizingVectorizer.build_tokenizer(self)` | simple | 3 | - |

---

## 🔹 `NaivelyCalibratedLinearSVC`

**完全限定名**: `examples.calibration.plot_calibration_curve.NaivelyCalibratedLinearSVC`

**文件路径**: `examples/calibration/plot_calibration_curve.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y` | `None` | `examples.calibration.plot_calibration_curve.NaivelyCalibratedLinearSVC.fit(self, X, y)` | simple | 5 | - |
| 2 | `predict_proba` | instance | `self, X` | `None` | `examples.calibration.plot_calibration_curve.NaivelyCalibratedLinearSVC.predict_proba(self, X)` | simple | 8 | - |

---

## 🔹 `NaivelyCalibratedLinearSVC`

**完全限定名**: `examples.calibration.plot_compare_calibration.NaivelyCalibratedLinearSVC`

**文件路径**: `examples/calibration/plot_compare_calibration.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y` | `None` | `examples.calibration.plot_compare_calibration.NaivelyCalibratedLinearSVC.fit(self, X, y)` | simple | 5 | - |
| 2 | `predict_proba` | instance | `self, X` | `None` | `examples.calibration.plot_compare_calibration.NaivelyCalibratedLinearSVC.predict_proba(self, X)` | simple | 8 | - |

---

## 🔹 `InductiveClusterer`

**完全限定名**: `examples.cluster.plot_inductive_clustering.InductiveClusterer`

**文件路径**: `examples/cluster/plot_inductive_clustering.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, clusterer, classifier` | `None` | `examples.cluster.plot_inductive_clustering.InductiveClusterer.__init__(self, clusterer, classifier)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `examples.cluster.plot_inductive_clustering.InductiveClusterer.fit(self, X, y = None)` | simple | 6 | - |
| 3 | `predict` | instance | `self, X` | `None` | `examples.cluster.plot_inductive_clustering.InductiveClusterer.predict(self, X)` | simple | 3 | - |
| 4 | `decision_function` | instance | `self, X` | `None` | `examples.cluster.plot_inductive_clustering.InductiveClusterer.decision_function(self, X)` | simple | 3 | - |

---

## 🔹 `CustomEstimator`

**完全限定名**: `examples.developing_estimators.sklearn_is_fitted.CustomEstimator`

**文件路径**: `examples/developing_estimators/sklearn_is_fitted.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, parameter = 1` | `None` | `examples.developing_estimators.sklearn_is_fitted.CustomEstimator.__init__(self, parameter = 1)` | simple | 2 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `examples.developing_estimators.sklearn_is_fitted.CustomEstimator.fit(self, X, y)` | simple | 8 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `examples.developing_estimators.sklearn_is_fitted.CustomEstimator.predict(self, X)` | simple | 10 | 抛异常 |
| 4 | `score` | instance | `self, X, y` | `None` | `examples.developing_estimators.sklearn_is_fitted.CustomEstimator.score(self, X, y)` | simple | 9 | 抛异常 |
| 5 | `__sklearn_is_fitted__` | instance | `self` | `None` | `examples.developing_estimators.sklearn_is_fitted.CustomEstimator.__sklearn_is_fitted__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `SequenceKernel`

**完全限定名**: `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel`

**文件路径**: `examples/gaussian_process/plot_gpr_on_structured_data.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, baseline_similarity = 0.5, baseline_simil...` | `None` | `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel.__init__(self, baseline_similarity = 0.5, baseline_similarity_bounds = (1e-05, 1))` | simple | 3 | 魔术方法 |
| 2 | `hyperparameter_baseline_similarity` | property | `self` | `None` | `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel.hyperparameter_baseline_similarity(self)` | simple | 4 | - |
| 3 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel.__call__(self, X, Y = None, eval_gradient = False)` | simple | 11 | 魔术方法, 有逻辑 |
| 4 | `diag` | instance | `self, X` | `None` | `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel.diag(self, X)` | simple | 2 | 有逻辑 |
| 5 | `is_stationary` | instance | `self` | `None` | `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel.is_stationary(self)` | simple | 2 | - |
| 6 | `clone_with_theta` | instance | `self, theta` | `None` | `examples.gaussian_process.plot_gpr_on_structured_data.SequenceKernel.clone_with_theta(self, theta)` | simple | 4 | - |

---

## 🔹 `ExampleClassifier`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.ExampleClassifier`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleClassifier.fit(self, X, y, sample_weight = None)` | simple | 5 | - |
| 2 | `predict` | instance | `self, X, groups = None` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleClassifier.predict(self, X, groups = None)` | simple | 4 | - |

---

## 🔹 `ExampleRegressor`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.ExampleRegressor`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleRegressor.fit(self, X, y, sample_weight = None)` | simple | 3 | - |
| 2 | `predict` | instance | `self, X` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleRegressor.predict(self, X)` | simple | 2 | - |

---

## 🔹 `ExampleTransformer`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.ExampleTransformer`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleTransformer.fit(self, X, y, sample_weight = None)` | simple | 3 | - |
| 2 | `transform` | instance | `self, X, groups = None` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleTransformer.transform(self, X, groups = None)` | simple | 3 | - |
| 3 | `fit_transform` | instance | `self, X, y, sample_weight = None, groups = None` | `None` | `examples.miscellaneous.plot_metadata_routing.ExampleTransformer.fit_transform(self, X, y, sample_weight = None, groups = None)` | simple | 2 | - |

---

## 🔹 `MetaClassifier`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.MetaClassifier`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaClassifier.__init__(self, estimator)` | simple | 2 | 魔术方法 |
| 2 | `get_metadata_routing` | instance | `self` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaClassifier.get_metadata_routing(self)` | simple | 12 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y, **fit_params` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaClassifier.fit(self, X, y, **fit_params)` | simple | 21 | 有逻辑 |
| 4 | `predict` | instance | `self, X, **predict_params` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaClassifier.predict(self, X, **predict_params)` | simple | 11 | - |

---

## 🔹 `MetaRegressor`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.MetaRegressor`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaRegressor.__init__(self, estimator)` | simple | 2 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaRegressor.fit(self, X, y, **fit_params)` | simple | 3 | - |
| 3 | `get_metadata_routing` | instance | `self` | `None` | `examples.miscellaneous.plot_metadata_routing.MetaRegressor.get_metadata_routing(self)` | simple | 6 | - |

---

## 🔹 `RouterConsumerClassifier`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.RouterConsumerClassifier`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator` | `None` | `examples.miscellaneous.plot_metadata_routing.RouterConsumerClassifier.__init__(self, estimator)` | simple | 2 | 魔术方法 |
| 2 | `get_metadata_routing` | instance | `self` | `None` | `examples.miscellaneous.plot_metadata_routing.RouterConsumerClassifier.get_metadata_routing(self)` | medium | 15 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y, sample_weight, **fit_params` | `None` | `examples.miscellaneous.plot_metadata_routing.RouterConsumerClassifier.fit(self, X, y, sample_weight, **fit_params)` | medium | 16 | 抛异常, 有逻辑 |
| 4 | `predict` | instance | `self, X, **predict_params` | `None` | `examples.miscellaneous.plot_metadata_routing.RouterConsumerClassifier.predict(self, X, **predict_params)` | simple | 11 | - |

---

## 🔹 `SimplePipeline`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.SimplePipeline`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, transformer, classifier` | `None` | `examples.miscellaneous.plot_metadata_routing.SimplePipeline.__init__(self, transformer, classifier)` | simple | 3 | 魔术方法 |
| 2 | `get_metadata_routing` | instance | `self` | `None` | `examples.miscellaneous.plot_metadata_routing.SimplePipeline.get_metadata_routing(self)` | medium | 23 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y, **fit_params` | `None` | `examples.miscellaneous.plot_metadata_routing.SimplePipeline.fit(self, X, y, **fit_params)` | medium | 14 | - |
| 4 | `predict` | instance | `self, X, **predict_params` | `None` | `examples.miscellaneous.plot_metadata_routing.SimplePipeline.predict(self, X, **predict_params)` | simple | 9 | - |

---

## 🔹 `WeightedMetaRegressor`

**完全限定名**: `examples.miscellaneous.plot_metadata_routing.WeightedMetaRegressor`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator` | `None` | `examples.miscellaneous.plot_metadata_routing.WeightedMetaRegressor.__init__(self, estimator)` | simple | 2 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **fit_params` | `None` | `examples.miscellaneous.plot_metadata_routing.WeightedMetaRegressor.fit(self, X, y, sample_weight = None, **fit_params)` | simple | 6 | - |
| 3 | `get_metadata_routing` | instance | `self` | `None` | `examples.miscellaneous.plot_metadata_routing.WeightedMetaRegressor.get_metadata_routing(self)` | simple | 10 | - |

---

## 🔹 `NMSlibTransformer`

**完全限定名**: `examples.neighbors.approximate_nearest_neighbors.NMSlibTransformer`

**文件路径**: `examples/neighbors/approximate_nearest_neighbors.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 5, metric = 'euclidean', me...` | `None` | `examples.neighbors.approximate_nearest_neighbors.NMSlibTransformer.__init__(self, n_neighbors = 5, metric = 'euclidean', method = 'sw-graph', n_jobs = -1)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X` | `None` | `examples.neighbors.approximate_nearest_neighbors.NMSlibTransformer.fit(self, X)` | medium | 16 | - |
| 3 | `transform` | instance | `self, X` | `None` | `examples.neighbors.approximate_nearest_neighbors.NMSlibTransformer.transform(self, X)` | medium | 27 | 有逻辑 |

---

## 🔹 `MidpointNormalize`

**完全限定名**: `examples.svm.plot_rbf_parameters.MidpointNormalize`

**文件路径**: `examples/svm/plot_rbf_parameters.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, vmin = None, vmax = None, midpoint = None...` | `None` | `examples.svm.plot_rbf_parameters.MidpointNormalize.__init__(self, vmin = None, vmax = None, midpoint = None, clip = False)` | simple | 3 | 魔术方法 |
| 2 | `__call__` | instance | `self, value, clip = None` | `None` | `examples.svm.plot_rbf_parameters.MidpointNormalize.__call__(self, value, clip = None)` | simple | 3 | 魔术方法 |

---

## 📦 模块: `doc.conf`

**文件路径**: `doc/conf.py`

**模块函数数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `add_js_css_files` | instance | `app, pagename, templatename, context, doctree` | `None` | `doc.conf.add_js_css_files(app, pagename, templatename, context, doctree)` | medium | 21 | 有逻辑 |
| 2 | `notebook_modification_function` | instance | `notebook_content, notebook_filename` | `None` | `doc.conf.notebook_modification_function(notebook_content, notebook_filename)` | complex | 75 | 有逻辑 |
| 3 | `reset_sklearn_config` | instance | `gallery_conf, fname` | `None` | `doc.conf.reset_sklearn_config(gallery_conf, fname)` | simple | 3 | - |
| 4 | `make_carousel_thumbs` | instance | `app, exception` | `None` | `doc.conf.make_carousel_thumbs(app, exception)` | medium | 12 | 有逻辑 |
| 5 | `filter_search_index` | instance | `app, exception` | `None` | `doc.conf.filter_search_index(app, exception)` | medium | 19 | 有逻辑 |
| 6 | `disable_plot_gallery_for_linkcheck` | instance | `app` | `None` | `doc.conf.disable_plot_gallery_for_linkcheck(app)` | simple | 3 | 有逻辑 |
| 7 | `skip_properties` | instance | `app, what, name, obj, skip, options` | `None` | `doc.conf.skip_properties(app, what, name, obj, skip, options)` | simple | 7 | 有逻辑 |
| 8 | `setup` | instance | `app` | `None` | `doc.conf.setup(app)` | simple | 13 | 有逻辑 |
| 9 | `infer_next_release_versions` | instance | `` | `None` | `doc.conf.infer_next_release_versions()` | complex | 43 | 有逻辑 |

---

## 📦 模块: `doc.conftest`

**文件路径**: `doc/conftest.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `setup_labeled_faces` | instance | `` | `None` | `doc.conftest.setup_labeled_faces()` | simple | 4 | 抛异常, 有逻辑 |
| 2 | `setup_rcv1` | instance | `` | `None` | `doc.conftest.setup_rcv1()` | simple | 6 | 抛异常, 有逻辑 |
| 3 | `setup_twenty_newsgroups` | instance | `` | `None` | `doc.conftest.setup_twenty_newsgroups()` | simple | 4 | 抛异常, 有逻辑 |
| 4 | `setup_working_with_text_data` | instance | `` | `None` | `doc.conftest.setup_working_with_text_data()` | simple | 5 | 抛异常, 有逻辑 |
| 5 | `setup_loading_other_datasets` | instance | `` | `None` | `doc.conftest.setup_loading_other_datasets()` | medium | 13 | 抛异常, 有逻辑 |
| 6 | `setup_compose` | instance | `` | `None` | `doc.conftest.setup_compose()` | simple | 5 | 抛异常, 有逻辑 |
| 7 | `setup_impute` | instance | `` | `None` | `doc.conftest.setup_impute()` | simple | 5 | 抛异常, 有逻辑 |
| 8 | `setup_grid_search` | instance | `` | `None` | `doc.conftest.setup_grid_search()` | simple | 5 | 抛异常, 有逻辑 |
| 9 | `setup_preprocessing` | instance | `` | `None` | `doc.conftest.setup_preprocessing()` | simple | 5 | 抛异常, 有逻辑 |
| 10 | `skip_if_matplotlib_not_installed` | instance | `fname` | `None` | `doc.conftest.skip_if_matplotlib_not_installed(fname)` | simple | 6 | 抛异常, 有逻辑 |
| 11 | `skip_if_cupy_not_installed` | instance | `fname` | `None` | `doc.conftest.skip_if_cupy_not_installed(fname)` | simple | 6 | 抛异常, 有逻辑 |
| 12 | `pytest_runtest_setup` | instance | `item` | `None` | `doc.conftest.pytest_runtest_setup(item)` | medium | 34 | 有逻辑 |
| 13 | `pytest_configure` | instance | `config` | `None` | `doc.conftest.pytest_configure(config)` | simple | 8 | 有逻辑 |
| 14 | `pytest_collection_modifyitems` | instance | `config, items` | `None` | `doc.conftest.pytest_collection_modifyitems(config, items)` | medium | 33 | 有逻辑 |

---

## 📦 模块: `doc.sphinxext.allow_nan_estimators`

**文件路径**: `doc/sphinxext/allow_nan_estimators.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `setup` | instance | `app` | `None` | `doc.sphinxext.allow_nan_estimators.setup(app)` | simple | 8 | - |

---

## 📦 模块: `doc.sphinxext.autoshortsummary`

**文件路径**: `doc/sphinxext/autoshortsummary.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `setup` | instance | `app` | `None` | `doc.sphinxext.autoshortsummary.setup(app)` | simple | 2 | - |

---

## 📦 模块: `doc.sphinxext.doi_role`

**文件路径**: `doc/sphinxext/doi_role.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `reference_role` | instance | `typ, rawtext, text, lineno, inliner, options = ...` | `None` | `doc.sphinxext.doi_role.reference_role(typ, rawtext, text, lineno, inliner, options = {}, content = [])` | medium | 15 | 有逻辑 |
| 2 | `setup_link_role` | instance | `app` | `None` | `doc.sphinxext.doi_role.setup_link_role(app)` | simple | 5 | - |
| 3 | `setup` | instance | `app` | `None` | `doc.sphinxext.doi_role.setup(app)` | simple | 3 | - |

---

## 📦 模块: `doc.sphinxext.dropdown_anchors`

**文件路径**: `doc/sphinxext/dropdown_anchors.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `setup` | instance | `app` | `None` | `doc.sphinxext.dropdown_anchors.setup(app)` | simple | 2 | - |

---

## 📦 模块: `doc.sphinxext.github_link`

**文件路径**: `doc/sphinxext/github_link.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_linkcode_resolve` | instance | `package, url_fmt` | `None` | `doc.sphinxext.github_link.make_linkcode_resolve(package, url_fmt)` | medium | 15 | 有逻辑 |

---

## 📦 模块: `doc.sphinxext.override_pst_pagetoc`

**文件路径**: `doc/sphinxext/override_pst_pagetoc.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `override_pst_pagetoc` | instance | `app, pagename, templatename, context, doctree` | `None` | `doc.sphinxext.override_pst_pagetoc.override_pst_pagetoc(app, pagename, templatename, context, doctree)` | complex | 71 | 有逻辑 |
| 2 | `setup` | instance | `app` | `None` | `doc.sphinxext.override_pst_pagetoc.setup(app)` | simple | 4 | 有逻辑 |

---

## 📦 模块: `doc.sphinxext.sphinx_issues`

**文件路径**: `doc/sphinxext/sphinx_issues.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `user_role` | instance | `name, rawtext, text, lineno, inliner, options =...` | `None` | `doc.sphinxext.sphinx_issues.user_role(name, rawtext, text, lineno, inliner, options = None, content = None)` | medium | 27 | 有逻辑 |
| 2 | `cve_role` | instance | `name, rawtext, text, lineno, inliner, options =...` | `None` | `doc.sphinxext.sphinx_issues.cve_role(name, rawtext, text, lineno, inliner, options = None, content = None)` | medium | 15 | 有逻辑 |
| 3 | `format_commit_text` | instance | `sha` | `None` | `doc.sphinxext.sphinx_issues.format_commit_text(sha)` | simple | 2 | - |
| 4 | `setup` | instance | `app` | `None` | `doc.sphinxext.sphinx_issues.setup(app)` | medium | 25 | 有逻辑 |

---

## 📦 模块: `examples.applications.plot_cyclical_feature_engineering`

**文件路径**: `examples/applications/plot_cyclical_feature_engineering.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `evaluate` | instance | `model, X, y, cv, model_prop = None, model_step ...` | `None` | `examples.applications.plot_cyclical_feature_engineering.evaluate(model, X, y, cv, model_prop = None, model_step = None)` | medium | 23 | 有逻辑 |
| 2 | `sin_transformer` | instance | `period` | `None` | `examples.applications.plot_cyclical_feature_engineering.sin_transformer(period)` | simple | 2 | - |
| 3 | `cos_transformer` | instance | `period` | `None` | `examples.applications.plot_cyclical_feature_engineering.cos_transformer(period)` | simple | 2 | - |
| 4 | `periodic_spline_transformer` | instance | `period, n_splines = None, degree = 3` | `None` | `examples.applications.plot_cyclical_feature_engineering.periodic_spline_transformer(period, n_splines = None, degree = 3)` | medium | 11 | 有逻辑 |

---

## 📦 模块: `examples.applications.plot_digits_denoising`

**文件路径**: `examples/applications/plot_digits_denoising.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_digits` | instance | `X, title` | `None` | `examples.applications.plot_digits_denoising.plot_digits(X, title)` | simple | 7 | 有逻辑 |

---

## 📦 模块: `examples.applications.plot_face_recognition`

**文件路径**: `examples/applications/plot_face_recognition.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_gallery` | instance | `images, titles, h, w, n_row = 3, n_col = 4` | `None` | `examples.applications.plot_face_recognition.plot_gallery(images, titles, h, w, n_row = 3, n_col = 4)` | simple | 10 | 有逻辑 |
| 2 | `title` | instance | `y_pred, y_test, target_names, i` | `None` | `examples.applications.plot_face_recognition.title(y_pred, y_test, target_names, i)` | simple | 4 | - |

---

## 📦 模块: `examples.applications.plot_model_complexity_influence`

**文件路径**: `examples/applications/plot_model_complexity_influence.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `generate_data` | instance | `case` | `None` | `examples.applications.plot_model_complexity_influence.generate_data(case)` | medium | 15 | 有逻辑 |
| 2 | `benchmark_influence` | instance | `conf` | `None` | `examples.applications.plot_model_complexity_influence.benchmark_influence(conf)` | complex | 35 | 有逻辑 |
| 3 | `plot_influence` | instance | `conf, mse_values, prediction_times, complexities` | `None` | `examples.applications.plot_model_complexity_influence.plot_influence(conf, mse_values, prediction_times, complexities)` | medium | 38 | - |

---

## 📦 模块: `examples.applications.plot_out_of_core_classification`

**文件路径**: `examples/applications/plot_out_of_core_classification.py`

**模块函数数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `stream_reuters_documents` | instance | `data_path = None` | `None` | `examples.applications.plot_out_of_core_classification.stream_reuters_documents(data_path = None)` | complex | 48 | 有逻辑 |
| 2 | `get_minibatch` | instance | `doc_iter, size, pos_class = positive_class` | `None` | `examples.applications.plot_out_of_core_classification.get_minibatch(doc_iter, size, pos_class = positive_class)` | medium | 15 | 有逻辑 |
| 3 | `iter_minibatches` | instance | `doc_iter, minibatch_size` | `None` | `examples.applications.plot_out_of_core_classification.iter_minibatches(doc_iter, minibatch_size)` | simple | 6 | 有逻辑 |
| 4 | `progress` | instance | `cls_name, stats` | `None` | `examples.applications.plot_out_of_core_classification.progress(cls_name, stats)` | simple | 9 | - |
| 5 | `plot_accuracy` | instance | `x, y, x_legend` | `None` | `examples.applications.plot_out_of_core_classification.plot_accuracy(x, y, x_legend)` | simple | 9 | - |
| 6 | `autolabel` | instance | `rectangles` | `None` | `examples.applications.plot_out_of_core_classification.autolabel(rectangles)` | medium | 12 | 有逻辑 |

---

## 📦 模块: `examples.applications.plot_prediction_latency`

**文件路径**: `examples/applications/plot_prediction_latency.py`

**模块函数数**: 10

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `atomic_benchmark_estimator` | instance | `estimator, X_test, verbose = False` | `None` | `examples.applications.plot_prediction_latency.atomic_benchmark_estimator(estimator, X_test, verbose = False)` | medium | 17 | 有逻辑 |
| 2 | `bulk_benchmark_estimator` | instance | `estimator, X_test, n_bulk_repeats, verbose` | `None` | `examples.applications.plot_prediction_latency.bulk_benchmark_estimator(estimator, X_test, n_bulk_repeats, verbose)` | medium | 17 | 有逻辑 |
| 3 | `benchmark_estimator` | instance | `estimator, X_test, n_bulk_repeats = 30, verbose...` | `None` | `examples.applications.plot_prediction_latency.benchmark_estimator(estimator, X_test, n_bulk_repeats = 30, verbose = False)` | medium | 19 | - |
| 4 | `generate_dataset` | instance | `n_train, n_test, n_features, noise = 0.1, verbo...` | `None` | `examples.applications.plot_prediction_latency.generate_dataset(n_train, n_test, n_features, noise = 0.1, verbose = False)` | medium | 27 | 有逻辑 |
| 5 | `boxplot_runtimes` | instance | `runtimes, pred_type, configuration` | `None` | `examples.applications.plot_prediction_latency.boxplot_runtimes(runtimes, pred_type, configuration)` | complex | 41 | 有逻辑 |
| 6 | `benchmark` | instance | `configuration` | `None` | `examples.applications.plot_prediction_latency.benchmark(configuration)` | medium | 21 | 有逻辑 |
| 7 | `n_feature_influence` | instance | `estimators, n_train, n_test, n_features, percen...` | `None` | `examples.applications.plot_prediction_latency.n_feature_influence(estimators, n_train, n_test, n_features, percentile)` | medium | 30 | 有逻辑 |
| 8 | `plot_n_features_influence` | instance | `percentiles, percentile` | `None` | `examples.applications.plot_prediction_latency.plot_n_features_influence(percentiles, percentile)` | medium | 17 | 有逻辑 |
| 9 | `benchmark_throughputs` | instance | `configuration, duration_secs = 0.1` | `None` | `examples.applications.plot_prediction_latency.benchmark_throughputs(configuration, duration_secs = 0.1)` | medium | 15 | 有逻辑 |
| 10 | `plot_benchmark_throughput` | instance | `throughputs, configuration` | `None` | `examples.applications.plot_prediction_latency.plot_benchmark_throughput(throughputs, configuration)` | medium | 27 | 有逻辑 |

---

## 📦 模块: `examples.applications.plot_species_distribution_modeling`

**文件路径**: `examples/applications/plot_species_distribution_modeling.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `construct_grids` | instance | `batch` | `None` | `examples.applications.plot_species_distribution_modeling.construct_grids(batch)` | medium | 25 | 有逻辑 |
| 2 | `create_species_bunch` | instance | `species_name, train, test, coverages, xgrid, ygrid` | `None` | `examples.applications.plot_species_distribution_modeling.create_species_bunch(species_name, train, test, coverages, xgrid, ygrid)` | medium | 21 | 有逻辑 |
| 3 | `plot_species_distribution` | instance | `species = ('bradypus_variegatus_0', 'microryzom...` | `None` | `examples.applications.plot_species_distribution_modeling.plot_species_distribution(species = ('bradypus_variegatus_0', 'microryzomys_minutus_0'))` | complex | 132 | 有逻辑 |

---

## 📦 模块: `examples.applications.plot_time_series_lagged_features`

**文件路径**: `examples/applications/plot_time_series_lagged_features.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `consolidate_scores` | instance | `cv_results, scores, metric` | `None` | `examples.applications.plot_time_series_lagged_features.consolidate_scores(cv_results, scores, metric)` | simple | 7 | 有逻辑 |
| 2 | `min_arg` | instance | `col` | `None` | `examples.applications.plot_time_series_lagged_features.min_arg(col)` | simple | 6 | - |

---

## 📦 模块: `examples.applications.plot_tomography_l1_reconstruction`

**文件路径**: `examples/applications/plot_tomography_l1_reconstruction.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `build_projection_operator` | instance | `l_x, n_dir` | `None` | `examples.applications.plot_tomography_l1_reconstruction.build_projection_operator(l_x, n_dir)` | medium | 30 | 有逻辑 |
| 2 | `generate_synthetic_data` | instance | `` | `None` | `examples.applications.plot_tomography_l1_reconstruction.generate_synthetic_data()` | medium | 12 | - |

---

## 📦 模块: `examples.applications.plot_topics_extraction_with_nmf_lda`

**文件路径**: `examples/applications/plot_topics_extraction_with_nmf_lda.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_top_words` | instance | `model, feature_names, n_top_words, title` | `None` | `examples.applications.plot_topics_extraction_with_nmf_lda.plot_top_words(model, feature_names, n_top_words, title)` | medium | 18 | 有逻辑 |

---

## 📦 模块: `examples.applications.wikipedia_principal_eigenvector`

**文件路径**: `examples/applications/wikipedia_principal_eigenvector.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `index` | instance | `redirects, index_map, k` | `None` | `examples.applications.wikipedia_principal_eigenvector.index(redirects, index_map, k)` | simple | 4 | - |
| 2 | `short_name` | instance | `nt_uri` | `None` | `examples.applications.wikipedia_principal_eigenvector.short_name(nt_uri)` | simple | 3 | - |
| 3 | `get_redirects` | instance | `redirects_filename` | `None` | `examples.applications.wikipedia_principal_eigenvector.get_redirects(redirects_filename)` | medium | 30 | 有逻辑 |
| 4 | `get_adjacency_matrix` | instance | `redirects_filename, page_links_filename, limit ...` | `None` | `examples.applications.wikipedia_principal_eigenvector.get_adjacency_matrix(redirects_filename, page_links_filename, limit = None)` | complex | 39 | 有逻辑 |
| 5 | `centrality_scores` | instance | `X, alpha = 0.85, max_iter = 100, tol = 1e-10` | `None` | `examples.applications.wikipedia_principal_eigenvector.centrality_scores(X, alpha = 0.85, max_iter = 100, tol = 1e-10)` | complex | 38 | 有逻辑 |

---

## 📦 模块: `examples.bicluster.plot_bicluster_newsgroups`

**文件路径**: `examples/bicluster/plot_bicluster_newsgroups.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `number_normalizer` | instance | `tokens` | `None` | `examples.bicluster.plot_bicluster_newsgroups.number_normalizer(tokens)` | simple | 8 | 有逻辑 |
| 2 | `bicluster_ncut` | instance | `i` | `None` | `examples.bicluster.plot_bicluster_newsgroups.bicluster_ncut(i)` | simple | 13 | 有逻辑 |

---

## 📦 模块: `examples.classification.plot_lda`

**文件路径**: `examples/classification/plot_lda.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `generate_data` | instance | `n_samples, n_features` | `None` | `examples.classification.plot_lda.generate_data(n_samples, n_features)` | medium | 15 | 有逻辑 |

---

## 📦 模块: `examples.classification.plot_lda_qda`

**文件路径**: `examples/classification/plot_lda_qda.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_data` | instance | `n_samples, n_features, cov_class_1, cov_class_2...` | `None` | `examples.classification.plot_lda_qda.make_data(n_samples, n_features, cov_class_1, cov_class_2, seed = 0)` | simple | 10 | - |
| 2 | `plot_ellipse` | instance | `mean, cov, color, ax` | `None` | `examples.classification.plot_lda_qda.plot_ellipse(mean, cov, color, ax)` | medium | 18 | - |
| 3 | `plot_result` | instance | `estimator, X, y, ax` | `None` | `examples.classification.plot_lda_qda.plot_result(estimator, X, y, ax)` | complex | 55 | 有逻辑 |

---

## 📦 模块: `examples.cluster.plot_adjusted_for_chance_measures`

**文件路径**: `examples/cluster/plot_adjusted_for_chance_measures.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `random_labels` | instance | `n_samples, n_classes` | `None` | `examples.cluster.plot_adjusted_for_chance_measures.random_labels(n_samples, n_classes)` | simple | 2 | - |
| 2 | `fixed_classes_uniform_labelings_scores` | instance | `score_func, n_samples, n_clusters_range, n_clas...` | `None` | `examples.cluster.plot_adjusted_for_chance_measures.fixed_classes_uniform_labelings_scores(score_func, n_samples, n_clusters_range, n_classes, n_runs = 5)` | simple | 11 | 有逻辑 |
| 3 | `uniform_labelings_scores` | instance | `score_func, n_samples, n_clusters_range, n_runs...` | `None` | `examples.cluster.plot_adjusted_for_chance_measures.uniform_labelings_scores(score_func, n_samples, n_clusters_range, n_runs = 5)` | simple | 9 | 有逻辑 |

---

## 📦 模块: `examples.cluster.plot_agglomerative_clustering_metrics`

**文件路径**: `examples/cluster/plot_agglomerative_clustering_metrics.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `sqr` | instance | `x` | `None` | `examples.cluster.plot_agglomerative_clustering_metrics.sqr(x)` | simple | 2 | - |

---

## 📦 模块: `examples.cluster.plot_agglomerative_dendrogram`

**文件路径**: `examples/cluster/plot_agglomerative_dendrogram.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_dendrogram` | instance | `model, **kwargs` | `None` | `examples.cluster.plot_agglomerative_dendrogram.plot_dendrogram(model, **kwargs)` | medium | 21 | 有逻辑 |

---

## 📦 模块: `examples.cluster.plot_digits_linkage`

**文件路径**: `examples/cluster/plot_digits_linkage.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_clustering` | instance | `X_red, labels, title = None` | `None` | `examples.cluster.plot_digits_linkage.plot_clustering(X_red, labels, title = None)` | medium | 20 | 有逻辑 |

---

## 📦 模块: `examples.cluster.plot_hdbscan`

**文件路径**: `examples/cluster/plot_hdbscan.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot` | instance | `X, labels, probabilities = None, parameters = N...` | `None` | `examples.cluster.plot_hdbscan.plot(X, labels, probabilities = None, parameters = None, ground_truth = False, ax = None)` | medium | 34 | 有逻辑 |

---

## 📦 模块: `examples.cluster.plot_inductive_clustering`

**文件路径**: `examples/cluster/plot_inductive_clustering.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_scatter` | instance | `X, color, alpha = 0.5` | `None` | `examples.cluster.plot_inductive_clustering.plot_scatter(X, color, alpha = 0.5)` | simple | 2 | - |

---

## 📦 模块: `examples.cluster.plot_kmeans_digits`

**文件路径**: `examples/cluster/plot_kmeans_digits.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `bench_k_means` | instance | `kmeans, name, data, labels` | `None` | `examples.cluster.plot_kmeans_digits.bench_k_means(kmeans, name, data, labels)` | complex | 48 | 有逻辑 |

---

## 📦 模块: `examples.cluster.plot_kmeans_stability_low_dim_dense`

**文件路径**: `examples/cluster/plot_kmeans_stability_low_dim_dense.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_data` | instance | `random_state, n_samples_per_center, grid_size, ...` | `None` | `examples.cluster.plot_kmeans_stability_low_dim_dense.make_data(random_state, n_samples_per_center, grid_size, scale)` | simple | 12 | 有逻辑 |

---

## 📦 模块: `examples.compose.plot_column_transformer`

**文件路径**: `examples/compose/plot_column_transformer.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `subject_body_extractor` | instance | `posts` | `None` | `examples.compose.plot_column_transformer.subject_body_extractor(posts)` | medium | 20 | 有逻辑 |
| 2 | `text_stats` | instance | `posts` | `None` | `examples.compose.plot_column_transformer.text_stats(posts)` | simple | 2 | 有逻辑 |

---

## 📦 模块: `examples.compose.plot_transformed_target`

**文件路径**: `examples/compose/plot_transformed_target.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute_score` | instance | `y_true, y_pred` | `None` | `examples.compose.plot_transformed_target.compute_score(y_true, y_pred)` | simple | 5 | - |

---

## 📦 模块: `examples.datasets.plot_random_multilabel_dataset`

**文件路径**: `examples/datasets/plot_random_multilabel_dataset.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_2d` | instance | `ax, n_labels = 1, n_classes = 3, length = 50` | `None` | `examples.datasets.plot_random_multilabel_dataset.plot_2d(ax, n_labels = 1, n_classes = 3, length = 50)` | medium | 26 | - |

---

## 📦 模块: `examples.decomposition.plot_faces_decomposition`

**文件路径**: `examples/decomposition/plot_faces_decomposition.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_gallery` | instance | `title, images, n_col = n_col, n_row = n_row, cm...` | `None` | `examples.decomposition.plot_faces_decomposition.plot_gallery(title, images, n_col = n_col, n_row = n_row, cmap = plt.cm.gray)` | medium | 24 | 有逻辑 |

---

## 📦 模块: `examples.decomposition.plot_ica_vs_pca`

**文件路径**: `examples/decomposition/plot_ica_vs_pca.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_samples` | instance | `S, axis_list = None` | `None` | `examples.decomposition.plot_ica_vs_pca.plot_samples(S, axis_list = None)` | medium | 26 | 有逻辑 |

---

## 📦 模块: `examples.decomposition.plot_image_denoising`

**文件路径**: `examples/decomposition/plot_image_denoising.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `show_with_diff` | instance | `image, reference, title` | `None` | `examples.decomposition.plot_image_denoising.show_with_diff(image, reference, title)` | medium | 19 | - |

---

## 📦 模块: `examples.decomposition.plot_pca_vs_fa_model_selection`

**文件路径**: `examples/decomposition/plot_pca_vs_fa_model_selection.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute_scores` | instance | `X` | `None` | `examples.decomposition.plot_pca_vs_fa_model_selection.compute_scores(X)` | simple | 12 | 有逻辑 |
| 2 | `shrunk_cov_score` | instance | `X` | `None` | `examples.decomposition.plot_pca_vs_fa_model_selection.shrunk_cov_score(X)` | simple | 4 | - |
| 3 | `lw_score` | instance | `X` | `None` | `examples.decomposition.plot_pca_vs_fa_model_selection.lw_score(X)` | simple | 2 | - |

---

## 📦 模块: `examples.decomposition.plot_sparse_coding`

**文件路径**: `examples/decomposition/plot_sparse_coding.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `ricker_function` | instance | `resolution, center, width` | `None` | `examples.decomposition.plot_sparse_coding.ricker_function(resolution, center, width)` | simple | 9 | - |
| 2 | `ricker_matrix` | instance | `width, resolution, n_components` | `None` | `examples.decomposition.plot_sparse_coding.ricker_matrix(width, resolution, n_components)` | simple | 8 | 有逻辑 |

---

## 📦 模块: `examples.ensemble.plot_adaboost_multiclass`

**文件路径**: `examples/ensemble/plot_adaboost_multiclass.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `misclassification_error` | instance | `y_true, y_pred` | `None` | `examples.ensemble.plot_adaboost_multiclass.misclassification_error(y_true, y_pred)` | simple | 2 | - |

---

## 📦 模块: `examples.ensemble.plot_bias_variance`

**文件路径**: `examples/ensemble/plot_bias_variance.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `f` | instance | `x` | `None` | `examples.ensemble.plot_bias_variance.f(x)` | simple | 4 | - |
| 2 | `generate` | instance | `n_samples, noise, n_repeat = 1` | `None` | `examples.ensemble.plot_bias_variance.generate(n_samples, noise, n_repeat = 1)` | medium | 15 | 有逻辑 |

---

## 📦 模块: `examples.ensemble.plot_feature_transformation`

**文件路径**: `examples/ensemble/plot_feature_transformation.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `rf_apply` | instance | `X, model` | `None` | `examples.ensemble.plot_feature_transformation.rf_apply(X, model)` | simple | 2 | - |
| 2 | `gbdt_apply` | instance | `X, model` | `None` | `examples.ensemble.plot_feature_transformation.gbdt_apply(X, model)` | simple | 2 | - |

---

## 📦 模块: `examples.ensemble.plot_gradient_boosting_categorical`

**文件路径**: `examples/ensemble/plot_gradient_boosting_categorical.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_performance_tradeoff` | instance | `results, title` | `None` | `examples.ensemble.plot_gradient_boosting_categorical.plot_performance_tradeoff(results, title)` | complex | 60 | 有逻辑 |

---

## 📦 模块: `examples.ensemble.plot_gradient_boosting_oob`

**文件路径**: `examples/ensemble/plot_gradient_boosting_oob.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `heldout_score` | instance | `clf, X_test, y_test` | `None` | `examples.ensemble.plot_gradient_boosting_oob.heldout_score(clf, X_test, y_test)` | simple | 6 | 有逻辑 |
| 2 | `cv_estimate` | instance | `n_splits = None` | `None` | `examples.ensemble.plot_gradient_boosting_oob.cv_estimate(n_splits = None)` | simple | 9 | 有逻辑 |

---

## 📦 模块: `examples.ensemble.plot_gradient_boosting_quantile`

**文件路径**: `examples/ensemble/plot_gradient_boosting_quantile.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `f` | instance | `x` | `None` | `examples.ensemble.plot_gradient_boosting_quantile.f(x)` | simple | 3 | - |
| 2 | `highlight_min` | instance | `x` | `None` | `examples.ensemble.plot_gradient_boosting_quantile.highlight_min(x)` | simple | 3 | 有逻辑 |
| 3 | `coverage_fraction` | instance | `y, y_low, y_high` | `None` | `examples.ensemble.plot_gradient_boosting_quantile.coverage_fraction(y, y_low, y_high)` | simple | 2 | - |

---

## 📦 模块: `examples.ensemble.plot_hgbt_regression`

**文件路径**: `examples/ensemble/plot_hgbt_regression.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `generate_missing_values` | instance | `X, missing_fraction` | `None` | `examples.ensemble.plot_hgbt_regression.generate_missing_values(X, missing_fraction)` | simple | 8 | - |

---

## 📦 模块: `examples.ensemble.plot_stack_predictors`

**文件路径**: `examples/ensemble/plot_stack_predictors.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `load_ames_housing` | instance | `` | `None` | `examples.ensemble.plot_stack_predictors.load_ames_housing()` | complex | 34 | - |

---

## 📦 模块: `examples.gaussian_process.plot_gpc_isoprobability`

**文件路径**: `examples/gaussian_process/plot_gpc_isoprobability.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `g` | instance | `x` | `None` | `examples.gaussian_process.plot_gpc_isoprobability.g(x)` | simple | 4 | - |

---

## 📦 模块: `examples.gaussian_process.plot_gpr_noisy`

**文件路径**: `examples/gaussian_process/plot_gpr_noisy.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `target_generator` | instance | `X, add_noise = False` | `None` | `examples.gaussian_process.plot_gpr_noisy.target_generator(X, add_noise = False)` | simple | 6 | 有逻辑 |

---

## 📦 模块: `examples.gaussian_process.plot_gpr_prior_posterior`

**文件路径**: `examples/gaussian_process/plot_gpr_prior_posterior.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_gpr_samples` | instance | `gpr_model, n_samples, ax` | `None` | `examples.gaussian_process.plot_gpr_prior_posterior.plot_gpr_samples(gpr_model, n_samples, ax)` | complex | 43 | 有逻辑 |

---

## 📦 模块: `examples.impute.plot_iterative_imputer_variants_comparison`

**文件路径**: `examples/impute/plot_iterative_imputer_variants_comparison.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute_score_for` | instance | `X, y, imputer = None` | `None` | `examples.impute.plot_iterative_imputer_variants_comparison.compute_score_for(X, y, imputer = None)` | simple | 11 | 有逻辑 |

---

## 📦 模块: `examples.impute.plot_missing_values`

**文件路径**: `examples/impute/plot_missing_values.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `add_missing_values` | instance | `X_full, y_full, rng` | `None` | `examples.impute.plot_missing_values.add_missing_values(X_full, y_full, rng)` | medium | 17 | - |
| 2 | `get_score` | instance | `X, y, imputer = None` | `None` | `examples.impute.plot_missing_values.get_score(X, y, imputer = None)` | simple | 10 | 有逻辑 |

---

## 📦 模块: `examples.inspection.plot_permutation_importance_multicollinear`

**文件路径**: `examples/inspection/plot_permutation_importance_multicollinear.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_permutation_importance` | instance | `clf, X, y, ax` | `None` | `examples.inspection.plot_permutation_importance_multicollinear.plot_permutation_importance(clf, X, y, ax)` | medium | 17 | 有逻辑 |

---

## 📦 模块: `examples.linear_model.plot_bayesian_ridge_curvefit`

**文件路径**: `examples/linear_model/plot_bayesian_ridge_curvefit.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `func` | instance | `x` | `None` | `examples.linear_model.plot_bayesian_ridge_curvefit.func(x)` | simple | 2 | - |

---

## 📦 模块: `examples.linear_model.plot_lasso_lars_ic`

**文件路径**: `examples/linear_model/plot_lasso_lars_ic.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `zou_et_al_criterion_rescaling` | instance | `criterion, n_samples, noise_variance` | `None` | `examples.linear_model.plot_lasso_lars_ic.zou_et_al_criterion_rescaling(criterion, n_samples, noise_variance)` | simple | 3 | - |

---

## 📦 模块: `examples.linear_model.plot_lasso_model_selection`

**文件路径**: `examples/linear_model/plot_lasso_model_selection.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `highlight_min` | instance | `x` | `None` | `examples.linear_model.plot_lasso_model_selection.highlight_min(x)` | simple | 3 | 有逻辑 |

---

## 📦 模块: `examples.linear_model.plot_logistic_multinomial`

**文件路径**: `examples/linear_model/plot_logistic_multinomial.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_hyperplanes` | instance | `classifier, X, ax` | `None` | `examples.linear_model.plot_logistic_multinomial.plot_hyperplanes(classifier, X, ax)` | medium | 20 | 有逻辑 |

---

## 📦 模块: `examples.linear_model.plot_poisson_regression_non_normal_loss`

**文件路径**: `examples/linear_model/plot_poisson_regression_non_normal_loss.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `score_estimator` | instance | `estimator, df_test` | `None` | `examples.linear_model.plot_poisson_regression_non_normal_loss.score_estimator(estimator, df_test)` | complex | 36 | 有逻辑 |
| 2 | `lorenz_curve` | instance | `y_true, y_pred, exposure` | `None` | `examples.linear_model.plot_poisson_regression_non_normal_loss.lorenz_curve(y_true, y_pred, exposure)` | medium | 13 | - |

---

## 📦 模块: `examples.linear_model.plot_polynomial_interpolation`

**文件路径**: `examples/linear_model/plot_polynomial_interpolation.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `f` | instance | `x` | `None` | `examples.linear_model.plot_polynomial_interpolation.f(x)` | simple | 3 | - |
| 2 | `g` | instance | `x` | `None` | `examples.linear_model.plot_polynomial_interpolation.g(x)` | simple | 3 | - |

---

## 📦 模块: `examples.linear_model.plot_sgd_early_stopping`

**文件路径**: `examples/linear_model/plot_sgd_early_stopping.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `load_mnist` | instance | `n_samples = None, class_0 = '0', class_1 = '8'` | `None` | `examples.linear_model.plot_sgd_early_stopping.load_mnist(n_samples = None, class_0 = '0', class_1 = '8')` | simple | 12 | 有逻辑 |
| 2 | `fit_and_score` | instance | `estimator, max_iter, X_train, X_test, y_train, ...` | `None` | `examples.linear_model.plot_sgd_early_stopping.fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test)` | medium | 14 | - |

---

## 📦 模块: `examples.linear_model.plot_sgd_iris`

**文件路径**: `examples/linear_model/plot_sgd_iris.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_hyperplane` | instance | `c, color` | `None` | `examples.linear_model.plot_sgd_iris.plot_hyperplane(c, color)` | simple | 5 | - |

---

## 📦 模块: `examples.linear_model.plot_sgd_loss_functions`

**文件路径**: `examples/linear_model/plot_sgd_loss_functions.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `modified_huber_loss` | instance | `y_true, y_pred` | `None` | `examples.linear_model.plot_sgd_loss_functions.modified_huber_loss(y_true, y_pred)` | simple | 6 | - |

---

## 📦 模块: `examples.linear_model.plot_tweedie_regression_insurance_claims`

**文件路径**: `examples/linear_model/plot_tweedie_regression_insurance_claims.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `load_mtpl2` | instance | `n_samples = None` | `None` | `examples.linear_model.plot_tweedie_regression_insurance_claims.load_mtpl2(n_samples = None)` | medium | 27 | 有逻辑 |
| 2 | `plot_obs_pred` | instance | `df, feature, weight, observed, predicted, y_lab...` | `None` | `examples.linear_model.plot_tweedie_regression_insurance_claims.plot_obs_pred(df, feature, weight, observed, predicted, y_label = None, title = None, ax = None, fill_legend = False)` | complex | 54 | 有逻辑 |
| 3 | `score_estimator` | instance | `estimator, X_train, X_test, df_train, df_test, ...` | `None` | `examples.linear_model.plot_tweedie_regression_insurance_claims.score_estimator(estimator, X_train, X_test, df_train, df_test, target, weights, tweedie_powers = None)` | complex | 58 | 有逻辑 |
| 4 | `lorenz_curve` | instance | `y_true, y_pred, exposure` | `None` | `examples.linear_model.plot_tweedie_regression_insurance_claims.lorenz_curve(y_true, y_pred, exposure)` | medium | 13 | - |

---

## 📦 模块: `examples.manifold.plot_compare_methods`

**文件路径**: `examples/manifold/plot_compare_methods.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_3d` | instance | `points, points_color, title` | `None` | `examples.manifold.plot_compare_methods.plot_3d(points, points_color, title)` | medium | 18 | - |
| 2 | `plot_2d` | instance | `points, points_color, title` | `None` | `examples.manifold.plot_compare_methods.plot_2d(points, points_color, title)` | simple | 5 | - |
| 3 | `add_2d_scatter` | instance | `ax, points, points_color, title = None` | `None` | `examples.manifold.plot_compare_methods.add_2d_scatter(ax, points, points_color, title = None)` | simple | 6 | - |

---

## 📦 模块: `examples.manifold.plot_lle_digits`

**文件路径**: `examples/manifold/plot_lle_digits.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_embedding` | instance | `X, title` | `None` | `examples.manifold.plot_lle_digits.plot_embedding(X, title)` | medium | 30 | 有逻辑 |

---

## 📦 模块: `examples.miscellaneous.plot_metadata_routing`

**文件路径**: `examples/miscellaneous/plot_metadata_routing.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_metadata` | instance | `obj, **kwargs` | `None` | `examples.miscellaneous.plot_metadata_routing.check_metadata(obj, **kwargs)` | simple | 8 | 有逻辑 |
| 2 | `print_routing` | instance | `obj` | `None` | `examples.miscellaneous.plot_metadata_routing.print_routing(obj)` | simple | 2 | - |

---

## 📦 模块: `examples.miscellaneous.plot_multilabel`

**文件路径**: `examples/miscellaneous/plot_multilabel.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_hyperplane` | instance | `clf, min_x, max_x, linestyle, label` | `None` | `examples.miscellaneous.plot_multilabel.plot_hyperplane(clf, min_x, max_x, linestyle, label)` | simple | 7 | - |
| 2 | `plot_subfigure` | instance | `X, Y, subplot, title, transform` | `None` | `examples.miscellaneous.plot_multilabel.plot_subfigure(X, Y, subplot, title, transform)` | complex | 57 | 抛异常, 有逻辑 |

---

## 📦 模块: `examples.miscellaneous.plot_outlier_detection_bench`

**文件路径**: `examples/miscellaneous/plot_outlier_detection_bench.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_estimator` | instance | `name, categorical_columns = None, iforest_kw = ...` | `None` | `examples.miscellaneous.plot_outlier_detection_bench.make_estimator(name, categorical_columns = None, iforest_kw = None, lof_kw = None)` | medium | 27 | 有逻辑 |
| 2 | `fit_predict` | instance | `estimator, X` | `None` | `examples.miscellaneous.plot_outlier_detection_bench.fit_predict(estimator, X)` | simple | 10 | 有逻辑 |

---

## 📦 模块: `examples.mixture.plot_concentration_prior`

**文件路径**: `examples/mixture/plot_concentration_prior.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_ellipses` | instance | `ax, weights, means, covars` | `None` | `examples.mixture.plot_concentration_prior.plot_ellipses(ax, weights, means, covars)` | medium | 16 | 有逻辑 |
| 2 | `plot_results` | instance | `ax1, ax2, estimator, X, y, title, plot_title = ...` | `None` | `examples.mixture.plot_concentration_prior.plot_results(ax1, ax2, estimator, X, y, title, plot_title = False)` | medium | 30 | 有逻辑 |

---

## 📦 模块: `examples.mixture.plot_gmm`

**文件路径**: `examples/mixture/plot_gmm.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_results` | instance | `X, Y_, means, covariances, index, title` | `None` | `examples.mixture.plot_gmm.plot_results(X, Y_, means, covariances, index, title)` | medium | 26 | 有逻辑 |

---

## 📦 模块: `examples.mixture.plot_gmm_covariances`

**文件路径**: `examples/mixture/plot_gmm_covariances.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_ellipses` | instance | `gmm, ax` | `None` | `examples.mixture.plot_gmm_covariances.make_ellipses(gmm, ax)` | medium | 22 | 有逻辑 |

---

## 📦 模块: `examples.mixture.plot_gmm_init`

**文件路径**: `examples/mixture/plot_gmm_init.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_initial_means` | instance | `X, init_params, r` | `None` | `examples.mixture.plot_gmm_init.get_initial_means(X, init_params, r)` | simple | 6 | - |

---

## 📦 模块: `examples.mixture.plot_gmm_selection`

**文件路径**: `examples/mixture/plot_gmm_selection.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `gmm_bic_score` | instance | `estimator, X` | `None` | `examples.mixture.plot_gmm_selection.gmm_bic_score(estimator, X)` | simple | 4 | - |

---

## 📦 模块: `examples.mixture.plot_gmm_sin`

**文件路径**: `examples/mixture/plot_gmm_sin.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_results` | instance | `X, Y, means, covariances, index, title` | `None` | `examples.mixture.plot_gmm_sin.plot_results(X, Y, means, covariances, index, title)` | medium | 26 | 有逻辑 |
| 2 | `plot_samples` | instance | `X, Y, n_components, index, title` | `None` | `examples.mixture.plot_gmm_sin.plot_samples(X, Y, n_components, index, title)` | medium | 15 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_cost_sensitive_learning`

**文件路径**: `examples/model_selection/plot_cost_sensitive_learning.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fpr_score` | instance | `y, y_pred, neg_label, pos_label` | `None` | `examples.model_selection.plot_cost_sensitive_learning.fpr_score(y, y_pred, neg_label, pos_label)` | simple | 5 | - |
| 2 | `credit_gain_score` | instance | `y, y_pred, neg_label, pos_label` | `None` | `examples.model_selection.plot_cost_sensitive_learning.credit_gain_score(y, y_pred, neg_label, pos_label)` | simple | 10 | 有逻辑 |
| 3 | `plot_roc_pr_curves` | instance | `vanilla_model, tuned_model, title` | `None` | `examples.model_selection.plot_cost_sensitive_learning.plot_roc_pr_curves(vanilla_model, tuned_model, title)` | complex | 71 | 有逻辑 |
| 4 | `business_metric` | instance | `y_true, y_pred, amount` | `None` | `examples.model_selection.plot_cost_sensitive_learning.business_metric(y_true, y_pred, amount)` | simple | 10 | - |

---

## 📦 模块: `examples.model_selection.plot_cv_indices`

**文件路径**: `examples/model_selection/plot_cv_indices.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `visualize_groups` | instance | `classes, groups, name` | `None` | `examples.model_selection.plot_cv_indices.visualize_groups(classes, groups, name)` | medium | 25 | - |
| 2 | `plot_cv_indices` | instance | `cv, X, y, group, ax, n_splits, lw = 10` | `None` | `examples.model_selection.plot_cv_indices.plot_cv_indices(cv, X, y, group, ax, n_splits, lw = 10)` | complex | 44 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_grid_search_digits`

**文件路径**: `examples/model_selection/plot_grid_search_digits.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `print_dataframe` | instance | `filtered_cv_results` | `None` | `examples.model_selection.plot_grid_search_digits.print_dataframe(filtered_cv_results)` | medium | 15 | 有逻辑 |
| 2 | `refit_strategy` | instance | `cv_results` | `None` | `examples.model_selection.plot_grid_search_digits.refit_strategy(cv_results)` | complex | 74 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_grid_search_refit_callable`

**文件路径**: `examples/model_selection/plot_grid_search_refit_callable.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `lower_bound` | instance | `cv_results` | `None` | `examples.model_selection.plot_grid_search_refit_callable.lower_bound(cv_results)` | medium | 22 | - |
| 2 | `best_low_complexity` | instance | `cv_results` | `None` | `examples.model_selection.plot_grid_search_refit_callable.best_low_complexity(cv_results)` | medium | 22 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_grid_search_stats`

**文件路径**: `examples/model_selection/plot_grid_search_stats.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `corrected_std` | instance | `differences, n_train, n_test` | `None` | `examples.model_selection.plot_grid_search_stats.corrected_std(differences, n_train, n_test)` | medium | 23 | - |
| 2 | `compute_corrected_ttest` | instance | `differences, df, n_train, n_test` | `None` | `examples.model_selection.plot_grid_search_stats.compute_corrected_ttest(differences, df, n_train, n_test)` | medium | 26 | - |

---

## 📦 模块: `examples.model_selection.plot_grid_search_text_feature_extraction`

**文件路径**: `examples/model_selection/plot_grid_search_text_feature_extraction.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `shorten_param` | instance | `param_name` | `None` | `examples.model_selection.plot_grid_search_text_feature_extraction.shorten_param(param_name)` | simple | 5 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_likelihood_ratios`

**文件路径**: `examples/model_selection/plot_likelihood_ratios.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `scoring` | instance | `estimator, X, y` | `None` | `examples.model_selection.plot_likelihood_ratios.scoring(estimator, X, y)` | simple | 4 | - |
| 2 | `extract_score` | instance | `cv_results` | `None` | `examples.model_selection.plot_likelihood_ratios.extract_score(cv_results)` | simple | 8 | - |
| 3 | `scoring_on_bootstrap` | instance | `estimator, X, y, rng, n_bootstrap = 100` | `None` | `examples.model_selection.plot_likelihood_ratios.scoring_on_bootstrap(estimator, X, y, rng, n_bootstrap = 100)` | medium | 11 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_randomized_search`

**文件路径**: `examples/model_selection/plot_randomized_search.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `report` | instance | `results, n_top = 3` | `None` | `examples.model_selection.plot_randomized_search.report(results, n_top = 3)` | medium | 13 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_successive_halving_heatmap`

**文件路径**: `examples/model_selection/plot_successive_halving_heatmap.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_heatmap` | instance | `ax, gs, is_sh = False, make_cbar = False` | `None` | `examples.model_selection.plot_successive_halving_heatmap.make_heatmap(ax, gs, is_sh = False, make_cbar = False)` | complex | 53 | 有逻辑 |

---

## 📦 模块: `examples.model_selection.plot_underfitting_overfitting`

**文件路径**: `examples/model_selection/plot_underfitting_overfitting.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `true_fun` | instance | `X` | `None` | `examples.model_selection.plot_underfitting_overfitting.true_fun(X)` | simple | 2 | - |

---

## 📦 模块: `examples.neighbors.approximate_nearest_neighbors`

**文件路径**: `examples/neighbors/approximate_nearest_neighbors.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `load_mnist` | instance | `n_samples` | `None` | `examples.neighbors.approximate_nearest_neighbors.load_mnist(n_samples)` | simple | 5 | - |

---

## 📦 模块: `examples.neighbors.plot_kde_1d`

**文件路径**: `examples/neighbors/plot_kde_1d.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `format_func` | instance | `x, loc` | `None` | `examples.neighbors.plot_kde_1d.format_func(x, loc)` | simple | 9 | 有逻辑 |

---

## 📦 模块: `examples.neighbors.plot_lof_outlier_detection`

**文件路径**: `examples/neighbors/plot_lof_outlier_detection.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `update_legend_marker_size` | instance | `handle, orig` | `None` | `examples.neighbors.plot_lof_outlier_detection.update_legend_marker_size(handle, orig)` | simple | 4 | - |

---

## 📦 模块: `examples.neighbors.plot_nca_illustration`

**文件路径**: `examples/neighbors/plot_nca_illustration.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `link_thickness_i` | instance | `X, i` | `None` | `examples.neighbors.plot_nca_illustration.link_thickness_i(X, i)` | simple | 9 | - |
| 2 | `relate_point` | instance | `X, i, ax` | `None` | `examples.neighbors.plot_nca_illustration.relate_point(X, i, ax)` | simple | 7 | 有逻辑 |

---

## 📦 模块: `examples.neighbors.plot_species_kde`

**文件路径**: `examples/neighbors/plot_species_kde.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `construct_grids` | instance | `batch` | `None` | `examples.neighbors.plot_species_kde.construct_grids(batch)` | medium | 25 | 有逻辑 |

---

## 📦 模块: `examples.neural_networks.plot_mlp_training_curves`

**文件路径**: `examples/neural_networks/plot_mlp_training_curves.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_on_dataset` | instance | `X, y, ax, name` | `None` | `examples.neural_networks.plot_mlp_training_curves.plot_on_dataset(X, y, ax, name)` | medium | 30 | 有逻辑 |

---

## 📦 模块: `examples.neural_networks.plot_rbm_logistic_classification`

**文件路径**: `examples/neural_networks/plot_rbm_logistic_classification.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `nudge_dataset` | instance | `X, Y` | `None` | `examples.neural_networks.plot_rbm_logistic_classification.nudge_dataset(X, Y)` | medium | 20 | 有逻辑 |

---

## 📦 模块: `examples.preprocessing.plot_all_scaling`

**文件路径**: `examples/preprocessing/plot_all_scaling.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `create_axes` | instance | `title, figsize = (16, 6)` | `None` | `examples.preprocessing.plot_all_scaling.create_axes(title, figsize = (16, 6))` | medium | 41 | 有逻辑 |
| 2 | `plot_distribution` | instance | `axes, X, y, hist_nbins = 50, title = '', x0_lab...` | `None` | `examples.preprocessing.plot_all_scaling.plot_distribution(axes, X, y, hist_nbins = 50, title = '', x0_label = '', x1_label = '')` | medium | 33 | 有逻辑 |
| 3 | `make_plot` | instance | `item_idx` | `None` | `examples.preprocessing.plot_all_scaling.make_plot(item_idx)` | complex | 40 | 有逻辑 |

---

## 📦 模块: `examples.preprocessing.plot_discretization_classification`

**文件路径**: `examples/preprocessing/plot_discretization_classification.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_name` | instance | `estimator` | `None` | `examples.preprocessing.plot_discretization_classification.get_name(estimator)` | simple | 6 | 有逻辑 |

---

## 📦 模块: `examples.preprocessing.plot_scaling_importance`

**文件路径**: `examples/preprocessing/plot_scaling_importance.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit_and_plot_model` | instance | `X_plot, y, clf, ax` | `None` | `examples.preprocessing.plot_scaling_importance.fit_and_plot_model(X_plot, y, clf, ax)` | medium | 13 | - |

---

## 📦 模块: `examples.preprocessing.plot_target_encoder`

**文件路径**: `examples/preprocessing/plot_target_encoder.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `evaluate_model_and_store` | instance | `name, pipe` | `None` | `examples.preprocessing.plot_target_encoder.evaluate_model_and_store(name, pipe)` | medium | 20 | - |

---

## 📦 模块: `examples.release_highlights.plot_release_highlights_0_22_0`

**文件路径**: `examples/release_highlights/plot_release_highlights_0_22_0.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `test_sklearn_compatible_estimator` | instance | `estimator, check` | `None` | `examples.release_highlights.plot_release_highlights_0_22_0.test_sklearn_compatible_estimator(estimator, check)` | simple | 2 | - |

---

## 📦 模块: `examples.release_highlights.plot_release_highlights_1_5_0`

**文件路径**: `examples/release_highlights/plot_release_highlights_1_5_0.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `custom_score` | instance | `y_observed, y_pred` | `None` | `examples.release_highlights.plot_release_highlights_1_5_0.custom_score(y_observed, y_pred)` | simple | 3 | - |
| 2 | `smallest_abs` | instance | `arr` | `None` | `examples.release_highlights.plot_release_highlights_1_5_0.smallest_abs(arr)` | simple | 3 | - |
| 3 | `levenshtein_distance` | instance | `x, y` | `None` | `examples.release_highlights.plot_release_highlights_1_5_0.levenshtein_distance(x, y)` | medium | 11 | 有逻辑 |

---

## 📦 模块: `examples.semi_supervised.plot_semi_supervised_newsgroups`

**文件路径**: `examples/semi_supervised/plot_semi_supervised_newsgroups.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `eval_and_get_f1` | instance | `clf, X_train, y_train, X_test, y_test` | `None` | `examples.semi_supervised.plot_semi_supervised_newsgroups.eval_and_get_f1(clf, X_train, y_train, X_test, y_test)` | simple | 10 | 有逻辑 |

---

## 📦 模块: `examples.svm.plot_custom_kernel`

**文件路径**: `examples/svm/plot_custom_kernel.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `my_kernel` | instance | `X, Y` | `None` | `examples.svm.plot_custom_kernel.my_kernel(X, Y)` | simple | 10 | - |

---

## 📦 模块: `examples.svm.plot_svm_kernels`

**文件路径**: `examples/svm/plot_svm_kernels.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_training_data_with_decision_boundary` | instance | `kernel, ax = None, long_title = True, support_v...` | `None` | `examples.svm.plot_svm_kernels.plot_training_data_with_decision_boundary(kernel, ax = None, long_title = True, support_vectors = True)` | complex | 49 | 有逻辑 |

---

## 📦 模块: `examples.svm.plot_weighted_samples`

**文件路径**: `examples/svm/plot_weighted_samples.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_decision_function` | instance | `classifier, sample_weight, axis, title` | `None` | `examples.svm.plot_weighted_samples.plot_decision_function(classifier, sample_weight, axis, title)` | medium | 22 | - |

---

## 📦 模块: `examples.text.plot_document_classification_20newsgroups`

**文件路径**: `examples/text/plot_document_classification_20newsgroups.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `size_mb` | instance | `docs` | `None` | `examples.text.plot_document_classification_20newsgroups.size_mb(docs)` | simple | 2 | 有逻辑 |
| 2 | `load_dataset` | instance | `verbose = False, remove = ()` | `None` | `examples.text.plot_document_classification_20newsgroups.load_dataset(verbose = False, remove = ())` | complex | 63 | 有逻辑 |
| 3 | `plot_feature_effects` | instance | `` | `None` | `examples.text.plot_document_classification_20newsgroups.plot_feature_effects()` | complex | 42 | 有逻辑 |
| 4 | `benchmark` | instance | `clf, custom_name = False` | `None` | `examples.text.plot_document_classification_20newsgroups.benchmark(clf, custom_name = False)` | medium | 28 | 有逻辑 |

---

## 📦 模块: `examples.text.plot_document_clustering`

**文件路径**: `examples/text/plot_document_clustering.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit_and_evaluate` | instance | `km, X, name = None, n_runs = 5` | `None` | `examples.text.plot_document_clustering.fit_and_evaluate(km, X, name = None, n_runs = 5)` | complex | 37 | 有逻辑 |

---

## 📦 模块: `examples.text.plot_hashing_vs_dict_vectorizer`

**文件路径**: `examples/text/plot_hashing_vs_dict_vectorizer.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `tokenize` | instance | `doc` | `None` | `examples.text.plot_hashing_vs_dict_vectorizer.tokenize(doc)` | simple | 8 | 有逻辑 |
| 2 | `token_freqs` | instance | `doc` | `None` | `examples.text.plot_hashing_vs_dict_vectorizer.token_freqs(doc)` | simple | 7 | 有逻辑 |
| 3 | `n_nonzero_columns` | instance | `X` | `None` | `examples.text.plot_hashing_vs_dict_vectorizer.n_nonzero_columns(X)` | simple | 7 | - |

---

## 📦 模块: `sklearn.__check_build.__init__`

**文件路径**: `sklearn/__check_build/__init__.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `raise_build_error` | instance | `e` | `None` | `sklearn.__check_build.__init__.raise_build_error(e)` | medium | 29 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.__init__`

**文件路径**: `sklearn/__init__.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `setup_module` | instance | `module` | `None` | `sklearn.__init__.setup_module(module)` | simple | 13 | 有逻辑 |

---

## 📦 模块: `sklearn._build_utils.tempita`

**文件路径**: `sklearn/_build_utils/tempita.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `process_tempita` | instance | `fromfile, outfile = None` | `None` | `sklearn._build_utils.tempita.process_tempita(fromfile, outfile = None)` | medium | 15 | - |
| 2 | `main` | instance | `` | `None` | `sklearn._build_utils.tempita.main()` | medium | 27 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn._config`

**文件路径**: `sklearn/_config.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_config` | instance | `` | `None` | `sklearn._config.get_config()` | medium | 26 | 有逻辑 |
| 2 | `set_config` | instance | `assume_finite = None, working_memory = None, pr...` | `None` | `sklearn._config.set_config(assume_finite = None, working_memory = None, print_changed_only = None, display = None, pairwise_dist_chunk_size = None, enable_cython_pairwise_dist = None, array_api_dispatch = None, transform_output = None, enable_metadata_routing = None, skip_parameter_validation = None)` | complex | 168 | 有逻辑 |
| 3 | `config_context` | instance | `assume_finite = None, working_memory = None, pr...` | `None` | `sklearn._config.config_context(assume_finite = None, working_memory = None, print_changed_only = None, display = None, pairwise_dist_chunk_size = None, enable_cython_pairwise_dist = None, array_api_dispatch = None, transform_output = None, enable_metadata_routing = None, skip_parameter_validation = None)` | complex | 174 | 有逻辑 |

---

## 📦 模块: `sklearn.base`

**文件路径**: `sklearn/base.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `clone` | instance | `estimator, safe = True` | `None` | `sklearn.base.clone(estimator, safe = True)` | complex | 52 | 有逻辑 |
| 2 | `is_classifier` | instance | `estimator` | `None` | `sklearn.base.is_classifier(estimator)` | medium | 29 | 有逻辑 |
| 3 | `is_regressor` | instance | `estimator` | `None` | `sklearn.base.is_regressor(estimator)` | medium | 29 | 有逻辑 |
| 4 | `is_clusterer` | instance | `estimator` | `None` | `sklearn.base.is_clusterer(estimator)` | medium | 31 | 有逻辑 |
| 5 | `is_outlier_detector` | instance | `estimator` | `None` | `sklearn.base.is_outlier_detector(estimator)` | medium | 14 | 有逻辑 |

---

## 📦 模块: `sklearn.calibration`

**文件路径**: `sklearn/calibration.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `calibration_curve` | instance | `y_true, y_prob, pos_label = None, n_bins = 5, s...` | `None` | `sklearn.calibration.calibration_curve(y_true, y_prob, pos_label = None, n_bins = 5, strategy = 'uniform')` | complex | 116 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.cluster._affinity_propagation`

**文件路径**: `sklearn/cluster/_affinity_propagation.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `affinity_propagation` | instance | `S, preference = None, convergence_iter = 15, ma...` | `None` | `sklearn.cluster._affinity_propagation.affinity_propagation(S, preference = None, convergence_iter = 15, max_iter = 200, damping = 0.5, copy = True, verbose = False, return_n_iter = False, random_state = None)` | complex | 121 | 有逻辑 |

---

## 📦 模块: `sklearn.cluster._agglomerative`

**文件路径**: `sklearn/cluster/_agglomerative.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `ward_tree` | instance | `X, connectivity = None, n_clusters = None, retu...` | `None` | `sklearn.cluster._agglomerative.ward_tree(X, connectivity = None, n_clusters = None, return_distance = False)` | complex | 232 | 抛异常, 有逻辑 |
| 2 | `linkage_tree` | instance | `X, connectivity = None, n_clusters = None, link...` | `None` | `sklearn.cluster._agglomerative.linkage_tree(X, connectivity = None, n_clusters = None, linkage = 'complete', affinity = 'euclidean', return_distance = False)` | complex | 274 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.cluster._dbscan`

**文件路径**: `sklearn/cluster/_dbscan.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `dbscan` | instance | `X, eps = 0.5, min_samples = 5, metric = 'minkow...` | `None` | `sklearn.cluster._dbscan.dbscan(X, eps = 0.5, min_samples = 5, metric = 'minkowski', metric_params = None, algorithm = 'auto', leaf_size = 30, p = 2, sample_weight = None, n_jobs = None)` | complex | 170 | 有逻辑 |

---

## 📦 模块: `sklearn.cluster._hdbscan.hdbscan`

**文件路径**: `sklearn/cluster/_hdbscan/hdbscan.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `remap_single_linkage_tree` | instance | `tree, internal_to_raw, non_finite` | `None` | `sklearn.cluster._hdbscan.hdbscan.remap_single_linkage_tree(tree, internal_to_raw, non_finite)` | complex | 43 | 有逻辑 |

---

## 📦 模块: `sklearn.cluster._kmeans`

**文件路径**: `sklearn/cluster/_kmeans.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `kmeans_plusplus` | instance | `X, n_clusters, sample_weight = None, x_squared_...` | `None` | `sklearn.cluster._kmeans.kmeans_plusplus(X, n_clusters, sample_weight = None, x_squared_norms = None, random_state = None, n_local_trials = None)` | complex | 104 | 抛异常, 有逻辑 |
| 2 | `k_means` | instance | `X, n_clusters, sample_weight = None, init = 'k-...` | `None` | `sklearn.cluster._kmeans.k_means(X, n_clusters, sample_weight = None, init = 'k-means++', n_init = 'auto', max_iter = 300, verbose = False, tol = 0.0001, random_state = None, copy_x = True, algorithm = 'lloyd', return_n_iter = False)` | complex | 156 | 有逻辑 |

---

## 📦 模块: `sklearn.cluster._mean_shift`

**文件路径**: `sklearn/cluster/_mean_shift.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `estimate_bandwidth` | instance | `X, quantile = 0.3, n_samples = None, random_sta...` | `None` | `sklearn.cluster._mean_shift.estimate_bandwidth(X, quantile = 0.3, n_samples = None, random_state = 0, n_jobs = None)` | complex | 64 | 有逻辑 |
| 2 | `mean_shift` | instance | `X, bandwidth = None, seeds = None, bin_seeding ...` | `None` | `sklearn.cluster._mean_shift.mean_shift(X, bandwidth = None, seeds = None, bin_seeding = False, min_bin_freq = 1, cluster_all = True, max_iter = 300, n_jobs = None)` | complex | 110 | 有逻辑 |
| 3 | `get_bin_seeds` | instance | `X, bin_size, min_bin_freq = 1` | `None` | `sklearn.cluster._mean_shift.get_bin_seeds(X, bin_size, min_bin_freq = 1)` | complex | 51 | 有逻辑 |

---

## 📦 模块: `sklearn.cluster._optics`

**文件路径**: `sklearn/cluster/_optics.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute_optics_graph` | instance | `X, min_samples, max_eps, metric, p, metric_para...` | `None` | `sklearn.cluster._optics.compute_optics_graph(X, min_samples, max_eps, metric, p, metric_params, algorithm, leaf_size, n_jobs)` | complex | 211 | 有逻辑 |
| 2 | `cluster_optics_dbscan` | instance | `reachability, core_distances, ordering, eps` | `None` | `sklearn.cluster._optics.cluster_optics_dbscan(reachability, core_distances, ordering, eps)` | complex | 63 | 有逻辑 |
| 3 | `cluster_optics_xi` | instance | `reachability, predecessor, ordering, min_sample...` | `None` | `sklearn.cluster._optics.cluster_optics_xi(reachability, predecessor, ordering, min_samples, min_cluster_size = None, xi = 0.05, predecessor_correction = True)` | complex | 109 | 有逻辑 |

---

## 📦 模块: `sklearn.cluster._spectral`

**文件路径**: `sklearn/cluster/_spectral.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `cluster_qr` | instance | `vectors` | `None` | `sklearn.cluster._spectral.cluster_qr(vectors)` | medium | 30 | - |
| 2 | `discretize` | instance | `vectors, copy = True, max_svd_restarts = 30, n_...` | `None` | `sklearn.cluster._spectral.discretize(vectors, copy = True, max_svd_restarts = 30, n_iter_max = 20, random_state = None)` | complex | 133 | 抛异常, 有逻辑 |
| 3 | `spectral_clustering` | instance | `affinity, n_clusters = 8, n_components = None, ...` | `None` | `sklearn.cluster._spectral.spectral_clustering(affinity, n_clusters = 8, n_components = None, eigen_solver = None, random_state = None, n_init = 10, eigen_tol = 'auto', assign_labels = 'kmeans', verbose = False)` | complex | 183 | 有逻辑 |

---

## 📦 模块: `sklearn.compose._column_transformer`

**文件路径**: `sklearn/compose/_column_transformer.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_column_transformer` | instance | `*transformers, remainder = 'drop', sparse_thres...` | `None` | `sklearn.compose._column_transformer.make_column_transformer(*transformers, remainder = 'drop', sparse_threshold = 0.3, n_jobs = None, verbose = False, verbose_feature_names_out = True, force_int_remainder_cols = 'deprecated')` | complex | 132 | 有逻辑 |

---

## 📦 模块: `sklearn.conftest`

**文件路径**: `sklearn/conftest.py`

**模块函数数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `raccoon_face_or_skip` | instance | `` | `None` | `sklearn.conftest.raccoon_face_or_skip()` | simple | 11 | 抛异常, 有逻辑 |
| 2 | `global_dtype` | instance | `request` | `None` | `sklearn.conftest.global_dtype(request)` | simple | 2 | - |
| 3 | `pytest_collection_modifyitems` | instance | `config, items` | `None` | `sklearn.conftest.pytest_collection_modifyitems(config, items)` | complex | 122 | 有逻辑 |
| 4 | `pyplot` | instance | `` | `None` | `sklearn.conftest.pyplot()` | medium | 16 | 有逻辑 |
| 5 | `pytest_generate_tests` | instance | `metafunc` | `None` | `sklearn.conftest.pytest_generate_tests(metafunc)` | medium | 43 | 抛异常, 有逻辑 |
| 6 | `pytest_addoption` | instance | `parser, pluginmanager` | `None` | `sklearn.conftest.pytest_addoption(parser, pluginmanager)` | simple | 3 | 有逻辑 |
| 7 | `pytest_configure` | instance | `config` | `None` | `sklearn.conftest.pytest_configure(config)` | complex | 42 | 有逻辑 |
| 8 | `hide_available_pandas` | instance | `monkeypatch` | `None` | `sklearn.conftest.hide_available_pandas(monkeypatch)` | simple | 10 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.covariance._empirical_covariance`

**文件路径**: `sklearn/covariance/_empirical_covariance.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `log_likelihood` | instance | `emp_cov, precision` | `None` | `sklearn.covariance._empirical_covariance.log_likelihood(emp_cov, precision)` | medium | 25 | 有逻辑 |
| 2 | `empirical_covariance` | instance | `X, assume_centered = False` | `None` | `sklearn.covariance._empirical_covariance.empirical_covariance(X, assume_centered = False)` | complex | 47 | 有逻辑 |

---

## 📦 模块: `sklearn.covariance._graph_lasso`

**文件路径**: `sklearn/covariance/_graph_lasso.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `alpha_max` | instance | `emp_cov` | `None` | `sklearn.covariance._graph_lasso.alpha_max(emp_cov)` | medium | 17 | 有逻辑 |
| 2 | `graphical_lasso` | instance | `emp_cov, alpha, mode = 'cd', tol = 0.0001, enet...` | `None` | `sklearn.covariance._graph_lasso.graphical_lasso(emp_cov, alpha, mode = 'cd', tol = 0.0001, enet_tol = 0.0001, max_iter = 100, verbose = False, return_costs = False, eps = np.finfo(np.float64).eps, return_n_iter = False)` | complex | 128 | 有逻辑 |
| 3 | `graphical_lasso_path` | instance | `X, alphas, cov_init = None, X_test = None, mode...` | `None` | `sklearn.covariance._graph_lasso.graphical_lasso_path(X, alphas, cov_init = None, X_test = None, mode = 'cd', tol = 0.0001, enet_tol = 0.0001, max_iter = 100, verbose = False, eps = np.finfo(np.float64).eps)` | complex | 126 | 有逻辑 |

---

## 📦 模块: `sklearn.covariance._robust_covariance`

**文件路径**: `sklearn/covariance/_robust_covariance.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `c_step` | instance | `X, n_support, remaining_iterations = 30, initia...` | `None` | `sklearn.covariance._robust_covariance.c_step(X, n_support, remaining_iterations = 30, initial_estimates = None, verbose = False, cov_computation_method = empirical_covariance, random_state = None)` | complex | 76 | 有逻辑 |
| 2 | `select_candidates` | instance | `X, n_support, n_trials, select = 1, n_iter = 30...` | `None` | `sklearn.covariance._robust_covariance.select_candidates(X, n_support, n_trials, select = 1, n_iter = 30, verbose = False, cov_computation_method = empirical_covariance, random_state = None)` | complex | 144 | 抛异常, 有逻辑 |
| 3 | `fast_mcd` | instance | `X, support_fraction = None, cov_computation_met...` | `None` | `sklearn.covariance._robust_covariance.fast_mcd(X, support_fraction = None, cov_computation_method = empirical_covariance, random_state = None)` | complex | 220 | 有逻辑 |

---

## 📦 模块: `sklearn.covariance._shrunk_covariance`

**文件路径**: `sklearn/covariance/_shrunk_covariance.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `shrunk_covariance` | instance | `emp_cov, shrinkage = 0.1` | `None` | `sklearn.covariance._shrunk_covariance.shrunk_covariance(emp_cov, shrinkage = 0.1)` | complex | 48 | 有逻辑 |
| 2 | `ledoit_wolf_shrinkage` | instance | `X, assume_centered = False, block_size = 1000` | `None` | `sklearn.covariance._shrunk_covariance.ledoit_wolf_shrinkage(X, assume_centered = False, block_size = 1000)` | complex | 104 | 有逻辑 |
| 3 | `ledoit_wolf` | instance | `X, assume_centered = False, block_size = 1000` | `None` | `sklearn.covariance._shrunk_covariance.ledoit_wolf(X, assume_centered = False, block_size = 1000)` | complex | 58 | 有逻辑 |
| 4 | `oas` | instance | `X, assume_centered = False` | `None` | `sklearn.covariance._shrunk_covariance.oas(X, assume_centered = False)` | complex | 65 | 有逻辑 |

---

## 📦 模块: `sklearn.datasets._arff_parser`

**文件路径**: `sklearn/datasets/_arff_parser.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `load_arff_from_gzip_file` | instance | `gzip_file, parser, output_type, openml_columns_...` | `None` | `sklearn.datasets._arff_parser.load_arff_from_gzip_file(gzip_file, parser, output_type, openml_columns_info, feature_names_to_select, target_names_to_select, shape = None, read_csv_kwargs = None)` | complex | 81 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._base`

**文件路径**: `sklearn/datasets/_base.py`

**模块函数数**: 15

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_data_home` | instance | `data_home = None` | `str` | `sklearn.datasets._base.get_data_home(data_home = None)` | complex | 39 | 有逻辑 |
| 2 | `clear_data_home` | instance | `data_home = None` | `None` | `sklearn.datasets._base.clear_data_home(data_home = None)` | medium | 16 | - |
| 3 | `load_files` | instance | `container_path, description = None, categories ...` | `None` | `sklearn.datasets._base.load_files(container_path, description = None, categories = None, load_content = True, shuffle = True, encoding = None, decode_error = 'strict', random_state = 0, allowed_extensions = None)` | complex | 178 | 有逻辑 |
| 4 | `load_csv_data` | instance | `data_file_name, data_module = DATA_MODULE, desc...` | `None` | `sklearn.datasets._base.load_csv_data(data_file_name, data_module = DATA_MODULE, descr_file_name = None, descr_module = DESCR_MODULE, encoding = 'utf-8')` | complex | 72 | 有逻辑 |
| 5 | `load_gzip_compressed_csv_data` | instance | `data_file_name, data_module = DATA_MODULE, desc...` | `None` | `sklearn.datasets._base.load_gzip_compressed_csv_data(data_file_name, data_module = DATA_MODULE, descr_file_name = None, descr_module = DESCR_MODULE, encoding = 'utf-8', **kwargs)` | complex | 63 | 有逻辑 |
| 6 | `load_descr` | instance | `descr_file_name, descr_module = DESCR_MODULE, e...` | `None` | `sklearn.datasets._base.load_descr(descr_file_name, descr_module = DESCR_MODULE, encoding = 'utf-8')` | medium | 28 | - |
| 7 | `load_wine` | instance | `return_X_y = False, as_frame = False` | `None` | `sklearn.datasets._base.load_wine(return_X_y = False, as_frame = False)` | complex | 118 | 有逻辑 |
| 8 | `load_iris` | instance | `return_X_y = False, as_frame = False` | `None` | `sklearn.datasets._base.load_iris(return_X_y = False, as_frame = False)` | complex | 123 | 有逻辑 |
| 9 | `load_breast_cancer` | instance | `return_X_y = False, as_frame = False` | `None` | `sklearn.datasets._base.load_breast_cancer(return_X_y = False, as_frame = False)` | complex | 147 | 有逻辑 |
| 10 | `load_digits` | instance | `n_class = 10, return_X_y = False, as_frame = False` | `None` | `sklearn.datasets._base.load_digits(n_class = 10, return_X_y = False, as_frame = False)` | complex | 130 | 有逻辑 |
| 11 | `load_diabetes` | instance | `return_X_y = False, as_frame = False, scaled = ...` | `None` | `sklearn.datasets._base.load_diabetes(return_X_y = False, as_frame = False, scaled = True)` | complex | 118 | 有逻辑 |
| 12 | `load_linnerud` | instance | `return_X_y = False, as_frame = False` | `None` | `sklearn.datasets._base.load_linnerud(return_X_y = False, as_frame = False)` | complex | 118 | 有逻辑 |
| 13 | `load_sample_images` | instance | `` | `None` | `sklearn.datasets._base.load_sample_images()` | complex | 61 | 抛异常, 有逻辑 |
| 14 | `load_sample_image` | instance | `image_name` | `None` | `sklearn.datasets._base.load_sample_image(image_name)` | complex | 39 | 抛异常, 有逻辑 |
| 15 | `fetch_file` | instance | `url, folder = None, local_filename = None, sha2...` | `None` | `sklearn.datasets._base.fetch_file(url, folder = None, local_filename = None, sha256 = None, n_retries = 3, delay = 1)` | complex | 53 | 有逻辑 |

---

## 📦 模块: `sklearn.datasets._california_housing`

**文件路径**: `sklearn/datasets/_california_housing.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_california_housing` | instance | `data_home = None, download_if_missing = True, r...` | `None` | `sklearn.datasets._california_housing.fetch_california_housing(data_home = None, download_if_missing = True, return_X_y = False, as_frame = False, n_retries = 3, delay = 1.0)` | complex | 180 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._covtype`

**文件路径**: `sklearn/datasets/_covtype.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_covtype` | instance | `data_home = None, download_if_missing = True, r...` | `None` | `sklearn.datasets._covtype.fetch_covtype(data_home = None, download_if_missing = True, random_state = None, shuffle = False, return_X_y = False, as_frame = False, n_retries = 3, delay = 1.0)` | complex | 174 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._kddcup99`

**文件路径**: `sklearn/datasets/_kddcup99.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_kddcup99` | instance | `subset = None, data_home = None, shuffle = Fals...` | `None` | `sklearn.datasets._kddcup99.fetch_kddcup99(subset = None, data_home = None, shuffle = False, random_state = None, percent10 = True, download_if_missing = True, return_X_y = False, as_frame = False, n_retries = 3, delay = 1.0)` | complex | 195 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._lfw`

**文件路径**: `sklearn/datasets/_lfw.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_lfw_people` | instance | `data_home = None, funneled = True, resize = 0.5...` | `None` | `sklearn.datasets._lfw.fetch_lfw_people(data_home = None, funneled = True, resize = 0.5, min_faces_per_person = 0, color = False, slice_ = (slice(70, 195), slice(78, 172)), download_if_missing = True, return_X_y = False, n_retries = 3, delay = 1.0)` | complex | 159 | 抛异常, 有逻辑 |
| 2 | `fetch_lfw_pairs` | instance | `subset = 'train', data_home = None, funneled = ...` | `None` | `sklearn.datasets._lfw.fetch_lfw_pairs(subset = 'train', data_home = None, funneled = True, resize = 0.5, color = False, slice_ = (slice(70, 195), slice(78, 172)), download_if_missing = True, n_retries = 3, delay = 1.0)` | complex | 157 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._olivetti_faces`

**文件路径**: `sklearn/datasets/_olivetti_faces.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_olivetti_faces` | instance | `data_home = None, shuffle = False, random_state...` | `None` | `sklearn.datasets._olivetti_faces.fetch_olivetti_faces(data_home = None, shuffle = False, random_state = 0, download_if_missing = True, return_X_y = False, n_retries = 3, delay = 1.0)` | complex | 133 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._openml`

**文件路径**: `sklearn/datasets/_openml.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_openml` | instance | `name: Optional[str] = None, version: Union[(str...` | `None` | `sklearn.datasets._openml.fetch_openml(name: Optional[str] = None, version: Union[(str, int)] = 'active', data_id: Optional[int] = None, data_home: Optional[Union[(str, os.PathLike)]] = None, target_column: Optional[Union[(str, List)]] = 'default-target', cache: bool = True, return_X_y: bool = False, as_frame: Union[(str, bool)] = 'auto', n_retries: int = 3, delay: float = 1.0, parser: str = 'auto', read_csv_kwargs: Optional[Dict] = None)` | complex | 387 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._rcv1`

**文件路径**: `sklearn/datasets/_rcv1.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fetch_rcv1` | instance | `data_home = None, subset = 'all', download_if_m...` | `None` | `sklearn.datasets._rcv1.fetch_rcv1(data_home = None, subset = 'all', download_if_missing = True, random_state = None, shuffle = False, return_X_y = False, n_retries = 3, delay = 1.0)` | complex | 229 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._samples_generator`

**文件路径**: `sklearn/datasets/_samples_generator.py`

**模块函数数**: 20

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_classification` | instance | `n_samples = 100, n_features = 20, n_informative...` | `None` | `sklearn.datasets._samples_generator.make_classification(n_samples = 100, n_features = 20, n_informative = 2, n_redundant = 2, n_repeated = 0, n_classes = 2, n_clusters_per_class = 2, weights = None, flip_y = 0.01, class_sep = 1.0, hypercube = True, shift = 0.0, scale = 1.0, shuffle = True, random_state = None, return_X_y = True)` | complex | 321 | 抛异常, 有逻辑 |
| 2 | `make_multilabel_classification` | instance | `n_samples = 100, n_features = 20, n_classes = 5...` | `None` | `sklearn.datasets._samples_generator.make_multilabel_classification(n_samples = 100, n_features = 20, n_classes = 5, n_labels = 2, length = 50, allow_unlabeled = True, sparse = False, return_indicator = 'dense', return_distributions = False, random_state = None)` | complex | 165 | 有逻辑 |
| 3 | `make_hastie_10_2` | instance | `n_samples = 12000, random_state = None` | `None` | `sklearn.datasets._samples_generator.make_hastie_10_2(n_samples = 12000, random_state = None)` | complex | 57 | 有逻辑 |
| 4 | `make_regression` | instance | `n_samples = 100, n_features = 100, n_informativ...` | `None` | `sklearn.datasets._samples_generator.make_regression(n_samples = 100, n_features = 100, n_informative = 10, n_targets = 1, bias = 0.0, effective_rank = None, tail_strength = 0.5, noise = 0.0, shuffle = True, coef = False, random_state = None)` | complex | 147 | 有逻辑 |
| 5 | `make_circles` | instance | `n_samples = 100, shuffle = True, noise = None, ...` | `None` | `sklearn.datasets._samples_generator.make_circles(n_samples = 100, shuffle = True, noise = None, random_state = None, factor = 0.8)` | complex | 85 | 抛异常, 有逻辑 |
| 6 | `make_moons` | instance | `n_samples = 100, shuffle = True, noise = None, ...` | `None` | `sklearn.datasets._samples_generator.make_moons(n_samples = 100, shuffle = True, noise = None, random_state = None)` | complex | 76 | 抛异常, 有逻辑 |
| 7 | `make_blobs` | instance | `n_samples = 100, n_features = 2, centers = None...` | `None` | `sklearn.datasets._samples_generator.make_blobs(n_samples = 100, n_features = 2, centers = None, cluster_std = 1.0, center_box = (-10.0, 10.0), shuffle = True, random_state = None, return_centers = False)` | complex | 165 | 抛异常, 有逻辑 |
| 8 | `make_friedman1` | instance | `n_samples = 100, n_features = 10, noise = 0.0, ...` | `None` | `sklearn.datasets._samples_generator.make_friedman1(n_samples = 100, n_features = 10, noise = 0.0, random_state = None)` | complex | 73 | 有逻辑 |
| 9 | `make_friedman2` | instance | `n_samples = 100, noise = 0.0, random_state = None` | `None` | `sklearn.datasets._samples_generator.make_friedman2(n_samples = 100, noise = 0.0, random_state = None)` | complex | 74 | 有逻辑 |
| 10 | `make_friedman3` | instance | `n_samples = 100, noise = 0.0, random_state = None` | `None` | `sklearn.datasets._samples_generator.make_friedman3(n_samples = 100, noise = 0.0, random_state = None)` | complex | 74 | 有逻辑 |
| 11 | `make_low_rank_matrix` | instance | `n_samples = 100, n_features = 100, effective_ra...` | `None` | `sklearn.datasets._samples_generator.make_low_rank_matrix(n_samples = 100, n_features = 100, effective_rank = 10, tail_strength = 0.5, random_state = None)` | complex | 94 | 有逻辑 |
| 12 | `make_sparse_coded_signal` | instance | `n_samples, n_components, n_features, n_nonzero_...` | `None` | `sklearn.datasets._samples_generator.make_sparse_coded_signal(n_samples, n_components, n_features, n_nonzero_coefs, random_state = None)` | complex | 85 | 有逻辑 |
| 13 | `make_sparse_uncorrelated` | instance | `n_samples = 100, n_features = 10, random_state ...` | `None` | `sklearn.datasets._samples_generator.make_sparse_uncorrelated(n_samples = 100, n_features = 10, random_state = None)` | complex | 58 | 有逻辑 |
| 14 | `make_spd_matrix` | instance | `n_dim, random_state = None` | `None` | `sklearn.datasets._samples_generator.make_spd_matrix(n_dim, random_state = None)` | medium | 38 | 有逻辑 |
| 15 | `make_sparse_spd_matrix` | instance | `n_dim = 1, alpha = 0.95, norm_diag = False, sma...` | `None` | `sklearn.datasets._samples_generator.make_sparse_spd_matrix(n_dim = 1, alpha = 0.95, norm_diag = False, smallest_coef = 0.1, largest_coef = 0.9, sparse_format = None, random_state = None)` | complex | 103 | 有逻辑 |
| 16 | `make_swiss_roll` | instance | `n_samples = 100, noise = 0.0, random_state = No...` | `None` | `sklearn.datasets._samples_generator.make_swiss_roll(n_samples = 100, noise = 0.0, random_state = None, hole = False)` | complex | 74 | 有逻辑 |
| 17 | `make_s_curve` | instance | `n_samples = 100, noise = 0.0, random_state = None` | `None` | `sklearn.datasets._samples_generator.make_s_curve(n_samples = 100, noise = 0.0, random_state = None)` | complex | 47 | 有逻辑 |
| 18 | `make_gaussian_quantiles` | instance | `mean = None, cov = 1.0, n_samples = 100, n_feat...` | `None` | `sklearn.datasets._samples_generator.make_gaussian_quantiles(mean = None, cov = 1.0, n_samples = 100, n_features = 2, n_classes = 3, shuffle = True, random_state = None)` | complex | 106 | 抛异常, 有逻辑 |
| 19 | `make_biclusters` | instance | `shape, n_clusters, noise = 0.0, minval = 10, ma...` | `None` | `sklearn.datasets._samples_generator.make_biclusters(shape, n_clusters, noise = 0.0, minval = 10, maxval = 100, shuffle = True, random_state = None)` | complex | 108 | 有逻辑 |
| 20 | `make_checkerboard` | instance | `shape, n_clusters, noise = 0.0, minval = 10, ma...` | `None` | `sklearn.datasets._samples_generator.make_checkerboard(shape, n_clusters, noise = 0.0, minval = 10, maxval = 100, shuffle = True, random_state = None)` | complex | 128 | 有逻辑 |

---

## 📦 模块: `sklearn.datasets._species_distributions`

**文件路径**: `sklearn/datasets/_species_distributions.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `construct_grids` | instance | `batch` | `None` | `sklearn.datasets._species_distributions.construct_grids(batch)` | medium | 25 | 有逻辑 |
| 2 | `fetch_species_distributions` | instance | `data_home = None, download_if_missing = True, n...` | `None` | `sklearn.datasets._species_distributions.fetch_species_distributions(data_home = None, download_if_missing = True, n_retries = 3, delay = 1.0)` | complex | 149 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._svmlight_format_io`

**文件路径**: `sklearn/datasets/_svmlight_format_io.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `load_svmlight_file` | instance | `f, n_features = None, dtype = np.float64, multi...` | `None` | `sklearn.datasets._svmlight_format_io.load_svmlight_file(f, n_features = None, dtype = np.float64, multilabel = False, zero_based = 'auto', query_id = False, offset = 0, length = -1)` | complex | 137 | 有逻辑 |
| 2 | `load_svmlight_files` | instance | `files, n_features = None, dtype = np.float64, m...` | `None` | `sklearn.datasets._svmlight_format_io.load_svmlight_files(files, n_features = None, dtype = np.float64, multilabel = False, zero_based = 'auto', query_id = False, offset = 0, length = -1)` | complex | 162 | 抛异常, 有逻辑 |
| 3 | `dump_svmlight_file` | instance | `X, y, f, zero_based = True, comment = None, que...` | `None` | `sklearn.datasets._svmlight_format_io.dump_svmlight_file(X, y, f, zero_based = True, comment = None, query_id = None, multilabel = False)` | complex | 129 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.datasets._twenty_newsgroups`

**文件路径**: `sklearn/datasets/_twenty_newsgroups.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `strip_newsgroup_header` | instance | `text` | `None` | `sklearn.datasets._twenty_newsgroups.strip_newsgroup_header(text)` | medium | 12 | - |
| 2 | `strip_newsgroup_quoting` | instance | `text` | `None` | `sklearn.datasets._twenty_newsgroups.strip_newsgroup_quoting(text)` | medium | 13 | 有逻辑 |
| 3 | `strip_newsgroup_footer` | instance | `text` | `None` | `sklearn.datasets._twenty_newsgroups.strip_newsgroup_footer(text)` | medium | 23 | 有逻辑 |
| 4 | `fetch_20newsgroups` | instance | `data_home = None, subset = 'train', categories ...` | `None` | `sklearn.datasets._twenty_newsgroups.fetch_20newsgroups(data_home = None, subset = 'train', categories = None, shuffle = True, random_state = 42, remove = (), download_if_missing = True, return_X_y = False, n_retries = 3, delay = 1.0)` | complex | 210 | 抛异常, 有逻辑 |
| 5 | `fetch_20newsgroups_vectorized` | instance | `subset = 'train', remove = (), data_home = None...` | `None` | `sklearn.datasets._twenty_newsgroups.fetch_20newsgroups_vectorized(subset = 'train', remove = (), data_home = None, download_if_missing = True, return_X_y = False, normalize = True, as_frame = False, n_retries = 3, delay = 1.0)` | complex | 223 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.decomposition._dict_learning`

**文件路径**: `sklearn/decomposition/_dict_learning.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `sparse_encode` | instance | `X, dictionary, gram = None, cov = None, algorit...` | `None` | `sklearn.decomposition._dict_learning.sparse_encode(X, dictionary, gram = None, cov = None, algorithm = 'lasso_lars', n_nonzero_coefs = None, alpha = None, copy_cov = True, init = None, max_iter = 1000, n_jobs = None, check_input = True, verbose = 0, positive = False)` | complex | 163 | 抛异常, 有逻辑 |
| 2 | `dict_learning_online` | instance | `X, n_components = 2, alpha = 1, max_iter = 100,...` | `None` | `sklearn.decomposition._dict_learning.dict_learning_online(X, n_components = 2, alpha = 1, max_iter = 100, return_code = True, dict_init = None, callback = None, batch_size = 256, verbose = False, shuffle = True, n_jobs = None, method = 'lars', random_state = None, positive_dict = False, positive_code = False, method_max_iter = 1000, tol = 0.001, max_no_improvement = 10)` | complex | 208 | 有逻辑 |
| 3 | `dict_learning` | instance | `X, n_components, alpha, max_iter = 100, tol = 1...` | `None` | `sklearn.decomposition._dict_learning.dict_learning(X, n_components, alpha, max_iter = 100, tol = 1e-08, method = 'lars', n_jobs = None, dict_init = None, code_init = None, callback = None, verbose = False, random_state = None, return_n_iter = False, positive_dict = False, positive_code = False, method_max_iter = 1000)` | complex | 177 | 有逻辑 |

---

## 📦 模块: `sklearn.decomposition._fastica`

**文件路径**: `sklearn/decomposition/_fastica.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fastica` | instance | `X, n_components = None, algorithm = 'parallel',...` | `None` | `sklearn.decomposition._fastica.fastica(X, n_components = None, algorithm = 'parallel', whiten = 'unit-variance', fun = 'logcosh', fun_args = None, max_iter = 200, tol = 0.0001, w_init = None, whiten_solver = 'svd', random_state = None, return_X_mean = False, compute_sources = True, return_n_iter = False)` | complex | 193 | 有逻辑 |

---

## 📦 模块: `sklearn.decomposition._nmf`

**文件路径**: `sklearn/decomposition/_nmf.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `norm` | instance | `x` | `None` | `sklearn.decomposition._nmf.norm(x)` | simple | 11 | 有逻辑 |
| 2 | `trace_dot` | instance | `X, Y` | `None` | `sklearn.decomposition._nmf.trace_dot(X, Y)` | simple | 11 | - |
| 3 | `non_negative_factorization` | instance | `X, W = None, H = None, n_components = 'auto', i...` | `None` | `sklearn.decomposition._nmf.non_negative_factorization(X, W = None, H = None, n_components = 'auto', init = None, update_H = True, solver = 'cd', beta_loss = 'frobenius', tol = 0.0001, max_iter = 200, alpha_W = 0.0, alpha_H = 'same', l1_ratio = 0.0, random_state = None, verbose = 0, shuffle = False)` | complex | 227 | 有逻辑 |

---

## 📦 模块: `sklearn.ensemble._gb`

**文件路径**: `sklearn/ensemble/_gb.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `set_huber_delta` | instance | `loss, y_true, raw_prediction, sample_weight = None` | `None` | `sklearn.ensemble._gb.set_huber_delta(loss, y_true, raw_prediction, sample_weight = None)` | simple | 6 | - |

---

## 📦 模块: `sklearn.ensemble._hist_gradient_boosting.utils`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/utils.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_equivalent_estimator` | instance | `estimator, lib = 'lightgbm', n_classes = None` | `None` | `sklearn.ensemble._hist_gradient_boosting.utils.get_equivalent_estimator(estimator, lib = 'lightgbm', n_classes = None)` | complex | 140 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.externals._arff`

**文件路径**: `sklearn/externals/_arff.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `encode_string` | instance | `s` | `None` | `sklearn.externals._arff.encode_string(s)` | simple | 4 | 有逻辑 |
| 2 | `load` | instance | `fp, encode_nominal = False, return_type = DENSE` | `None` | `sklearn.externals._arff.load(fp, encode_nominal = False, return_type = DENSE)` | medium | 17 | 有逻辑 |
| 3 | `loads` | instance | `s, encode_nominal = False, return_type = DENSE` | `None` | `sklearn.externals._arff.loads(s, encode_nominal = False, return_type = DENSE)` | medium | 17 | 有逻辑 |
| 4 | `dump` | instance | `obj, fp` | `None` | `sklearn.externals._arff.dump(obj, fp)` | medium | 17 | 有逻辑 |
| 5 | `dumps` | instance | `obj` | `None` | `sklearn.externals._arff.dumps(obj)` | simple | 8 | - |

---

## 📦 模块: `sklearn.externals._numpydoc.docscrape`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `strip_blank_lines` | instance | `l` | `None` | `sklearn.externals._numpydoc.docscrape.strip_blank_lines(l)` | simple | 7 | 有逻辑 |
| 2 | `dedent_lines` | instance | `lines` | `None` | `sklearn.externals._numpydoc.docscrape.dedent_lines(lines)` | simple | 3 | - |
| 3 | `get_doc_object` | instance | `obj, what = None, doc = None, config = None, cl...` | `None` | `sklearn.externals._numpydoc.docscrape.get_doc_object(obj, what = None, doc = None, config = None, class_doc = ClassDoc, func_doc = FunctionDoc, obj_doc = ObjDoc)` | medium | 29 | 有逻辑 |

---

## 📦 模块: `sklearn.externals._packaging.version`

**文件路径**: `sklearn/externals/_packaging/version.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `parse` | instance | `version: str` | `Union[('LegacyVersion', 'Version')]` | `sklearn.externals._packaging.version.parse(version: str)` | medium | 18 | 有逻辑 |

---

## 📦 模块: `sklearn.externals._scipy.sparse.csgraph._laplacian`

**文件路径**: `sklearn/externals/_scipy/sparse/csgraph/_laplacian.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `laplacian` | instance | `csgraph, normed = False, return_diag = False, u...` | `None` | `sklearn.externals._scipy.sparse.csgraph._laplacian.laplacian(csgraph, normed = False, return_diag = False, use_out_degree = False, copy = True, form = 'array', dtype = None, symmetrized = False)` | complex | 350 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat._internal`

**文件路径**: `sklearn/externals/array_api_compat/_internal.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_xp` | instance | `xp: ModuleType` | `Callable[([Callable[..., _T]], Callable[(Ellipsis, _T)])]` | `sklearn.externals.array_api_compat._internal.get_xp(xp: ModuleType)` | medium | 39 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat.common._aliases`

**文件路径**: `sklearn/externals/array_api_compat/common/_aliases.py`

**模块函数数**: 37

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `arange` | instance | `stop: float | None = None, step: float = 1, xp:...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.arange(stop: float | None = None, step: float = 1, xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 13 | - |
| 2 | `empty` | instance | `shape: int | tuple[(int, Ellipsis)], xp: Namesp...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.empty(shape: int | tuple[(int, Ellipsis)], xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | simple | 10 | - |
| 3 | `empty_like` | instance | `xp: Namespace, dtype: DType | None = None, devi...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.empty_like(xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 11 | - |
| 4 | `eye` | instance | `xp: Namespace, k: int = 0, dtype: DType | None ...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.eye(xp: Namespace, k: int = 0, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 13 | - |
| 5 | `full` | instance | `shape: int | tuple[(int, Ellipsis)], fill_value...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.full(shape: int | tuple[(int, Ellipsis)], fill_value: complex, xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 11 | - |
| 6 | `full_like` | instance | `fill_value: complex, xp: Namespace, dtype: DTyp...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.full_like(fill_value: complex, xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 12 | - |
| 7 | `linspace` | instance | `num: int, xp: Namespace, dtype: DType | None = ...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.linspace(num: int, xp: Namespace, dtype: DType | None = None, device: Device | None = None, endpoint: bool = True, **kwargs: object)` | medium | 14 | - |
| 8 | `ones` | instance | `shape: int | tuple[(int, Ellipsis)], xp: Namesp...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.ones(shape: int | tuple[(int, Ellipsis)], xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | simple | 10 | - |
| 9 | `ones_like` | instance | `xp: Namespace, dtype: DType | None = None, devi...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.ones_like(xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 11 | - |
| 10 | `zeros` | instance | `shape: int | tuple[(int, Ellipsis)], xp: Namesp...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.zeros(shape: int | tuple[(int, Ellipsis)], xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | simple | 10 | - |
| 11 | `zeros_like` | instance | `xp: Namespace, dtype: DType | None = None, devi...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.zeros_like(xp: Namespace, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 11 | - |
| 12 | `unique_all` | instance | `xp: Namespace` | `UniqueAllResult` | `sklearn.externals.array_api_compat.common._aliases.unique_all(xp: Namespace)` | medium | 18 | - |
| 13 | `unique_counts` | instance | `xp: Namespace` | `UniqueCountsResult` | `sklearn.externals.array_api_compat.common._aliases.unique_counts(xp: Namespace)` | simple | 7 | - |
| 14 | `unique_inverse` | instance | `xp: Namespace` | `UniqueInverseResult` | `sklearn.externals.array_api_compat.common._aliases.unique_inverse(xp: Namespace)` | medium | 13 | - |
| 15 | `unique_values` | instance | `xp: Namespace` | `Array` | `sklearn.externals.array_api_compat.common._aliases.unique_values(xp: Namespace)` | simple | 9 | - |
| 16 | `std` | instance | `xp: Namespace, axis: int | tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.std(xp: Namespace, axis: int | tuple[(int, Ellipsis)] | None = None, correction: float = 0.0, keepdims: bool = False, **kwargs: object)` | medium | 11 | - |
| 17 | `var` | instance | `xp: Namespace, axis: int | tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.var(xp: Namespace, axis: int | tuple[(int, Ellipsis)] | None = None, correction: float = 0.0, keepdims: bool = False, **kwargs: object)` | medium | 11 | - |
| 18 | `cumulative_sum` | instance | `xp: Namespace, axis: int | None = None, dtype: ...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.cumulative_sum(xp: Namespace, axis: int | None = None, dtype: DType | None = None, include_initial: bool = False, **kwargs: object)` | complex | 36 | 抛异常, 有逻辑 |
| 19 | `cumulative_prod` | instance | `xp: Namespace, axis: int | None = None, dtype: ...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.cumulative_prod(xp: Namespace, axis: int | None = None, dtype: DType | None = None, include_initial: bool = False, **kwargs: object)` | complex | 35 | 抛异常, 有逻辑 |
| 20 | `clip` | instance | `min: float | Array | None = None, max: float | ...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.clip(min: float | Array | None = None, max: float | Array | None = None, xp: Namespace, out: Array | None = None)` | complex | 65 | 有逻辑 |
| 21 | `permute_dims` | instance | `axes: tuple[(int, Ellipsis)], xp: Namespace` | `Array` | `sklearn.externals.array_api_compat.common._aliases.permute_dims(axes: tuple[(int, Ellipsis)], xp: Namespace)` | simple | 2 | - |
| 22 | `reshape` | instance | `shape: tuple[(int, Ellipsis)], xp: Namespace, c...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.reshape(shape: tuple[(int, Ellipsis)], xp: Namespace, copy: Optional[bool] = None, **kwargs: object)` | medium | 16 | 有逻辑 |
| 23 | `argsort` | instance | `xp: Namespace, axis: int = -1, descending: bool...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.argsort(xp: Namespace, axis: int = -1, descending: bool = False, stable: bool = True, **kwargs: object)` | medium | 30 | 有逻辑 |
| 24 | `sort` | instance | `xp: Namespace, axis: int = -1, descending: bool...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.sort(xp: Namespace, axis: int = -1, descending: bool = False, stable: bool = True, **kwargs: object)` | medium | 19 | 有逻辑 |
| 25 | `nonzero` | instance | `xp: Namespace, **kwargs: object` | `tuple[(Array, Ellipsis)]` | `sklearn.externals.array_api_compat.common._aliases.nonzero(xp: Namespace, **kwargs: object)` | simple | 4 | 抛异常, 有逻辑 |
| 26 | `ceil` | instance | `xp: Namespace, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._aliases.ceil(xp: Namespace, **kwargs: object)` | simple | 4 | 有逻辑 |
| 27 | `floor` | instance | `xp: Namespace, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._aliases.floor(xp: Namespace, **kwargs: object)` | simple | 4 | 有逻辑 |
| 28 | `trunc` | instance | `xp: Namespace, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._aliases.trunc(xp: Namespace, **kwargs: object)` | simple | 4 | 有逻辑 |
| 29 | `matmul` | instance | `xp: Namespace, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._aliases.matmul(xp: Namespace, **kwargs: object)` | simple | 2 | - |
| 30 | `matrix_transpose` | instance | `xp: Namespace` | `Array` | `sklearn.externals.array_api_compat.common._aliases.matrix_transpose(xp: Namespace)` | simple | 4 | 抛异常, 有逻辑 |
| 31 | `tensordot` | instance | `xp: Namespace, axes: int | tuple[(Sequence[int]...` | `Array` | `sklearn.externals.array_api_compat.common._aliases.tensordot(xp: Namespace, axes: int | tuple[(Sequence[int], Sequence[int])] = 2, **kwargs: object)` | simple | 10 | - |
| 32 | `vecdot` | instance | `xp: Namespace, axis: int = -1` | `Array` | `sklearn.externals.array_api_compat.common._aliases.vecdot(xp: Namespace, axis: int = -1)` | medium | 15 | 抛异常, 有逻辑 |
| 33 | `isdtype` | instance | `dtype: DType, kind: DType | str | tuple[(DType ...` | `bool` | `sklearn.externals.array_api_compat.common._aliases.isdtype(dtype: DType, kind: DType | str | tuple[(DType | str, Ellipsis)], xp: Namespace, _tuple: bool = True)` | complex | 45 | 抛异常, 有逻辑 |
| 34 | `unstack` | instance | `xp: Namespace, axis: int = 0` | `tuple[(Array, Ellipsis)]` | `sklearn.externals.array_api_compat.common._aliases.unstack(xp: Namespace, axis: int = 0)` | simple | 4 | 抛异常, 有逻辑 |
| 35 | `sign` | instance | `xp: Namespace, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._aliases.sign(xp: Namespace, **kwargs: object)` | simple | 12 | 有逻辑 |
| 36 | `finfo` | instance | `xp: Namespace` | `Any` | `sklearn.externals.array_api_compat.common._aliases.finfo(xp: Namespace)` | simple | 7 | 有逻辑 |
| 37 | `iinfo` | instance | `xp: Namespace` | `Any` | `sklearn.externals.array_api_compat.common._aliases.iinfo(xp: Namespace)` | simple | 5 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat.common._fft`

**文件路径**: `sklearn/externals/array_api_compat/common/_fft.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fft` | instance | `xp: Namespace, n: int | None = None, axis: int ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.fft(xp: Namespace, n: int | None = None, axis: int = -1, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 2 | `ifft` | instance | `xp: Namespace, n: int | None = None, axis: int ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.ifft(xp: Namespace, n: int | None = None, axis: int = -1, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 3 | `fftn` | instance | `xp: Namespace, s: Sequence[int] | None = None, ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.fftn(xp: Namespace, s: Sequence[int] | None = None, axes: Sequence[int] | None = None, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 4 | `ifftn` | instance | `xp: Namespace, s: Sequence[int] | None = None, ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.ifftn(xp: Namespace, s: Sequence[int] | None = None, axes: Sequence[int] | None = None, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 5 | `rfft` | instance | `xp: Namespace, n: int | None = None, axis: int ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.rfft(xp: Namespace, n: int | None = None, axis: int = -1, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 6 | `irfft` | instance | `xp: Namespace, n: int | None = None, axis: int ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.irfft(xp: Namespace, n: int | None = None, axis: int = -1, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 7 | `rfftn` | instance | `xp: Namespace, s: Sequence[int] | None = None, ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.rfftn(xp: Namespace, s: Sequence[int] | None = None, axes: Sequence[int] | None = None, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 8 | `irfftn` | instance | `xp: Namespace, s: Sequence[int] | None = None, ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.irfftn(xp: Namespace, s: Sequence[int] | None = None, axes: Sequence[int] | None = None, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 9 | `hfft` | instance | `xp: Namespace, n: int | None = None, axis: int ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.hfft(xp: Namespace, n: int | None = None, axis: int = -1, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 10 | `ihfft` | instance | `xp: Namespace, n: int | None = None, axis: int ...` | `Array` | `sklearn.externals.array_api_compat.common._fft.ihfft(xp: Namespace, n: int | None = None, axis: int = -1, norm: _Norm = 'backward')` | medium | 13 | 有逻辑 |
| 11 | `fftfreq` | instance | `xp: Namespace, d: float = 1.0, dtype: DType | N...` | `Array` | `sklearn.externals.array_api_compat.common._fft.fftfreq(xp: Namespace, d: float = 1.0, dtype: DType | None = None, device: Device | None = None)` | medium | 15 | 抛异常, 有逻辑 |
| 12 | `rfftfreq` | instance | `xp: Namespace, d: float = 1.0, dtype: DType | N...` | `Array` | `sklearn.externals.array_api_compat.common._fft.rfftfreq(xp: Namespace, d: float = 1.0, dtype: DType | None = None, device: Device | None = None)` | medium | 15 | 抛异常, 有逻辑 |
| 13 | `fftshift` | instance | `xp: Namespace, axes: int | Sequence[int] | None...` | `Array` | `sklearn.externals.array_api_compat.common._fft.fftshift(xp: Namespace, axes: int | Sequence[int] | None = None)` | simple | 4 | - |
| 14 | `ifftshift` | instance | `xp: Namespace, axes: int | Sequence[int] | None...` | `Array` | `sklearn.externals.array_api_compat.common._fft.ifftshift(xp: Namespace, axes: int | Sequence[int] | None = None)` | simple | 4 | - |

---

## 📦 模块: `sklearn.externals.array_api_compat.common._helpers`

**文件路径**: `sklearn/externals/array_api_compat/common/_helpers.py`

**模块函数数**: 25

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `is_numpy_array` | instance | `x: object` | `TypeGuard[npt.NDArray[Any]]` | `sklearn.externals.array_api_compat.common._helpers.is_numpy_array(x: object)` | medium | 27 | 有逻辑 |
| 2 | `is_cupy_array` | instance | `x: object` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_cupy_array(x: object)` | medium | 23 | 有逻辑 |
| 3 | `is_torch_array` | instance | `x: object` | `TypeIs[torch.Tensor]` | `sklearn.externals.array_api_compat.common._helpers.is_torch_array(x: object)` | medium | 20 | 有逻辑 |
| 4 | `is_ndonnx_array` | instance | `x: object` | `TypeIs[ndx.Array]` | `sklearn.externals.array_api_compat.common._helpers.is_ndonnx_array(x: object)` | medium | 21 | 有逻辑 |
| 5 | `is_dask_array` | instance | `x: object` | `TypeIs[da.Array]` | `sklearn.externals.array_api_compat.common._helpers.is_dask_array(x: object)` | medium | 21 | 有逻辑 |
| 6 | `is_jax_array` | instance | `x: object` | `TypeIs[jax.Array]` | `sklearn.externals.array_api_compat.common._helpers.is_jax_array(x: object)` | medium | 22 | 有逻辑 |
| 7 | `is_pydata_sparse_array` | instance | `x: object` | `TypeIs[sparse.SparseArray]` | `sklearn.externals.array_api_compat.common._helpers.is_pydata_sparse_array(x: object)` | medium | 23 | 有逻辑 |
| 8 | `is_array_api_obj` | instance | `x: object` | `TypeIs[_ArrayApiObj]` | `sklearn.externals.array_api_compat.common._helpers.is_array_api_obj(x: object)` | medium | 19 | 有逻辑 |
| 9 | `is_numpy_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_numpy_namespace(xp: Namespace)` | medium | 19 | 有逻辑 |
| 10 | `is_cupy_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_cupy_namespace(xp: Namespace)` | medium | 19 | 有逻辑 |
| 11 | `is_torch_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_torch_namespace(xp: Namespace)` | medium | 19 | 有逻辑 |
| 12 | `is_ndonnx_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_ndonnx_namespace(xp: Namespace)` | medium | 17 | 有逻辑 |
| 13 | `is_dask_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_dask_namespace(xp: Namespace)` | medium | 19 | 有逻辑 |
| 14 | `is_jax_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_jax_namespace(xp: Namespace)` | medium | 20 | 有逻辑 |
| 15 | `is_pydata_sparse_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_pydata_sparse_namespace(xp: Namespace)` | medium | 17 | 有逻辑 |
| 16 | `is_array_api_strict_namespace` | instance | `xp: Namespace` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_array_api_strict_namespace(xp: Namespace)` | medium | 17 | 有逻辑 |
| 17 | `array_namespace` | instance | `*xs: Array | complex | None, api_version: str |...` | `Namespace` | `sklearn.externals.array_api_compat.common._helpers.array_namespace(*xs: Array | complex | None, api_version: str | None = None, use_compat: bool | None = None)` | complex | 166 | 抛异常, 有逻辑 |
| 18 | `device` | instance | `` | `Device` | `sklearn.externals.array_api_compat.common._helpers.device()` | complex | 66 | 有逻辑 |
| 19 | `to_device` | instance | `stream: int | Any | None = None` | `Array` | `sklearn.externals.array_api_compat.common._helpers.to_device(stream: int | Any | None = None)` | complex | 81 | 抛异常, 有逻辑 |
| 20 | `size` | instance | `x: HasShape[Collection[SupportsIndex]]` | `int` | `sklearn.externals.array_api_compat.common._helpers.size(x: HasShape[Collection[SupportsIndex]])` | simple | 1 | - |
| 21 | `size` | instance | `x: HasShape[Collection[None]]` | `None` | `sklearn.externals.array_api_compat.common._helpers.size(x: HasShape[Collection[None]])` | simple | 1 | - |
| 22 | `size` | instance | `x: HasShape[Collection[SupportsIndex | None]]` | `int | None` | `sklearn.externals.array_api_compat.common._helpers.size(x: HasShape[Collection[SupportsIndex | None]])` | simple | 1 | - |
| 23 | `size` | instance | `x: HasShape[Collection[SupportsIndex | None]]` | `int | None` | `sklearn.externals.array_api_compat.common._helpers.size(x: HasShape[Collection[SupportsIndex | None]])` | simple | 18 | - |
| 24 | `is_writeable_array` | instance | `x: object` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_writeable_array(x: object)` | medium | 17 | 有逻辑 |
| 25 | `is_lazy_array` | instance | `x: object` | `bool` | `sklearn.externals.array_api_compat.common._helpers.is_lazy_array(x: object)` | medium | 54 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat.common._linalg`

**文件路径**: `sklearn/externals/array_api_compat/common/_linalg.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `cross` | instance | `xp: Namespace, axis: int = -1, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._linalg.cross(xp: Namespace, axis: int = -1, **kwargs: object)` | simple | 10 | - |
| 2 | `outer` | instance | `xp: Namespace, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._linalg.outer(xp: Namespace, **kwargs: object)` | simple | 2 | - |
| 3 | `eigh` | instance | `xp: Namespace, **kwargs: object` | `EighResult` | `sklearn.externals.array_api_compat.common._linalg.eigh(xp: Namespace, **kwargs: object)` | simple | 2 | - |
| 4 | `qr` | instance | `xp: Namespace, mode: Literal[('reduced', 'compl...` | `QRResult` | `sklearn.externals.array_api_compat.common._linalg.qr(xp: Namespace, mode: Literal[('reduced', 'complete')] = 'reduced', **kwargs: object)` | simple | 9 | - |
| 5 | `slogdet` | instance | `xp: Namespace, **kwargs: object` | `SlogdetResult` | `sklearn.externals.array_api_compat.common._linalg.slogdet(xp: Namespace, **kwargs: object)` | simple | 2 | - |
| 6 | `svd` | instance | `xp: Namespace, full_matrices: bool = True, **kw...` | `SVDResult` | `sklearn.externals.array_api_compat.common._linalg.svd(xp: Namespace, full_matrices: bool = True, **kwargs: object)` | simple | 9 | - |
| 7 | `cholesky` | instance | `xp: Namespace, upper: bool = False, **kwargs: o...` | `Array` | `sklearn.externals.array_api_compat.common._linalg.cholesky(xp: Namespace, upper: bool = False, **kwargs: object)` | medium | 15 | 有逻辑 |
| 8 | `matrix_rank` | instance | `xp: Namespace, rtol: float | Array | None = Non...` | `Array` | `sklearn.externals.array_api_compat.common._linalg.matrix_rank(xp: Namespace, rtol: float | Array | None = None, **kwargs: object)` | medium | 20 | 抛异常, 有逻辑 |
| 9 | `pinv` | instance | `xp: Namespace, rtol: float | Array | None = Non...` | `Array` | `sklearn.externals.array_api_compat.common._linalg.pinv(xp: Namespace, rtol: float | Array | None = None, **kwargs: object)` | medium | 13 | 有逻辑 |
| 10 | `matrix_norm` | instance | `xp: Namespace, keepdims: bool = False, ord: Lit...` | `Array` | `sklearn.externals.array_api_compat.common._linalg.matrix_norm(xp: Namespace, keepdims: bool = False, ord: Literal[(1, 2, -1, -2)] | JustFloat | Literal[('fro', 'nuc')] | None = 'fro')` | simple | 9 | - |
| 11 | `svdvals` | instance | `xp: Namespace` | `Array | tuple[(Array, Ellipsis)]` | `sklearn.externals.array_api_compat.common._linalg.svdvals(xp: Namespace)` | simple | 2 | - |
| 12 | `vector_norm` | instance | `xp: Namespace, axis: int | tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.common._linalg.vector_norm(xp: Namespace, axis: int | tuple[(int, Ellipsis)] | None = None, keepdims: bool = False, ord: JustInt | JustFloat = 2)` | complex | 51 | 有逻辑 |
| 13 | `diagonal` | instance | `xp: Namespace, offset: int = 0, **kwargs: object` | `Array` | `sklearn.externals.array_api_compat.common._linalg.diagonal(xp: Namespace, offset: int = 0, **kwargs: object)` | simple | 2 | - |
| 14 | `trace` | instance | `xp: Namespace, offset: int = 0, dtype: DType | ...` | `Array` | `sklearn.externals.array_api_compat.common._linalg.trace(xp: Namespace, offset: int = 0, dtype: DType | None = None, **kwargs: object)` | medium | 12 | - |

---

## 📦 模块: `sklearn.externals.array_api_compat.cupy._aliases`

**文件路径**: `sklearn/externals/array_api_compat/cupy/_aliases.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `asarray` | instance | `dtype: Optional[DType] = None, device: Optional...` | `Array` | `sklearn.externals.array_api_compat.cupy._aliases.asarray(dtype: Optional[DType] = None, device: Optional[Device] = None, copy: Optional[bool] = None, **kwargs)` | medium | 28 | 抛异常, 有逻辑 |
| 2 | `astype` | instance | `copy: bool = True, device: Optional[Device] = None` | `Array` | `sklearn.externals.array_api_compat.cupy._aliases.astype(copy: bool = True, device: Optional[Device] = None)` | medium | 12 | 有逻辑 |
| 3 | `count_nonzero` | instance | `x: Array, axis = None, keepdims = False` | `Array` | `sklearn.externals.array_api_compat.cupy._aliases.count_nonzero(x: Array, axis = None, keepdims = False)` | medium | 11 | 有逻辑 |
| 4 | `take_along_axis` | instance | `axis: int = -1` | `None` | `sklearn.externals.array_api_compat.cupy._aliases.take_along_axis(axis: int = -1)` | simple | 2 | - |

---

## 📦 模块: `sklearn.externals.array_api_compat.dask.array._aliases`

**文件路径**: `sklearn/externals/array_api_compat/dask/array/_aliases.py`

**模块函数数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `astype` | instance | `copy: py_bool = True, device: Device | None = None` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.astype(copy: py_bool = True, device: Device | None = None)` | medium | 21 | 有逻辑 |
| 2 | `arange` | instance | `stop: float | None = None, step: float = 1, dty...` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.arange(stop: float | None = None, step: float = 1, dtype: DType | None = None, device: Device | None = None, **kwargs: object)` | medium | 29 | 有逻辑 |
| 3 | `asarray` | instance | `dtype: DType | None = None, device: Device | No...` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.asarray(dtype: DType | None = None, device: Device | None = None, copy: py_bool | None = None, **kwargs: object)` | medium | 34 | 抛异常, 有逻辑 |
| 4 | `clip` | instance | `min: float | Array | None = None, max: float | ...` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.clip(min: float | Array | None = None, max: float | Array | None = None)` | medium | 36 | 有逻辑 |
| 5 | `sort` | instance | `axis: int = -1, descending: py_bool = False, st...` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.sort(axis: int = -1, descending: py_bool = False, stable: py_bool = True)` | medium | 33 | 有逻辑 |
| 6 | `argsort` | instance | `axis: int = -1, descending: py_bool = False, st...` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.argsort(axis: int = -1, descending: py_bool = False, stable: py_bool = True)` | complex | 35 | 有逻辑 |
| 7 | `count_nonzero` | instance | `x: Array, axis: int | None = None, keepdims: py...` | `Array` | `sklearn.externals.array_api_compat.dask.array._aliases.count_nonzero(x: Array, axis: int | None = None, keepdims: py_bool = False)` | medium | 11 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat.dask.array.linalg`

**文件路径**: `sklearn/externals/array_api_compat/dask/array/linalg.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `qr` | instance | `x: _Array, mode: Literal[('reduced', 'complete'...` | `QRResult` | `sklearn.externals.array_api_compat.dask.array.linalg.qr(x: _Array, mode: Literal[('reduced', 'complete')] = 'reduced', **kwargs: object)` | simple | 8 | 抛异常, 有逻辑 |
| 2 | `svd` | instance | `x: _Array, full_matrices: bool = True, **kwargs` | `SVDResult` | `sklearn.externals.array_api_compat.dask.array.linalg.svd(x: _Array, full_matrices: bool = True, **kwargs)` | simple | 4 | 抛异常, 有逻辑 |
| 3 | `svdvals` | instance | `x: _Array` | `_Array` | `sklearn.externals.array_api_compat.dask.array.linalg.svdvals(x: _Array)` | simple | 4 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat.numpy._aliases`

**文件路径**: `sklearn/externals/array_api_compat/numpy/_aliases.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `asarray` | instance | `dtype: DType | None = None, device: Device | No...` | `Array` | `sklearn.externals.array_api_compat.numpy._aliases.asarray(dtype: DType | None = None, device: Device | None = None, copy: _Copy | None = None, **kwargs: Any)` | medium | 25 | 有逻辑 |
| 2 | `astype` | instance | `copy: py_bool = True, device: Device | None = None` | `Array` | `sklearn.externals.array_api_compat.numpy._aliases.astype(copy: py_bool = True, device: Device | None = None)` | simple | 10 | - |
| 3 | `count_nonzero` | instance | `x: Array, axis: int | tuple[(int, Ellipsis)] | ...` | `Array` | `sklearn.externals.array_api_compat.numpy._aliases.count_nonzero(x: Array, axis: int | tuple[(int, Ellipsis)] | None = None, keepdims: py_bool = False)` | simple | 11 | 有逻辑 |
| 4 | `take_along_axis` | instance | `axis: int = -1` | `None` | `sklearn.externals.array_api_compat.numpy._aliases.take_along_axis(axis: int = -1)` | simple | 2 | - |

---

## 📦 模块: `sklearn.externals.array_api_compat.numpy.linalg`

**文件路径**: `sklearn/externals/array_api_compat/numpy/linalg.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `solve` | instance | `` | `Array` | `sklearn.externals.array_api_compat.numpy.linalg.solve()` | complex | 47 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_compat.torch._aliases`

**文件路径**: `sklearn/externals/array_api_compat/torch/_aliases.py`

**模块函数数**: 49

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `result_type` | instance | `*arrays_and_dtypes: Array | DType | bool | int ...` | `DType` | `sklearn.externals.array_api_compat.torch._aliases.result_type(*arrays_and_dtypes: Array | DType | bool | int | float | complex)` | medium | 31 | 抛异常, 有逻辑 |
| 2 | `can_cast` | instance | `` | `bool` | `sklearn.externals.array_api_compat.torch._aliases.can_cast()` | simple | 4 | 有逻辑 |
| 3 | `asarray` | instance | `dtype: DType | None = None, device: Device | No...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.asarray(dtype: DType | None = None, device: Device | None = None, copy: bool | None = None, **kwargs: Any)` | medium | 19 | 有逻辑 |
| 4 | `max` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.max(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False)` | simple | 5 | 有逻辑 |
| 5 | `min` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.min(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False)` | simple | 5 | 有逻辑 |
| 6 | `sort` | instance | `axis: int = -1, descending: bool = False, stabl...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.sort(axis: int = -1, descending: bool = False, stable: bool = True, **kwargs)` | simple | 2 | - |
| 7 | `prod` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.prod(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, dtype: Optional[DType] = None, keepdims: bool = False, **kwargs)` | medium | 22 | 有逻辑 |
| 8 | `sum` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.sum(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, dtype: Optional[DType] = None, keepdims: bool = False, **kwargs)` | medium | 18 | 有逻辑 |
| 9 | `any` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.any(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False, **kwargs)` | medium | 23 | 有逻辑 |
| 10 | `all` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.all(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False, **kwargs)` | medium | 23 | 有逻辑 |
| 11 | `mean` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.mean(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False, **kwargs)` | medium | 16 | 有逻辑 |
| 12 | `std` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.std(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, correction: Union[(int, float)] = 0.0, keepdims: bool = False, **kwargs)` | medium | 30 | 抛异常, 有逻辑 |
| 13 | `var` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.var(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, correction: Union[(int, float)] = 0.0, keepdims: bool = False, **kwargs)` | medium | 26 | 有逻辑 |
| 14 | `concat` | instance | `axis: Optional[int] = 0, **kwargs` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.concat(axis: Optional[int] = 0, **kwargs)` | simple | 9 | 有逻辑 |
| 15 | `squeeze` | instance | `axis: Union[(int, Tuple[(int, Ellipsis)])]` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.squeeze(axis: Union[(int, Tuple[(int, Ellipsis)])])` | medium | 12 | 抛异常, 有逻辑 |
| 16 | `broadcast_to` | instance | `shape: Tuple[(int, Ellipsis)], **kwargs` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.broadcast_to(shape: Tuple[(int, Ellipsis)], **kwargs)` | simple | 2 | - |
| 17 | `permute_dims` | instance | `axes: Tuple[(int, Ellipsis)]` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.permute_dims(axes: Tuple[(int, Ellipsis)])` | simple | 2 | - |
| 18 | `flip` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.flip(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, **kwargs)` | simple | 6 | 有逻辑 |
| 19 | `roll` | instance | `shift: Union[(int, Tuple[(int, Ellipsis)])], ax...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.roll(shift: Union[(int, Tuple[(int, Ellipsis)])], axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, **kwargs)` | simple | 2 | - |
| 20 | `nonzero` | instance | `**kwargs` | `Tuple[(Array, Ellipsis)]` | `sklearn.externals.array_api_compat.torch._aliases.nonzero(**kwargs)` | simple | 4 | 抛异常, 有逻辑 |
| 21 | `diff` | instance | `axis: int = -1, n: int = 1, prepend: Optional[A...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.diff(axis: int = -1, n: int = 1, prepend: Optional[Array] = None, append: Optional[Array] = None)` | simple | 10 | - |
| 22 | `count_nonzero` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.count_nonzero(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False)` | medium | 18 | 有逻辑 |
| 23 | `repeat` | instance | `axis: int | None = None` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.repeat(axis: int | None = None)` | simple | 2 | - |
| 24 | `where` | instance | `` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.where()` | simple | 8 | - |
| 25 | `reshape` | instance | `shape: Tuple[(int, Ellipsis)], copy: Optional[b...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.reshape(shape: Tuple[(int, Ellipsis)], copy: Optional[bool] = None, **kwargs)` | simple | 9 | 抛异常, 有逻辑 |
| 26 | `arange` | instance | `stop: Optional[Union[(int, float)]] = None, ste...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.arange(stop: Optional[Union[(int, float)]] = None, step: Union[(int, float)] = 1, dtype: Optional[DType] = None, device: Optional[Device] = None, **kwargs)` | medium | 18 | 有逻辑 |
| 27 | `eye` | instance | `k: int = 0, dtype: Optional[DType] = None, devi...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.eye(k: int = 0, dtype: Optional[DType] = None, device: Optional[Device] = None, **kwargs)` | medium | 14 | 有逻辑 |
| 28 | `linspace` | instance | `num: int, dtype: Optional[DType] = None, device...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.linspace(num: int, dtype: Optional[DType] = None, device: Optional[Device] = None, endpoint: bool = True, **kwargs)` | medium | 12 | 有逻辑 |
| 29 | `full` | instance | `shape: Union[(int, Tuple[(int, Ellipsis)])], fi...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.full(shape: Union[(int, Tuple[(int, Ellipsis)])], fill_value: bool | int | float | complex, dtype: Optional[DType] = None, device: Optional[Device] = None, **kwargs)` | simple | 10 | 有逻辑 |
| 30 | `ones` | instance | `shape: Union[(int, Tuple[(int, Ellipsis)])], dt...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.ones(shape: Union[(int, Tuple[(int, Ellipsis)])], dtype: Optional[DType] = None, device: Optional[Device] = None, **kwargs)` | simple | 6 | - |
| 31 | `zeros` | instance | `shape: Union[(int, Tuple[(int, Ellipsis)])], dt...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.zeros(shape: Union[(int, Tuple[(int, Ellipsis)])], dtype: Optional[DType] = None, device: Optional[Device] = None, **kwargs)` | simple | 6 | - |
| 32 | `empty` | instance | `shape: Union[(int, Tuple[(int, Ellipsis)])], dt...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.empty(shape: Union[(int, Tuple[(int, Ellipsis)])], dtype: Optional[DType] = None, device: Optional[Device] = None, **kwargs)` | simple | 6 | - |
| 33 | `tril` | instance | `k: int = 0` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.tril(k: int = 0)` | simple | 2 | - |
| 34 | `triu` | instance | `k: int = 0` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.triu(k: int = 0)` | simple | 2 | - |
| 35 | `expand_dims` | instance | `axis: int = 0` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.expand_dims(axis: int = 0)` | simple | 2 | - |
| 36 | `astype` | instance | `copy: bool = True, device: Optional[Device] = None` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.astype(copy: bool = True, device: Optional[Device] = None)` | medium | 11 | 有逻辑 |
| 37 | `broadcast_arrays` | instance | `*arrays: Array` | `List[Array]` | `sklearn.externals.array_api_compat.torch._aliases.broadcast_arrays(*arrays: Array)` | simple | 3 | 有逻辑 |
| 38 | `unique_all` | instance | `x: Array` | `UniqueAllResult` | `sklearn.externals.array_api_compat.torch._aliases.unique_all(x: Array)` | simple | 6 | 抛异常, 有逻辑 |
| 39 | `unique_counts` | instance | `x: Array` | `UniqueCountsResult` | `sklearn.externals.array_api_compat.torch._aliases.unique_counts(x: Array)` | simple | 7 | 有逻辑 |
| 40 | `unique_inverse` | instance | `x: Array` | `UniqueInverseResult` | `sklearn.externals.array_api_compat.torch._aliases.unique_inverse(x: Array)` | simple | 3 | - |
| 41 | `unique_values` | instance | `x: Array` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.unique_values(x: Array)` | simple | 2 | - |
| 42 | `matmul` | instance | `**kwargs` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.matmul(**kwargs)` | simple | 4 | - |
| 43 | `vecdot` | instance | `axis: int = -1` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.vecdot(axis: int = -1)` | simple | 3 | - |
| 44 | `tensordot` | instance | `axes: Union[(int, Tuple[(Sequence[int], Sequenc...` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.tensordot(axes: Union[(int, Tuple[(Sequence[int], Sequence[int])])] = 2, **kwargs)` | simple | 12 | - |
| 45 | `isdtype` | instance | `dtype: DType, kind: Union[(DType, str, Tuple[(U...` | `bool` | `sklearn.externals.array_api_compat.torch._aliases.isdtype(dtype: DType, kind: Union[(DType, str, Tuple[(Union[(DType, str)], Ellipsis)])], _tuple = True)` | complex | 35 | 抛异常, 有逻辑 |
| 46 | `take` | instance | `axis: Optional[int] = None, **kwargs` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.take(axis: Optional[int] = None, **kwargs)` | simple | 6 | 抛异常, 有逻辑 |
| 47 | `take_along_axis` | instance | `axis: int = -1` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.take_along_axis(axis: int = -1)` | simple | 2 | - |
| 48 | `sign` | instance | `` | `Array` | `sklearn.externals.array_api_compat.torch._aliases.sign()` | simple | 13 | 有逻辑 |
| 49 | `meshgrid` | instance | `*arrays: Array, indexing: Literal[('xy', 'ij')]...` | `List[Array]` | `sklearn.externals.array_api_compat.torch._aliases.meshgrid(*arrays: Array, indexing: Literal[('xy', 'ij')] = 'xy')` | simple | 4 | - |

---

## 📦 模块: `sklearn.externals.array_api_compat.torch.fft`

**文件路径**: `sklearn/externals/array_api_compat/torch/fft.py`

**模块函数数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fftn` | instance | `s: Sequence[int] = None, axes: Sequence[int] = ...` | `Array` | `sklearn.externals.array_api_compat.torch.fft.fftn(s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal[('backward', 'ortho', 'forward')] = 'backward', **kwargs)` | simple | 10 | - |
| 2 | `ifftn` | instance | `s: Sequence[int] = None, axes: Sequence[int] = ...` | `Array` | `sklearn.externals.array_api_compat.torch.fft.ifftn(s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal[('backward', 'ortho', 'forward')] = 'backward', **kwargs)` | simple | 10 | - |
| 3 | `rfftn` | instance | `s: Sequence[int] = None, axes: Sequence[int] = ...` | `Array` | `sklearn.externals.array_api_compat.torch.fft.rfftn(s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal[('backward', 'ortho', 'forward')] = 'backward', **kwargs)` | simple | 10 | - |
| 4 | `irfftn` | instance | `s: Sequence[int] = None, axes: Sequence[int] = ...` | `Array` | `sklearn.externals.array_api_compat.torch.fft.irfftn(s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal[('backward', 'ortho', 'forward')] = 'backward', **kwargs)` | simple | 10 | - |
| 5 | `fftshift` | instance | `axes: Union[(int, Sequence[int])] = None, **kwargs` | `Array` | `sklearn.externals.array_api_compat.torch.fft.fftshift(axes: Union[(int, Sequence[int])] = None, **kwargs)` | simple | 8 | - |
| 6 | `ifftshift` | instance | `axes: Union[(int, Sequence[int])] = None, **kwargs` | `Array` | `sklearn.externals.array_api_compat.torch.fft.ifftshift(axes: Union[(int, Sequence[int])] = None, **kwargs)` | simple | 8 | - |

---

## 📦 模块: `sklearn.externals.array_api_compat.torch.linalg`

**文件路径**: `sklearn/externals/array_api_compat/torch/linalg.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `cross` | instance | `axis: int = -1` | `Array` | `sklearn.externals.array_api_compat.torch.linalg.cross(axis: int = -1)` | simple | 8 | 抛异常, 有逻辑 |
| 2 | `vecdot` | instance | `axis: int = -1, **kwargs` | `Array` | `sklearn.externals.array_api_compat.torch.linalg.vecdot(axis: int = -1, **kwargs)` | medium | 21 | 抛异常, 有逻辑 |
| 3 | `solve` | instance | `**kwargs` | `Array` | `sklearn.externals.array_api_compat.torch.linalg.solve(**kwargs)` | simple | 19 | 有逻辑 |
| 4 | `trace` | instance | `offset: int = 0, dtype: Optional[DType] = None` | `Array` | `sklearn.externals.array_api_compat.torch.linalg.trace(offset: int = 0, dtype: Optional[DType] = None)` | simple | 3 | - |
| 5 | `vector_norm` | instance | `axis: Optional[Union[(int, Tuple[(int, Ellipsis...` | `Array` | `sklearn.externals.array_api_compat.torch.linalg.vector_norm(axis: Optional[Union[(int, Tuple[(int, Ellipsis)])]] = None, keepdims: bool = False, ord: JustInt | JustFloat = 2, **kwargs)` | medium | 30 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_extra._delegation`

**文件路径**: `sklearn/externals/array_api_extra/_delegation.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `isclose` | instance | `a: Array | complex, b: Array | complex, rtol: f...` | `Array` | `sklearn.externals.array_api_extra._delegation.isclose(a: Array | complex, b: Array | complex, rtol: float = 1e-05, atol: float = 1e-08, equal_nan: bool = False, xp: ModuleType | None = None)` | complex | 90 | 有逻辑 |
| 2 | `nan_to_num` | instance | `fill_value: int | float = 0.0, xp: ModuleType |...` | `Array` | `sklearn.externals.array_api_extra._delegation.nan_to_num(fill_value: int | float = 0.0, xp: ModuleType | None = None)` | complex | 77 | 抛异常, 有逻辑 |
| 3 | `one_hot` | instance | `num_classes: int, dtype: DType | None = None, a...` | `Array` | `sklearn.externals.array_api_extra._delegation.one_hot(num_classes: int, dtype: DType | None = None, axis: int = -1, xp: ModuleType | None = None)` | complex | 75 | 抛异常, 有逻辑 |
| 4 | `pad` | instance | `x: Array, pad_width: int | tuple[(int, int)] | ...` | `Array` | `sklearn.externals.array_api_extra._delegation.pad(x: Array, pad_width: int | tuple[(int, int)] | Sequence[tuple[(int, int)]], mode: Literal['constant'] = 'constant', constant_values: complex = 0, xp: ModuleType | None = None)` | complex | 57 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_extra._lib._funcs`

**文件路径**: `sklearn/externals/array_api_extra/_lib/_funcs.py`

**模块函数数**: 17

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `apply_where` | instance | `xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.apply_where(xp: ModuleType | None = None)` | simple | 9 | - |
| 2 | `apply_where` | instance | `fill_value: Array | complex, xp: ModuleType | N...` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.apply_where(fill_value: Array | complex, xp: ModuleType | None = None)` | simple | 9 | - |
| 3 | `apply_where` | instance | `fill_value: Array | complex | None = None, xp: ...` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.apply_where(fill_value: Array | complex | None = None, xp: ModuleType | None = None)` | simple | 84 | - |
| 4 | `atleast_nd` | instance | `ndim: int, xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.atleast_nd(ndim: int, xp: ModuleType | None = None)` | complex | 41 | 有逻辑 |
| 5 | `broadcast_shapes` | instance | `*shapes: tuple[(float | None, Ellipsis)]` | `tuple[(int | None, Ellipsis)]` | `sklearn.externals.array_api_extra._lib._funcs.broadcast_shapes(*shapes: tuple[(float | None, Ellipsis)])` | complex | 59 | 抛异常, 有逻辑 |
| 6 | `cov` | instance | `xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.cov(xp: ModuleType | None = None)` | complex | 92 | 有逻辑 |
| 7 | `one_hot` | instance | `num_classes: int, xp: ModuleType` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.one_hot(num_classes: int, xp: ModuleType)` | simple | 15 | 有逻辑 |
| 8 | `create_diagonal` | instance | `offset: int = 0, xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.create_diagonal(offset: int = 0, xp: ModuleType | None = None)` | complex | 61 | 抛异常, 有逻辑 |
| 9 | `default_dtype` | instance | `xp: ModuleType, kind: Literal[('real floating',...` | `DType` | `sklearn.externals.array_api_extra._lib._funcs.default_dtype(xp: ModuleType, kind: Literal[('real floating', 'complex floating', 'integral', 'indexing')] = 'real floating', device: Device | None = None)` | complex | 36 | 抛异常, 有逻辑 |
| 10 | `expand_dims` | instance | `axis: int | tuple[(int, Ellipsis)] = (0,), xp: ...` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.expand_dims(axis: int | tuple[(int, Ellipsis)] = (0,), xp: ModuleType | None = None)` | complex | 84 | 抛异常, 有逻辑 |
| 11 | `isclose` | instance | `a: Array | complex, b: Array | complex, rtol: f...` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.isclose(a: Array | complex, b: Array | complex, rtol: float = 1e-05, atol: float = 1e-08, equal_nan: bool = False, xp: ModuleType)` | complex | 45 | 有逻辑 |
| 12 | `kron` | instance | `xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.kron(xp: ModuleType | None = None)` | complex | 110 | 有逻辑 |
| 13 | `nan_to_num` | instance | `fill_value: int | float = 0.0, xp: ModuleType` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.nan_to_num(fill_value: int | float = 0.0, xp: ModuleType)` | complex | 39 | 有逻辑 |
| 14 | `nunique` | instance | `xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.nunique(xp: ModuleType | None = None)` | complex | 53 | 有逻辑 |
| 15 | `pad` | instance | `x: Array, pad_width: int | tuple[(int, int)] | ...` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.pad(x: Array, pad_width: int | tuple[(int, int)] | Sequence[tuple[(int, int)]], constant_values: complex = 0, xp: ModuleType)` | complex | 49 | 抛异常, 有逻辑 |
| 16 | `setdiff1d` | instance | `assume_unique: bool = False, xp: ModuleType | N...` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.setdiff1d(assume_unique: bool = False, xp: ModuleType | None = None)` | complex | 55 | 有逻辑 |
| 17 | `sinc` | instance | `xp: ModuleType | None = None` | `Array` | `sklearn.externals.array_api_extra._lib._funcs.sinc(xp: ModuleType | None = None)` | complex | 87 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_extra._lib._lazy`

**文件路径**: `sklearn/externals/array_api_extra/_lib/_lazy.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `lazy_apply` | instance | `func: Callable[(P, Array | ArrayLike)], *args: ...` | `Array` | `sklearn.externals.array_api_extra._lib._lazy.lazy_apply(func: Callable[(P, Array | ArrayLike)], *args: Array | complex | None, shape: tuple[(int | None, Ellipsis)] | None = None, dtype: DType | None = None, as_numpy: bool = False, xp: ModuleType | None = None, **kwargs: P.kwargs)` | simple | 9 | - |
| 2 | `lazy_apply` | instance | `func: Callable[(P, Sequence[Array | ArrayLike])...` | `tuple[(Array, Ellipsis)]` | `sklearn.externals.array_api_extra._lib._lazy.lazy_apply(func: Callable[(P, Sequence[Array | ArrayLike])], *args: Array | complex | None, shape: Sequence[tuple[(int | None, Ellipsis)]], dtype: Sequence[DType] | None = None, as_numpy: bool = False, xp: ModuleType | None = None, **kwargs: P.kwargs)` | simple | 9 | - |
| 3 | `lazy_apply` | instance | `func: Callable[(P, Array | ArrayLike | Sequence...` | `Array | tuple[(Array, Ellipsis)]` | `sklearn.externals.array_api_extra._lib._lazy.lazy_apply(func: Callable[(P, Array | ArrayLike | Sequence[Array | ArrayLike])], *args: Array | complex | None, shape: tuple[(int | None, Ellipsis)] | Sequence[tuple[(int | None, Ellipsis)]] | None = None, dtype: DType | Sequence[DType] | None = None, as_numpy: bool = False, xp: ModuleType | None = None, **kwargs: P.kwargs)` | simple | 246 | - |

---

## 📦 模块: `sklearn.externals.array_api_extra._lib._utils._helpers`

**文件路径**: `sklearn/externals/array_api_extra/_lib/_utils/_helpers.py`

**模块函数数**: 11

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `in1d` | instance | `assume_unique: bool = False, invert: bool = Fal...` | `Array` | `sklearn.externals.array_api_extra._lib._utils._helpers.in1d(assume_unique: bool = False, invert: bool = False, xp: ModuleType | None = None)` | complex | 60 | 有逻辑 |
| 2 | `mean` | instance | `axis: int | tuple[(int, Ellipsis)] | None = Non...` | `Array` | `sklearn.externals.array_api_extra._lib._utils._helpers.mean(axis: int | tuple[(int, Ellipsis)] | None = None, keepdims: bool = False, xp: ModuleType | None = None)` | medium | 21 | 有逻辑 |
| 3 | `is_python_scalar` | instance | `x: object` | `TypeIs[complex]` | `sklearn.externals.array_api_extra._lib._utils._helpers.is_python_scalar(x: object)` | simple | 6 | 有逻辑 |
| 4 | `asarrays` | instance | `a: Array | complex, b: Array | complex, xp: Mod...` | `tuple[(Array, Array)]` | `sklearn.externals.array_api_extra._lib._utils._helpers.asarrays(a: Array | complex, b: Array | complex, xp: ModuleType)` | complex | 72 | 抛异常, 有逻辑 |
| 5 | `ndindex` | instance | `*x: int` | `Generator[tuple[(int, Ellipsis)]]` | `sklearn.externals.array_api_extra._lib._utils._helpers.ndindex(*x: int)` | medium | 21 | 有逻辑 |
| 6 | `eager_shape` | instance | `` | `tuple[(int, Ellipsis)]` | `sklearn.externals.array_api_extra._lib._utils._helpers.eager_shape()` | medium | 20 | 抛异常, 有逻辑 |
| 7 | `meta_namespace` | instance | `*arrays: Array | complex | None, xp: ModuleType...` | `ModuleType` | `sklearn.externals.array_api_extra._lib._utils._helpers.meta_namespace(*arrays: Array | complex | None, xp: ModuleType | None = None)` | medium | 27 | 有逻辑 |
| 8 | `capabilities` | instance | `xp: ModuleType, device: Device | None = None` | `dict[(str, int | None)]` | `sklearn.externals.array_api_extra._lib._utils._helpers.capabilities(xp: ModuleType, device: Device | None = None)` | complex | 44 | 有逻辑 |
| 9 | `pickle_flatten` | instance | `obj: object, cls: type[T] | tuple[(type[T], Ell...` | `tuple[(list[T], FlattenRest)]` | `sklearn.externals.array_api_extra._lib._utils._helpers.pickle_flatten(obj: object, cls: type[T] | tuple[(type[T], Ellipsis)])` | complex | 97 | 有逻辑 |
| 10 | `pickle_unflatten` | instance | `instances: Iterable[object], rest: FlattenRest` | `Any` | `sklearn.externals.array_api_extra._lib._utils._helpers.pickle_unflatten(instances: Iterable[object], rest: FlattenRest)` | complex | 44 | 抛异常, 有逻辑 |
| 11 | `jax_autojit` | instance | `func: Callable[(P, T)]` | `Callable[(P, T)]` | `sklearn.externals.array_api_extra._lib._utils._helpers.jax_autojit(func: Callable[(P, T)])` | complex | 59 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.array_api_extra.testing`

**文件路径**: `sklearn/externals/array_api_extra/testing.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `lazy_xp_function` | instance | `func: Callable[(Ellipsis, Any)], allow_dask_com...` | `None` | `sklearn.externals.array_api_extra.testing.lazy_xp_function(func: Callable[(Ellipsis, Any)], allow_dask_compute: bool | int = False, jax_jit: bool = True, static_argnums: Deprecated = DEPRECATED, static_argnames: Deprecated = DEPRECATED)` | complex | 165 | 抛异常, 有逻辑 |
| 2 | `patch_lazy_xp_functions` | instance | `request: pytest.FixtureRequest, monkeypatch: py...` | `contextlib.AbstractContextManager[None]` | `sklearn.externals.array_api_extra.testing.patch_lazy_xp_functions(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch | None = None, xp: ModuleType)` | complex | 124 | 有逻辑 |

---

## 📦 模块: `sklearn.externals.conftest`

**文件路径**: `sklearn/externals/conftest.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `pytest_ignore_collect` | instance | `collection_path, config` | `None` | `sklearn.externals.conftest.pytest_ignore_collect(collection_path, config)` | simple | 2 | - |

---

## 📦 模块: `sklearn.feature_extraction.image`

**文件路径**: `sklearn/feature_extraction/image.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `img_to_graph` | instance | `img, mask = None, return_as = sparse.coo_matrix...` | `None` | `sklearn.feature_extraction.image.img_to_graph(img, mask = None, return_as = sparse.coo_matrix, dtype = None)` | complex | 41 | - |
| 2 | `grid_to_graph` | instance | `n_x, n_y, n_z = 1, mask = None, return_as = spa...` | `None` | `sklearn.feature_extraction.image.grid_to_graph(n_x, n_y, n_z = 1, mask = None, return_as = sparse.coo_matrix, dtype = int)` | complex | 47 | 有逻辑 |
| 3 | `extract_patches_2d` | instance | `image, patch_size, max_patches = None, random_s...` | `None` | `sklearn.feature_extraction.image.extract_patches_2d(image, patch_size, max_patches = None, random_state = None)` | complex | 96 | 抛异常, 有逻辑 |
| 4 | `reconstruct_from_patches_2d` | instance | `patches, image_size` | `None` | `sklearn.feature_extraction.image.reconstruct_from_patches_2d(patches, image_size)` | complex | 58 | 有逻辑 |

---

## 📦 模块: `sklearn.feature_extraction.text`

**文件路径**: `sklearn/feature_extraction/text.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `strip_accents_unicode` | instance | `s` | `None` | `sklearn.feature_extraction.text.strip_accents_unicode(s)` | medium | 30 | 有逻辑 |
| 2 | `strip_accents_ascii` | instance | `s` | `None` | `sklearn.feature_extraction.text.strip_accents_ascii(s)` | medium | 22 | 有逻辑 |
| 3 | `strip_tags` | instance | `s` | `None` | `sklearn.feature_extraction.text.strip_tags(s)` | medium | 17 | - |

---

## 📦 模块: `sklearn.feature_selection._mutual_info`

**文件路径**: `sklearn/feature_selection/_mutual_info.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `mutual_info_regression` | instance | `X, y, discrete_features = 'auto', n_neighbors =...` | `None` | `sklearn.feature_selection._mutual_info.mutual_info_regression(X, y, discrete_features = 'auto', n_neighbors = 3, copy = True, random_state = None, n_jobs = None)` | complex | 114 | 有逻辑 |
| 2 | `mutual_info_classif` | instance | `X, y, discrete_features = 'auto', n_neighbors =...` | `None` | `sklearn.feature_selection._mutual_info.mutual_info_classif(X, y, discrete_features = 'auto', n_neighbors = 3, copy = True, random_state = None, n_jobs = None)` | complex | 116 | 有逻辑 |

---

## 📦 模块: `sklearn.feature_selection._univariate_selection`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `f_oneway` | instance | `*args` | `None` | `sklearn.feature_selection._univariate_selection.f_oneway(*args)` | complex | 75 | 有逻辑 |
| 2 | `f_classif` | instance | `X, y` | `None` | `sklearn.feature_selection._univariate_selection.f_classif(X, y)` | complex | 47 | 有逻辑 |
| 3 | `chi2` | instance | `X, y` | `None` | `sklearn.feature_selection._univariate_selection.chi2(X, y)` | complex | 90 | 抛异常, 有逻辑 |
| 4 | `r_regression` | instance | `X, y, center = True, force_finite = True` | `None` | `sklearn.feature_selection._univariate_selection.r_regression(X, y, center = True, force_finite = True)` | complex | 94 | 有逻辑 |
| 5 | `f_regression` | instance | `X, y, center = True, force_finite = True` | `None` | `sklearn.feature_selection._univariate_selection.f_regression(X, y, center = True, force_finite = True)` | complex | 115 | 有逻辑 |

---

## 📦 模块: `sklearn.inspection._partial_dependence`

**文件路径**: `sklearn/inspection/_partial_dependence.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `partial_dependence` | instance | `estimator, X, features, sample_weight = None, c...` | `None` | `sklearn.inspection._partial_dependence.partial_dependence(estimator, X, features, sample_weight = None, categorical_features = None, feature_names = None, response_method = 'auto', percentiles = (0.05, 0.95), grid_resolution = 100, custom_values = None, method = 'auto', kind = 'average')` | complex | 409 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.inspection._permutation_importance`

**文件路径**: `sklearn/inspection/_permutation_importance.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `permutation_importance` | instance | `estimator, X, y, scoring = None, n_repeats = 5,...` | `None` | `sklearn.inspection._permutation_importance.permutation_importance(estimator, X, y, scoring = None, n_repeats = 5, n_jobs = None, random_state = None, sample_weight = None, max_samples = 1.0)` | complex | 176 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.isotonic`

**文件路径**: `sklearn/isotonic.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_increasing` | instance | `x, y` | `None` | `sklearn.isotonic.check_increasing(x, y)` | complex | 67 | 有逻辑 |
| 2 | `isotonic_regression` | instance | `y, sample_weight = None, y_min = None, y_max = ...` | `None` | `sklearn.isotonic.isotonic_regression(y, sample_weight = None, y_min = None, y_max = None, increasing = True)` | complex | 69 | 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._base`

**文件路径**: `sklearn/linear_model/_base.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_dataset` | instance | `X, y, sample_weight, random_state = None` | `None` | `sklearn.linear_model._base.make_dataset(X, y, sample_weight, random_state = None)` | complex | 51 | 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._coordinate_descent`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `lasso_path` | instance | `X, y, eps = 0.001, n_alphas = 100, alphas = Non...` | `None` | `sklearn.linear_model._coordinate_descent.lasso_path(X, y, eps = 0.001, n_alphas = 100, alphas = None, precompute = 'auto', Xy = None, copy_X = True, coef_init = None, verbose = False, return_n_iter = False, positive = False, **params)` | complex | 175 | 有逻辑 |
| 2 | `enet_path` | instance | `X, y, l1_ratio = 0.5, eps = 0.001, n_alphas = 1...` | `None` | `sklearn.linear_model._coordinate_descent.enet_path(X, y, l1_ratio = 0.5, eps = 0.001, n_alphas = 100, alphas = None, precompute = 'auto', Xy = None, copy_X = True, coef_init = None, verbose = False, return_n_iter = False, positive = False, check_input = True, **params)` | complex | 340 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._least_angle`

**文件路径**: `sklearn/linear_model/_least_angle.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `lars_path` | instance | `X, y, Xy = None, Gram = None, max_iter = 500, a...` | `None` | `sklearn.linear_model._least_angle.lars_path(X, y, Xy = None, Gram = None, max_iter = 500, alpha_min = 0, method = 'lar', copy_X = True, eps = np.finfo(float).eps, copy_Gram = True, verbose = 0, return_path = True, return_n_iter = False, positive = False)` | complex | 170 | 抛异常, 有逻辑 |
| 2 | `lars_path_gram` | instance | `Xy, Gram, n_samples, max_iter = 500, alpha_min ...` | `None` | `sklearn.linear_model._least_angle.lars_path_gram(Xy, Gram, n_samples, max_iter = 500, alpha_min = 0, method = 'lar', copy_X = True, eps = np.finfo(float).eps, copy_Gram = True, verbose = 0, return_path = True, return_n_iter = False, positive = False)` | complex | 156 | 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._linear_loss`

**文件路径**: `sklearn/linear_model/_linear_loss.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `sandwich_dot` | instance | `X, W` | `None` | `sklearn.linear_model._linear_loss.sandwich_dot(X, W)` | medium | 23 | 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._omp`

**文件路径**: `sklearn/linear_model/_omp.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `orthogonal_mp` | instance | `X, y, n_nonzero_coefs = None, tol = None, preco...` | `None` | `sklearn.linear_model._omp.orthogonal_mp(X, y, n_nonzero_coefs = None, tol = None, precompute = False, copy_X = True, return_path = False, return_n_iter = False)` | complex | 162 | 抛异常, 有逻辑 |
| 2 | `orthogonal_mp_gram` | instance | `Gram, Xy, n_nonzero_coefs = None, tol = None, n...` | `None` | `sklearn.linear_model._omp.orthogonal_mp_gram(Gram, Xy, n_nonzero_coefs = None, tol = None, norms_squared = None, copy_Gram = True, copy_Xy = True, return_path = False, return_n_iter = False)` | complex | 162 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._ridge`

**文件路径**: `sklearn/linear_model/_ridge.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `ridge_regression` | instance | `X, y, alpha, sample_weight = None, solver = 'au...` | `None` | `sklearn.linear_model._ridge.ridge_regression(X, y, alpha, sample_weight = None, solver = 'auto', max_iter = None, tol = 0.0001, verbose = 0, positive = False, random_state = None, return_n_iter = False, return_intercept = False, check_input = True)` | complex | 194 | 有逻辑 |
| 2 | `resolve_solver` | instance | `solver, positive, return_intercept, is_sparse, xp` | `None` | `sklearn.linear_model._ridge.resolve_solver(solver, positive, return_intercept, is_sparse, xp)` | medium | 30 | 抛异常, 有逻辑 |
| 3 | `resolve_solver_for_numpy` | instance | `positive, return_intercept, is_sparse` | `None` | `sklearn.linear_model._ridge.resolve_solver_for_numpy(positive, return_intercept, is_sparse)` | simple | 12 | 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._sag`

**文件路径**: `sklearn/linear_model/_sag.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_auto_step_size` | instance | `max_squared_sum, alpha_scaled, loss, fit_interc...` | `None` | `sklearn.linear_model._sag.get_auto_step_size(max_squared_sum, alpha_scaled, loss, fit_intercept, n_samples = None, is_saga = False)` | complex | 67 | 抛异常, 有逻辑 |
| 2 | `sag_solver` | instance | `X, y, sample_weight = None, loss = 'log', alpha...` | `None` | `sklearn.linear_model._sag.sag_solver(X, y, sample_weight = None, loss = 'log', alpha = 1.0, beta = 0.0, max_iter = 1000, tol = 0.001, verbose = 0, random_state = None, check_input = True, max_squared_sum = None, warm_start_mem = None, is_saga = False)` | complex | 284 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.linear_model._stochastic_gradient`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit_binary` | instance | `est, i, X, y, alpha, learning_rate, max_iter, p...` | `None` | `sklearn.linear_model._stochastic_gradient.fit_binary(est, i, X, y, alpha, learning_rate, max_iter, pos_weight, neg_weight, sample_weight, validation_mask = None, random_state = None)` | complex | 129 | 有逻辑 |

---

## 📦 模块: `sklearn.manifold._locally_linear`

**文件路径**: `sklearn/manifold/_locally_linear.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `barycenter_weights` | instance | `X, Y, indices, reg = 0.001` | `None` | `sklearn.manifold._locally_linear.barycenter_weights(X, Y, indices, reg = 0.001)` | complex | 52 | 抛异常, 有逻辑 |
| 2 | `barycenter_kneighbors_graph` | instance | `X, n_neighbors, reg = 0.001, n_jobs = None` | `None` | `sklearn.manifold._locally_linear.barycenter_kneighbors_graph(X, n_neighbors, reg = 0.001, n_jobs = None)` | complex | 40 | 有逻辑 |
| 3 | `null_space` | instance | `M, k, k_skip = 1, eigen_solver = 'arpack', tol ...` | `None` | `sklearn.manifold._locally_linear.null_space(M, k, k_skip = 1, eigen_solver = 'arpack', tol = 1e-06, max_iter = 100, random_state = None)` | complex | 74 | 抛异常, 有逻辑 |
| 4 | `locally_linear_embedding` | instance | `X, n_neighbors, n_components, reg = 0.001, eige...` | `None` | `sklearn.manifold._locally_linear.locally_linear_embedding(X, n_neighbors, n_components, reg = 0.001, eigen_solver = 'auto', tol = 1e-06, max_iter = 100, method = 'standard', hessian_tol = 0.0001, modified_tol = 1e-12, random_state = None, n_jobs = None)` | complex | 135 | 有逻辑 |

---

## 📦 模块: `sklearn.manifold._mds`

**文件路径**: `sklearn/manifold/_mds.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `smacof` | instance | `dissimilarities, metric = True, n_components = ...` | `None` | `sklearn.manifold._mds.smacof(dissimilarities, metric = True, n_components = 2, init = None, n_init = 'warn', n_jobs = None, max_iter = 300, verbose = 0, eps = 1e-06, random_state = None, return_n_iter = False, normalized_stress = 'auto')` | complex | 218 | 有逻辑 |

---

## 📦 模块: `sklearn.manifold._spectral_embedding`

**文件路径**: `sklearn/manifold/_spectral_embedding.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `spectral_embedding` | instance | `adjacency, n_components = 8, eigen_solver = Non...` | `None` | `sklearn.manifold._spectral_embedding.spectral_embedding(adjacency, n_components = 8, eigen_solver = None, random_state = None, eigen_tol = 'auto', norm_laplacian = True, drop_first = True)` | complex | 131 | 有逻辑 |

---

## 📦 模块: `sklearn.manifold._t_sne`

**文件路径**: `sklearn/manifold/_t_sne.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `trustworthiness` | instance | `X, X_embedded, n_neighbors = 5, metric = 'eucli...` | `None` | `sklearn.manifold._t_sne.trustworthiness(X, X_embedded, n_neighbors = 5, metric = 'euclidean')` | complex | 102 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.metrics._classification`

**文件路径**: `sklearn/metrics/_classification.py`

**模块函数数**: 21

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `accuracy_score` | instance | `y_true, y_pred, normalize = True, sample_weight...` | `None` | `sklearn.metrics._classification.accuracy_score(y_true, y_pred, normalize = True, sample_weight = None)` | complex | 76 | 有逻辑 |
| 2 | `confusion_matrix` | instance | `y_true, y_pred, labels = None, sample_weight = ...` | `None` | `sklearn.metrics._classification.confusion_matrix(y_true, y_pred, labels = None, sample_weight = None, normalize = None)` | complex | 196 | 抛异常, 有逻辑 |
| 3 | `multilabel_confusion_matrix` | instance | `y_true, y_pred, sample_weight = None, labels = ...` | `None` | `sklearn.metrics._classification.multilabel_confusion_matrix(y_true, y_pred, sample_weight = None, labels = None, samplewise = False)` | complex | 236 | 抛异常, 有逻辑 |
| 4 | `cohen_kappa_score` | instance | `y1, y2, labels = None, weights = None, sample_w...` | `None` | `sklearn.metrics._classification.cohen_kappa_score(y1, y2, labels = None, weights = None, sample_weight = None)` | complex | 103 | 抛异常, 有逻辑 |
| 5 | `jaccard_score` | instance | `y_true, y_pred, labels = None, pos_label = 1, a...` | `None` | `sklearn.metrics._classification.jaccard_score(y_true, y_pred, labels = None, pos_label = 1, average = 'binary', sample_weight = None, zero_division = 'warn')` | complex | 183 | 有逻辑 |
| 6 | `matthews_corrcoef` | instance | `y_true, y_pred, sample_weight = None` | `None` | `sklearn.metrics._classification.matthews_corrcoef(y_true, y_pred, sample_weight = None)` | complex | 89 | 抛异常, 有逻辑 |
| 7 | `zero_one_loss` | instance | `y_true, y_pred, normalize = True, sample_weight...` | `None` | `sklearn.metrics._classification.zero_one_loss(y_true, y_pred, normalize = True, sample_weight = None)` | complex | 75 | 有逻辑 |
| 8 | `f1_score` | instance | `y_true, y_pred, labels = None, pos_label = 1, a...` | `None` | `sklearn.metrics._classification.f1_score(y_true, y_pred, labels = None, pos_label = 1, average = 'binary', sample_weight = None, zero_division = 'warn')` | complex | 173 | 有逻辑 |
| 9 | `fbeta_score` | instance | `y_true, y_pred, beta, labels = None, pos_label ...` | `None` | `sklearn.metrics._classification.fbeta_score(y_true, y_pred, beta, labels = None, pos_label = 1, average = 'binary', sample_weight = None, zero_division = 'warn')` | complex | 200 | 有逻辑 |
| 10 | `precision_recall_fscore_support` | instance | `y_true, y_pred, beta = 1.0, labels = None, pos_...` | `None` | `sklearn.metrics._classification.precision_recall_fscore_support(y_true, y_pred, beta = 1.0, labels = None, pos_label = 1, average = None, warn_for = ('precision', 'recall', 'f-score'), sample_weight = None, zero_division = 'warn')` | complex | 258 | 有逻辑 |
| 11 | `class_likelihood_ratios` | instance | `y_true, y_pred, labels = None, sample_weight = ...` | `None` | `sklearn.metrics._classification.class_likelihood_ratios(y_true, y_pred, labels = None, sample_weight = None, raise_warning = 'deprecated', replace_undefined_by = np.nan)` | complex | 271 | 抛异常, 有逻辑 |
| 12 | `precision_score` | instance | `y_true, y_pred, labels = None, pos_label = 1, a...` | `None` | `sklearn.metrics._classification.precision_score(y_true, y_pred, labels = None, pos_label = 1, average = 'binary', sample_weight = None, zero_division = 'warn')` | complex | 162 | 有逻辑 |
| 13 | `recall_score` | instance | `y_true, y_pred, labels = None, pos_label = 1, a...` | `None` | `sklearn.metrics._classification.recall_score(y_true, y_pred, labels = None, pos_label = 1, average = 'binary', sample_weight = None, zero_division = 'warn')` | complex | 163 | 有逻辑 |
| 14 | `balanced_accuracy_score` | instance | `y_true, y_pred, sample_weight = None, adjusted ...` | `None` | `sklearn.metrics._classification.balanced_accuracy_score(y_true, y_pred, sample_weight = None, adjusted = False)` | complex | 93 | 有逻辑 |
| 15 | `classification_report` | instance | `y_true, y_pred, labels = None, target_names = N...` | `None` | `sklearn.metrics._classification.classification_report(y_true, y_pred, labels = None, target_names = None, sample_weight = None, digits = 2, output_dict = False, zero_division = 'warn')` | complex | 226 | 抛异常, 有逻辑 |
| 16 | `hamming_loss` | instance | `y_true, y_pred, sample_weight = None` | `None` | `sklearn.metrics._classification.hamming_loss(y_true, y_pred, sample_weight = None)` | complex | 103 | 抛异常, 有逻辑 |
| 17 | `log_loss` | instance | `y_true, y_pred, normalize = True, sample_weight...` | `None` | `sklearn.metrics._classification.log_loss(y_true, y_pred, normalize = True, sample_weight = None, labels = None)` | complex | 84 | 有逻辑 |
| 18 | `hinge_loss` | instance | `y_true, pred_decision, labels = None, sample_we...` | `None` | `sklearn.metrics._classification.hinge_loss(y_true, pred_decision, labels = None, sample_weight = None)` | complex | 141 | 抛异常, 有逻辑 |
| 19 | `brier_score_loss` | instance | `y_true, y_proba, sample_weight = None, pos_labe...` | `None` | `sklearn.metrics._classification.brier_score_loss(y_true, y_proba, sample_weight = None, pos_label = None, labels = None, scale_by_half = 'auto')` | complex | 144 | 有逻辑 |
| 20 | `d2_log_loss_score` | instance | `y_true, y_pred, sample_weight = None, labels = ...` | `None` | `sklearn.metrics._classification.d2_log_loss_score(y_true, y_pred, sample_weight = None, labels = None)` | complex | 81 | 有逻辑 |
| 21 | `d2_brier_score` | instance | `y_true, y_proba, sample_weight = None, pos_labe...` | `None` | `sklearn.metrics._classification.d2_brier_score(y_true, y_proba, sample_weight = None, pos_label = None, labels = None)` | complex | 93 | 有逻辑 |

---

## 📦 模块: `sklearn.metrics._pairwise_distances_reduction._dispatcher`

**文件路径**: `sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `sqeuclidean_row_norms` | instance | `X, num_threads` | `None` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.sqeuclidean_row_norms(X, num_threads)` | medium | 25 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.metrics._ranking`

**文件路径**: `sklearn/metrics/_ranking.py`

**模块函数数**: 13

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `auc` | instance | `x, y` | `None` | `sklearn.metrics._ranking.auc(x, y)` | complex | 63 | 抛异常, 有逻辑 |
| 2 | `average_precision_score` | instance | `y_true, y_score, average = 'macro', pos_label =...` | `None` | `sklearn.metrics._ranking.average_precision_score(y_true, y_score, average = 'macro', pos_label = 1, sample_weight = None)` | complex | 151 | 抛异常, 有逻辑 |
| 3 | `det_curve` | instance | `y_true, y_score, pos_label = None, sample_weigh...` | `None` | `sklearn.metrics._ranking.det_curve(y_true, y_score, pos_label = None, sample_weight = None, drop_intermediate = False)` | complex | 152 | 抛异常, 有逻辑 |
| 4 | `roc_auc_score` | instance | `y_true, y_score, average = 'macro', sample_weig...` | `None` | `sklearn.metrics._ranking.roc_auc_score(y_true, y_score, average = 'macro', sample_weight = None, max_fpr = None, multi_class = 'raise', labels = None)` | complex | 235 | 抛异常, 有逻辑 |
| 5 | `confusion_matrix_at_thresholds` | instance | `y_true, y_score, pos_label = None, sample_weigh...` | `None` | `sklearn.metrics._ranking.confusion_matrix_at_thresholds(y_true, y_score, pos_label = None, sample_weight = None)` | complex | 133 | 抛异常, 有逻辑 |
| 6 | `precision_recall_curve` | instance | `y_true, y_score, pos_label = None, sample_weigh...` | `None` | `sklearn.metrics._ranking.precision_recall_curve(y_true, y_score, pos_label = None, sample_weight = None, drop_intermediate = False)` | complex | 147 | 有逻辑 |
| 7 | `roc_curve` | instance | `y_true, y_score, pos_label = None, sample_weigh...` | `None` | `sklearn.metrics._ranking.roc_curve(y_true, y_score, pos_label = None, sample_weight = None, drop_intermediate = True)` | complex | 155 | 有逻辑 |
| 8 | `label_ranking_average_precision_score` | instance | `y_true, y_score, sample_weight = None` | `None` | `sklearn.metrics._ranking.label_ranking_average_precision_score(y_true, y_score, sample_weight = None)` | complex | 91 | 抛异常, 有逻辑 |
| 9 | `coverage_error` | instance | `y_true, y_score, sample_weight = None` | `None` | `sklearn.metrics._ranking.coverage_error(y_true, y_score, sample_weight = None)` | complex | 67 | 抛异常, 有逻辑 |
| 10 | `label_ranking_loss` | instance | `y_true, y_score, sample_weight = None` | `None` | `sklearn.metrics._ranking.label_ranking_loss(y_true, y_score, sample_weight = None)` | complex | 92 | 抛异常, 有逻辑 |
| 11 | `dcg_score` | instance | `y_true, y_score, k = None, log_base = 2, sample...` | `None` | `sklearn.metrics._ranking.dcg_score(y_true, y_score, k = None, log_base = 2, sample_weight = None, ignore_ties = False)` | complex | 107 | 有逻辑 |
| 12 | `ndcg_score` | instance | `y_true, y_score, k = None, sample_weight = None...` | `None` | `sklearn.metrics._ranking.ndcg_score(y_true, y_score, k = None, sample_weight = None, ignore_ties = False)` | complex | 108 | 抛异常, 有逻辑 |
| 13 | `top_k_accuracy_score` | instance | `y_true, y_score, k = 2, normalize = True, sampl...` | `None` | `sklearn.metrics._ranking.top_k_accuracy_score(y_true, y_score, k = 2, normalize = True, sample_weight = None, labels = None)` | complex | 161 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.metrics._regression`

**文件路径**: `sklearn/metrics/_regression.py`

**模块函数数**: 17

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `mean_absolute_error` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.mean_absolute_error(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 82 | 有逻辑 |
| 2 | `mean_pinball_loss` | instance | `y_true, y_pred, sample_weight = None, alpha = 0...` | `None` | `sklearn.metrics._regression.mean_pinball_loss(y_true, y_pred, sample_weight = None, alpha = 0.5, multioutput = 'uniform_average')` | complex | 87 | 有逻辑 |
| 3 | `mean_absolute_percentage_error` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.mean_absolute_percentage_error(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 95 | 有逻辑 |
| 4 | `mean_squared_error` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.mean_squared_error(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 80 | 有逻辑 |
| 5 | `root_mean_squared_error` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.root_mean_squared_error(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 73 | 有逻辑 |
| 6 | `mean_squared_log_error` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.mean_squared_log_error(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 77 | 抛异常, 有逻辑 |
| 7 | `root_mean_squared_log_error` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.root_mean_squared_log_error(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 67 | 抛异常, 有逻辑 |
| 8 | `median_absolute_error` | instance | `y_true, y_pred, multioutput = 'uniform_average'...` | `None` | `sklearn.metrics._regression.median_absolute_error(y_true, y_pred, multioutput = 'uniform_average', sample_weight = None)` | complex | 74 | 有逻辑 |
| 9 | `explained_variance_score` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.explained_variance_score(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average', force_finite = True)` | complex | 131 | 有逻辑 |
| 10 | `r2_score` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.r2_score(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average', force_finite = True)` | complex | 163 | 有逻辑 |
| 11 | `max_error` | instance | `y_true, y_pred` | `None` | `sklearn.metrics._regression.max_error(y_true, y_pred)` | medium | 34 | 抛异常, 有逻辑 |
| 12 | `mean_tweedie_deviance` | instance | `y_true, y_pred, sample_weight = None, power = 0` | `None` | `sklearn.metrics._regression.mean_tweedie_deviance(y_true, y_pred, sample_weight = None, power = 0)` | complex | 82 | 抛异常, 有逻辑 |
| 13 | `mean_poisson_deviance` | instance | `y_true, y_pred, sample_weight = None` | `None` | `sklearn.metrics._regression.mean_poisson_deviance(y_true, y_pred, sample_weight = None)` | medium | 33 | - |
| 14 | `mean_gamma_deviance` | instance | `y_true, y_pred, sample_weight = None` | `None` | `sklearn.metrics._regression.mean_gamma_deviance(y_true, y_pred, sample_weight = None)` | medium | 34 | - |
| 15 | `d2_tweedie_score` | instance | `y_true, y_pred, sample_weight = None, power = 0` | `None` | `sklearn.metrics._regression.d2_tweedie_score(y_true, y_pred, sample_weight = None, power = 0)` | complex | 101 | 抛异常, 有逻辑 |
| 16 | `d2_pinball_score` | instance | `y_true, y_pred, sample_weight = None, alpha = 0...` | `None` | `sklearn.metrics._regression.d2_pinball_score(y_true, y_pred, sample_weight = None, alpha = 0.5, multioutput = 'uniform_average')` | complex | 161 | 有逻辑 |
| 17 | `d2_absolute_error_score` | instance | `y_true, y_pred, sample_weight = None, multioutp...` | `None` | `sklearn.metrics._regression.d2_absolute_error_score(y_true, y_pred, sample_weight = None, multioutput = 'uniform_average')` | complex | 86 | 有逻辑 |

---

## 📦 模块: `sklearn.metrics._scorer`

**文件路径**: `sklearn/metrics/_scorer.py`

**模块函数数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_scorer` | instance | `scoring` | `None` | `sklearn.metrics._scorer.get_scorer(scoring)` | complex | 48 | 抛异常, 有逻辑 |
| 2 | `make_scorer` | instance | `score_func, response_method = 'predict', greate...` | `None` | `sklearn.metrics._scorer.make_scorer(score_func, response_method = 'predict', greater_is_better = True, **kwargs)` | complex | 63 | 有逻辑 |
| 3 | `positive_likelihood_ratio` | instance | `y_true, y_pred` | `None` | `sklearn.metrics._scorer.positive_likelihood_ratio(y_true, y_pred)` | simple | 2 | - |
| 4 | `negative_likelihood_ratio` | instance | `y_true, y_pred` | `None` | `sklearn.metrics._scorer.negative_likelihood_ratio(y_true, y_pred)` | simple | 2 | - |
| 5 | `get_scorer_names` | instance | `` | `None` | `sklearn.metrics._scorer.get_scorer_names()` | medium | 23 | - |
| 6 | `check_scoring` | instance | `estimator = None, scoring = None, allow_none = ...` | `None` | `sklearn.metrics._scorer.check_scoring(estimator = None, scoring = None, allow_none = False, raise_exc = True)` | complex | 105 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.metrics.cluster._bicluster`

**文件路径**: `sklearn/metrics/cluster/_bicluster.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `consensus_score` | instance | `a, b, similarity = 'jaccard'` | `None` | `sklearn.metrics.cluster._bicluster.consensus_score(a, b, similarity = 'jaccard')` | complex | 55 | 有逻辑 |

---

## 📦 模块: `sklearn.metrics.cluster._supervised`

**文件路径**: `sklearn/metrics/cluster/_supervised.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_clusterings` | instance | `labels_true, labels_pred` | `None` | `sklearn.metrics.cluster._supervised.check_clusterings(labels_true, labels_pred)` | complex | 44 | 抛异常, 有逻辑 |
| 2 | `contingency_matrix` | instance | `labels_true, labels_pred, eps = None, sparse = ...` | `None` | `sklearn.metrics.cluster._supervised.contingency_matrix(labels_true, labels_pred, eps = None, sparse = False, dtype = np.int64)` | complex | 76 | 抛异常, 有逻辑 |
| 3 | `pair_confusion_matrix` | instance | `labels_true, labels_pred` | `None` | `sklearn.metrics.cluster._supervised.pair_confusion_matrix(labels_true, labels_pred)` | complex | 76 | - |
| 4 | `rand_score` | instance | `labels_true, labels_pred` | `None` | `sklearn.metrics.cluster._supervised.rand_score(labels_true, labels_pred)` | complex | 71 | 有逻辑 |
| 5 | `adjusted_rand_score` | instance | `labels_true, labels_pred` | `None` | `sklearn.metrics.cluster._supervised.adjusted_rand_score(labels_true, labels_pred)` | complex | 103 | 有逻辑 |
| 6 | `homogeneity_completeness_v_measure` | instance | `labels_true, labels_pred, beta = 1.0` | `None` | `sklearn.metrics.cluster._supervised.homogeneity_completeness_v_measure(labels_true, labels_pred, beta = 1.0)` | complex | 91 | 有逻辑 |
| 7 | `homogeneity_score` | instance | `labels_true, labels_pred` | `None` | `sklearn.metrics.cluster._supervised.homogeneity_score(labels_true, labels_pred)` | complex | 67 | 有逻辑 |
| 8 | `completeness_score` | instance | `labels_true, labels_pred` | `None` | `sklearn.metrics.cluster._supervised.completeness_score(labels_true, labels_pred)` | complex | 67 | 有逻辑 |
| 9 | `v_measure_score` | instance | `labels_true, labels_pred, beta = 1.0` | `None` | `sklearn.metrics.cluster._supervised.v_measure_score(labels_true, labels_pred, beta = 1.0)` | complex | 94 | 有逻辑 |
| 10 | `mutual_info_score` | instance | `labels_true, labels_pred, contingency = None` | `None` | `sklearn.metrics.cluster._supervised.mutual_info_score(labels_true, labels_pred, contingency = None)` | complex | 106 | 有逻辑 |
| 11 | `adjusted_mutual_info_score` | instance | `labels_true, labels_pred, average_method = 'ari...` | `None` | `sklearn.metrics.cluster._supervised.adjusted_mutual_info_score(labels_true, labels_pred, average_method = 'arithmetic')` | complex | 128 | 有逻辑 |
| 12 | `normalized_mutual_info_score` | instance | `labels_true, labels_pred, average_method = 'ari...` | `None` | `sklearn.metrics.cluster._supervised.normalized_mutual_info_score(labels_true, labels_pred, average_method = 'arithmetic')` | complex | 102 | 有逻辑 |
| 13 | `fowlkes_mallows_score` | instance | `labels_true, labels_pred, sparse = 'deprecated'` | `None` | `sklearn.metrics.cluster._supervised.fowlkes_mallows_score(labels_true, labels_pred, sparse = 'deprecated')` | complex | 88 | 有逻辑 |
| 14 | `entropy` | instance | `labels` | `None` | `sklearn.metrics.cluster._supervised.entropy(labels)` | medium | 18 | 有逻辑 |

---

## 📦 模块: `sklearn.metrics.cluster._unsupervised`

**文件路径**: `sklearn/metrics/cluster/_unsupervised.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_number_of_labels` | instance | `n_labels, n_samples` | `None` | `sklearn.metrics.cluster._unsupervised.check_number_of_labels(n_labels, n_samples)` | medium | 16 | 抛异常, 有逻辑 |
| 2 | `silhouette_score` | instance | `X, labels, metric = 'euclidean', sample_size = ...` | `None` | `sklearn.metrics.cluster._unsupervised.silhouette_score(X, labels, metric = 'euclidean', sample_size = None, random_state = None, **kwds)` | complex | 88 | 有逻辑 |
| 3 | `silhouette_samples` | instance | `X, labels, metric = 'euclidean', **kwds` | `None` | `sklearn.metrics.cluster._unsupervised.silhouette_samples(X, labels, metric = 'euclidean', **kwds)` | complex | 113 | 抛异常, 有逻辑 |
| 4 | `calinski_harabasz_score` | instance | `X, labels` | `None` | `sklearn.metrics.cluster._unsupervised.calinski_harabasz_score(X, labels)` | complex | 71 | 有逻辑 |
| 5 | `davies_bouldin_score` | instance | `X, labels` | `None` | `sklearn.metrics.cluster._unsupervised.davies_bouldin_score(X, labels)` | complex | 75 | 有逻辑 |

---

## 📦 模块: `sklearn.metrics.pairwise`

**文件路径**: `sklearn/metrics/pairwise.py`

**模块函数数**: 26

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_pairwise_arrays` | instance | `X, Y, precomputed = False, dtype = 'infer_float...` | `None` | `sklearn.metrics.pairwise.check_pairwise_arrays(X, Y, precomputed = False, dtype = 'infer_float', accept_sparse = 'csr', ensure_all_finite = True, ensure_2d = True, copy = False)` | complex | 135 | 抛异常, 有逻辑 |
| 2 | `check_paired_arrays` | instance | `X, Y` | `None` | `sklearn.metrics.pairwise.check_paired_arrays(X, Y)` | medium | 33 | 抛异常, 有逻辑 |
| 3 | `euclidean_distances` | instance | `X, Y = None, Y_norm_squared = None, squared = F...` | `None` | `sklearn.metrics.pairwise.euclidean_distances(X, Y = None, Y_norm_squared = None, squared = False, X_norm_squared = None)` | complex | 106 | 抛异常, 有逻辑 |
| 4 | `nan_euclidean_distances` | instance | `X, Y = None, squared = False, missing_values = ...` | `None` | `sklearn.metrics.pairwise.nan_euclidean_distances(X, Y = None, squared = False, missing_values = np.nan, copy = True)` | complex | 125 | 有逻辑 |
| 5 | `pairwise_distances_argmin_min` | instance | `X, Y, axis = 1, metric = 'euclidean', metric_kw...` | `None` | `sklearn.metrics.pairwise.pairwise_distances_argmin_min(X, Y, axis = 1, metric = 'euclidean', metric_kwargs = None)` | complex | 135 | 有逻辑 |
| 6 | `pairwise_distances_argmin` | instance | `X, Y, axis = 1, metric = 'euclidean', metric_kw...` | `None` | `sklearn.metrics.pairwise.pairwise_distances_argmin(X, Y, axis = 1, metric = 'euclidean', metric_kwargs = None)` | complex | 127 | 有逻辑 |
| 7 | `haversine_distances` | instance | `X, Y = None` | `None` | `sklearn.metrics.pairwise.haversine_distances(X, Y = None)` | complex | 52 | 有逻辑 |
| 8 | `manhattan_distances` | instance | `X, Y = None` | `None` | `sklearn.metrics.pairwise.manhattan_distances(X, Y = None)` | complex | 72 | 有逻辑 |
| 9 | `cosine_distances` | instance | `X, Y = None` | `None` | `sklearn.metrics.pairwise.cosine_distances(X, Y = None)` | complex | 47 | 有逻辑 |
| 10 | `paired_euclidean_distances` | instance | `X, Y` | `None` | `sklearn.metrics.pairwise.paired_euclidean_distances(X, Y)` | medium | 29 | - |
| 11 | `paired_manhattan_distances` | instance | `X, Y` | `None` | `sklearn.metrics.pairwise.paired_manhattan_distances(X, Y)` | complex | 38 | 有逻辑 |
| 12 | `paired_cosine_distances` | instance | `X, Y` | `None` | `sklearn.metrics.pairwise.paired_cosine_distances(X, Y)` | medium | 36 | 有逻辑 |
| 13 | `paired_distances` | instance | `X, Y, metric = 'euclidean', **kwds` | `None` | `sklearn.metrics.pairwise.paired_distances(X, Y, metric = 'euclidean', **kwds)` | complex | 59 | 有逻辑 |
| 14 | `linear_kernel` | instance | `X, Y = None, dense_output = True` | `None` | `sklearn.metrics.pairwise.linear_kernel(X, Y = None, dense_output = True)` | medium | 36 | 有逻辑 |
| 15 | `polynomial_kernel` | instance | `X, Y = None, degree = 3, gamma = None, coef0 = 1` | `None` | `sklearn.metrics.pairwise.polynomial_kernel(X, Y = None, degree = 3, gamma = None, coef0 = 1)` | complex | 50 | 有逻辑 |
| 16 | `sigmoid_kernel` | instance | `X, Y = None, gamma = None, coef0 = 1` | `None` | `sklearn.metrics.pairwise.sigmoid_kernel(X, Y = None, gamma = None, coef0 = 1)` | complex | 48 | 有逻辑 |
| 17 | `rbf_kernel` | instance | `X, Y = None, gamma = None` | `None` | `sklearn.metrics.pairwise.rbf_kernel(X, Y = None, gamma = None)` | complex | 46 | 有逻辑 |
| 18 | `laplacian_kernel` | instance | `X, Y = None, gamma = None` | `None` | `sklearn.metrics.pairwise.laplacian_kernel(X, Y = None, gamma = None)` | complex | 50 | 有逻辑 |
| 19 | `cosine_similarity` | instance | `X, Y = None, dense_output = True` | `None` | `sklearn.metrics.pairwise.cosine_similarity(X, Y = None, dense_output = True)` | complex | 56 | 有逻辑 |
| 20 | `additive_chi2_kernel` | instance | `X, Y = None` | `None` | `sklearn.metrics.pairwise.additive_chi2_kernel(X, Y = None)` | complex | 79 | 抛异常, 有逻辑 |
| 21 | `chi2_kernel` | instance | `X, Y = None, gamma = 1.0` | `None` | `sklearn.metrics.pairwise.chi2_kernel(X, Y = None, gamma = 1.0)` | complex | 62 | 有逻辑 |
| 22 | `distance_metrics` | instance | `` | `None` | `sklearn.metrics.pairwise.distance_metrics()` | medium | 30 | 有逻辑 |
| 23 | `pairwise_distances_chunked` | instance | `X, Y = None, reduce_func = None, metric = 'eucl...` | `None` | `sklearn.metrics.pairwise.pairwise_distances_chunked(X, Y = None, reduce_func = None, metric = 'euclidean', n_jobs = None, working_memory = None, **kwds)` | complex | 171 | 有逻辑 |
| 24 | `pairwise_distances` | instance | `X, Y = None, metric = 'euclidean', n_jobs = Non...` | `None` | `sklearn.metrics.pairwise.pairwise_distances(X, Y = None, metric = 'euclidean', n_jobs = None, ensure_all_finite = True, **kwds)` | complex | 186 | 抛异常, 有逻辑 |
| 25 | `kernel_metrics` | instance | `` | `None` | `sklearn.metrics.pairwise.kernel_metrics()` | medium | 30 | 有逻辑 |
| 26 | `pairwise_kernels` | instance | `X, Y = None, metric = 'linear', filter_params =...` | `None` | `sklearn.metrics.pairwise.pairwise_kernels(X, Y = None, metric = 'linear', filter_params = False, n_jobs = None, **kwds)` | complex | 104 | 有逻辑 |

---

## 📦 模块: `sklearn.model_selection._split`

**文件路径**: `sklearn/model_selection/_split.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_cv` | instance | `cv = 5, y = None, classifier = False` | `None` | `sklearn.model_selection._split.check_cv(cv = 5, y = None, classifier = False)` | complex | 65 | 抛异常, 有逻辑 |
| 2 | `train_test_split` | instance | `*arrays, test_size = None, train_size = None, r...` | `None` | `sklearn.model_selection._split.train_test_split(*arrays, test_size = None, train_size = None, random_state = None, shuffle = True, stratify = None)` | complex | 180 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.model_selection._validation`

**文件路径**: `sklearn/model_selection/_validation.py`

**模块函数数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `cross_validate` | instance | `estimator, X, y = None, groups = None, scoring ...` | `None` | `sklearn.model_selection._validation.cross_validate(estimator, X, y = None, groups = None, scoring = None, cv = None, n_jobs = None, verbose = 0, params = None, pre_dispatch = '2*n_jobs', return_train_score = False, return_estimator = False, return_indices = False, error_score = np.nan)` | complex | 324 | 抛异常, 有逻辑 |
| 2 | `cross_val_score` | instance | `estimator, X, y = None, groups = None, scoring ...` | `None` | `sklearn.model_selection._validation.cross_val_score(estimator, X, y = None, groups = None, scoring = None, cv = None, n_jobs = None, verbose = 0, params = None, pre_dispatch = '2*n_jobs', error_score = np.nan)` | complex | 156 | 有逻辑 |
| 3 | `cross_val_predict` | instance | `estimator, X, y = None, groups = None, cv = Non...` | `None` | `sklearn.model_selection._validation.cross_val_predict(estimator, X, y = None, groups = None, cv = None, n_jobs = None, verbose = 0, params = None, pre_dispatch = '2*n_jobs', method = 'predict')` | complex | 252 | 抛异常, 有逻辑 |
| 4 | `permutation_test_score` | instance | `estimator, X, y, groups = None, cv = None, n_pe...` | `None` | `sklearn.model_selection._validation.permutation_test_score(estimator, X, y, groups = None, cv = None, n_permutations = 100, n_jobs = None, random_state = 0, verbose = 0, scoring = None, params = None)` | complex | 242 | 抛异常, 有逻辑 |
| 5 | `learning_curve` | instance | `estimator, X, y, groups = None, train_sizes = n...` | `None` | `sklearn.model_selection._validation.learning_curve(estimator, X, y, groups = None, train_sizes = np.linspace(0.1, 1.0, 5), cv = None, scoring = None, exploit_incremental_learning = False, n_jobs = None, pre_dispatch = 'all', verbose = 0, shuffle = False, random_state = None, error_score = np.nan, return_times = False, params = None)` | complex | 333 | 抛异常, 有逻辑 |
| 6 | `validation_curve` | instance | `estimator, X, y, param_name, param_range, group...` | `None` | `sklearn.model_selection._validation.validation_curve(estimator, X, y, param_name, param_range, groups = None, cv = None, scoring = None, n_jobs = None, pre_dispatch = 'all', verbose = 0, error_score = np.nan, params = None)` | complex | 229 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.neighbors._base`

**文件路径**: `sklearn/neighbors/_base.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `sort_graph_by_row_values` | instance | `graph, copy = False, warn_when_not_sorted = True` | `None` | `sklearn.neighbors._base.sort_graph_by_row_values(graph, copy = False, warn_when_not_sorted = True)` | complex | 89 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.neighbors._graph`

**文件路径**: `sklearn/neighbors/_graph.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `kneighbors_graph` | instance | `X, n_neighbors, mode = 'connectivity', metric =...` | `None` | `sklearn.neighbors._graph.kneighbors_graph(X, n_neighbors, mode = 'connectivity', metric = 'minkowski', p = 2, metric_params = None, include_self = False, n_jobs = None)` | complex | 90 | 有逻辑 |
| 2 | `radius_neighbors_graph` | instance | `X, radius, mode = 'connectivity', metric = 'min...` | `None` | `sklearn.neighbors._graph.radius_neighbors_graph(X, radius, mode = 'connectivity', metric = 'minkowski', p = 2, metric_params = None, include_self = False, n_jobs = None)` | complex | 93 | 有逻辑 |

---

## 📦 模块: `sklearn.neural_network._base`

**文件路径**: `sklearn/neural_network/_base.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `inplace_identity` | instance | `X` | `None` | `sklearn.neural_network._base.inplace_identity(X)` | simple | 9 | - |
| 2 | `inplace_exp` | instance | `X` | `None` | `sklearn.neural_network._base.inplace_exp(X)` | simple | 9 | - |
| 3 | `inplace_logistic` | instance | `X` | `None` | `sklearn.neural_network._base.inplace_logistic(X)` | simple | 9 | - |
| 4 | `inplace_tanh` | instance | `X` | `None` | `sklearn.neural_network._base.inplace_tanh(X)` | simple | 9 | - |
| 5 | `inplace_relu` | instance | `X` | `None` | `sklearn.neural_network._base.inplace_relu(X)` | simple | 9 | - |
| 6 | `inplace_softmax` | instance | `X` | `None` | `sklearn.neural_network._base.inplace_softmax(X)` | simple | 11 | - |
| 7 | `inplace_identity_derivative` | instance | `Z, delta` | `None` | `sklearn.neural_network._base.inplace_identity_derivative(Z, delta)` | simple | 12 | - |
| 8 | `inplace_logistic_derivative` | instance | `Z, delta` | `None` | `sklearn.neural_network._base.inplace_logistic_derivative(Z, delta)` | medium | 17 | - |
| 9 | `inplace_tanh_derivative` | instance | `Z, delta` | `None` | `sklearn.neural_network._base.inplace_tanh_derivative(Z, delta)` | medium | 16 | - |
| 10 | `inplace_relu_derivative` | instance | `Z, delta` | `None` | `sklearn.neural_network._base.inplace_relu_derivative(Z, delta)` | medium | 16 | - |
| 11 | `squared_loss` | instance | `y_true, y_pred, sample_weight = None` | `None` | `sklearn.neural_network._base.squared_loss(y_true, y_pred, sample_weight = None)` | medium | 22 | 有逻辑 |
| 12 | `poisson_loss` | instance | `y_true, y_pred, sample_weight = None` | `None` | `sklearn.neural_network._base.poisson_loss(y_true, y_pred, sample_weight = None)` | medium | 25 | 有逻辑 |
| 13 | `log_loss` | instance | `y_true, y_prob, sample_weight = None` | `None` | `sklearn.neural_network._base.log_loss(y_true, y_prob, sample_weight = None)` | medium | 29 | 有逻辑 |
| 14 | `binary_log_loss` | instance | `y_true, y_prob, sample_weight = None` | `None` | `sklearn.neural_network._base.binary_log_loss(y_true, y_prob, sample_weight = None)` | medium | 30 | 有逻辑 |

---

## 📦 模块: `sklearn.pipeline`

**文件路径**: `sklearn/pipeline.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `make_pipeline` | instance | `*steps, memory = None, transform_input = None, ...` | `None` | `sklearn.pipeline.make_pipeline(*steps, memory = None, transform_input = None, verbose = False)` | complex | 62 | 有逻辑 |
| 2 | `make_union` | instance | `*transformers, n_jobs = None, verbose = False, ...` | `None` | `sklearn.pipeline.make_union(*transformers, n_jobs = None, verbose = False, verbose_feature_names_out = True)` | complex | 57 | 有逻辑 |

---

## 📦 模块: `sklearn.preprocessing._data`

**文件路径**: `sklearn/preprocessing/_data.py`

**模块函数数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `scale` | instance | `X, axis = 0, with_mean = True, with_std = True,...` | `None` | `sklearn.preprocessing._data.scale(X, axis = 0, with_mean = True, with_std = True, copy = True)` | complex | 157 | 抛异常, 有逻辑 |
| 2 | `minmax_scale` | instance | `X, feature_range = (0, 1), axis = 0, copy = True` | `None` | `sklearn.preprocessing._data.minmax_scale(X, feature_range = (0, 1), axis = 0, copy = True)` | complex | 109 | 有逻辑 |
| 3 | `maxabs_scale` | instance | `X, axis = 0, copy = True` | `None` | `sklearn.preprocessing._data.maxabs_scale(X, axis = 0, copy = True)` | complex | 92 | 有逻辑 |
| 4 | `robust_scale` | instance | `X, axis = 0, with_centering = True, with_scalin...` | `None` | `sklearn.preprocessing._data.robust_scale(X, axis = 0, with_centering = True, with_scaling = True, quantile_range = (25.0, 75.0), copy = True, unit_variance = False)` | complex | 135 | 有逻辑 |
| 5 | `normalize` | instance | `X, norm = 'l2', axis = 1, copy = True, return_n...` | `None` | `sklearn.preprocessing._data.normalize(X, norm = 'l2', axis = 1, copy = True, return_norm = False)` | complex | 112 | 抛异常, 有逻辑 |
| 6 | `binarize` | instance | `X, threshold = 0.0, copy = True` | `None` | `sklearn.preprocessing._data.binarize(X, threshold = 0.0, copy = True)` | complex | 57 | 抛异常, 有逻辑 |
| 7 | `add_dummy_feature` | instance | `X, value = 1.0` | `None` | `sklearn.preprocessing._data.add_dummy_feature(X, value = 1.0)` | complex | 55 | 有逻辑 |
| 8 | `quantile_transform` | instance | `X, axis = 0, n_quantiles = 1000, output_distrib...` | `None` | `sklearn.preprocessing._data.quantile_transform(X, axis = 0, n_quantiles = 1000, output_distribution = 'uniform', ignore_implicit_zeros = False, subsample = int(100000.0), random_state = None, copy = True)` | complex | 142 | 有逻辑 |
| 9 | `power_transform` | instance | `X, method = 'yeo-johnson', standardize = True, ...` | `None` | `sklearn.preprocessing._data.power_transform(X, method = 'yeo-johnson', standardize = True, copy = True)` | complex | 101 | 有逻辑 |

---

## 📦 模块: `sklearn.preprocessing._label`

**文件路径**: `sklearn/preprocessing/_label.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `label_binarize` | instance | `y, classes, neg_label = 0, pos_label = 1, spars...` | `None` | `sklearn.preprocessing._label.label_binarize(y, classes, neg_label = 0, pos_label = 1, sparse_output = False)` | complex | 216 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.random_projection`

**文件路径**: `sklearn/random_projection.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `johnson_lindenstrauss_min_dim` | instance | `n_samples, eps = 0.1` | `None` | `sklearn.random_projection.johnson_lindenstrauss_min_dim(n_samples, eps = 0.1)` | complex | 84 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.svm._bounds`

**文件路径**: `sklearn/svm/_bounds.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `l1_min_c` | instance | `X, y, loss = 'squared_hinge', fit_intercept = T...` | `None` | `sklearn.svm._bounds.l1_min_c(X, y, loss = 'squared_hinge', fit_intercept = True, intercept_scaling = 1.0)` | complex | 73 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.tree._export`

**文件路径**: `sklearn/tree/_export.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `plot_tree` | instance | `decision_tree, max_depth = None, feature_names ...` | `None` | `sklearn.tree._export.plot_tree(decision_tree, max_depth = None, feature_names = None, class_names = None, label = 'all', filled = False, impurity = True, node_ids = False, proportion = False, rounded = False, precision = 3, ax = None, fontsize = None)` | complex | 117 | 有逻辑 |
| 2 | `export_graphviz` | instance | `decision_tree, out_file = None, max_depth = Non...` | `None` | `sklearn.tree._export.export_graphviz(decision_tree, out_file = None, max_depth = None, feature_names = None, class_names = None, label = 'all', filled = False, leaves_parallel = False, impurity = True, node_ids = False, proportion = False, rotate = False, rounded = False, special_characters = False, precision = 3, fontname = 'helvetica')` | complex | 166 | 抛异常, 有逻辑 |
| 3 | `export_text` | instance | `decision_tree, feature_names = None, class_name...` | `None` | `sklearn.tree._export.export_text(decision_tree, feature_names = None, class_names = None, max_depth = 10, spacing = 3, decimals = 2, show_weights = False)` | complex | 184 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.tree._reingold_tilford`

**文件路径**: `sklearn/tree/_reingold_tilford.py`

**模块函数数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `buchheim` | instance | `tree` | `None` | `sklearn.tree._reingold_tilford.buchheim(tree)` | simple | 6 | 有逻辑 |
| 2 | `third_walk` | instance | `tree, n` | `None` | `sklearn.tree._reingold_tilford.third_walk(tree, n)` | simple | 4 | 有逻辑 |
| 3 | `first_walk` | instance | `v, distance = 1.0` | `None` | `sklearn.tree._reingold_tilford.first_walk(v, distance = 1.0)` | medium | 23 | 有逻辑 |
| 4 | `apportion` | instance | `v, default_ancestor, distance` | `None` | `sklearn.tree._reingold_tilford.apportion(v, default_ancestor, distance)` | complex | 35 | 有逻辑 |
| 5 | `move_subtree` | instance | `wl, wr, shift` | `None` | `sklearn.tree._reingold_tilford.move_subtree(wl, wr, shift)` | simple | 10 | - |
| 6 | `execute_shifts` | instance | `v` | `None` | `sklearn.tree._reingold_tilford.execute_shifts(v)` | simple | 8 | 有逻辑 |
| 7 | `ancestor` | instance | `vil, v, default_ancestor` | `None` | `sklearn.tree._reingold_tilford.ancestor(vil, v, default_ancestor)` | simple | 9 | 有逻辑 |
| 8 | `second_walk` | instance | `v, m = 0, depth = 0, min = None` | `None` | `sklearn.tree._reingold_tilford.second_walk(v, m = 0, depth = 0, min = None)` | simple | 11 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._array_api`

**文件路径**: `sklearn/utils/_array_api.py`

**模块函数数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `yield_namespaces` | instance | `include_numpy_namespaces = True` | `None` | `sklearn.utils._array_api.yield_namespaces(include_numpy_namespaces = True)` | medium | 29 | 有逻辑 |
| 2 | `yield_namespace_device_dtype_combinations` | instance | `include_numpy_namespaces = True` | `None` | `sklearn.utils._array_api.yield_namespace_device_dtype_combinations(include_numpy_namespaces = True)` | complex | 49 | 有逻辑 |
| 3 | `device` | instance | `*array_list, remove_none = True, remove_types =...` | `None` | `sklearn.utils._array_api.device(*array_list, remove_none = True, remove_types = (str,))` | medium | 42 | 抛异常, 有逻辑 |
| 4 | `size` | instance | `x` | `None` | `sklearn.utils._array_api.size(x)` | medium | 14 | - |
| 5 | `supported_float_dtypes` | instance | `xp, device = None` | `None` | `sklearn.utils._array_api.supported_float_dtypes(xp, device = None)` | complex | 45 | 有逻辑 |
| 6 | `get_namespace` | instance | `*arrays, remove_none = True, remove_types = (st...` | `None` | `sklearn.utils._array_api.get_namespace(*arrays, remove_none = True, remove_types = (str,), xp = None)` | complex | 84 | 有逻辑 |
| 7 | `get_namespace_and_device` | instance | `*array_list, remove_none = True, remove_types =...` | `None` | `sklearn.utils._array_api.get_namespace_and_device(*array_list, remove_none = True, remove_types = (str,), xp = None)` | complex | 47 | 有逻辑 |
| 8 | `move_to` | instance | `*arrays, xp, device` | `None` | `sklearn.utils._array_api.move_to(*arrays, xp, device)` | complex | 94 | 抛异常, 有逻辑 |
| 9 | `indexing_dtype` | instance | `xp` | `None` | `sklearn.utils._array_api.indexing_dtype(xp)` | medium | 22 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._available_if`

**文件路径**: `sklearn/utils/_available_if.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `available_if` | instance | `check` | `None` | `sklearn.utils._available_if.available_if(check)` | complex | 40 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils._chunking`

**文件路径**: `sklearn/utils/_chunking.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `chunk_generator` | instance | `gen, chunksize` | `None` | `sklearn.utils._chunking.chunk_generator(gen, chunksize)` | simple | 9 | 有逻辑 |
| 2 | `gen_batches` | instance | `n, batch_size, min_batch_size = 0` | `None` | `sklearn.utils._chunking.gen_batches(n, batch_size, min_batch_size = 0)` | complex | 46 | 有逻辑 |
| 3 | `gen_even_slices` | instance | `n, n_packs, n_samples = None` | `None` | `sklearn.utils._chunking.gen_even_slices(n, n_packs, n_samples = None)` | complex | 49 | 有逻辑 |
| 4 | `get_chunk_n_rows` | instance | `row_bytes, max_n_rows = None, working_memory = ...` | `None` | `sklearn.utils._chunking.get_chunk_n_rows(row_bytes, max_n_rows = None, working_memory = None)` | complex | 39 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._dataframe`

**文件路径**: `sklearn/utils/_dataframe.py`

**模块函数数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `is_df_or_series` | instance | `X` | `None` | `sklearn.utils._dataframe.is_df_or_series(X)` | medium | 14 | 有逻辑 |
| 2 | `is_pandas_df_or_series` | instance | `X` | `None` | `sklearn.utils._dataframe.is_pandas_df_or_series(X)` | medium | 18 | 有逻辑 |
| 3 | `is_pandas_df` | instance | `X` | `None` | `sklearn.utils._dataframe.is_pandas_df(X)` | medium | 18 | 有逻辑 |
| 4 | `is_pyarrow_data` | instance | `X` | `None` | `sklearn.utils._dataframe.is_pyarrow_data(X)` | medium | 19 | 有逻辑 |
| 5 | `is_polars_df_or_series` | instance | `X` | `None` | `sklearn.utils._dataframe.is_polars_df_or_series(X)` | medium | 18 | 有逻辑 |
| 6 | `is_polars_df` | instance | `X` | `None` | `sklearn.utils._dataframe.is_polars_df(X)` | medium | 18 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._indexing`

**文件路径**: `sklearn/utils/_indexing.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `resample` | instance | `*arrays, replace = True, n_samples = None, rand...` | `None` | `sklearn.utils._indexing.resample(*arrays, replace = True, n_samples = None, random_state = None, stratify = None, sample_weight = None)` | complex | 185 | 抛异常, 有逻辑 |
| 2 | `shuffle` | instance | `*arrays, random_state = None, n_samples = None` | `None` | `sklearn.utils._indexing.shuffle(*arrays, random_state = None, n_samples = None)` | complex | 69 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._mask`

**文件路径**: `sklearn/utils/_mask.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `safe_mask` | instance | `X, mask` | `None` | `sklearn.utils._mask.safe_mask(X, mask)` | complex | 36 | 有逻辑 |
| 2 | `axis0_safe_slice` | instance | `X, mask, len_mask` | `None` | `sklearn.utils._mask.axis0_safe_slice(X, mask, len_mask)` | medium | 35 | 有逻辑 |
| 3 | `indices_to_mask` | instance | `indices, mask_length` | `None` | `sklearn.utils._mask.indices_to_mask(indices, mask_length)` | medium | 30 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils._metadata_requests`

**文件路径**: `sklearn/utils/_metadata_requests.py`

**模块函数数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `request_is_alias` | instance | `item` | `None` | `sklearn.utils._metadata_requests.request_is_alias(item)` | medium | 21 | 有逻辑 |
| 2 | `request_is_valid` | instance | `item` | `None` | `sklearn.utils._metadata_requests.request_is_valid(item)` | medium | 14 | 有逻辑 |
| 3 | `get_routing_for_object` | instance | `obj = None` | `None` | `sklearn.utils._metadata_requests.get_routing_for_object(obj = None)` | complex | 40 | 有逻辑 |
| 4 | `process_routing` | instance | `**kwargs` | `None` | `sklearn.utils._metadata_requests.process_routing(**kwargs)` | complex | 72 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils._missing`

**文件路径**: `sklearn/utils/_missing.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `is_scalar_nan` | instance | `x` | `None` | `sklearn.utils._missing.is_scalar_nan(x)` | complex | 36 | 有逻辑 |
| 2 | `is_pandas_na` | instance | `x` | `None` | `sklearn.utils._missing.is_pandas_na(x)` | medium | 24 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._optional_dependencies`

**文件路径**: `sklearn/utils/_optional_dependencies.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_matplotlib_support` | instance | `caller_name` | `None` | `sklearn.utils._optional_dependencies.check_matplotlib_support(caller_name)` | medium | 18 | 抛异常, 有逻辑 |
| 2 | `check_pandas_support` | instance | `caller_name` | `None` | `sklearn.utils._optional_dependencies.check_pandas_support(caller_name)` | medium | 22 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils._param_validation`

**文件路径**: `sklearn/utils/_param_validation.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `validate_parameter_constraints` | instance | `parameter_constraints, params, caller_name` | `None` | `sklearn.utils._param_validation.validate_parameter_constraints(parameter_constraints, params, caller_name)` | complex | 74 | 抛异常, 有逻辑 |
| 2 | `make_constraint` | instance | `constraint` | `None` | `sklearn.utils._param_validation.make_constraint(constraint)` | complex | 44 | 抛异常, 有逻辑 |
| 3 | `validate_params` | instance | `parameter_constraints, prefer_skip_nested_valid...` | `None` | `sklearn.utils._param_validation.validate_params(parameter_constraints, prefer_skip_nested_validation)` | complex | 84 | 抛异常, 有逻辑 |
| 4 | `generate_invalid_param_val` | instance | `constraint` | `None` | `sklearn.utils._param_validation.generate_invalid_param_val(constraint)` | complex | 60 | 抛异常, 有逻辑 |
| 5 | `generate_valid_param` | instance | `constraint` | `None` | `sklearn.utils._param_validation.generate_valid_param(constraint)` | complex | 83 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils._repr_html.estimator`

**文件路径**: `sklearn/utils/_repr_html/estimator.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `estimator_html_repr` | instance | `estimator` | `None` | `sklearn.utils._repr_html.estimator.estimator_html_repr(estimator)` | complex | 94 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._set_output`

**文件路径**: `sklearn/utils/_set_output.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `check_library_installed` | instance | `library` | `None` | `sklearn.utils._set_output.check_library_installed(library)` | simple | 9 | 抛异常, 有逻辑 |
| 2 | `get_columns` | instance | `columns` | `None` | `sklearn.utils._set_output.get_columns(columns)` | simple | 7 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._show_versions`

**文件路径**: `sklearn/utils/_show_versions.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `show_versions` | instance | `` | `None` | `sklearn.utils._show_versions.show_versions()` | medium | 39 | 有逻辑 |

---

## 📦 模块: `sklearn.utils._tags`

**文件路径**: `sklearn/utils/_tags.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_tags` | instance | `estimator` | `Tags` | `sklearn.utils._tags.get_tags(estimator)` | complex | 47 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils._unique`

**文件路径**: `sklearn/utils/_unique.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `attach_unique` | instance | `*ys, return_tuple = False` | `None` | `sklearn.utils._unique.attach_unique(*ys, return_tuple = False)` | medium | 32 | 有逻辑 |
| 2 | `cached_unique` | instance | `*ys, xp = None` | `None` | `sklearn.utils._unique.cached_unique(*ys, xp = None)` | medium | 28 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.class_weight`

**文件路径**: `sklearn/utils/class_weight.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute_class_weight` | instance | `class_weight, classes, y, sample_weight = None` | `None` | `sklearn.utils.class_weight.compute_class_weight(class_weight, classes, y, sample_weight = None)` | complex | 82 | 抛异常, 有逻辑 |
| 2 | `compute_sample_weight` | instance | `class_weight, y, indices = None` | `None` | `sklearn.utils.class_weight.compute_sample_weight(class_weight, y, indices = None)` | complex | 118 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils.discovery`

**文件路径**: `sklearn/utils/discovery.py`

**模块函数数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `all_estimators` | instance | `type_filter = None` | `None` | `sklearn.utils.discovery.all_estimators(type_filter = None)` | complex | 129 | 抛异常, 有逻辑 |
| 2 | `all_displays` | instance | `` | `None` | `sklearn.utils.discovery.all_displays()` | complex | 41 | 有逻辑 |
| 3 | `all_functions` | instance | `` | `None` | `sklearn.utils.discovery.all_functions()` | complex | 46 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.estimator_checks`

**文件路径**: `sklearn/utils/estimator_checks.py`

**模块函数数**: 105

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `estimator_checks_generator` | instance | `estimator, legacy: bool = True, expected_failed...` | `None` | `sklearn.utils.estimator_checks.estimator_checks_generator(estimator, legacy: bool = True, expected_failed_checks: dict[(str, str)] | None = None, mark: Literal[('xfail', 'skip', None)] = None, xfail_strict: bool | None = None)` | complex | 67 | 有逻辑 |
| 2 | `parametrize_with_checks` | instance | `estimators, legacy: bool = True, expected_faile...` | `None` | `sklearn.utils.estimator_checks.parametrize_with_checks(estimators, legacy: bool = True, expected_failed_checks: Callable | None = None, xfail_strict: bool | None = None)` | complex | 108 | 抛异常, 有逻辑 |
| 3 | `check_estimator` | instance | `estimator = None, legacy: bool = True, expected...` | `None` | `sklearn.utils.estimator_checks.check_estimator(estimator = None, legacy: bool = True, expected_failed_checks: dict[(str, str)] | None = None, on_skip: Literal['warn'] | None = 'warn', on_fail: Literal[('raise', 'warn')] | None = 'raise', callback: Callable | None = None)` | complex | 216 | 抛异常, 有逻辑 |
| 4 | `check_supervised_y_no_nan` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_supervised_y_no_nan(name, estimator_orig)` | medium | 32 | 有逻辑 |
| 5 | `check_array_api_input` | instance | `name, estimator_orig, array_namespace, device =...` | `None` | `sklearn.utils.estimator_checks.check_array_api_input(name, estimator_orig, array_namespace, device = None, dtype_name = 'float64', check_values = False, check_sample_weight = False)` | complex | 194 | 抛异常, 有逻辑 |
| 6 | `check_array_api_input_and_values` | instance | `name, estimator_orig, array_namespace, device =...` | `None` | `sklearn.utils.estimator_checks.check_array_api_input_and_values(name, estimator_orig, array_namespace, device = None, dtype_name = 'float64', check_sample_weight = False)` | medium | 17 | - |
| 7 | `check_estimator_sparse_tag` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimator_sparse_tag(name, estimator_orig)` | complex | 50 | 抛异常, 有逻辑 |
| 8 | `check_estimator_sparse_matrix` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimator_sparse_matrix(name, estimator_orig)` | simple | 2 | - |
| 9 | `check_estimator_sparse_array` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimator_sparse_array(name, estimator_orig)` | simple | 2 | - |
| 10 | `check_f_contiguous_array_estimator` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_f_contiguous_array_estimator(name, estimator_orig)` | medium | 20 | 有逻辑 |
| 11 | `check_sample_weights_pandas_series` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weights_pandas_series(name, estimator_orig)` | complex | 44 | 抛异常, 有逻辑 |
| 12 | `check_sample_weights_not_an_array` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weights_not_an_array(name, estimator_orig)` | medium | 27 | 有逻辑 |
| 13 | `check_sample_weights_list` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weights_list(name, estimator_orig)` | simple | 12 | 抛异常 |
| 14 | `check_sample_weights_shape` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weights_shape(name, estimator_orig)` | medium | 34 | 抛异常, 有逻辑 |
| 15 | `check_sample_weight_equivalence_on_dense_data` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weight_equivalence_on_dense_data(name, estimator_orig)` | simple | 2 | - |
| 16 | `check_sample_weight_equivalence_on_sparse_data` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weight_equivalence_on_sparse_data(name, estimator_orig)` | simple | 2 | - |
| 17 | `check_sample_weights_not_overwritten` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sample_weights_not_overwritten(name, estimator_orig)` | complex | 38 | - |
| 18 | `check_dtype_object` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_dtype_object(name, estimator_orig)` | complex | 46 | 抛异常, 有逻辑 |
| 19 | `check_complex_data` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_complex_data(name, estimator_orig)` | simple | 12 | 抛异常, 有逻辑 |
| 20 | `check_dict_unchanged` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_dict_unchanged(name, estimator_orig)` | medium | 18 | 有逻辑 |
| 21 | `check_dont_overwrite_parameters` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_dont_overwrite_parameters(name, estimator_orig)` | complex | 54 | 有逻辑 |
| 22 | `check_fit2d_predict1d` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit2d_predict1d(name, estimator_orig)` | medium | 21 | 有逻辑 |
| 23 | `check_methods_subset_invariance` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_methods_subset_invariance(name, estimator_orig)` | medium | 34 | 有逻辑 |
| 24 | `check_methods_sample_order_invariance` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_methods_sample_order_invariance(name, estimator_orig)` | complex | 42 | 有逻辑 |
| 25 | `check_fit2d_1sample` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit2d_1sample(name, estimator_orig)` | medium | 38 | 有逻辑 |
| 26 | `check_fit2d_1feature` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit2d_1feature(name, estimator_orig)` | medium | 28 | 有逻辑 |
| 27 | `check_fit1d` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit1d(name, estimator_orig)` | medium | 16 | 有逻辑 |
| 28 | `check_transformer_general` | instance | `name, transformer, readonly_memmap = False` | `None` | `sklearn.utils.estimator_checks.check_transformer_general(name, transformer, readonly_memmap = False)` | medium | 15 | 有逻辑 |
| 29 | `check_transformer_data_not_an_array` | instance | `name, transformer` | `None` | `sklearn.utils.estimator_checks.check_transformer_data_not_an_array(name, transformer)` | medium | 15 | - |
| 30 | `check_transformers_unfitted` | instance | `name, transformer` | `None` | `sklearn.utils.estimator_checks.check_transformers_unfitted(name, transformer)` | medium | 14 | 抛异常 |
| 31 | `check_transformers_unfitted_stateless` | instance | `name, transformer` | `None` | `sklearn.utils.estimator_checks.check_transformers_unfitted_stateless(name, transformer)` | simple | 12 | 抛异常, 有逻辑 |
| 32 | `check_pipeline_consistency` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_pipeline_consistency(name, estimator_orig)` | medium | 30 | 抛异常, 有逻辑 |
| 33 | `check_mixin_order` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_mixin_order(name, estimator_orig)` | complex | 38 | 有逻辑 |
| 34 | `check_fit_score_takes_y` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit_score_takes_y(name, estimator_orig)` | medium | 27 | 有逻辑 |
| 35 | `check_estimators_dtypes` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_dtypes(name, estimator_orig)` | medium | 20 | 有逻辑 |
| 36 | `check_transformer_preserve_dtypes` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_transformer_preserve_dtypes(name, transformer_orig)` | medium | 32 | 有逻辑 |
| 37 | `check_estimators_empty_data_messages` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_empty_data_messages(name, estimator_orig)` | medium | 21 | 抛异常, 有逻辑 |
| 38 | `check_estimators_nan_inf` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_nan_inf(name, estimator_orig)` | complex | 46 | 有逻辑 |
| 39 | `check_nonsquare_error` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_nonsquare_error(name, estimator_orig)` | medium | 13 | 抛异常 |
| 40 | `check_estimators_pickle` | instance | `name, estimator_orig, readonly_memmap = False` | `None` | `sklearn.utils.estimator_checks.check_estimators_pickle(name, estimator_orig, readonly_memmap = False)` | complex | 51 | 有逻辑 |
| 41 | `check_estimators_partial_fit_n_features` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_partial_fit_n_features(name, estimator_orig)` | medium | 26 | 抛异常, 有逻辑 |
| 42 | `check_classifier_multioutput` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_classifier_multioutput(name, estimator_orig)` | complex | 59 | 有逻辑 |
| 43 | `check_regressor_multioutput` | instance | `name, estimator` | `None` | `sklearn.utils.estimator_checks.check_regressor_multioutput(name, estimator)` | medium | 23 | 有逻辑 |
| 44 | `check_clustering` | instance | `name, clusterer_orig, readonly_memmap = False` | `None` | `sklearn.utils.estimator_checks.check_clustering(name, clusterer_orig, readonly_memmap = False)` | complex | 56 | 有逻辑 |
| 45 | `check_clusterer_compute_labels_predict` | instance | `name, clusterer_orig` | `None` | `sklearn.utils.estimator_checks.check_clusterer_compute_labels_predict(name, clusterer_orig)` | simple | 12 | 有逻辑 |
| 46 | `check_classifiers_one_label` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_one_label(name, classifier_orig)` | medium | 21 | 有逻辑 |
| 47 | `check_classifiers_one_label_sample_weights` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_one_label_sample_weights(name, classifier_orig)` | medium | 34 | 抛异常, 有逻辑 |
| 48 | `check_classifiers_train` | instance | `name, classifier_orig, readonly_memmap = False,...` | `None` | `sklearn.utils.estimator_checks.check_classifiers_train(name, classifier_orig, readonly_memmap = False, X_dtype = 'float64')` | complex | 136 | 抛异常, 有逻辑 |
| 49 | `check_outlier_corruption` | instance | `num_outliers, expected_outliers, decision` | `None` | `sklearn.utils.estimator_checks.check_outlier_corruption(num_outliers, expected_outliers, decision)` | medium | 20 | 有逻辑 |
| 50 | `check_outliers_train` | instance | `name, estimator_orig, readonly_memmap = True` | `None` | `sklearn.utils.estimator_checks.check_outliers_train(name, estimator_orig, readonly_memmap = True)` | complex | 70 | 有逻辑 |
| 51 | `check_outlier_contamination` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_outlier_contamination(name, estimator_orig)` | medium | 25 | 抛异常, 有逻辑 |
| 52 | `check_classifiers_multilabel_representation_invariance` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_multilabel_representation_invariance(name, classifier_orig)` | complex | 39 | - |
| 53 | `check_classifiers_multilabel_output_format_predict` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_multilabel_output_format_predict(name, classifier_orig)` | complex | 43 | 抛异常, 有逻辑 |
| 54 | `check_classifiers_multilabel_output_format_predict_proba` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_multilabel_output_format_predict_proba(name, classifier_orig)` | complex | 82 | 抛异常, 有逻辑 |
| 55 | `check_classifiers_multilabel_output_format_decision_function` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_multilabel_output_format_decision_function(name, classifier_orig)` | complex | 44 | 抛异常, 有逻辑 |
| 56 | `check_get_feature_names_out_error` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_get_feature_names_out_error(name, estimator_orig)` | medium | 13 | 抛异常 |
| 57 | `check_estimators_fit_returns_self` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_fit_returns_self(name, estimator_orig)` | simple | 10 | 有逻辑 |
| 58 | `check_readonly_memmap_input` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_readonly_memmap_input(name, estimator_orig)` | medium | 16 | 抛异常 |
| 59 | `check_estimators_unfitted` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_unfitted(name, estimator_orig)` | medium | 27 | 抛异常, 有逻辑 |
| 60 | `check_supervised_y_2d` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_supervised_y_2d(name, estimator_orig)` | medium | 32 | 有逻辑 |
| 61 | `check_classifiers_predictions` | instance | `X, y, name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_predictions(X, y, name, classifier_orig)` | complex | 56 | 有逻辑 |
| 62 | `check_classifiers_classes` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_classes(name, classifier_orig)` | medium | 32 | 有逻辑 |
| 63 | `check_regressors_int` | instance | `name, regressor_orig` | `None` | `sklearn.utils.estimator_checks.check_regressors_int(name, regressor_orig)` | medium | 25 | 有逻辑 |
| 64 | `check_regressors_train` | instance | `name, regressor_orig, readonly_memmap = False, ...` | `None` | `sklearn.utils.estimator_checks.check_regressors_train(name, regressor_orig, readonly_memmap = False, X_dtype = np.float64)` | complex | 48 | 抛异常, 有逻辑 |
| 65 | `check_regressors_no_decision_function` | instance | `name, regressor_orig` | `None` | `sklearn.utils.estimator_checks.check_regressors_no_decision_function(name, regressor_orig)` | simple | 14 | 有逻辑 |
| 66 | `check_class_weight_classifiers` | instance | `name, classifier_orig` | `None` | `sklearn.utils.estimator_checks.check_class_weight_classifiers(name, classifier_orig)` | complex | 42 | 有逻辑 |
| 67 | `check_class_weight_balanced_classifiers` | instance | `name, classifier_orig, X_train, y_train, X_test...` | `None` | `sklearn.utils.estimator_checks.check_class_weight_balanced_classifiers(name, classifier_orig, X_train, y_train, X_test, y_test, weights)` | medium | 19 | 有逻辑 |
| 68 | `check_class_weight_balanced_linear_classifier` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_class_weight_balanced_linear_classifier(name, estimator_orig)` | medium | 38 | 有逻辑 |
| 69 | `check_estimators_overwrite_params` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimators_overwrite_params(name, estimator_orig)` | medium | 31 | 有逻辑 |
| 70 | `check_no_attributes_set_in_init` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_no_attributes_set_in_init(name, estimator_orig)` | medium | 30 | 抛异常, 有逻辑 |
| 71 | `check_sparsify_coefficients` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_sparsify_coefficients(name, estimator_orig)` | medium | 32 | - |
| 72 | `check_classifier_data_not_an_array` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_classifier_data_not_an_array(name, estimator_orig)` | medium | 22 | 有逻辑 |
| 73 | `check_regressor_data_not_an_array` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_regressor_data_not_an_array(name, estimator_orig)` | simple | 6 | 有逻辑 |
| 74 | `check_estimators_data_not_an_array` | instance | `name, estimator_orig, X, y, obj_type` | `None` | `sklearn.utils.estimator_checks.check_estimators_data_not_an_array(name, estimator_orig, X, y, obj_type)` | complex | 44 | 抛异常, 有逻辑 |
| 75 | `check_estimator_cloneable` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimator_cloneable(name, estimator_orig)` | simple | 6 | 抛异常, 有逻辑 |
| 76 | `check_estimator_repr` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimator_repr(name, estimator_orig)` | simple | 7 | 抛异常, 有逻辑 |
| 77 | `check_parameters_default_constructible` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_parameters_default_constructible(name, estimator_orig)` | complex | 125 | 有逻辑 |
| 78 | `check_positive_only_tag_during_fit` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_positive_only_tag_during_fit(name, estimator_orig)` | medium | 33 | 抛异常, 有逻辑 |
| 79 | `check_non_transformer_estimators_n_iter` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_non_transformer_estimators_n_iter(name, estimator_orig)` | medium | 21 | 有逻辑 |
| 80 | `check_transformer_n_iter` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_transformer_n_iter(name, estimator_orig)` | medium | 28 | 有逻辑 |
| 81 | `check_get_params_invariance` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_get_params_invariance(name, estimator_orig)` | simple | 8 | 有逻辑 |
| 82 | `check_set_params` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_set_params(name, estimator_orig)` | complex | 54 | 有逻辑 |
| 83 | `check_classifiers_regression_target` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_classifiers_regression_target(name, estimator_orig)` | medium | 17 | 抛异常, 有逻辑 |
| 84 | `check_decision_proba_consistency` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_decision_proba_consistency(name, estimator_orig)` | medium | 42 | 有逻辑 |
| 85 | `check_outliers_fit_predict` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_outliers_fit_predict(name, estimator_orig)` | medium | 41 | 有逻辑 |
| 86 | `check_fit_non_negative` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit_non_negative(name, estimator_orig)` | simple | 8 | 有逻辑 |
| 87 | `check_fit_idempotent` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit_idempotent(name, estimator_orig)` | complex | 58 | 有逻辑 |
| 88 | `check_fit_check_is_fitted` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_fit_check_is_fitted(name, estimator_orig)` | medium | 37 | 抛异常, 有逻辑 |
| 89 | `check_n_features_in` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_n_features_in(name, estimator_orig)` | medium | 24 | 有逻辑 |
| 90 | `check_requires_y_none` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_requires_y_none(name, estimator_orig)` | medium | 31 | 抛异常, 有逻辑 |
| 91 | `check_n_features_in_after_fitting` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_n_features_in_after_fitting(name, estimator_orig)` | complex | 96 | 有逻辑 |
| 92 | `check_valid_tag_types` | instance | `name, estimator` | `None` | `sklearn.utils.estimator_checks.check_valid_tag_types(name, estimator)` | complex | 51 | 有逻辑 |
| 93 | `check_estimator_tags_renamed` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_estimator_tags_renamed(name, estimator_orig)` | medium | 20 | 抛异常, 有逻辑 |
| 94 | `check_dataframe_column_names_consistency` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_dataframe_column_names_consistency(name, estimator_orig)` | complex | 139 | 抛异常, 有逻辑 |
| 95 | `check_transformer_get_feature_names_out` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_transformer_get_feature_names_out(name, transformer_orig)` | complex | 46 | 有逻辑 |
| 96 | `check_transformer_get_feature_names_out_pandas` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_transformer_get_feature_names_out_pandas(name, transformer_orig)` | complex | 55 | 抛异常, 有逻辑 |
| 97 | `check_param_validation` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_param_validation(name, estimator_orig)` | complex | 112 | 抛异常, 有逻辑 |
| 98 | `check_set_output_transform` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_set_output_transform(name, transformer_orig)` | complex | 46 | 有逻辑 |
| 99 | `check_set_output_transform_pandas` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_set_output_transform_pandas(name, transformer_orig)` | simple | 2 | - |
| 100 | `check_global_output_transform_pandas` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_global_output_transform_pandas(name, transformer_orig)` | simple | 2 | - |
| 101 | `check_set_output_transform_polars` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_set_output_transform_polars(name, transformer_orig)` | simple | 2 | - |
| 102 | `check_global_set_output_transform_polars` | instance | `name, transformer_orig` | `None` | `sklearn.utils.estimator_checks.check_global_set_output_transform_polars(name, transformer_orig)` | simple | 2 | - |
| 103 | `check_inplace_ensure_writeable` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_inplace_ensure_writeable(name, estimator_orig)` | medium | 43 | 有逻辑 |
| 104 | `check_do_not_raise_errors_in_init_or_set_params` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_do_not_raise_errors_in_init_or_set_params(name, estimator_orig)` | simple | 14 | 抛异常, 有逻辑 |
| 105 | `check_classifier_not_supporting_multiclass` | instance | `name, estimator_orig` | `None` | `sklearn.utils.estimator_checks.check_classifier_not_supporting_multiclass(name, estimator_orig)` | complex | 36 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils.extmath`

**文件路径**: `sklearn/utils/extmath.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `squared_norm` | instance | `x` | `None` | `sklearn.utils.extmath.squared_norm(x)` | medium | 26 | 有逻辑 |
| 2 | `row_norms` | instance | `X, squared = False` | `None` | `sklearn.utils.extmath.row_norms(X, squared = False)` | complex | 36 | 有逻辑 |
| 3 | `fast_logdet` | instance | `A` | `None` | `sklearn.utils.extmath.fast_logdet(A)` | complex | 38 | 有逻辑 |
| 4 | `density` | instance | `w` | `None` | `sklearn.utils.extmath.density(w)` | medium | 26 | 有逻辑 |
| 5 | `safe_sparse_dot` | instance | `a, b, dense_output = False` | `None` | `sklearn.utils.extmath.safe_sparse_dot(a, b, dense_output = False)` | complex | 71 | 有逻辑 |
| 6 | `randomized_range_finder` | instance | `A, size, n_iter, power_iteration_normalizer = '...` | `None` | `sklearn.utils.extmath.randomized_range_finder(A, size, n_iter, power_iteration_normalizer = 'auto', random_state = None)` | complex | 70 | 有逻辑 |
| 7 | `randomized_svd` | instance | `M, n_components, n_oversamples = 10, n_iter = '...` | `None` | `sklearn.utils.extmath.randomized_svd(M, n_components, n_oversamples = 10, n_iter = 'auto', power_iteration_normalizer = 'auto', transpose = 'auto', flip_sign = True, random_state = None, svd_lapack_driver = 'gesdd')` | complex | 156 | 有逻辑 |
| 8 | `weighted_mode` | instance | `a, w, axis = 0` | `None` | `sklearn.utils.extmath.weighted_mode(a, w, axis = 0)` | complex | 72 | 有逻辑 |
| 9 | `cartesian` | instance | `arrays, out = None` | `None` | `sklearn.utils.extmath.cartesian(arrays, out = None)` | complex | 57 | 有逻辑 |
| 10 | `svd_flip` | instance | `u, v, u_based_decision = True` | `None` | `sklearn.utils.extmath.svd_flip(u, v, u_based_decision = True)` | complex | 59 | 有逻辑 |
| 11 | `softmax` | instance | `X, copy = True` | `None` | `sklearn.utils.extmath.softmax(X, copy = True)` | complex | 40 | 有逻辑 |
| 12 | `make_nonnegative` | instance | `X, min_value = 0` | `None` | `sklearn.utils.extmath.make_nonnegative(X, min_value = 0)` | medium | 31 | 抛异常, 有逻辑 |
| 13 | `stable_cumsum` | instance | `arr, axis = None, rtol = 1e-05, atol = 1e-08` | `None` | `sklearn.utils.extmath.stable_cumsum(arr, axis = None, rtol = 1e-05, atol = 1e-08)` | complex | 40 | 有逻辑 |
| 14 | `safe_sqr` | instance | `X, copy = True` | `None` | `sklearn.utils.extmath.safe_sqr(X, copy = True)` | medium | 33 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.fixes`

**文件路径**: `sklearn/utils/fixes.py`

**模块函数数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `pd_fillna` | instance | `pd, frame` | `None` | `sklearn.utils.fixes.pd_fillna(pd, frame)` | medium | 14 | 有逻辑 |
| 2 | `tarfile_extractall` | instance | `tarfile, path` | `None` | `sklearn.utils.fixes.tarfile_extractall(tarfile, path)` | simple | 8 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.graph`

**文件路径**: `sklearn/utils/graph.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `single_source_shortest_path_length` | instance | `graph, source, cutoff = None` | `None` | `sklearn.utils.graph.single_source_shortest_path_length(graph, source, cutoff = None)` | complex | 53 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.multiclass`

**文件路径**: `sklearn/utils/multiclass.py`

**模块函数数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `unique_labels` | instance | `*ys` | `None` | `sklearn.utils.multiclass.unique_labels(*ys)` | complex | 79 | 抛异常, 有逻辑 |
| 2 | `is_multilabel` | instance | `y` | `None` | `sklearn.utils.multiclass.is_multilabel(y)` | complex | 70 | 有逻辑 |
| 3 | `check_classification_targets` | instance | `y` | `None` | `sklearn.utils.multiclass.check_classification_targets(y)` | complex | 37 | 抛异常, 有逻辑 |
| 4 | `type_of_target` | instance | `y, input_name = '', raise_unknown = False` | `None` | `sklearn.utils.multiclass.type_of_target(y, input_name = '', raise_unknown = False)` | complex | 197 | 抛异常, 有逻辑 |
| 5 | `class_distribution` | instance | `y, sample_weight = None` | `None` | `sklearn.utils.multiclass.class_distribution(y, sample_weight = None)` | complex | 72 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.parallel`

**文件路径**: `sklearn/utils/parallel.py`

**模块函数数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `delayed` | instance | `function` | `None` | `sklearn.utils.parallel.delayed(function)` | medium | 31 | 有逻辑 |

---

## 📦 模块: `sklearn.utils.sparsefuncs`

**文件路径**: `sklearn/utils/sparsefuncs.py`

**模块函数数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `inplace_csr_column_scale` | instance | `X, scale` | `None` | `sklearn.utils.sparsefuncs.inplace_csr_column_scale(X, scale)` | complex | 39 | 有逻辑 |
| 2 | `inplace_csr_row_scale` | instance | `X, scale` | `None` | `sklearn.utils.sparsefuncs.inplace_csr_row_scale(X, scale)` | medium | 16 | 有逻辑 |
| 3 | `mean_variance_axis` | instance | `X, axis, weights = None, return_sum_weights = F...` | `None` | `sklearn.utils.sparsefuncs.mean_variance_axis(X, axis, weights = None, return_sum_weights = False)` | complex | 76 | 有逻辑 |
| 4 | `incr_mean_variance_axis` | instance | `X, axis, last_mean, last_var, last_n, weights =...` | `None` | `sklearn.utils.sparsefuncs.incr_mean_variance_axis(X, axis, last_mean, last_var, last_n, weights = None)` | complex | 113 | 抛异常, 有逻辑 |
| 5 | `inplace_column_scale` | instance | `X, scale` | `None` | `sklearn.utils.sparsefuncs.inplace_column_scale(X, scale)` | complex | 43 | 有逻辑 |
| 6 | `inplace_row_scale` | instance | `X, scale` | `None` | `sklearn.utils.sparsefuncs.inplace_row_scale(X, scale)` | complex | 42 | 有逻辑 |
| 7 | `inplace_swap_row_csc` | instance | `X, m, n` | `None` | `sklearn.utils.sparsefuncs.inplace_swap_row_csc(X, m, n)` | medium | 27 | 抛异常, 有逻辑 |
| 8 | `inplace_swap_row_csr` | instance | `X, m, n` | `None` | `sklearn.utils.sparsefuncs.inplace_swap_row_csr(X, m, n)` | complex | 61 | 抛异常, 有逻辑 |
| 9 | `inplace_swap_row` | instance | `X, m, n` | `None` | `sklearn.utils.sparsefuncs.inplace_swap_row(X, m, n)` | complex | 43 | 有逻辑 |
| 10 | `inplace_swap_column` | instance | `X, m, n` | `None` | `sklearn.utils.sparsefuncs.inplace_swap_column(X, m, n)` | complex | 47 | 有逻辑 |
| 11 | `min_max_axis` | instance | `X, axis, ignore_nan = False` | `None` | `sklearn.utils.sparsefuncs.min_max_axis(X, axis, ignore_nan = False)` | medium | 34 | 有逻辑 |
| 12 | `count_nonzero` | instance | `X, axis = None, sample_weight = None` | `None` | `sklearn.utils.sparsefuncs.count_nonzero(X, axis = None, sample_weight = None)` | complex | 52 | 抛异常, 有逻辑 |
| 13 | `csc_median_axis_0` | instance | `X` | `None` | `sklearn.utils.sparsefuncs.csc_median_axis_0(X)` | medium | 29 | 抛异常, 有逻辑 |
| 14 | `sparse_matmul_to_dense` | instance | `A, B, out = None` | `None` | `sklearn.utils.sparsefuncs.sparse_matmul_to_dense(A, B, out = None)` | complex | 61 | 抛异常, 有逻辑 |

---

## 📦 模块: `sklearn.utils.validation`

**文件路径**: `sklearn/utils/validation.py`

**模块函数数**: 15

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `assert_all_finite` | instance | `X, allow_nan = False, estimator_name = None, in...` | `None` | `sklearn.utils.validation.assert_all_finite(X, allow_nan = False, estimator_name = None, input_name = '')` | complex | 44 | 有逻辑 |
| 2 | `as_float_array` | instance | `X, copy = True, ensure_all_finite = True` | `None` | `sklearn.utils.validation.as_float_array(X, copy = True, ensure_all_finite = True)` | complex | 62 | 抛异常, 有逻辑 |
| 3 | `check_memory` | instance | `memory` | `None` | `sklearn.utils.validation.check_memory(memory)` | complex | 38 | 抛异常, 有逻辑 |
| 4 | `check_consistent_length` | instance | `*arrays` | `None` | `sklearn.utils.validation.check_consistent_length(*arrays)` | medium | 23 | 抛异常, 有逻辑 |
| 5 | `indexable` | instance | `*iterables` | `None` | `sklearn.utils.validation.indexable(*iterables)` | medium | 33 | 有逻辑 |
| 6 | `check_array` | instance | `array, accept_sparse = False, accept_large_spar...` | `None` | `sklearn.utils.validation.check_array(array, accept_sparse = False, accept_large_sparse = True, dtype = 'numeric', order = None, copy = False, force_writeable = False, ensure_all_finite = True, ensure_non_negative = False, ensure_2d = True, allow_nd = False, ensure_min_samples = 1, ensure_min_features = 1, estimator = None, input_name = '')` | complex | 421 | 抛异常, 有逻辑 |
| 7 | `check_X_y` | instance | `X, y, accept_sparse = False, accept_large_spars...` | `None` | `sklearn.utils.validation.check_X_y(X, y, accept_sparse = False, accept_large_sparse = True, dtype = 'numeric', order = None, copy = False, force_writeable = False, ensure_all_finite = True, ensure_2d = True, allow_nd = False, multi_output = False, ensure_min_samples = 1, ensure_min_features = 1, y_numeric = False, estimator = None)` | complex | 166 | 抛异常, 有逻辑 |
| 8 | `column_or_1d` | instance | `y, dtype = None, input_name = 'y', warn = False...` | `None` | `sklearn.utils.validation.column_or_1d(y, dtype = None, input_name = 'y', warn = False, device = None)` | complex | 76 | 抛异常, 有逻辑 |
| 9 | `check_random_state` | instance | `seed` | `None` | `sklearn.utils.validation.check_random_state(seed)` | medium | 31 | 抛异常, 有逻辑 |
| 10 | `has_fit_parameter` | instance | `estimator, parameter` | `None` | `sklearn.utils.validation.has_fit_parameter(estimator, parameter)` | medium | 31 | 有逻辑 |
| 11 | `check_symmetric` | instance | `array, tol = 1e-10, raise_warning = True, raise...` | `None` | `sklearn.utils.validation.check_symmetric(array, tol = 1e-10, raise_warning = True, raise_exception = False)` | complex | 76 | 抛异常, 有逻辑 |
| 12 | `check_is_fitted` | instance | `estimator, attributes = None, msg = None, all_o...` | `None` | `sklearn.utils.validation.check_is_fitted(estimator, attributes = None, msg = None, all_or_any = all)` | complex | 85 | 抛异常, 有逻辑 |
| 13 | `check_non_negative` | instance | `X, whom` | `None` | `sklearn.utils.validation.check_non_negative(X, whom)` | medium | 26 | 抛异常, 有逻辑 |
| 14 | `check_scalar` | instance | `x, name, target_type, min_val = None, max_val =...` | `None` | `sklearn.utils.validation.check_scalar(x, name, target_type, min_val = None, max_val = None, include_boundaries = 'both')` | complex | 126 | 抛异常, 有逻辑 |
| 15 | `validate_data` | instance | `X = 'no_validation', y = 'no_validation', reset...` | `None` | `sklearn.utils.validation.validate_data(X = 'no_validation', y = 'no_validation', reset = True, validate_separately = False, skip_check_array = False, **check_params)` | complex | 133 | 抛异常, 有逻辑 |

---

## 🔹 `BaseLink`

**完全限定名**: `sklearn._loss.link.BaseLink`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `link` | instance | `self, y_pred, out = None` | `None` | `sklearn._loss.link.BaseLink.link(self, y_pred, out = None)` | medium | 20 | 抽象方法 |
| 2 | `inverse` | instance | `self, raw_prediction, out = None` | `None` | `sklearn._loss.link.BaseLink.inverse(self, raw_prediction, out = None)` | medium | 20 | 抽象方法 |

---

## 🔹 `HalfLogitLink`

**完全限定名**: `sklearn._loss.link.HalfLogitLink`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `link` | instance | `self, y_pred, out = None` | `None` | `sklearn._loss.link.HalfLogitLink.link(self, y_pred, out = None)` | simple | 4 | - |
| 2 | `inverse` | instance | `self, raw_prediction, out = None` | `None` | `sklearn._loss.link.HalfLogitLink.inverse(self, raw_prediction, out = None)` | simple | 2 | - |

---

## 🔹 `IdentityLink`

**完全限定名**: `sklearn._loss.link.IdentityLink`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `link` | instance | `self, y_pred, out = None` | `None` | `sklearn._loss.link.IdentityLink.link(self, y_pred, out = None)` | simple | 6 | 有逻辑 |

---

## 🔹 `Interval`

**完全限定名**: `sklearn._loss.link.Interval`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__post_init__` | instance | `self` | `None` | `sklearn._loss.link.Interval.__post_init__(self)` | simple | 6 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `includes` | instance | `self, x` | `None` | `sklearn._loss.link.Interval.includes(self, x)` | medium | 27 | 有逻辑 |

---

## 🔹 `LogLink`

**完全限定名**: `sklearn._loss.link.LogLink`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `link` | instance | `self, y_pred, out = None` | `None` | `sklearn._loss.link.LogLink.link(self, y_pred, out = None)` | simple | 2 | - |
| 2 | `inverse` | instance | `self, raw_prediction, out = None` | `None` | `sklearn._loss.link.LogLink.inverse(self, raw_prediction, out = None)` | simple | 2 | - |

---

## 🔹 `LogitLink`

**完全限定名**: `sklearn._loss.link.LogitLink`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `link` | instance | `self, y_pred, out = None` | `None` | `sklearn._loss.link.LogitLink.link(self, y_pred, out = None)` | simple | 2 | - |
| 2 | `inverse` | instance | `self, raw_prediction, out = None` | `None` | `sklearn._loss.link.LogitLink.inverse(self, raw_prediction, out = None)` | simple | 2 | - |

---

## 🔹 `MultinomialLogit`

**完全限定名**: `sklearn._loss.link.MultinomialLogit`

**文件路径**: `sklearn/_loss/link.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `symmetrize_raw_prediction` | instance | `self, raw_prediction` | `None` | `sklearn._loss.link.MultinomialLogit.symmetrize_raw_prediction(self, raw_prediction)` | simple | 2 | - |
| 2 | `link` | instance | `self, y_pred, out = None` | `None` | `sklearn._loss.link.MultinomialLogit.link(self, y_pred, out = None)` | simple | 4 | - |
| 3 | `inverse` | instance | `self, raw_prediction, out = None` | `None` | `sklearn._loss.link.MultinomialLogit.inverse(self, raw_prediction, out = None)` | simple | 7 | 有逻辑 |

---

## 🔹 `AbsoluteError`

**完全限定名**: `sklearn._loss.loss.AbsoluteError`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None` | `None` | `sklearn._loss.loss.AbsoluteError.__init__(self, sample_weight = None)` | simple | 4 | 魔术方法 |
| 2 | `fit_intercept_only` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.AbsoluteError.fit_intercept_only(self, y_true, sample_weight = None)` | simple | 10 | 有逻辑 |

---

## 🔹 `BaseLoss`

**完全限定名**: `sklearn._loss.loss.BaseLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 11

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, closs, link, n_classes = None` | `None` | `sklearn._loss.loss.BaseLoss.__init__(self, closs, link, n_classes = None)` | simple | 8 | 魔术方法 |
| 2 | `in_y_true_range` | instance | `self, y` | `None` | `sklearn._loss.loss.BaseLoss.in_y_true_range(self, y)` | simple | 8 | 有逻辑 |
| 3 | `in_y_pred_range` | instance | `self, y` | `None` | `sklearn._loss.loss.BaseLoss.in_y_pred_range(self, y)` | simple | 8 | 有逻辑 |
| 4 | `loss` | instance | `self, y_true, raw_prediction, sample_weight = N...` | `None` | `sklearn._loss.loss.BaseLoss.loss(self, y_true, raw_prediction, sample_weight = None, loss_out = None, n_threads = 1)` | complex | 44 | 有逻辑 |
| 5 | `loss_gradient` | instance | `self, y_true, raw_prediction, sample_weight = N...` | `None` | `sklearn._loss.loss.BaseLoss.loss_gradient(self, y_true, raw_prediction, sample_weight = None, loss_out = None, gradient_out = None, n_threads = 1)` | complex | 62 | 有逻辑 |
| 6 | `gradient` | instance | `self, y_true, raw_prediction, sample_weight = N...` | `None` | `sklearn._loss.loss.BaseLoss.gradient(self, y_true, raw_prediction, sample_weight = None, gradient_out = None, n_threads = 1)` | complex | 48 | 有逻辑 |
| 7 | `gradient_hessian` | instance | `self, y_true, raw_prediction, sample_weight = N...` | `None` | `sklearn._loss.loss.BaseLoss.gradient_hessian(self, y_true, raw_prediction, sample_weight = None, gradient_out = None, hessian_out = None, n_threads = 1)` | complex | 65 | 有逻辑 |
| 8 | `__call__` | instance | `self, y_true, raw_prediction, sample_weight = N...` | `None` | `sklearn._loss.loss.BaseLoss.__call__(self, y_true, raw_prediction, sample_weight = None, n_threads = 1)` | medium | 30 | 魔术方法 |
| 9 | `fit_intercept_only` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.BaseLoss.fit_intercept_only(self, y_true, sample_weight = None)` | complex | 41 | 有逻辑 |
| 10 | `constant_to_optimal_zero` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.BaseLoss.constant_to_optimal_zero(self, y_true, sample_weight = None)` | medium | 20 | - |
| 11 | `init_gradient_and_hessian` | instance | `self, n_samples, dtype = np.float64, order = 'F'` | `None` | `sklearn._loss.loss.BaseLoss.init_gradient_and_hessian(self, n_samples, dtype = np.float64, order = 'F')` | complex | 50 | 抛异常, 有逻辑 |

---

## 🔹 `ExponentialLoss`

**完全限定名**: `sklearn._loss.loss.ExponentialLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None` | `None` | `sklearn._loss.loss.ExponentialLoss.__init__(self, sample_weight = None)` | simple | 7 | 魔术方法 |
| 2 | `constant_to_optimal_zero` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.ExponentialLoss.constant_to_optimal_zero(self, y_true, sample_weight = None)` | simple | 6 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, raw_prediction` | `None` | `sklearn._loss.loss.ExponentialLoss.predict_proba(self, raw_prediction)` | medium | 20 | 有逻辑 |

---

## 🔹 `HalfBinomialLoss`

**完全限定名**: `sklearn._loss.loss.HalfBinomialLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None` | `None` | `sklearn._loss.loss.HalfBinomialLoss.__init__(self, sample_weight = None)` | simple | 7 | 魔术方法 |
| 2 | `constant_to_optimal_zero` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.HalfBinomialLoss.constant_to_optimal_zero(self, y_true, sample_weight = None)` | simple | 6 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, raw_prediction` | `None` | `sklearn._loss.loss.HalfBinomialLoss.predict_proba(self, raw_prediction)` | medium | 20 | 有逻辑 |

---

## 🔹 `HalfGammaLoss`

**完全限定名**: `sklearn._loss.loss.HalfGammaLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None` | `None` | `sklearn._loss.loss.HalfGammaLoss.__init__(self, sample_weight = None)` | simple | 3 | 魔术方法 |
| 2 | `constant_to_optimal_zero` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.HalfGammaLoss.constant_to_optimal_zero(self, y_true, sample_weight = None)` | simple | 5 | 有逻辑 |

---

## 🔹 `HalfMultinomialLoss`

**完全限定名**: `sklearn._loss.loss.HalfMultinomialLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None, n_classes = 3` | `None` | `sklearn._loss.loss.HalfMultinomialLoss.__init__(self, sample_weight = None, n_classes = 3)` | simple | 8 | 魔术方法 |
| 2 | `in_y_true_range` | instance | `self, y` | `None` | `sklearn._loss.loss.HalfMultinomialLoss.in_y_true_range(self, y)` | simple | 8 | 有逻辑 |
| 3 | `fit_intercept_only` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.HalfMultinomialLoss.fit_intercept_only(self, y_true, sample_weight = None)` | medium | 25 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, raw_prediction` | `None` | `sklearn._loss.loss.HalfMultinomialLoss.predict_proba(self, raw_prediction)` | medium | 14 | - |
| 5 | `gradient_proba` | instance | `self, y_true, raw_prediction, sample_weight = N...` | `None` | `sklearn._loss.loss.HalfMultinomialLoss.gradient_proba(self, y_true, raw_prediction, sample_weight = None, gradient_out = None, proba_out = None, n_threads = 1)` | complex | 54 | 有逻辑 |

---

## 🔹 `HalfPoissonLoss`

**完全限定名**: `sklearn._loss.loss.HalfPoissonLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None` | `None` | `sklearn._loss.loss.HalfPoissonLoss.__init__(self, sample_weight = None)` | simple | 3 | 魔术方法 |
| 2 | `constant_to_optimal_zero` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.HalfPoissonLoss.constant_to_optimal_zero(self, y_true, sample_weight = None)` | simple | 5 | 有逻辑 |

---

## 🔹 `HalfSquaredError`

**完全限定名**: `sklearn._loss.loss.HalfSquaredError`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None` | `None` | `sklearn._loss.loss.HalfSquaredError.__init__(self, sample_weight = None)` | simple | 3 | 魔术方法 |

---

## 🔹 `HalfTweedieLoss`

**完全限定名**: `sklearn._loss.loss.HalfTweedieLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None, power = 1.5` | `None` | `sklearn._loss.loss.HalfTweedieLoss.__init__(self, sample_weight = None, power = 1.5)` | medium | 11 | 魔术方法, 有逻辑 |
| 2 | `constant_to_optimal_zero` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.HalfTweedieLoss.constant_to_optimal_zero(self, y_true, sample_weight = None)` | medium | 19 | 有逻辑 |

---

## 🔹 `HalfTweedieLossIdentity`

**完全限定名**: `sklearn._loss.loss.HalfTweedieLossIdentity`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None, power = 1.5` | `None` | `sklearn._loss.loss.HalfTweedieLossIdentity.__init__(self, sample_weight = None, power = 1.5)` | medium | 16 | 魔术方法, 有逻辑 |

---

## 🔹 `HuberLoss`

**完全限定名**: `sklearn._loss.loss.HuberLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None, quantile = 0.9, del...` | `None` | `sklearn._loss.loss.HuberLoss.__init__(self, sample_weight = None, quantile = 0.9, delta = 0.5)` | medium | 16 | 魔术方法 |
| 2 | `fit_intercept_only` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.HuberLoss.fit_intercept_only(self, y_true, sample_weight = None)` | medium | 17 | 有逻辑 |

---

## 🔹 `PinballLoss`

**完全限定名**: `sklearn._loss.loss.PinballLoss`

**文件路径**: `sklearn/_loss/loss.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_weight = None, quantile = 0.5` | `None` | `sklearn._loss.loss.PinballLoss.__init__(self, sample_weight = None, quantile = 0.5)` | medium | 15 | 魔术方法 |
| 2 | `fit_intercept_only` | instance | `self, y_true, sample_weight = None` | `None` | `sklearn._loss.loss.PinballLoss.fit_intercept_only(self, y_true, sample_weight = None)` | medium | 12 | 有逻辑 |

---

## 🔹 `BaseEstimator`

**完全限定名**: `sklearn.base.BaseEstimator`

**文件路径**: `sklearn/base.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__dir__` | instance | `self` | `None` | `sklearn.base.BaseEstimator.__dir__(self)` | simple | 6 | 魔术方法, 有逻辑 |
| 2 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.base.BaseEstimator.get_params(self, deep = True)` | medium | 23 | 有逻辑 |
| 3 | `set_params` | instance | `self, **params` | `None` | `sklearn.base.BaseEstimator.set_params(self, **params)` | complex | 43 | 抛异常, 有逻辑 |
| 4 | `__sklearn_clone__` | instance | `self` | `None` | `sklearn.base.BaseEstimator.__sklearn_clone__(self)` | simple | 2 | 魔术方法 |
| 5 | `__repr__` | instance | `self, N_CHAR_MAX = 700` | `None` | `sklearn.base.BaseEstimator.__repr__(self, N_CHAR_MAX = 700)` | medium | 51 | 魔术方法, 有逻辑 |
| 6 | `__getstate__` | instance | `self` | `None` | `sklearn.base.BaseEstimator.__getstate__(self)` | medium | 21 | 魔术方法, 抛异常, 有逻辑 |
| 7 | `__setstate__` | instance | `self, state` | `None` | `sklearn.base.BaseEstimator.__setstate__(self, state)` | medium | 15 | 魔术方法, 有逻辑 |
| 8 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.BaseEstimator.__sklearn_tags__(self)` | simple | 8 | 魔术方法 |

---

## 🔹 `BiclusterMixin`

**完全限定名**: `sklearn.base.BiclusterMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `biclusters_` | property | `self` | `None` | `sklearn.base.BiclusterMixin.biclusters_(self)` | simple | 6 | - |
| 2 | `get_indices` | instance | `self, i` | `None` | `sklearn.base.BiclusterMixin.get_indices(self, i)` | medium | 20 | 有逻辑 |
| 3 | `get_shape` | instance | `self, i` | `None` | `sklearn.base.BiclusterMixin.get_shape(self, i)` | medium | 18 | 有逻辑 |
| 4 | `get_submatrix` | instance | `self, i, data` | `None` | `sklearn.base.BiclusterMixin.get_submatrix(self, i, data)` | medium | 24 | 有逻辑 |

---

## 🔹 `ClassNamePrefixFeaturesOutMixin`

**完全限定名**: `sklearn.base.ClassNamePrefixFeaturesOutMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.base.ClassNamePrefixFeaturesOutMixin.get_feature_names_out(self, input_features = None)` | medium | 21 | 有逻辑 |

---

## 🔹 `ClassifierMixin`

**完全限定名**: `sklearn.base.ClassifierMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.ClassifierMixin.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 2 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.base.ClassifierMixin.score(self, X, y, sample_weight = None)` | medium | 27 | 有逻辑 |

---

## 🔹 `ClusterMixin`

**完全限定名**: `sklearn.base.ClusterMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.ClusterMixin.__sklearn_tags__(self)` | simple | 6 | 魔术方法, 有逻辑 |
| 2 | `fit_predict` | instance | `self, X, y = None, **kwargs` | `None` | `sklearn.base.ClusterMixin.fit_predict(self, X, y = None, **kwargs)` | medium | 26 | 有逻辑 |

---

## 🔹 `DensityMixin`

**完全限定名**: `sklearn.base.DensityMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.DensityMixin.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 2 | `score` | instance | `self, X, y = None` | `None` | `sklearn.base.DensityMixin.score(self, X, y = None)` | medium | 16 | 有逻辑 |

---

## 🔹 `MultiOutputMixin`

**完全限定名**: `sklearn.base.MultiOutputMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.MultiOutputMixin.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `OneToOneFeatureMixin`

**完全限定名**: `sklearn.base.OneToOneFeatureMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.base.OneToOneFeatureMixin.get_feature_names_out(self, input_features = None)` | medium | 25 | 有逻辑 |

---

## 🔹 `OutlierMixin`

**完全限定名**: `sklearn.base.OutlierMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.OutlierMixin.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 2 | `fit_predict` | instance | `self, X, y = None, **kwargs` | `None` | `sklearn.base.OutlierMixin.fit_predict(self, X, y = None, **kwargs)` | complex | 51 | 抛异常, 有逻辑 |

---

## 🔹 `RegressorMixin`

**完全限定名**: `sklearn.base.RegressorMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.RegressorMixin.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 2 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.base.RegressorMixin.score(self, X, y, sample_weight = None)` | complex | 45 | 有逻辑 |

---

## 🔹 `TransformerMixin`

**完全限定名**: `sklearn.base.TransformerMixin`

**文件路径**: `sklearn/base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.base.TransformerMixin.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 2 | `fit_transform` | instance | `self, X, y = None, **fit_params` | `None` | `sklearn.base.TransformerMixin.fit_transform(self, X, y = None, **fit_params)` | complex | 60 | 抛异常, 有逻辑 |

---

## 🔹 `CalibratedClassifierCV`

**完全限定名**: `sklearn.calibration.CalibratedClassifierCV`

**文件路径**: `sklearn/calibration.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, method = 'sigmoid', cv ...` | `None` | `sklearn.calibration.CalibratedClassifierCV.__init__(self, estimator = None, method = 'sigmoid', cv = None, n_jobs = None, ensemble = 'auto')` | medium | 14 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **fit_params` | `None` | `sklearn.calibration.CalibratedClassifierCV.fit(self, X, y, sample_weight = None, **fit_params)` | complex | 168 | 抛异常, 有逻辑 |
| 3 | `predict_proba` | instance | `self, X` | `None` | `sklearn.calibration.CalibratedClassifierCV.predict_proba(self, X)` | medium | 28 | 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.calibration.CalibratedClassifierCV.predict(self, X)` | medium | 23 | 有逻辑 |
| 5 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.calibration.CalibratedClassifierCV.get_metadata_routing(self)` | medium | 25 | - |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.calibration.CalibratedClassifierCV.__sklearn_tags__(self)` | simple | 8 | 魔术方法 |

---

## 🔹 `CalibrationDisplay`

**完全限定名**: `sklearn.calibration.CalibrationDisplay`

**文件路径**: `sklearn/calibration.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, prob_true, prob_pred, y_prob, estimator_n...` | `None` | `sklearn.calibration.CalibrationDisplay.__init__(self, prob_true, prob_pred, y_prob, estimator_name = None, pos_label = None)` | simple | 8 | 魔术方法 |
| 2 | `plot` | instance | `self, ax = None, name = None, ref_line = True, ...` | `None` | `sklearn.calibration.CalibrationDisplay.plot(self, ax = None, name = None, ref_line = True, **kwargs)` | complex | 53 | 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, n_bins = 5, strategy = 'u...` | `None` | `sklearn.calibration.CalibrationDisplay.from_estimator(cls, estimator, X, y, n_bins = 5, strategy = 'uniform', pos_label = None, name = None, ax = None, ref_line = True, **kwargs)` | complex | 122 | 有逻辑 |
| 4 | `from_predictions` | class | `cls, y_true, y_prob, n_bins = 5, strategy = 'un...` | `None` | `sklearn.calibration.CalibrationDisplay.from_predictions(cls, y_true, y_prob, n_bins = 5, strategy = 'uniform', pos_label = None, name = None, ax = None, ref_line = True, **kwargs)` | complex | 112 | 有逻辑 |

---

## 🔹 `AffinityPropagation`

**完全限定名**: `sklearn.cluster._affinity_propagation.AffinityPropagation`

**文件路径**: `sklearn/cluster/_affinity_propagation.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, damping = 0.5, max_iter = 200, convergenc...` | `None` | `sklearn.cluster._affinity_propagation.AffinityPropagation.__init__(self, damping = 0.5, max_iter = 200, convergence_iter = 15, copy = True, preference = None, affinity = 'euclidean', verbose = False, random_state = None)` | medium | 20 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._affinity_propagation.AffinityPropagation.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._affinity_propagation.AffinityPropagation.fit(self, X, y = None)` | complex | 59 | 抛异常, 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.cluster._affinity_propagation.AffinityPropagation.predict(self, X)` | complex | 34 | 抛异常, 有逻辑 |
| 5 | `fit_predict` | instance | `self, X, y = None` | `None` | `sklearn.cluster._affinity_propagation.AffinityPropagation.fit_predict(self, X, y = None)` | medium | 20 | 有逻辑 |

---

## 🔹 `AgglomerativeClustering`

**完全限定名**: `sklearn.cluster._agglomerative.AgglomerativeClustering`

**文件路径**: `sklearn/cluster/_agglomerative.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 2, metric = 'euclidean', mem...` | `None` | `sklearn.cluster._agglomerative.AgglomerativeClustering.__init__(self, n_clusters = 2, metric = 'euclidean', memory = None, connectivity = None, compute_full_tree = 'auto', linkage = 'ward', distance_threshold = None, compute_distances = False)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._agglomerative.AgglomerativeClustering.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `fit_predict` | instance | `self, X, y = None` | `None` | `sklearn.cluster._agglomerative.AgglomerativeClustering.fit_predict(self, X, y = None)` | medium | 22 | 有逻辑 |

---

## 🔹 `FeatureAgglomeration`

**完全限定名**: `sklearn.cluster._agglomerative.FeatureAgglomeration`

**文件路径**: `sklearn/cluster/_agglomerative.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 2, metric = 'euclidean', mem...` | `None` | `sklearn.cluster._agglomerative.FeatureAgglomeration.__init__(self, n_clusters = 2, metric = 'euclidean', memory = None, connectivity = None, compute_full_tree = 'auto', linkage = 'ward', pooling_func = np.mean, distance_threshold = None, compute_distances = False)` | medium | 24 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._agglomerative.FeatureAgglomeration.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `fit_predict` | property | `self` | `None` | `sklearn.cluster._agglomerative.FeatureAgglomeration.fit_predict(self)` | simple | 3 | 抛异常 |

---

## 🔹 `BaseSpectral`

**完全限定名**: `sklearn.cluster._bicluster.BaseSpectral`

**文件路径**: `sklearn/cluster/_bicluster.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 3, svd_method = 'randomized'...` | `None` | `sklearn.cluster._bicluster.BaseSpectral.__init__(self, n_clusters = 3, svd_method = 'randomized', n_svd_vecs = None, mini_batch = False, init = 'k-means++', n_init = 10, random_state = None)` | medium | 17 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._bicluster.BaseSpectral.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._bicluster.BaseSpectral.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SpectralBiclustering`

**完全限定名**: `sklearn.cluster._bicluster.SpectralBiclustering`

**文件路径**: `sklearn/cluster/_bicluster.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 3, method = 'bistochastic', ...` | `None` | `sklearn.cluster._bicluster.SpectralBiclustering.__init__(self, n_clusters = 3, method = 'bistochastic', n_components = 6, n_best = 3, svd_method = 'randomized', n_svd_vecs = None, mini_batch = False, init = 'k-means++', n_init = 10, random_state = None)` | medium | 20 | 魔术方法 |

---

## 🔹 `SpectralCoclustering`

**完全限定名**: `sklearn.cluster._bicluster.SpectralCoclustering`

**文件路径**: `sklearn/cluster/_bicluster.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 3, svd_method = 'randomized'...` | `None` | `sklearn.cluster._bicluster.SpectralCoclustering.__init__(self, n_clusters = 3, svd_method = 'randomized', n_svd_vecs = None, mini_batch = False, init = 'k-means++', n_init = 10, random_state = None)` | medium | 14 | 魔术方法 |

---

## 🔹 `Birch`

**完全限定名**: `sklearn.cluster._birch.Birch`

**文件路径**: `sklearn/cluster/_birch.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, threshold = 0.5, branching_factor = 50, n...` | `None` | `sklearn.cluster._birch.Birch.__init__(self, threshold = 0.5, branching_factor = 50, n_clusters = 3, compute_labels = True)` | medium | 12 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._birch.Birch.fit(self, X, y = None)` | medium | 18 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X = None, y = None` | `None` | `sklearn.cluster._birch.Birch.partial_fit(self, X = None, y = None)` | medium | 25 | 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.cluster._birch.Birch.predict(self, X)` | medium | 19 | - |
| 5 | `transform` | instance | `self, X` | `None` | `sklearn.cluster._birch.Birch.transform(self, X)` | medium | 21 | - |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._birch.Birch.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `BisectingKMeans`

**完全限定名**: `sklearn.cluster._bisect_k_means.BisectingKMeans`

**文件路径**: `sklearn/cluster/_bisect_k_means.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 8, init = 'random', n_init =...` | `None` | `sklearn.cluster._bisect_k_means.BisectingKMeans.__init__(self, n_clusters = 8, init = 'random', n_init = 1, random_state = None, max_iter = 300, verbose = 0, tol = 0.0001, copy_x = True, algorithm = 'lloyd', bisecting_strategy = 'biggest_inertia')` | medium | 27 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.cluster._bisect_k_means.BisectingKMeans.fit(self, X, y = None, sample_weight = None)` | complex | 92 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.cluster._bisect_k_means.BisectingKMeans.predict(self, X)` | medium | 31 | - |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._bisect_k_means.BisectingKMeans.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `DBSCAN`

**完全限定名**: `sklearn.cluster._dbscan.DBSCAN`

**文件路径**: `sklearn/cluster/_dbscan.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, eps = 0.5, min_samples = 5, metric = 'euc...` | `None` | `sklearn.cluster._dbscan.DBSCAN.__init__(self, eps = 0.5, min_samples = 5, metric = 'euclidean', metric_params = None, algorithm = 'auto', leaf_size = 30, p = None, n_jobs = None)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.cluster._dbscan.DBSCAN.fit(self, X, y = None, sample_weight = None)` | complex | 78 | 有逻辑 |
| 3 | `fit_predict` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.cluster._dbscan.DBSCAN.fit_predict(self, X, y = None, sample_weight = None)` | medium | 31 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._dbscan.DBSCAN.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `AgglomerationTransform`

**完全限定名**: `sklearn.cluster._feature_agglomeration.AgglomerationTransform`

**文件路径**: `sklearn/cluster/_feature_agglomeration.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `transform` | instance | `self, X` | `None` | `sklearn.cluster._feature_agglomeration.AgglomerationTransform.transform(self, X)` | medium | 33 | 有逻辑 |
| 2 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.cluster._feature_agglomeration.AgglomerationTransform.inverse_transform(self, X)` | medium | 19 | - |

---

## 🔹 `HDBSCAN`

**完全限定名**: `sklearn.cluster._hdbscan.hdbscan.HDBSCAN`

**文件路径**: `sklearn/cluster/_hdbscan/hdbscan.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, min_cluster_size = 5, min_samples = None,...` | `None` | `sklearn.cluster._hdbscan.hdbscan.HDBSCAN.__init__(self, min_cluster_size = 5, min_samples = None, cluster_selection_epsilon = 0.0, max_cluster_size = None, metric = 'euclidean', metric_params = None, alpha = 1.0, algorithm = 'auto', leaf_size = 40, n_jobs = None, cluster_selection_method = 'eom', allow_single_cluster = False, store_centers = None, copy = 'warn')` | complex | 31 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._hdbscan.hdbscan.HDBSCAN.fit(self, X, y = None)` | complex | 200 | 抛异常, 有逻辑 |
| 3 | `fit_predict` | instance | `self, X, y = None` | `None` | `sklearn.cluster._hdbscan.hdbscan.HDBSCAN.fit_predict(self, X, y = None)` | medium | 20 | - |
| 4 | `dbscan_clustering` | instance | `self, cut_distance, min_cluster_size = 5` | `None` | `sklearn.cluster._hdbscan.hdbscan.HDBSCAN.dbscan_clustering(self, cut_distance, min_cluster_size = 5)` | complex | 48 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._hdbscan.hdbscan.HDBSCAN.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `KMeans`

**完全限定名**: `sklearn.cluster._kmeans.KMeans`

**文件路径**: `sklearn/cluster/_kmeans.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 8, init = 'k-means++', n_ini...` | `None` | `sklearn.cluster._kmeans.KMeans.__init__(self, n_clusters = 8, init = 'k-means++', n_init = 'auto', max_iter = 300, tol = 0.0001, verbose = 0, random_state = None, copy_x = True, algorithm = 'lloyd')` | medium | 25 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.cluster._kmeans.KMeans.fit(self, X, y = None, sample_weight = None)` | complex | 128 | 有逻辑 |

---

## 🔹 `MiniBatchKMeans`

**完全限定名**: `sklearn.cluster._kmeans.MiniBatchKMeans`

**文件路径**: `sklearn/cluster/_kmeans.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 8, init = 'k-means++', max_i...` | `None` | `sklearn.cluster._kmeans.MiniBatchKMeans.__init__(self, n_clusters = 8, init = 'k-means++', max_iter = 100, batch_size = 1024, verbose = 0, compute_labels = True, random_state = None, tol = 0.0, max_no_improvement = 10, init_size = None, n_init = 'auto', reassignment_ratio = 0.01)` | medium | 31 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.cluster._kmeans.MiniBatchKMeans.fit(self, X, y = None, sample_weight = None)` | complex | 155 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.cluster._kmeans.MiniBatchKMeans.partial_fit(self, X, y = None, sample_weight = None)` | complex | 101 | 有逻辑 |

---

## 🔹 `MeanShift`

**完全限定名**: `sklearn.cluster._mean_shift.MeanShift`

**文件路径**: `sklearn/cluster/_mean_shift.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, bandwidth = None, seeds = None, bin_seedi...` | `None` | `sklearn.cluster._mean_shift.MeanShift.__init__(self, bandwidth = None, seeds = None, bin_seeding = False, min_bin_freq = 1, cluster_all = True, n_jobs = None, max_iter = 300)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._mean_shift.MeanShift.fit(self, X, y = None)` | complex | 92 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.cluster._mean_shift.MeanShift.predict(self, X)` | medium | 17 | - |

---

## 🔹 `OPTICS`

**完全限定名**: `sklearn.cluster._optics.OPTICS`

**文件路径**: `sklearn/cluster/_optics.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, min_samples = 5, max_eps = np.inf, metric...` | `None` | `sklearn.cluster._optics.OPTICS.__init__(self, min_samples = 5, max_eps = np.inf, metric = 'minkowski', p = 2, metric_params = None, cluster_method = 'xi', eps = None, xi = 0.05, predecessor_correction = True, min_cluster_size = None, algorithm = 'auto', leaf_size = 30, memory = None, n_jobs = None)` | complex | 32 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._optics.OPTICS.fit(self, X, y = None)` | complex | 91 | 抛异常, 有逻辑 |

---

## 🔹 `SpectralClustering`

**完全限定名**: `sklearn.cluster._spectral.SpectralClustering`

**文件路径**: `sklearn/cluster/_spectral.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_clusters = 8, eigen_solver = None, n_co...` | `None` | `sklearn.cluster._spectral.SpectralClustering.__init__(self, n_clusters = 8, eigen_solver = None, n_components = None, random_state = None, n_init = 10, gamma = 1.0, affinity = 'rbf', n_neighbors = 10, eigen_tol = 'auto', assign_labels = 'kmeans', degree = 3, coef0 = 1, kernel_params = None, n_jobs = None, verbose = False)` | complex | 34 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.cluster._spectral.SpectralClustering.fit(self, X, y = None)` | complex | 101 | 有逻辑 |
| 3 | `fit_predict` | instance | `self, X, y = None` | `None` | `sklearn.cluster._spectral.SpectralClustering.fit_predict(self, X, y = None)` | medium | 23 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.cluster._spectral.SpectralClustering.__sklearn_tags__(self)` | simple | 8 | 魔术方法 |

---

## 🔹 `ColumnTransformer`

**完全限定名**: `sklearn.compose._column_transformer.ColumnTransformer`

**文件路径**: `sklearn/compose/_column_transformer.py`

**公共方法数**: 12

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, transformers, remainder = 'drop', sparse_...` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.__init__(self, transformers, remainder = 'drop', sparse_threshold = 0.3, n_jobs = None, transformer_weights = None, verbose = False, verbose_feature_names_out = True, force_int_remainder_cols = 'deprecated')` | medium | 20 | 魔术方法 |
| 2 | `set_output` | instance | `self, transform = None` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.set_output(self, transform = None)` | complex | 40 | 有逻辑 |
| 3 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.get_params(self, deep = True)` | medium | 19 | 有逻辑 |
| 4 | `set_params` | instance | `self, **kwargs` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.set_params(self, **kwargs)` | medium | 19 | - |
| 5 | `named_transformers_` | property | `self` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.named_transformers_(self)` | simple | 9 | 有逻辑 |
| 6 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.get_feature_names_out(self, input_features = None)` | complex | 45 | 有逻辑 |
| 7 | `fit` | instance | `self, X, y = None, **params` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.fit(self, X, y = None, **params)` | medium | 31 | 有逻辑 |
| 8 | `fit_transform` | instance | `self, X, y = None, **params` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.fit_transform(self, X, y = None, **params)` | complex | 85 | 有逻辑 |
| 9 | `transform` | instance | `self, X, **params` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.transform(self, X, **params)` | complex | 82 | 抛异常, 有逻辑 |
| 10 | `__getitem__` | instance | `self, key` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.__getitem__(self, key)` | simple | 9 | 魔术方法, 抛异常, 有逻辑 |
| 11 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.get_metadata_routing(self)` | complex | 41 | 有逻辑 |
| 12 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.compose._column_transformer.ColumnTransformer.__sklearn_tags__(self)` | medium | 14 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `make_column_selector`

**完全限定名**: `sklearn.compose._column_transformer.make_column_selector`

**文件路径**: `sklearn/compose/_column_transformer.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, pattern = None, dtype_include = None, dty...` | `None` | `sklearn.compose._column_transformer.make_column_selector.__init__(self, pattern = None, dtype_include = None, dtype_exclude = None)` | simple | 4 | 魔术方法 |
| 2 | `__call__` | instance | `self, df` | `None` | `sklearn.compose._column_transformer.make_column_selector.__call__(self, df)` | medium | 22 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `TransformedTargetRegressor`

**完全限定名**: `sklearn.compose._target.TransformedTargetRegressor`

**文件路径**: `sklearn/compose/_target.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, regressor = None, transformer = None, fun...` | `None` | `sklearn.compose._target.TransformedTargetRegressor.__init__(self, regressor = None, transformer = None, func = None, inverse_func = None, check_inverse = True)` | medium | 14 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.compose._target.TransformedTargetRegressor.fit(self, X, y, **fit_params)` | complex | 75 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X, **predict_params` | `None` | `sklearn.compose._target.TransformedTargetRegressor.predict(self, X, **predict_params)` | complex | 46 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.compose._target.TransformedTargetRegressor.__sklearn_tags__(self)` | simple | 7 | 魔术方法 |
| 5 | `n_features_in_` | property | `self` | `None` | `sklearn.compose._target.TransformedTargetRegressor.n_features_in_(self)` | medium | 14 | 抛异常, 有逻辑 |
| 6 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.compose._target.TransformedTargetRegressor.get_metadata_routing(self)` | medium | 21 | - |

---

## 🔹 `EllipticEnvelope`

**完全限定名**: `sklearn.covariance._elliptic_envelope.EllipticEnvelope`

**文件路径**: `sklearn/covariance/_elliptic_envelope.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, store_precision = True, assume_centered =...` | `None` | `sklearn.covariance._elliptic_envelope.EllipticEnvelope.__init__(self, store_precision = True, assume_centered = False, support_fraction = None, contamination = 0.1, random_state = None)` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._elliptic_envelope.EllipticEnvelope.fit(self, X, y = None)` | medium | 19 | 有逻辑 |
| 3 | `decision_function` | instance | `self, X` | `None` | `sklearn.covariance._elliptic_envelope.EllipticEnvelope.decision_function(self, X)` | medium | 19 | 有逻辑 |
| 4 | `score_samples` | instance | `self, X` | `None` | `sklearn.covariance._elliptic_envelope.EllipticEnvelope.score_samples(self, X)` | medium | 15 | - |
| 5 | `predict` | instance | `self, X` | `None` | `sklearn.covariance._elliptic_envelope.EllipticEnvelope.predict(self, X)` | medium | 19 | 有逻辑 |
| 6 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.covariance._elliptic_envelope.EllipticEnvelope.score(self, X, y, sample_weight = None)` | medium | 24 | 有逻辑 |

---

## 🔹 `EmpiricalCovariance`

**完全限定名**: `sklearn.covariance._empirical_covariance.EmpiricalCovariance`

**文件路径**: `sklearn/covariance/_empirical_covariance.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, store_precision = True, assume_centered =...` | `None` | `sklearn.covariance._empirical_covariance.EmpiricalCovariance.__init__(self, store_precision = True, assume_centered = False)` | simple | 3 | 魔术方法 |
| 2 | `get_precision` | instance | `self` | `None` | `sklearn.covariance._empirical_covariance.EmpiricalCovariance.get_precision(self)` | medium | 13 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._empirical_covariance.EmpiricalCovariance.fit(self, X, y = None)` | medium | 26 | 有逻辑 |
| 4 | `score` | instance | `self, X_test, y = None` | `None` | `sklearn.covariance._empirical_covariance.EmpiricalCovariance.score(self, X_test, y = None)` | medium | 30 | 有逻辑 |
| 5 | `error_norm` | instance | `self, comp_cov, norm = 'frobenius', scaling = T...` | `None` | `sklearn.covariance._empirical_covariance.EmpiricalCovariance.error_norm(self, comp_cov, norm = 'frobenius', scaling = True, squared = True)` | complex | 50 | 抛异常, 有逻辑 |
| 6 | `mahalanobis` | instance | `self, X` | `None` | `sklearn.covariance._empirical_covariance.EmpiricalCovariance.mahalanobis(self, X)` | medium | 28 | - |

---

## 🔹 `BaseGraphicalLasso`

**完全限定名**: `sklearn.covariance._graph_lasso.BaseGraphicalLasso`

**文件路径**: `sklearn/covariance/_graph_lasso.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, tol = 0.0001, enet_tol = 0.0001, max_iter...` | `None` | `sklearn.covariance._graph_lasso.BaseGraphicalLasso.__init__, assume_centered = False)` | medium | 17 | 魔术方法 |

---

## 🔹 `GraphicalLasso`

**完全限定名**: `sklearn.covariance._graph_lasso.GraphicalLasso`

**文件路径**: `sklearn/covariance/_graph_lasso.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 0.01, mode = 'cd', covariance = N...` | `None` | `sklearn.covariance._graph_lasso.GraphicalLasso.__init__(self, alpha = 0.01, mode = 'cd', covariance = None, tol = 0.0001, enet_tol = 0.0001, max_iter = 100, verbose = False, eps = np.finfo(np.float64).eps, assume_centered = False)` | medium | 24 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._graph_lasso.GraphicalLasso.fit(self, X, y = None)` | complex | 41 | 有逻辑 |

---

## 🔹 `GraphicalLassoCV`

**完全限定名**: `sklearn.covariance._graph_lasso.GraphicalLassoCV`

**文件路径**: `sklearn/covariance/_graph_lasso.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alphas = 4, n_refinements = 4, cv = None,...` | `None` | `sklearn.covariance._graph_lasso.GraphicalLassoCV.__init__(self, alphas = 4, n_refinements = 4, cv = None, tol = 0.0001, enet_tol = 0.0001, max_iter = 100, mode = 'cd', n_jobs = None, verbose = False, eps = np.finfo(np.float64).eps, assume_centered = False)` | medium | 28 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, **params` | `None` | `sklearn.covariance._graph_lasso.GraphicalLassoCV.fit(self, X, y = None, **params)` | complex | 185 | 有逻辑 |
| 3 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.covariance._graph_lasso.GraphicalLassoCV.get_metadata_routing(self)` | medium | 19 | - |

---

## 🔹 `MinCovDet`

**完全限定名**: `sklearn.covariance._robust_covariance.MinCovDet`

**文件路径**: `sklearn/covariance/_robust_covariance.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, store_precision = True, assume_centered =...` | `None` | `sklearn.covariance._robust_covariance.MinCovDet.__init__(self, store_precision = True, assume_centered = False, support_fraction = None, random_state = None)` | medium | 12 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._robust_covariance.MinCovDet.fit(self, X, y = None)` | complex | 52 | 有逻辑 |
| 3 | `correct_covariance` | instance | `self, data` | `None` | `sklearn.covariance._robust_covariance.MinCovDet.correct_covariance(self, data)` | complex | 38 | 抛异常, 有逻辑 |
| 4 | `reweight_covariance` | instance | `self, data` | `None` | `sklearn.covariance._robust_covariance.MinCovDet.reweight_covariance(self, data)` | complex | 63 | 有逻辑 |

---

## 🔹 `LedoitWolf`

**完全限定名**: `sklearn.covariance._shrunk_covariance.LedoitWolf`

**文件路径**: `sklearn/covariance/_shrunk_covariance.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, store_precision = True, assume_centered =...` | `None` | `sklearn.covariance._shrunk_covariance.LedoitWolf.__init__(self, store_precision = True, assume_centered = False, block_size = 1000)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._shrunk_covariance.LedoitWolf.fit(self, X, y = None)` | medium | 30 | 有逻辑 |

---

## 🔹 `OAS`

**完全限定名**: `sklearn.covariance._shrunk_covariance.OAS`

**文件路径**: `sklearn/covariance/_shrunk_covariance.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._shrunk_covariance.OAS.fit(self, X, y = None)` | medium | 29 | 有逻辑 |

---

## 🔹 `ShrunkCovariance`

**完全限定名**: `sklearn.covariance._shrunk_covariance.ShrunkCovariance`

**文件路径**: `sklearn/covariance/_shrunk_covariance.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, store_precision = True, assume_centered =...` | `None` | `sklearn.covariance._shrunk_covariance.ShrunkCovariance.__init__(self, store_precision = True, assume_centered = False, shrinkage = 0.1)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.covariance._shrunk_covariance.ShrunkCovariance.fit(self, X, y = None)` | medium | 29 | 有逻辑 |

---

## 🔹 `CCA`

**完全限定名**: `sklearn.cross_decomposition._pls.CCA`

**文件路径**: `sklearn/cross_decomposition/_pls.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, scale = True, max_iter ...` | `None` | `sklearn.cross_decomposition._pls.CCA.__init__(self, n_components = 2, scale = True, max_iter = 500, tol = 1e-06, copy = True)` | medium | 13 | 魔术方法 |

---

## 🔹 `PLSCanonical`

**完全限定名**: `sklearn.cross_decomposition._pls.PLSCanonical`

**文件路径**: `sklearn/cross_decomposition/_pls.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, scale = True, algorithm...` | `None` | `sklearn.cross_decomposition._pls.PLSCanonical.__init__(self, n_components = 2, scale = True, algorithm = 'nipals', max_iter = 500, tol = 1e-06, copy = True)` | medium | 20 | 魔术方法 |

---

## 🔹 `PLSRegression`

**完全限定名**: `sklearn.cross_decomposition._pls.PLSRegression`

**文件路径**: `sklearn/cross_decomposition/_pls.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, scale = True, max_iter ...` | `None` | `sklearn.cross_decomposition._pls.PLSRegression.__init__(self, n_components = 2, scale = True, max_iter = 500, tol = 1e-06, copy = True)` | medium | 13 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.cross_decomposition._pls.PLSRegression.fit(self, X, y)` | medium | 23 | - |

---

## 🔹 `PLSSVD`

**完全限定名**: `sklearn.cross_decomposition._pls.PLSSVD`

**文件路径**: `sklearn/cross_decomposition/_pls.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, scale = True, copy = True` | `None` | `sklearn.cross_decomposition._pls.PLSSVD.__init__(self, n_components = 2, scale = True, copy = True)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.cross_decomposition._pls.PLSSVD.fit(self, X, y)` | complex | 63 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X, y = None` | `None` | `sklearn.cross_decomposition._pls.PLSSVD.transform(self, X, y = None)` | medium | 31 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.cross_decomposition._pls.PLSSVD.fit_transform(self, X, y = None)` | medium | 19 | 有逻辑 |

---

## 🔹 `DictionaryLearning`

**完全限定名**: `sklearn.decomposition._dict_learning.DictionaryLearning`

**文件路径**: `sklearn/decomposition/_dict_learning.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, alpha = 1, max_iter ...` | `None` | `sklearn.decomposition._dict_learning.DictionaryLearning.__init__(self, n_components = None, alpha = 1, max_iter = 1000, tol = 1e-08, fit_algorithm = 'lars', transform_algorithm = 'omp', transform_n_nonzero_coefs = None, transform_alpha = None, n_jobs = None, code_init = None, dict_init = None, callback = None, verbose = False, split_sign = False, random_state = None, positive_code = False, positive_dict = False, transform_max_iter = 1000)` | complex | 42 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._dict_learning.DictionaryLearning.fit(self, X, y = None)` | medium | 19 | 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._dict_learning.DictionaryLearning.fit_transform(self, X, y = None)` | complex | 51 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._dict_learning.DictionaryLearning.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `MiniBatchDictionaryLearning`

**完全限定名**: `sklearn.decomposition._dict_learning.MiniBatchDictionaryLearning`

**文件路径**: `sklearn/decomposition/_dict_learning.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, alpha = 1, max_iter ...` | `None` | `sklearn.decomposition._dict_learning.MiniBatchDictionaryLearning.__init__(self, n_components = None, alpha = 1, max_iter = 1000, fit_algorithm = 'lars', n_jobs = None, batch_size = 256, shuffle = True, dict_init = None, transform_algorithm = 'omp', transform_n_nonzero_coefs = None, transform_alpha = None, verbose = False, split_sign = False, random_state = None, positive_code = False, positive_dict = False, transform_max_iter = 1000, callback = None, tol = 0.001, max_no_improvement = 10)` | complex | 47 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._dict_learning.MiniBatchDictionaryLearning.fit(self, X, y = None)` | complex | 80 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._dict_learning.MiniBatchDictionaryLearning.partial_fit(self, X, y = None)` | complex | 43 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._dict_learning.MiniBatchDictionaryLearning.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SparseCoder`

**完全限定名**: `sklearn.decomposition._dict_learning.SparseCoder`

**文件路径**: `sklearn/decomposition/_dict_learning.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, dictionary, transform_algorithm = 'omp', ...` | `None` | `sklearn.decomposition._dict_learning.SparseCoder.__init__(self, dictionary, transform_algorithm = 'omp', transform_n_nonzero_coefs = None, transform_alpha = None, split_sign = False, n_jobs = None, positive_code = False, transform_max_iter = 1000)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._dict_learning.SparseCoder.fit(self, X, y = None)` | medium | 27 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._dict_learning.SparseCoder.transform(self, X, y = None)` | medium | 21 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.decomposition._dict_learning.SparseCoder.inverse_transform(self, X)` | medium | 15 | - |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._dict_learning.SparseCoder.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `FactorAnalysis`

**完全限定名**: `sklearn.decomposition._factor_analysis.FactorAnalysis`

**文件路径**: `sklearn/decomposition/_factor_analysis.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, tol = 0.01, copy = T...` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.__init__(self, n_components = None, tol = 0.01, copy = True, max_iter = 1000, noise_variance_init = None, svd_method = 'randomized', iterated_power = 3, rotation = None, random_state = 0)` | medium | 23 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.fit(self, X, y = None)` | complex | 107 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.transform(self, X)` | medium | 29 | - |
| 4 | `get_covariance` | instance | `self` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.get_covariance(self)` | medium | 15 | - |
| 5 | `get_precision` | instance | `self` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.get_precision(self)` | medium | 27 | 有逻辑 |
| 6 | `score_samples` | instance | `self, X` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.score_samples(self, X)` | medium | 21 | - |
| 7 | `score` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._factor_analysis.FactorAnalysis.score(self, X, y = None)` | medium | 17 | - |

---

## 🔹 `FastICA`

**完全限定名**: `sklearn.decomposition._fastica.FastICA`

**文件路径**: `sklearn/decomposition/_fastica.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, algorithm = 'paralle...` | `None` | `sklearn.decomposition._fastica.FastICA.__init__(self, n_components = None, algorithm = 'parallel', whiten = 'unit-variance', fun = 'logcosh', fun_args = None, max_iter = 200, tol = 0.0001, w_init = None, whiten_solver = 'svd', random_state = None)` | medium | 25 | 魔术方法 |
| 2 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._fastica.FastICA.fit_transform(self, X, y = None)` | medium | 19 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._fastica.FastICA.fit(self, X, y = None)` | medium | 19 | 有逻辑 |
| 4 | `transform` | instance | `self, X, copy = True` | `None` | `sklearn.decomposition._fastica.FastICA.transform(self, X, copy = True)` | medium | 31 | 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X, copy = True` | `None` | `sklearn.decomposition._fastica.FastICA.inverse_transform(self, X, copy = True)` | medium | 24 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._fastica.FastICA.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `IncrementalPCA`

**完全限定名**: `sklearn.decomposition._incremental_pca.IncrementalPCA`

**文件路径**: `sklearn/decomposition/_incremental_pca.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, whiten = False, copy...` | `None` | `sklearn.decomposition._incremental_pca.IncrementalPCA.__init__(self, n_components = None, whiten = False, copy = True, batch_size = None)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._incremental_pca.IncrementalPCA.fit(self, X, y = None)` | complex | 50 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y = None, check_input = True` | `None` | `sklearn.decomposition._incremental_pca.IncrementalPCA.partial_fit(self, X, y = None, check_input = True)` | complex | 123 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.decomposition._incremental_pca.IncrementalPCA.transform(self, X)` | complex | 40 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._incremental_pca.IncrementalPCA.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `KernelPCA`

**完全限定名**: `sklearn.decomposition._kernel_pca.KernelPCA`

**文件路径**: `sklearn/decomposition/_kernel_pca.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, kernel = 'linear', g...` | `None` | `sklearn.decomposition._kernel_pca.KernelPCA.__init__(self, n_components = None, kernel = 'linear', gamma = None, degree = 3, coef0 = 1, kernel_params = None, alpha = 1.0, fit_inverse_transform = False, eigen_solver = 'auto', tol = 0, max_iter = None, iterated_power = 'auto', remove_zero_eig = False, random_state = None, copy_X = True, n_jobs = None)` | complex | 36 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._kernel_pca.KernelPCA.fit(self, X, y = None)` | medium | 35 | 抛异常, 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None, **params` | `None` | `sklearn.decomposition._kernel_pca.KernelPCA.fit_transform(self, X, y = None, **params)` | medium | 30 | 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.decomposition._kernel_pca.KernelPCA.transform(self, X)` | medium | 30 | 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.decomposition._kernel_pca.KernelPCA.inverse_transform(self, X)` | complex | 51 | 抛异常, 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._kernel_pca.KernelPCA.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `LatentDirichletAllocation`

**完全限定名**: `sklearn.decomposition._lda.LatentDirichletAllocation`

**文件路径**: `sklearn/decomposition/_lda.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 10, doc_topic_prior = None...` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.__init__(self, n_components = 10, doc_topic_prior = None, topic_word_prior = None, learning_method = 'batch', learning_decay = 0.7, learning_offset = 10.0, max_iter = 10, batch_size = 128, evaluate_every = -1, total_samples = 1000000.0, perp_tol = 0.1, mean_change_tol = 0.001, max_doc_update_iter = 100, n_jobs = None, verbose = 0, random_state = None)` | complex | 36 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 3 | `partial_fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.partial_fit(self, X, y = None)` | complex | 46 | 抛异常, 有逻辑 |
| 4 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.fit(self, X, y = None)` | complex | 81 | 有逻辑 |
| 5 | `transform` | instance | `self, X, normalize = True` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.transform(self, X, normalize = True)` | medium | 27 | 有逻辑 |
| 6 | `fit_transform` | instance | `self, X, y = None, normalize = True` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.fit_transform(self, X, y = None, normalize = True)` | medium | 24 | 有逻辑 |
| 7 | `score` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.score(self, X, y = None)` | medium | 24 | 有逻辑 |
| 8 | `perplexity` | instance | `self, X, sub_sampling = False` | `None` | `sklearn.decomposition._lda.LatentDirichletAllocation.perplexity(self, X, sub_sampling = False)` | medium | 27 | 有逻辑 |

---

## 🔹 `MiniBatchNMF`

**完全限定名**: `sklearn.decomposition._nmf.MiniBatchNMF`

**文件路径**: `sklearn/decomposition/_nmf.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 'auto', init = None, batch...` | `None` | `sklearn.decomposition._nmf.MiniBatchNMF.__init__(self, n_components = 'auto', init = None, batch_size = 1024, beta_loss = 'frobenius', tol = 0.0001, max_no_improvement = 10, max_iter = 200, alpha_W = 0.0, alpha_H = 'same', l1_ratio = 0.0, forget_factor = 0.7, fresh_restarts = False, fresh_restarts_max_iter = 30, transform_max_iter = None, random_state = None, verbose = 0)` | complex | 39 | 魔术方法 |
| 2 | `fit_transform` | instance | `self, X, y = None, W = None, H = None` | `None` | `sklearn.decomposition._nmf.MiniBatchNMF.fit_transform(self, X, y = None, W = None, H = None)` | complex | 43 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.decomposition._nmf.MiniBatchNMF.transform(self, X)` | medium | 25 | - |
| 4 | `partial_fit` | instance | `self, X, y = None, W = None, H = None` | `None` | `sklearn.decomposition._nmf.MiniBatchNMF.partial_fit(self, X, y = None, W = None, H = None)` | complex | 59 | 有逻辑 |

---

## 🔹 `NMF`

**完全限定名**: `sklearn.decomposition._nmf.NMF`

**文件路径**: `sklearn/decomposition/_nmf.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 'auto', init = None, solve...` | `None` | `sklearn.decomposition._nmf.NMF.__init__(self, n_components = 'auto', init = None, solver = 'cd', beta_loss = 'frobenius', tol = 0.0001, max_iter = 200, random_state = None, alpha_W = 0.0, alpha_H = 'same', l1_ratio = 0.0, verbose = 0, shuffle = False)` | medium | 31 | 魔术方法 |
| 2 | `fit_transform` | instance | `self, X, y = None, W = None, H = None` | `None` | `sklearn.decomposition._nmf.NMF.fit_transform(self, X, y = None, W = None, H = None)` | complex | 43 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.decomposition._nmf.NMF.transform(self, X)` | medium | 28 | - |

---

## 🔹 `PCA`

**完全限定名**: `sklearn.decomposition._pca.PCA`

**文件路径**: `sklearn/decomposition/_pca.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, copy = True, whiten ...` | `None` | `sklearn.decomposition._pca.PCA.__init__(self, n_components = None, copy = True, whiten = False, svd_solver = 'auto', tol = 0.0, iterated_power = 'auto', n_oversamples = 10, power_iteration_normalizer = 'auto', random_state = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._pca.PCA.fit(self, X, y = None)` | medium | 19 | - |
| 3 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._pca.PCA.fit_transform(self, X, y = None)` | medium | 36 | 有逻辑 |
| 4 | `score_samples` | instance | `self, X` | `None` | `sklearn.decomposition._pca.PCA.score_samples(self, X)` | medium | 26 | - |
| 5 | `score` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._pca.PCA.score(self, X, y = None)` | medium | 22 | - |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._pca.PCA.__sklearn_tags__(self)` | medium | 13 | 魔术方法 |

---

## 🔹 `MiniBatchSparsePCA`

**完全限定名**: `sklearn.decomposition._sparse_pca.MiniBatchSparsePCA`

**文件路径**: `sklearn/decomposition/_sparse_pca.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, alpha = 1, ridge_alp...` | `None` | `sklearn.decomposition._sparse_pca.MiniBatchSparsePCA.__init__(self, n_components = None, alpha = 1, ridge_alpha = 0.01, max_iter = 1000, callback = None, batch_size = 3, verbose = False, shuffle = True, n_jobs = None, method = 'lars', random_state = None, tol = 0.001, max_no_improvement = 10)` | complex | 32 | 魔术方法 |

---

## 🔹 `SparsePCA`

**完全限定名**: `sklearn.decomposition._sparse_pca.SparsePCA`

**文件路径**: `sklearn/decomposition/_sparse_pca.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, alpha = 1, ridge_alp...` | `None` | `sklearn.decomposition._sparse_pca.SparsePCA.__init__(self, n_components = None, alpha = 1, ridge_alpha = 0.01, max_iter = 1000, tol = 1e-08, method = 'lars', n_jobs = None, U_init = None, V_init = None, verbose = False, random_state = None)` | medium | 28 | 魔术方法 |

---

## 🔹 `TruncatedSVD`

**完全限定名**: `sklearn.decomposition._truncated_svd.TruncatedSVD`

**文件路径**: `sklearn/decomposition/_truncated_svd.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, algorithm = 'randomized...` | `None` | `sklearn.decomposition._truncated_svd.TruncatedSVD.__init__(self, n_components = 2, algorithm = 'randomized', n_iter = 5, n_oversamples = 10, power_iteration_normalizer = 'auto', random_state = None, tol = 0.0)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._truncated_svd.TruncatedSVD.fit(self, X, y = None)` | medium | 18 | 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.decomposition._truncated_svd.TruncatedSVD.fit_transform(self, X, y = None)` | complex | 67 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.decomposition._truncated_svd.TruncatedSVD.transform(self, X)` | medium | 16 | - |
| 5 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.decomposition._truncated_svd.TruncatedSVD.inverse_transform(self, X)` | medium | 17 | - |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.decomposition._truncated_svd.TruncatedSVD.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `DiscriminantAnalysisPredictionMixin`

**完全限定名**: `sklearn.discriminant_analysis.DiscriminantAnalysisPredictionMixin`

**文件路径**: `sklearn/discriminant_analysis.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `decision_function` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.DiscriminantAnalysisPredictionMixin.decision_function(self, X)` | medium | 19 | 有逻辑 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.DiscriminantAnalysisPredictionMixin.predict(self, X)` | medium | 18 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.DiscriminantAnalysisPredictionMixin.predict_proba(self, X)` | medium | 15 | 有逻辑 |
| 4 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.DiscriminantAnalysisPredictionMixin.predict_log_proba(self, X)` | medium | 18 | - |

---

## 🔹 `LinearDiscriminantAnalysis`

**完全限定名**: `sklearn.discriminant_analysis.LinearDiscriminantAnalysis`

**文件路径**: `sklearn/discriminant_analysis.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, solver = 'svd', shrinkage = None, priors ...` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.__init__(self, solver = 'svd', shrinkage = None, priors = None, n_components = None, store_covariance = False, tol = 0.0001, covariance_estimator = None)` | medium | 17 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.fit(self, X, y)` | complex | 92 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.transform(self, X)` | medium | 28 | 抛异常, 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.predict_proba(self, X)` | medium | 21 | 有逻辑 |
| 5 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.predict_log_proba(self, X)` | medium | 19 | - |
| 6 | `decision_function` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.decision_function(self, X)` | medium | 22 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `QuadraticDiscriminantAnalysis`

**完全限定名**: `sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis`

**文件路径**: `sklearn/discriminant_analysis.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, solver = 'svd', shrinkage = None, priors ...` | `None` | `sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.__init__(self, solver = 'svd', shrinkage = None, priors = None, reg_param = 0.0, store_covariance = False, tol = 0.0001, covariance_estimator = None)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.fit(self, X, y)` | complex | 101 | 抛异常, 有逻辑 |
| 3 | `decision_function` | instance | `self, X` | `None` | `sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.decision_function(self, X)` | medium | 22 | 有逻辑 |

---

## 🔹 `DummyClassifier`

**完全限定名**: `sklearn.dummy.DummyClassifier`

**文件路径**: `sklearn/dummy.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, strategy = 'prior', random_state = None, ...` | `None` | `sklearn.dummy.DummyClassifier.__init__(self, strategy = 'prior', random_state = None, constant = None)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.dummy.DummyClassifier.fit(self, X, y, sample_weight = None)` | complex | 89 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.dummy.DummyClassifier.predict(self, X)` | complex | 86 | 抛异常, 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.dummy.DummyClassifier.predict_proba(self, X)` | complex | 62 | 有逻辑 |
| 5 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.dummy.DummyClassifier.predict_log_proba(self, X)` | medium | 21 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.dummy.DummyClassifier.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 7 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.dummy.DummyClassifier.score(self, X, y, sample_weight = None)` | medium | 28 | 有逻辑 |

---

## 🔹 `DummyRegressor`

**完全限定名**: `sklearn.dummy.DummyRegressor`

**文件路径**: `sklearn/dummy.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, strategy = 'mean', constant = None, quant...` | `None` | `sklearn.dummy.DummyRegressor.__init__(self, strategy = 'mean', constant = None, quantile = None)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.dummy.DummyRegressor.fit(self, X, y, sample_weight = None)` | complex | 80 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X, return_std = False` | `None` | `sklearn.dummy.DummyRegressor.predict(self, X, return_std = False)` | medium | 37 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.dummy.DummyRegressor.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 5 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.dummy.DummyRegressor.score(self, X, y, sample_weight = None)` | medium | 32 | 有逻辑 |

---

## 🔹 `BaggingClassifier`

**完全限定名**: `sklearn.ensemble._bagging.BaggingClassifier`

**文件路径**: `sklearn/ensemble/_bagging.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 10, max_...` | `None` | `sklearn.ensemble._bagging.BaggingClassifier.__init__(self, estimator = None, n_estimators = 10, max_samples = None, max_features = 1.0, bootstrap = True, bootstrap_features = False, oob_score = False, warm_start = False, n_jobs = None, random_state = None, verbose = 0)` | medium | 28 | 魔术方法 |
| 2 | `predict` | instance | `self, X, **params` | `None` | `sklearn.ensemble._bagging.BaggingClassifier.predict(self, X, **params)` | medium | 33 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X, **params` | `None` | `sklearn.ensemble._bagging.BaggingClassifier.predict_proba(self, X, **params)` | complex | 73 | 有逻辑 |
| 4 | `predict_log_proba` | instance | `self, X, **params` | `None` | `sklearn.ensemble._bagging.BaggingClassifier.predict_log_proba(self, X, **params)` | complex | 79 | 有逻辑 |
| 5 | `decision_function` | instance | `self, X, **params` | `None` | `sklearn.ensemble._bagging.BaggingClassifier.decision_function(self, X, **params)` | complex | 65 | 有逻辑 |

---

## 🔹 `BaggingRegressor`

**完全限定名**: `sklearn.ensemble._bagging.BaggingRegressor`

**文件路径**: `sklearn/ensemble/_bagging.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 10, max_...` | `None` | `sklearn.ensemble._bagging.BaggingRegressor.__init__(self, estimator = None, n_estimators = 10, max_samples = None, max_features = 1.0, bootstrap = True, bootstrap_features = False, oob_score = False, warm_start = False, n_jobs = None, random_state = None, verbose = 0)` | medium | 28 | 魔术方法 |
| 2 | `predict` | instance | `self, X, **params` | `None` | `sklearn.ensemble._bagging.BaggingRegressor.predict(self, X, **params)` | complex | 64 | 有逻辑 |

---

## 🔹 `BaseBagging`

**完全限定名**: `sklearn.ensemble._bagging.BaseBagging`

**文件路径**: `sklearn/ensemble/_bagging.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 10, max_...` | `None` | `sklearn.ensemble._bagging.BaseBagging.__init__(self, estimator = None, n_estimators = 10, max_samples = None, max_features = 1.0, bootstrap = True, bootstrap_features = False, oob_score = False, warm_start = False, n_jobs = None, random_state = None, verbose = 0)` | medium | 28 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **fit_params` | `None` | `sklearn.ensemble._bagging.BaseBagging.fit(self, X, y, sample_weight = None, **fit_params)` | complex | 66 | 有逻辑 |
| 3 | `estimators_samples_` | property | `self` | `None` | `sklearn.ensemble._bagging.BaseBagging.estimators_samples_(self)` | medium | 13 | 有逻辑 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.ensemble._bagging.BaseBagging.get_metadata_routing(self)` | complex | 57 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._bagging.BaseBagging.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `BaseEnsemble`

**完全限定名**: `sklearn.ensemble._base.BaseEnsemble`

**文件路径**: `sklearn/ensemble/_base.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 10, esti...` | `None` | `sklearn.ensemble._base.BaseEnsemble.__init__(self, estimator = None, n_estimators = 10, estimator_params = tuple())` | simple | 11 | 魔术方法, 抽象方法 |
| 2 | `__len__` | instance | `self` | `None` | `sklearn.ensemble._base.BaseEnsemble.__len__(self)` | simple | 3 | 魔术方法 |
| 3 | `__getitem__` | instance | `self, index` | `None` | `sklearn.ensemble._base.BaseEnsemble.__getitem__(self, index)` | simple | 3 | 魔术方法 |
| 4 | `__iter__` | instance | `self` | `None` | `sklearn.ensemble._base.BaseEnsemble.__iter__(self)` | simple | 3 | 魔术方法 |

---

## 🔹 `BaseForest`

**完全限定名**: `sklearn.ensemble._forest.BaseForest`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_estimators = 100, estimator_...` | `None` | `sklearn.ensemble._forest.BaseForest.__init__(self, estimator, n_estimators = 100, estimator_params = tuple(), bootstrap = False, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, class_weight = None, max_samples = None)` | medium | 29 | 魔术方法, 抽象方法 |
| 2 | `apply` | instance | `self, X` | `None` | `sklearn.ensemble._forest.BaseForest.apply(self, X)` | medium | 25 | 有逻辑 |
| 3 | `decision_path` | instance | `self, X` | `None` | `sklearn.ensemble._forest.BaseForest.decision_path(self, X)` | complex | 39 | 有逻辑 |
| 4 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.ensemble._forest.BaseForest.fit(self, X, y, sample_weight = None)` | complex | 213 | 抛异常, 有逻辑 |
| 5 | `feature_importances_` | property | `self` | `None` | `sklearn.ensemble._forest.BaseForest.feature_importances_(self)` | medium | 33 | 有逻辑 |
| 6 | `estimators_samples_` | property | `self` | `None` | `sklearn.ensemble._forest.BaseForest.estimators_samples_(self)` | simple | 12 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._forest.BaseForest.__sklearn_tags__(self)` | simple | 7 | 魔术方法, 有逻辑 |

---

## 🔹 `ExtraTreesClassifier`

**完全限定名**: `sklearn.ensemble._forest.ExtraTreesClassifier`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_estimators = 100, criterion = 'gini', m...` | `None` | `sklearn.ensemble._forest.ExtraTreesClassifier.__init__(self, n_estimators = 100, criterion = 'gini', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = 'sqrt', max_leaf_nodes = None, min_impurity_decrease = 0.0, bootstrap = False, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, class_weight = None, ccp_alpha = 0.0, max_samples = None, monotonic_cst = None)` | complex | 59 | 魔术方法 |

---

## 🔹 `ExtraTreesRegressor`

**完全限定名**: `sklearn.ensemble._forest.ExtraTreesRegressor`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_estimators = 100, criterion = 'squared_...` | `None` | `sklearn.ensemble._forest.ExtraTreesRegressor.__init__(self, n_estimators = 100, criterion = 'squared_error', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = 1.0, max_leaf_nodes = None, min_impurity_decrease = 0.0, bootstrap = False, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, ccp_alpha = 0.0, max_samples = None, monotonic_cst = None)` | complex | 57 | 魔术方法 |

---

## 🔹 `ForestClassifier`

**完全限定名**: `sklearn.ensemble._forest.ForestClassifier`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_estimators = 100, estimator_...` | `None` | `sklearn.ensemble._forest.ForestClassifier.__init__(self, estimator, n_estimators = 100, estimator_params = tuple(), bootstrap = False, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, class_weight = None, max_samples = None)` | medium | 28 | 魔术方法, 抽象方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._forest.ForestClassifier.predict(self, X)` | medium | 38 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._forest.ForestClassifier.predict_proba(self, X)` | complex | 47 | 有逻辑 |
| 4 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.ensemble._forest.ForestClassifier.predict_log_proba(self, X)` | medium | 31 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._forest.ForestClassifier.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `ForestRegressor`

**完全限定名**: `sklearn.ensemble._forest.ForestRegressor`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_estimators = 100, estimator_...` | `None` | `sklearn.ensemble._forest.ForestRegressor.__init__(self, estimator, n_estimators = 100, estimator_params = tuple(), bootstrap = False, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, max_samples = None)` | medium | 26 | 魔术方法, 抽象方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._forest.ForestRegressor.predict(self, X)` | medium | 42 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._forest.ForestRegressor.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `RandomForestClassifier`

**完全限定名**: `sklearn.ensemble._forest.RandomForestClassifier`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_estimators = 100, criterion = 'gini', m...` | `None` | `sklearn.ensemble._forest.RandomForestClassifier.__init__(self, n_estimators = 100, criterion = 'gini', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = 'sqrt', max_leaf_nodes = None, min_impurity_decrease = 0.0, bootstrap = True, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, class_weight = None, ccp_alpha = 0.0, max_samples = None, monotonic_cst = None)` | complex | 59 | 魔术方法 |

---

## 🔹 `RandomForestRegressor`

**完全限定名**: `sklearn.ensemble._forest.RandomForestRegressor`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_estimators = 100, criterion = 'squared_...` | `None` | `sklearn.ensemble._forest.RandomForestRegressor.__init__(self, n_estimators = 100, criterion = 'squared_error', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = 1.0, max_leaf_nodes = None, min_impurity_decrease = 0.0, bootstrap = True, oob_score = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False, ccp_alpha = 0.0, max_samples = None, monotonic_cst = None)` | complex | 57 | 魔术方法 |

---

## 🔹 `RandomTreesEmbedding`

**完全限定名**: `sklearn.ensemble._forest.RandomTreesEmbedding`

**文件路径**: `sklearn/ensemble/_forest.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_estimators = 100, max_depth = 5, min_sa...` | `None` | `sklearn.ensemble._forest.RandomTreesEmbedding.__init__(self, n_estimators = 100, max_depth = 5, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_leaf_nodes = None, min_impurity_decrease = 0.0, sparse_output = True, n_jobs = None, random_state = None, verbose = 0, warm_start = False)` | complex | 46 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.ensemble._forest.RandomTreesEmbedding.fit(self, X, y = None, sample_weight = None)` | medium | 29 | 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.ensemble._forest.RandomTreesEmbedding.fit_transform(self, X, y = None, sample_weight = None)` | medium | 33 | 有逻辑 |
| 4 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.ensemble._forest.RandomTreesEmbedding.get_feature_names_out(self, input_features = None)` | medium | 31 | 有逻辑 |
| 5 | `transform` | instance | `self, X` | `None` | `sklearn.ensemble._forest.RandomTreesEmbedding.transform(self, X)` | medium | 18 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._forest.RandomTreesEmbedding.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `BaseGradientBoosting`

**完全限定名**: `sklearn.ensemble._gb.BaseGradientBoosting`

**文件路径**: `sklearn/ensemble/_gb.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss, learning_rate, n_estimators, criter...` | `None` | `sklearn.ensemble._gb.BaseGradientBoosting.__init__(self, loss, learning_rate, n_estimators, criterion, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_depth, min_impurity_decrease, init, subsample, max_features, ccp_alpha, random_state, alpha = 0.9, verbose = 0, max_leaf_nodes = None, warm_start = False, validation_fraction = 0.1, n_iter_no_change = None, tol = 0.0001)` | complex | 46 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, monitor = None` | `None` | `sklearn.ensemble._gb.BaseGradientBoosting.fit(self, X, y, sample_weight = None, monitor = None)` | complex | 196 | 抛异常, 有逻辑 |
| 3 | `feature_importances_` | property | `self` | `None` | `sklearn.ensemble._gb.BaseGradientBoosting.feature_importances_(self)` | complex | 39 | 有逻辑 |
| 4 | `apply` | instance | `self, X` | `None` | `sklearn.ensemble._gb.BaseGradientBoosting.apply(self, X)` | medium | 34 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._gb.BaseGradientBoosting.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `GradientBoostingClassifier`

**完全限定名**: `sklearn.ensemble._gb.GradientBoostingClassifier`

**文件路径**: `sklearn/ensemble/_gb.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'log_loss', learning_rate = 0.1, n...` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.__init__(self, loss = 'log_loss', learning_rate = 0.1, n_estimators = 100, subsample = 1.0, criterion = 'friedman_mse', min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_depth = 3, min_impurity_decrease = 0.0, init = None, random_state = None, max_features = None, verbose = 0, max_leaf_nodes = None, warm_start = False, validation_fraction = 0.1, n_iter_no_change = None, tol = 0.0001, ccp_alpha = 0.0)` | complex | 46 | 魔术方法 |
| 2 | `decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.decision_function(self, X)` | medium | 26 | 有逻辑 |
| 3 | `staged_decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.staged_decision_function(self, X)` | medium | 23 | 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.predict(self, X)` | medium | 21 | 有逻辑 |
| 5 | `staged_predict` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.staged_predict(self, X)` | medium | 26 | 有逻辑 |
| 6 | `predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.predict_proba(self, X)` | medium | 23 | 有逻辑 |
| 7 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.predict_log_proba(self, X)` | medium | 23 | 有逻辑 |
| 8 | `staged_predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingClassifier.staged_predict_proba(self, X)` | medium | 27 | 抛异常, 有逻辑 |

---

## 🔹 `GradientBoostingRegressor`

**完全限定名**: `sklearn.ensemble._gb.GradientBoostingRegressor`

**文件路径**: `sklearn/ensemble/_gb.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'squared_error', learning_rate = 0...` | `None` | `sklearn.ensemble._gb.GradientBoostingRegressor.__init__(self, loss = 'squared_error', learning_rate = 0.1, n_estimators = 100, subsample = 1.0, criterion = 'friedman_mse', min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_depth = 3, min_impurity_decrease = 0.0, init = None, random_state = None, max_features = None, alpha = 0.9, verbose = 0, max_leaf_nodes = None, warm_start = False, validation_fraction = 0.1, n_iter_no_change = None, tol = 0.0001, ccp_alpha = 0.0)` | complex | 48 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingRegressor.predict(self, X)` | medium | 20 | 有逻辑 |
| 3 | `staged_predict` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingRegressor.staged_predict(self, X)` | medium | 20 | 有逻辑 |
| 4 | `apply` | instance | `self, X` | `None` | `sklearn.ensemble._gb.GradientBoostingRegressor.apply(self, X)` | medium | 22 | 有逻辑 |

---

## 🔹 `VerboseReporter`

**完全限定名**: `sklearn.ensemble._gb.VerboseReporter`

**文件路径**: `sklearn/ensemble/_gb.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, verbose` | `None` | `sklearn.ensemble._gb.VerboseReporter.__init__(self, verbose)` | simple | 2 | 魔术方法 |
| 2 | `init` | instance | `self, est, begin_at_stage = 0` | `None` | `sklearn.ensemble._gb.VerboseReporter.init(self, est, begin_at_stage = 0)` | medium | 29 | 有逻辑 |
| 3 | `update` | instance | `self, j, est` | `None` | `sklearn.ensemble._gb.VerboseReporter.update(self, j, est)` | medium | 33 | 有逻辑 |

---

## 🔹 `BaseHistGradientBoosting`

**完全限定名**: `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.BaseHistGradientBoosting`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss, learning_rate, max_iter, max_leaf_n...` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.BaseHistGradientBoosting.__init__(self, loss, learning_rate, max_iter, max_leaf_nodes, max_depth, min_samples_leaf, l2_regularization, max_features, max_bins, categorical_features, monotonic_cst, interaction_cst, warm_start, early_stopping, scoring, validation_fraction, n_iter_no_change, tol, verbose, random_state)` | complex | 44 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, X_val = None,...` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.BaseHistGradientBoosting.fit(self, X, y, sample_weight = None, X_val = None, y_val = None, sample_weight_val = None)` | complex | 559 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.BaseHistGradientBoosting.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 4 | `n_iter_` | property | `self` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.BaseHistGradientBoosting.n_iter_(self)` | simple | 4 | - |

---

## 🔹 `HistGradientBoostingClassifier`

**完全限定名**: `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'log_loss', learning_rate = 0.1, m...` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.__init__(self, loss = 'log_loss', learning_rate = 0.1, max_iter = 100, max_leaf_nodes = 31, max_depth = None, min_samples_leaf = 20, l2_regularization = 0.0, max_features = 1.0, max_bins = 255, categorical_features = 'from_dtype', monotonic_cst = None, interaction_cst = None, warm_start = False, early_stopping = 'auto', scoring = 'loss', validation_fraction = 0.1, n_iter_no_change = 10, tol = 1e-07, verbose = 0, random_state = None, class_weight = None)` | complex | 48 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.predict(self, X)` | medium | 22 | 有逻辑 |
| 3 | `staged_predict` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.staged_predict(self, X)` | medium | 25 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.predict_proba(self, X)` | medium | 15 | 有逻辑 |
| 5 | `staged_predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.staged_predict_proba(self, X)` | medium | 19 | 有逻辑 |
| 6 | `decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.decision_function(self, X)` | medium | 20 | 有逻辑 |
| 7 | `staged_decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier.staged_decision_function(self, X)` | medium | 23 | 有逻辑 |

---

## 🔹 `HistGradientBoostingRegressor`

**完全限定名**: `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingRegressor`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'squared_error', quantile = None, ...` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingRegressor.__init__(self, loss = 'squared_error', quantile = None, learning_rate = 0.1, max_iter = 100, max_leaf_nodes = 31, max_depth = None, min_samples_leaf = 20, l2_regularization = 0.0, max_features = 1.0, max_bins = 255, categorical_features = 'from_dtype', monotonic_cst = None, interaction_cst = None, warm_start = False, early_stopping = 'auto', scoring = 'loss', validation_fraction = 0.1, n_iter_no_change = 10, tol = 1e-07, verbose = 0, random_state = None)` | complex | 48 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingRegressor.predict(self, X)` | medium | 17 | 有逻辑 |
| 3 | `staged_predict` | instance | `self, X` | `None` | `sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingRegressor.staged_predict(self, X)` | medium | 20 | 有逻辑 |

---

## 🔹 `TreeGrower`

**完全限定名**: `sklearn.ensemble._hist_gradient_boosting.grower.TreeGrower`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/grower.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, X_binned, gradients, hessians, max_leaf_n...` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeGrower.__init__(self, X_binned, gradients, hessians, max_leaf_nodes = None, max_depth = None, min_samples_leaf = 20, min_gain_to_split = 0.0, min_hessian_to_split = 0.001, n_bins = 256, n_bins_non_missing = None, has_missing_values = False, is_categorical = None, monotonic_cst = None, interaction_cst = None, l2_regularization = 0.0, feature_fraction_per_split = 1.0, rng = np.random.default_rng(), shrinkage = 1.0, n_threads = None)` | complex | 112 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `grow` | instance | `self` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeGrower.grow(self)` | simple | 6 | 有逻辑 |
| 3 | `split_next` | instance | `self` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeGrower.split_next(self)` | complex | 165 | 有逻辑 |
| 4 | `make_predictor` | instance | `self, binning_thresholds` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeGrower.make_predictor(self, binning_thresholds)` | complex | 34 | 有逻辑 |

---

## 🔹 `TreeNode`

**完全限定名**: `sklearn.ensemble._hist_gradient_boosting.grower.TreeNode`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/grower.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, depth, sample_indices, partition_start, p...` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeNode.__init__(self, depth, sample_indices, partition_start, partition_stop, sum_gradients, sum_hessians, value = None)` | medium | 35 | 魔术方法, 有逻辑 |
| 2 | `set_children_bounds` | instance | `self, lower, upper` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeNode.set_children_bounds(self, lower, upper)` | simple | 8 | 有逻辑 |
| 3 | `__lt__` | instance | `self, other_node` | `None` | `sklearn.ensemble._hist_gradient_boosting.grower.TreeNode.__lt__(self, other_node)` | medium | 15 | 魔术方法, 有逻辑 |

---

## 🔹 `TreePredictor`

**完全限定名**: `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor`

**文件路径**: `sklearn/ensemble/_hist_gradient_boosting/predictor.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, nodes, binned_left_cat_bitsets, raw_left_...` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.__init__(self, nodes, binned_left_cat_bitsets, raw_left_cat_bitsets)` | simple | 4 | 魔术方法 |
| 2 | `get_n_leaf_nodes` | instance | `self` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.get_n_leaf_nodes(self)` | simple | 3 | - |
| 3 | `get_max_depth` | instance | `self` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.get_max_depth(self)` | simple | 3 | - |
| 4 | `predict` | instance | `self, X, known_cat_bitsets, f_idx_map, n_threads` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.predict(self, X, known_cat_bitsets, f_idx_map, n_threads)` | medium | 35 | 有逻辑 |
| 5 | `predict_binned` | instance | `self, X, missing_values_bin_idx, n_threads` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.predict_binned(self, X, missing_values_bin_idx, n_threads)` | medium | 29 | 有逻辑 |
| 6 | `compute_partial_dependence` | instance | `self, grid, target_features, out` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.compute_partial_dependence(self, grid, target_features, out)` | medium | 16 | 有逻辑 |
| 7 | `__setstate__` | instance | `self, state` | `None` | `sklearn.ensemble._hist_gradient_boosting.predictor.TreePredictor.__setstate__(self, state)` | simple | 18 | 魔术方法, 有逻辑 |

---

## 🔹 `IsolationForest`

**完全限定名**: `sklearn.ensemble._iforest.IsolationForest`

**文件路径**: `sklearn/ensemble/_iforest.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_estimators = 100, max_samples = 'auto',...` | `None` | `sklearn.ensemble._iforest.IsolationForest.__init__(self, n_estimators = 100, max_samples = 'auto', contamination = 'auto', max_features = 1.0, bootstrap = False, n_jobs = None, random_state = None, verbose = 0, warm_start = False)` | medium | 28 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.ensemble._iforest.IsolationForest.fit(self, X, y = None, sample_weight = None)` | complex | 93 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._iforest.IsolationForest.predict(self, X)` | complex | 39 | 有逻辑 |
| 4 | `decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._iforest.IsolationForest.decision_function(self, X)` | complex | 50 | 有逻辑 |
| 5 | `score_samples` | instance | `self, X` | `None` | `sklearn.ensemble._iforest.IsolationForest.score_samples(self, X)` | complex | 53 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._iforest.IsolationForest.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `StackingClassifier`

**完全限定名**: `sklearn.ensemble._stacking.StackingClassifier`

**文件路径**: `sklearn/ensemble/_stacking.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimators, final_estimator = None, cv = ...` | `None` | `sklearn.ensemble._stacking.StackingClassifier.__init__(self, estimators, final_estimator = None, cv = None, stack_method = 'auto', n_jobs = None, passthrough = False, verbose = 0)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.ensemble._stacking.StackingClassifier.fit(self, X, y, **fit_params)` | complex | 48 | 有逻辑 |
| 3 | `predict` | instance | `self, X, **predict_params` | `None` | `sklearn.ensemble._stacking.StackingClassifier.predict(self, X, **predict_params)` | complex | 51 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._stacking.StackingClassifier.predict_proba(self, X)` | medium | 22 | 有逻辑 |
| 5 | `decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._stacking.StackingClassifier.decision_function(self, X)` | medium | 17 | 有逻辑 |
| 6 | `transform` | instance | `self, X` | `None` | `sklearn.ensemble._stacking.StackingClassifier.transform(self, X)` | medium | 16 | 有逻辑 |

---

## 🔹 `StackingRegressor`

**完全限定名**: `sklearn.ensemble._stacking.StackingRegressor`

**文件路径**: `sklearn/ensemble/_stacking.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimators, final_estimator = None, cv = ...` | `None` | `sklearn.ensemble._stacking.StackingRegressor.__init__(self, estimators, final_estimator = None, cv = None, n_jobs = None, passthrough = False, verbose = 0)` | medium | 19 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.ensemble._stacking.StackingRegressor.fit(self, X, y, **fit_params)` | medium | 32 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.ensemble._stacking.StackingRegressor.transform(self, X)` | medium | 15 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y, **fit_params` | `None` | `sklearn.ensemble._stacking.StackingRegressor.fit_transform(self, X, y, **fit_params)` | medium | 30 | 有逻辑 |
| 5 | `predict` | instance | `self, X, **predict_params` | `None` | `sklearn.ensemble._stacking.StackingRegressor.predict(self, X, **predict_params)` | complex | 42 | 有逻辑 |

---

## 🔹 `VotingClassifier`

**完全限定名**: `sklearn.ensemble._voting.VotingClassifier`

**文件路径**: `sklearn/ensemble/_voting.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimators, voting = 'hard', weights = No...` | `None` | `sklearn.ensemble._voting.VotingClassifier.__init__(self, estimators, voting = 'hard', weights = None, n_jobs = None, flatten_transform = True, verbose = False)` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.ensemble._voting.VotingClassifier.fit(self, X, y, **fit_params)` | complex | 52 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._voting.VotingClassifier.predict(self, X)` | medium | 28 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._voting.VotingClassifier.predict_proba(self, X)` | medium | 18 | 有逻辑 |
| 5 | `transform` | instance | `self, X` | `None` | `sklearn.ensemble._voting.VotingClassifier.transform(self, X)` | medium | 31 | 有逻辑 |
| 6 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.ensemble._voting.VotingClassifier.get_feature_names_out(self, input_features = None)` | medium | 36 | 抛异常, 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._voting.VotingClassifier.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `VotingRegressor`

**完全限定名**: `sklearn.ensemble._voting.VotingRegressor`

**文件路径**: `sklearn/ensemble/_voting.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimators, weights = None, n_jobs = None...` | `None` | `sklearn.ensemble._voting.VotingRegressor.__init__(self, estimators, weights = None, n_jobs = None, verbose = False)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.ensemble._voting.VotingRegressor.fit(self, X, y, **fit_params)` | medium | 33 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._voting.VotingRegressor.predict(self, X)` | medium | 18 | 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.ensemble._voting.VotingRegressor.transform(self, X)` | medium | 15 | 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.ensemble._voting.VotingRegressor.get_feature_names_out(self, input_features = None)` | medium | 20 | 有逻辑 |

---

## 🔹 `AdaBoostClassifier`

**完全限定名**: `sklearn.ensemble._weight_boosting.AdaBoostClassifier`

**文件路径**: `sklearn/ensemble/_weight_boosting.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 50, lear...` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.__init__(self, estimator = None, n_estimators = 50, learning_rate = 1.0, random_state = None)` | medium | 14 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.predict(self, X)` | medium | 23 | 有逻辑 |
| 3 | `staged_predict` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.staged_predict(self, X)` | medium | 33 | 有逻辑 |
| 4 | `decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.decision_function(self, X)` | complex | 42 | 有逻辑 |
| 5 | `staged_decision_function` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.staged_decision_function(self, X)` | complex | 50 | 有逻辑 |
| 6 | `predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.predict_proba(self, X)` | medium | 27 | 有逻辑 |
| 7 | `staged_predict_proba` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.staged_predict_proba(self, X)` | medium | 29 | 有逻辑 |
| 8 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostClassifier.predict_log_proba(self, X)` | medium | 20 | 有逻辑 |

---

## 🔹 `AdaBoostRegressor`

**完全限定名**: `sklearn.ensemble._weight_boosting.AdaBoostRegressor`

**文件路径**: `sklearn/ensemble/_weight_boosting.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 50, lear...` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostRegressor.__init__(self, estimator = None, n_estimators = 50, learning_rate = 1.0, loss = 'linear', random_state = None)` | medium | 18 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostRegressor.predict(self, X)` | medium | 21 | 有逻辑 |
| 3 | `staged_predict` | instance | `self, X` | `None` | `sklearn.ensemble._weight_boosting.AdaBoostRegressor.staged_predict(self, X)` | medium | 25 | 有逻辑 |

---

## 🔹 `BaseWeightBoosting`

**完全限定名**: `sklearn.ensemble._weight_boosting.BaseWeightBoosting`

**文件路径**: `sklearn/ensemble/_weight_boosting.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, n_estimators = 50, esti...` | `None` | `sklearn.ensemble._weight_boosting.BaseWeightBoosting.__init__(self, estimator = None, n_estimators = 50, estimator_params = tuple(), learning_rate = 1.0, random_state = None)` | medium | 17 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.ensemble._weight_boosting.BaseWeightBoosting.fit(self, X, y, sample_weight = None)` | complex | 95 | 有逻辑 |
| 3 | `staged_score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.ensemble._weight_boosting.BaseWeightBoosting.staged_score(self, X, y, sample_weight = None)` | medium | 30 | 有逻辑 |
| 4 | `feature_importances_` | property | `self` | `None` | `sklearn.ensemble._weight_boosting.BaseWeightBoosting.feature_importances_(self)` | complex | 38 | 抛异常, 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.ensemble._weight_boosting.BaseWeightBoosting.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `EstimatorCheckFailedWarning`

**完全限定名**: `sklearn.exceptions.EstimatorCheckFailedWarning`

**文件路径**: `sklearn/exceptions.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, check_name: str, exception: Ex...` | `None` | `sklearn.exceptions.EstimatorCheckFailedWarning.__init__(self, estimator, check_name: str, exception: Exception, status: str, expected_to_fail: bool, expected_to_fail_reason: str)` | medium | 16 | 魔术方法 |
| 2 | `__repr__` | instance | `self` | `None` | `sklearn.exceptions.EstimatorCheckFailedWarning.__repr__(self)` | medium | 11 | 魔术方法, 有逻辑 |
| 3 | `__str__` | instance | `self` | `None` | `sklearn.exceptions.EstimatorCheckFailedWarning.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `InconsistentVersionWarning`

**完全限定名**: `sklearn.exceptions.InconsistentVersionWarning`

**文件路径**: `sklearn/exceptions.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator_name, current_sklearn_version, ...` | `None` | `sklearn.exceptions.InconsistentVersionWarning.__init__(self, estimator_name, current_sklearn_version, original_sklearn_version)` | simple | 6 | 魔术方法 |
| 2 | `__str__` | instance | `self` | `None` | `sklearn.exceptions.InconsistentVersionWarning.__str__(self)` | medium | 11 | 魔术方法 |

---

## 🔹 `UnsetMetadataPassedError`

**完全限定名**: `sklearn.exceptions.UnsetMetadataPassedError`

**文件路径**: `sklearn/exceptions.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, message, unrequested_params, routed_params` | `None` | `sklearn.exceptions.UnsetMetadataPassedError.__init__(self, message, unrequested_params, routed_params)` | simple | 4 | 魔术方法 |

---

## 🔹 `ArffDecoder`

**完全限定名**: `sklearn.externals._arff.ArffDecoder`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self` | `None` | `sklearn.externals._arff.ArffDecoder.__init__(self)` | simple | 4 | 魔术方法 |
| 2 | `decode` | instance | `self, s, encode_nominal = False, return_type = ...` | `None` | `sklearn.externals._arff.ArffDecoder.decode(self, s, encode_nominal = False, return_type = DENSE)` | medium | 21 | 抛异常, 有逻辑 |

---

## 🔹 `ArffEncoder`

**完全限定名**: `sklearn.externals._arff.ArffEncoder`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `encode` | instance | `self, obj` | `None` | `sklearn.externals._arff.ArffEncoder.encode(self, obj)` | simple | 9 | 有逻辑 |
| 2 | `iter_encode` | instance | `self, obj` | `None` | `sklearn.externals._arff.ArffEncoder.iter_encode(self, obj)` | complex | 60 | 抛异常, 有逻辑 |

---

## 🔹 `ArffException`

**完全限定名**: `sklearn.externals._arff.ArffException`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self` | `None` | `sklearn.externals._arff.ArffException.__init__(self)` | simple | 2 | 魔术方法 |
| 2 | `__str__` | instance | `self` | `None` | `sklearn.externals._arff.ArffException.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `BadAttributeName`

**完全限定名**: `sklearn.externals._arff.BadAttributeName`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, value, value2` | `None` | `sklearn.externals._arff.BadAttributeName.__init__(self, value, value2)` | simple | 7 | 魔术方法 |

---

## 🔹 `BadDataFormat`

**完全限定名**: `sklearn.externals._arff.BadDataFormat`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, value` | `None` | `sklearn.externals._arff.BadDataFormat.__init__(self, value)` | simple | 6 | 魔术方法 |

---

## 🔹 `BadLayout`

**完全限定名**: `sklearn.externals._arff.BadLayout`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, msg = ''` | `None` | `sklearn.externals._arff.BadLayout.__init__(self, msg = '')` | simple | 4 | 魔术方法, 有逻辑 |

---

## 🔹 `BadNominalFormatting`

**完全限定名**: `sklearn.externals._arff.BadNominalFormatting`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, value` | `None` | `sklearn.externals._arff.BadNominalFormatting.__init__(self, value)` | simple | 6 | 魔术方法 |

---

## 🔹 `BadNominalValue`

**完全限定名**: `sklearn.externals._arff.BadNominalValue`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, value` | `None` | `sklearn.externals._arff.BadNominalValue.__init__(self, value)` | simple | 6 | 魔术方法 |

---

## 🔹 `BadObject`

**完全限定名**: `sklearn.externals._arff.BadObject`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, msg = 'Invalid object.'` | `None` | `sklearn.externals._arff.BadObject.__init__(self, msg = 'Invalid object.')` | simple | 2 | 魔术方法 |
| 2 | `__str__` | instance | `self` | `None` | `sklearn.externals._arff.BadObject.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `COOData`

**完全限定名**: `sklearn.externals._arff.COOData`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `decode_rows` | instance | `self, stream, conversors` | `None` | `sklearn.externals._arff.COOData.decode_rows(self, stream, conversors)` | medium | 25 | 抛异常, 有逻辑 |
| 2 | `encode_data` | instance | `self, data, attributes` | `None` | `sklearn.externals._arff.COOData.encode_data(self, data, attributes)` | medium | 35 | 抛异常, 有逻辑 |

---

## 🔹 `DenseGeneratorData`

**完全限定名**: `sklearn.externals._arff.DenseGeneratorData`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `decode_rows` | instance | `self, stream, conversors` | `None` | `sklearn.externals._arff.DenseGeneratorData.decode_rows(self, stream, conversors)` | medium | 15 | 抛异常, 有逻辑 |
| 2 | `encode_data` | instance | `self, data, attributes` | `None` | `sklearn.externals._arff.DenseGeneratorData.encode_data(self, data, attributes)` | medium | 29 | 抛异常, 有逻辑 |

---

## 🔹 `EncodedNominalConversor`

**完全限定名**: `sklearn.externals._arff.EncodedNominalConversor`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, values` | `None` | `sklearn.externals._arff.EncodedNominalConversor.__init__(self, values)` | simple | 3 | 魔术方法, 有逻辑 |
| 2 | `__call__` | instance | `self, value` | `None` | `sklearn.externals._arff.EncodedNominalConversor.__call__(self, value)` | simple | 5 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `LODGeneratorData`

**完全限定名**: `sklearn.externals._arff.LODGeneratorData`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `decode_rows` | instance | `self, stream, conversors` | `None` | `sklearn.externals._arff.LODGeneratorData.decode_rows(self, stream, conversors)` | medium | 16 | 抛异常, 有逻辑 |
| 2 | `encode_data` | instance | `self, data, attributes` | `None` | `sklearn.externals._arff.LODGeneratorData.encode_data(self, data, attributes)` | medium | 23 | 抛异常, 有逻辑 |

---

## 🔹 `NominalConversor`

**完全限定名**: `sklearn.externals._arff.NominalConversor`

**文件路径**: `sklearn/externals/_arff.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, values` | `None` | `sklearn.externals._arff.NominalConversor.__init__(self, values)` | simple | 3 | 魔术方法 |
| 2 | `__call__` | instance | `self, value` | `None` | `sklearn.externals._arff.NominalConversor.__call__(self, value)` | simple | 10 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `ClassDoc`

**完全限定名**: `sklearn.externals._numpydoc.docscrape.ClassDoc`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, cls, doc = None, modulename = '', func_do...` | `None` | `sklearn.externals._numpydoc.docscrape.ClassDoc.__init__(self, cls, doc = None, modulename = '', func_doc = FunctionDoc, config = None)` | complex | 53 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `methods` | property | `self` | `None` | `sklearn.externals._numpydoc.docscrape.ClassDoc.methods(self)` | medium | 12 | 有逻辑 |
| 3 | `properties` | property | `self` | `None` | `sklearn.externals._numpydoc.docscrape.ClassDoc.properties(self)` | medium | 17 | 有逻辑 |

---

## 🔹 `FunctionDoc`

**完全限定名**: `sklearn.externals._numpydoc.docscrape.FunctionDoc`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, func, role = 'func', doc = None, config =...` | `None` | `sklearn.externals._numpydoc.docscrape.FunctionDoc.__init__(self, func, role = 'func', doc = None, config = None)` | simple | 11 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `get_func` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.FunctionDoc.get_func(self)` | simple | 7 | 有逻辑 |
| 3 | `__str__` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.FunctionDoc.__str__(self)` | simple | 14 | 魔术方法, 有逻辑 |

---

## 🔹 `NumpyDocString`

**完全限定名**: `sklearn.externals._numpydoc.docscrape.NumpyDocString`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, docstring, config = None` | `None` | `sklearn.externals._numpydoc.docscrape.NumpyDocString.__init__(self, docstring, config = None)` | simple | 12 | 魔术方法, 有逻辑 |
| 2 | `__getitem__` | instance | `self, key` | `None` | `sklearn.externals._numpydoc.docscrape.NumpyDocString.__getitem__(self, key)` | simple | 2 | 魔术方法 |
| 3 | `__setitem__` | instance | `self, key, val` | `None` | `sklearn.externals._numpydoc.docscrape.NumpyDocString.__setitem__(self, key, val)` | simple | 5 | 魔术方法, 有逻辑 |
| 4 | `__iter__` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.NumpyDocString.__iter__(self)` | simple | 2 | 魔术方法 |
| 5 | `__len__` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.NumpyDocString.__len__(self)` | simple | 2 | 魔术方法 |
| 6 | `__str__` | instance | `self, func_role = ''` | `None` | `sklearn.externals._numpydoc.docscrape.NumpyDocString.__str__(self, func_role = '')` | medium | 23 | 魔术方法, 有逻辑 |

---

## 🔹 `ObjDoc`

**完全限定名**: `sklearn.externals._numpydoc.docscrape.ObjDoc`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, obj, doc = None, config = None` | `None` | `sklearn.externals._numpydoc.docscrape.ObjDoc.__init__(self, obj, doc = None, config = None)` | simple | 5 | 魔术方法, 有逻辑 |

---

## 🔹 `ParseError`

**完全限定名**: `sklearn.externals._numpydoc.docscrape.ParseError`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__str__` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.ParseError.__str__(self)` | simple | 5 | 魔术方法, 有逻辑 |

---

## 🔹 `Reader`

**完全限定名**: `sklearn.externals._numpydoc.docscrape.Reader`

**文件路径**: `sklearn/externals/_numpydoc/docscrape.py`

**公共方法数**: 11

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, data` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.__init__(self, data)` | medium | 14 | 魔术方法, 有逻辑 |
| 2 | `__getitem__` | instance | `self, n` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.__getitem__(self, n)` | simple | 2 | 魔术方法 |
| 3 | `reset` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.reset(self)` | simple | 2 | - |
| 4 | `read` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.read(self)` | simple | 7 | 有逻辑 |
| 5 | `seek_next_non_empty_line` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.seek_next_non_empty_line(self)` | simple | 6 | 有逻辑 |
| 6 | `eof` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.eof(self)` | simple | 2 | - |
| 7 | `read_to_condition` | instance | `self, condition_func` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.read_to_condition(self, condition_func)` | simple | 9 | 有逻辑 |
| 8 | `read_to_next_empty_line` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.read_to_next_empty_line(self)` | simple | 7 | - |
| 9 | `read_to_next_unindented_line` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.read_to_next_unindented_line(self)` | simple | 5 | - |
| 10 | `peek` | instance | `self, n = 0` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.peek(self, n = 0)` | simple | 5 | 有逻辑 |
| 11 | `is_empty` | instance | `self` | `None` | `sklearn.externals._numpydoc.docscrape.Reader.is_empty(self)` | simple | 2 | - |

---

## 🔹 `InfinityType`

**完全限定名**: `sklearn.externals._packaging._structures.InfinityType`

**文件路径**: `sklearn/externals/_packaging/_structures.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__repr__` | instance | `self` | `str` | `sklearn.externals._packaging._structures.InfinityType.__repr__(self)` | simple | 2 | 魔术方法 |
| 2 | `__hash__` | instance | `self` | `int` | `sklearn.externals._packaging._structures.InfinityType.__hash__(self)` | simple | 2 | 魔术方法 |
| 3 | `__lt__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.InfinityType.__lt__(self, other: object)` | simple | 2 | 魔术方法 |
| 4 | `__le__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.InfinityType.__le__(self, other: object)` | simple | 2 | 魔术方法 |
| 5 | `__eq__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.InfinityType.__eq__(self, other: object)` | simple | 2 | 魔术方法 |
| 6 | `__ne__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.InfinityType.__ne__(self, other: object)` | simple | 2 | 魔术方法 |
| 7 | `__gt__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.InfinityType.__gt__(self, other: object)` | simple | 2 | 魔术方法 |
| 8 | `__ge__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.InfinityType.__ge__(self, other: object)` | simple | 2 | 魔术方法 |
| 9 | `__neg__` | instance | `self: object` | `'NegativeInfinityType'` | `sklearn.externals._packaging._structures.InfinityType.__neg__(self: object)` | simple | 2 | 魔术方法 |

---

## 🔹 `NegativeInfinityType`

**完全限定名**: `sklearn.externals._packaging._structures.NegativeInfinityType`

**文件路径**: `sklearn/externals/_packaging/_structures.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__repr__` | instance | `self` | `str` | `sklearn.externals._packaging._structures.NegativeInfinityType.__repr__(self)` | simple | 2 | 魔术方法 |
| 2 | `__hash__` | instance | `self` | `int` | `sklearn.externals._packaging._structures.NegativeInfinityType.__hash__(self)` | simple | 2 | 魔术方法 |
| 3 | `__lt__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.NegativeInfinityType.__lt__(self, other: object)` | simple | 2 | 魔术方法 |
| 4 | `__le__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.NegativeInfinityType.__le__(self, other: object)` | simple | 2 | 魔术方法 |
| 5 | `__eq__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.NegativeInfinityType.__eq__(self, other: object)` | simple | 2 | 魔术方法 |
| 6 | `__ne__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.NegativeInfinityType.__ne__(self, other: object)` | simple | 2 | 魔术方法 |
| 7 | `__gt__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.NegativeInfinityType.__gt__(self, other: object)` | simple | 2 | 魔术方法 |
| 8 | `__ge__` | instance | `self, other: object` | `bool` | `sklearn.externals._packaging._structures.NegativeInfinityType.__ge__(self, other: object)` | simple | 2 | 魔术方法 |
| 9 | `__neg__` | instance | `self: object` | `InfinityType` | `sklearn.externals._packaging._structures.NegativeInfinityType.__neg__(self: object)` | simple | 2 | 魔术方法 |

---

## 🔹 `LegacyVersion`

**完全限定名**: `sklearn.externals._packaging.version.LegacyVersion`

**文件路径**: `sklearn/externals/_packaging/version.py`

**公共方法数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, version: str` | `None` | `sklearn.externals._packaging.version.LegacyVersion.__init__(self, version: str)` | simple | 9 | 魔术方法 |
| 2 | `__str__` | instance | `self` | `str` | `sklearn.externals._packaging.version.LegacyVersion.__str__(self)` | simple | 2 | 魔术方法 |
| 3 | `__repr__` | instance | `self` | `str` | `sklearn.externals._packaging.version.LegacyVersion.__repr__(self)` | simple | 2 | 魔术方法 |
| 4 | `public` | property | `self` | `str` | `sklearn.externals._packaging.version.LegacyVersion.public(self)` | simple | 2 | - |
| 5 | `base_version` | property | `self` | `str` | `sklearn.externals._packaging.version.LegacyVersion.base_version(self)` | simple | 2 | - |
| 6 | `epoch` | property | `self` | `int` | `sklearn.externals._packaging.version.LegacyVersion.epoch(self)` | simple | 2 | - |
| 7 | `release` | property | `self` | `None` | `sklearn.externals._packaging.version.LegacyVersion.release(self)` | simple | 2 | - |
| 8 | `pre` | property | `self` | `None` | `sklearn.externals._packaging.version.LegacyVersion.pre(self)` | simple | 2 | - |
| 9 | `post` | property | `self` | `None` | `sklearn.externals._packaging.version.LegacyVersion.post(self)` | simple | 2 | - |
| 10 | `dev` | property | `self` | `None` | `sklearn.externals._packaging.version.LegacyVersion.dev(self)` | simple | 2 | - |
| 11 | `local` | property | `self` | `None` | `sklearn.externals._packaging.version.LegacyVersion.local(self)` | simple | 2 | - |
| 12 | `is_prerelease` | property | `self` | `bool` | `sklearn.externals._packaging.version.LegacyVersion.is_prerelease(self)` | simple | 2 | - |
| 13 | `is_postrelease` | property | `self` | `bool` | `sklearn.externals._packaging.version.LegacyVersion.is_postrelease(self)` | simple | 2 | - |
| 14 | `is_devrelease` | property | `self` | `bool` | `sklearn.externals._packaging.version.LegacyVersion.is_devrelease(self)` | simple | 2 | - |

---

## 🔹 `Version`

**完全限定名**: `sklearn.externals._packaging.version.Version`

**文件路径**: `sklearn/externals/_packaging/version.py`

**公共方法数**: 17

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, version: str` | `None` | `sklearn.externals._packaging.version.Version.__init__(self, version: str)` | medium | 28 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `__repr__` | instance | `self` | `str` | `sklearn.externals._packaging.version.Version.__repr__(self)` | simple | 2 | 魔术方法 |
| 3 | `__str__` | instance | `self` | `str` | `sklearn.externals._packaging.version.Version.__str__(self)` | medium | 27 | 魔术方法, 有逻辑 |
| 4 | `epoch` | property | `self` | `int` | `sklearn.externals._packaging.version.Version.epoch(self)` | simple | 3 | - |
| 5 | `release` | property | `self` | `Tuple[(int, Ellipsis)]` | `sklearn.externals._packaging.version.Version.release(self)` | simple | 3 | - |
| 6 | `pre` | property | `self` | `Optional[Tuple[(str, int)]]` | `sklearn.externals._packaging.version.Version.pre(self)` | simple | 3 | - |
| 7 | `post` | property | `self` | `Optional[int]` | `sklearn.externals._packaging.version.Version.post(self)` | simple | 2 | 有逻辑 |
| 8 | `dev` | property | `self` | `Optional[int]` | `sklearn.externals._packaging.version.Version.dev(self)` | simple | 2 | 有逻辑 |
| 9 | `local` | property | `self` | `Optional[str]` | `sklearn.externals._packaging.version.Version.local(self)` | simple | 5 | 有逻辑 |
| 10 | `public` | property | `self` | `str` | `sklearn.externals._packaging.version.Version.public(self)` | simple | 2 | - |
| 11 | `base_version` | property | `self` | `str` | `sklearn.externals._packaging.version.Version.base_version(self)` | simple | 11 | 有逻辑 |
| 12 | `is_prerelease` | property | `self` | `bool` | `sklearn.externals._packaging.version.Version.is_prerelease(self)` | simple | 2 | - |
| 13 | `is_postrelease` | property | `self` | `bool` | `sklearn.externals._packaging.version.Version.is_postrelease(self)` | simple | 2 | - |
| 14 | `is_devrelease` | property | `self` | `bool` | `sklearn.externals._packaging.version.Version.is_devrelease(self)` | simple | 2 | - |
| 15 | `major` | property | `self` | `int` | `sklearn.externals._packaging.version.Version.major(self)` | simple | 2 | 有逻辑 |
| 16 | `minor` | property | `self` | `int` | `sklearn.externals._packaging.version.Version.minor(self)` | simple | 2 | 有逻辑 |
| 17 | `micro` | property | `self` | `int` | `sklearn.externals._packaging.version.Version.micro(self)` | simple | 2 | 有逻辑 |

---

## 🔹 `HasShape`

**完全限定名**: `sklearn.externals.array_api_compat.common._typing.HasShape`

**文件路径**: `sklearn/externals/array_api_compat/common/_typing.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `shape` | property | `` | `_T_co` | `sklearn.externals.array_api_compat.common._typing.HasShape.shape()` | simple | 1 | - |

---

## 🔹 `JustComplex`

**完全限定名**: `sklearn.externals.array_api_compat.common._typing.JustComplex`

**文件路径**: `sklearn/externals/array_api_compat/common/_typing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__class__` | property | `` | `type[complex]` | `sklearn.externals.array_api_compat.common._typing.JustComplex.__class__()` | simple | 1 | 魔术方法 |
| 2 | `__class__` | instance | `` | `None` | `sklearn.externals.array_api_compat.common._typing.JustComplex.__class__()` | simple | 1 | 魔术方法 |

---

## 🔹 `JustFloat`

**完全限定名**: `sklearn.externals.array_api_compat.common._typing.JustFloat`

**文件路径**: `sklearn/externals/array_api_compat/common/_typing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__class__` | property | `` | `type[float]` | `sklearn.externals.array_api_compat.common._typing.JustFloat.__class__()` | simple | 1 | 魔术方法 |
| 2 | `__class__` | instance | `` | `None` | `sklearn.externals.array_api_compat.common._typing.JustFloat.__class__()` | simple | 1 | 魔术方法 |

---

## 🔹 `JustInt`

**完全限定名**: `sklearn.externals.array_api_compat.common._typing.JustInt`

**文件路径**: `sklearn/externals/array_api_compat/common/_typing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__class__` | property | `` | `type[int]` | `sklearn.externals.array_api_compat.common._typing.JustInt.__class__()` | simple | 1 | 魔术方法 |
| 2 | `__class__` | instance | `` | `None` | `sklearn.externals.array_api_compat.common._typing.JustInt.__class__()` | simple | 1 | 魔术方法 |

---

## 🔹 `NestedSequence`

**完全限定名**: `sklearn.externals.array_api_compat.common._typing.NestedSequence`

**文件路径**: `sklearn/externals/array_api_compat/common/_typing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__getitem__` | instance | `` | `_T_co | NestedSequence[_T_co]` | `sklearn.externals.array_api_compat.common._typing.NestedSequence.__getitem__()` | simple | 1 | 魔术方法 |
| 2 | `__len__` | instance | `` | `int` | `sklearn.externals.array_api_compat.common._typing.NestedSequence.__len__()` | simple | 1 | 魔术方法 |

---

## 🔹 `SupportsArrayNamespace`

**完全限定名**: `sklearn.externals.array_api_compat.common._typing.SupportsArrayNamespace`

**文件路径**: `sklearn/externals/array_api_compat/common/_typing.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__array_namespace__` | instance | `api_version: str | None` | `_T_co` | `sklearn.externals.array_api_compat.common._typing.SupportsArrayNamespace.__array_namespace__(api_version: str | None)` | simple | 1 | 魔术方法 |

---

## 🔹 `at`

**完全限定名**: `sklearn.externals.array_api_extra._lib._at.at`

**文件路径**: `sklearn/externals/array_api_extra/_lib/_at.py`

**公共方法数**: 10

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `` | `None` | `sklearn.externals.array_api_extra._lib._at.at.__init__()` | simple | 5 | 魔术方法 |
| 2 | `__getitem__` | instance | `` | `Self` | `sklearn.externals.array_api_extra._lib._at.at.__getitem__()` | simple | 11 | 魔术方法, 抛异常, 有逻辑 |
| 3 | `set` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.set(copy: bool | None = None, xp: ModuleType | None = None)` | simple | 9 | - |
| 4 | `add` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.add(copy: bool | None = None, xp: ModuleType | None = None)` | simple | 13 | 有逻辑 |
| 5 | `subtract` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.subtract(copy: bool | None = None, xp: ModuleType | None = None)` | medium | 11 | - |
| 6 | `multiply` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.multiply(copy: bool | None = None, xp: ModuleType | None = None)` | medium | 11 | - |
| 7 | `divide` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.divide(copy: bool | None = None, xp: ModuleType | None = None)` | medium | 11 | - |
| 8 | `power` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.power(copy: bool | None = None, xp: ModuleType | None = None)` | simple | 9 | - |
| 9 | `min` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.min(copy: bool | None = None, xp: ModuleType | None = None)` | medium | 18 | 有逻辑 |
| 10 | `max` | instance | `copy: bool | None = None, xp: ModuleType | None...` | `Array` | `sklearn.externals.array_api_extra._lib._at.at.max(copy: bool | None = None, xp: ModuleType | None = None)` | medium | 13 | 有逻辑 |

---

## 🔹 `Backend`

**完全限定名**: `sklearn.externals.array_api_extra._lib._backends.Backend`

**文件路径**: `sklearn/externals/array_api_extra/_lib/_backends.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `modname` | property | `self` | `str` | `sklearn.externals.array_api_extra._lib._backends.Backend.modname(self)` | simple | 3 | - |
| 2 | `like` | instance | `self, *others: Backend` | `bool` | `sklearn.externals.array_api_extra._lib._backends.Backend.like(self, *others: Backend)` | simple | 3 | 有逻辑 |
| 3 | `pytest_param` | instance | `self` | `Any` | `sklearn.externals.array_api_extra._lib._backends.Backend.pytest_param(self)` | medium | 25 | 有逻辑 |

---

## 🔹 `CountingDaskScheduler`

**完全限定名**: `sklearn.externals.array_api_extra.testing.CountingDaskScheduler`

**文件路径**: `sklearn/externals/array_api_extra/testing.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, max_count: int, msg: str` | `None` | `sklearn.externals.array_api_extra.testing.CountingDaskScheduler.__init__(self, max_count: int, msg: str)` | simple | 4 | 魔术方法 |
| 2 | `__call__` | instance | `self, dsk: Graph, keys: Sequence[Key] | Key, **...` | `Any` | `sklearn.externals.array_api_extra.testing.CountingDaskScheduler.__call__(self, dsk: Graph, keys: Sequence[Key] | Key, **kwargs: Any)` | simple | 11 | 魔术方法 |

---

## 🔹 `DictVectorizer`

**完全限定名**: `sklearn.feature_extraction._dict_vectorizer.DictVectorizer`

**文件路径**: `sklearn/feature_extraction/_dict_vectorizer.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, dtype = np.float64, separator = '=', spar...` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.__init__(self, dtype = np.float64, separator = '=', sparse = True, sort = True)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.fit(self, X, y = None)` | complex | 52 | 抛异常, 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.fit_transform(self, X, y = None)` | medium | 24 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X, dict_type = dict` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.inverse_transform(self, X, dict_type = dict)` | complex | 42 | 有逻辑 |
| 5 | `transform` | instance | `self, X` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.transform(self, X)` | medium | 19 | - |
| 6 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.get_feature_names_out(self, input_features = None)` | medium | 19 | 有逻辑 |
| 7 | `restrict` | instance | `self, support, indices = False` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.restrict(self, support, indices = False)` | complex | 49 | 有逻辑 |
| 8 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction._dict_vectorizer.DictVectorizer.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `FeatureHasher`

**完全限定名**: `sklearn.feature_extraction._hash.FeatureHasher`

**文件路径**: `sklearn/feature_extraction/_hash.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_features = 2 ** 20, input_type = 'dict'...` | `None` | `sklearn.feature_extraction._hash.FeatureHasher.__init__(self, n_features = 2 ** 20, input_type = 'dict', dtype = np.float64, alternate_sign = True)` | medium | 12 | 魔术方法 |
| 2 | `fit` | instance | `self, X = None, y = None` | `None` | `sklearn.feature_extraction._hash.FeatureHasher.fit(self, X = None, y = None)` | medium | 20 | 有逻辑 |
| 3 | `transform` | instance | `self, raw_X` | `None` | `sklearn.feature_extraction._hash.FeatureHasher.transform(self, raw_X)` | complex | 46 | 抛异常, 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction._hash.FeatureHasher.__sklearn_tags__(self)` | simple | 9 | 魔术方法, 有逻辑 |

---

## 🔹 `PatchExtractor`

**完全限定名**: `sklearn.feature_extraction.image.PatchExtractor`

**文件路径**: `sklearn/feature_extraction/image.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, patch_size = None, max_patches = None, ra...` | `None` | `sklearn.feature_extraction.image.PatchExtractor.__init__(self, patch_size = None, max_patches = None, random_state = None)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction.image.PatchExtractor.fit(self, X, y = None)` | medium | 23 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.feature_extraction.image.PatchExtractor.transform(self, X)` | complex | 63 | 抛异常, 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction.image.PatchExtractor.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `CountVectorizer`

**完全限定名**: `sklearn.feature_extraction.text.CountVectorizer`

**文件路径**: `sklearn/feature_extraction/text.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, input = 'content', encoding = 'utf-8', de...` | `None` | `sklearn.feature_extraction.text.CountVectorizer.__init__(self, input = 'content', encoding = 'utf-8', decode_error = 'strict', strip_accents = None, lowercase = True, preprocessor = None, tokenizer = None, stop_words = None, token_pattern = '(?u)\\b\\w\\w+\\b', ngram_range = (1, 1), analyzer = 'word', max_df = 1.0, min_df = 1, max_features = None, vocabulary = None, binary = False, dtype = np.int64)` | complex | 38 | 魔术方法 |
| 2 | `fit` | instance | `self, raw_documents, y = None` | `None` | `sklearn.feature_extraction.text.CountVectorizer.fit(self, raw_documents, y = None)` | medium | 18 | - |
| 3 | `fit_transform` | instance | `self, raw_documents, y = None` | `None` | `sklearn.feature_extraction.text.CountVectorizer.fit_transform(self, raw_documents, y = None)` | complex | 66 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, raw_documents` | `None` | `sklearn.feature_extraction.text.CountVectorizer.transform(self, raw_documents)` | medium | 27 | 抛异常, 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.feature_extraction.text.CountVectorizer.inverse_transform(self, X)` | medium | 32 | 有逻辑 |
| 6 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.feature_extraction.text.CountVectorizer.get_feature_names_out(self, input_features = None)` | medium | 18 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction.text.CountVectorizer.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `HashingVectorizer`

**完全限定名**: `sklearn.feature_extraction.text.HashingVectorizer`

**文件路径**: `sklearn/feature_extraction/text.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, input = 'content', encoding = 'utf-8', de...` | `None` | `sklearn.feature_extraction.text.HashingVectorizer.__init__(self, input = 'content', encoding = 'utf-8', decode_error = 'strict', strip_accents = None, lowercase = True, preprocessor = None, tokenizer = None, stop_words = None, token_pattern = '(?u)\\b\\w\\w+\\b', ngram_range = (1, 1), analyzer = 'word', n_features = 2 ** 20, binary = False, norm = 'l2', alternate_sign = True, dtype = np.float64)` | complex | 36 | 魔术方法 |
| 2 | `partial_fit` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction.text.HashingVectorizer.partial_fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction.text.HashingVectorizer.fit(self, X, y = None)` | medium | 30 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.feature_extraction.text.HashingVectorizer.transform(self, X)` | medium | 29 | 抛异常, 有逻辑 |
| 5 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction.text.HashingVectorizer.fit_transform(self, X, y = None)` | medium | 19 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction.text.HashingVectorizer.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `TfidfTransformer`

**完全限定名**: `sklearn.feature_extraction.text.TfidfTransformer`

**文件路径**: `sklearn/feature_extraction/text.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, norm = 'l2', use_idf = True, smooth_idf =...` | `None` | `sklearn.feature_extraction.text.TfidfTransformer.__init__(self, norm = 'l2', use_idf = True, smooth_idf = True, sublinear_tf = False)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.feature_extraction.text.TfidfTransformer.fit(self, X, y = None)` | medium | 46 | 有逻辑 |
| 3 | `transform` | instance | `self, X, copy = True` | `None` | `sklearn.feature_extraction.text.TfidfTransformer.transform(self, X, copy = True)` | complex | 42 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction.text.TfidfTransformer.__sklearn_tags__(self)` | simple | 7 | 魔术方法, 有逻辑 |

---

## 🔹 `TfidfVectorizer`

**完全限定名**: `sklearn.feature_extraction.text.TfidfVectorizer`

**文件路径**: `sklearn/feature_extraction/text.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, input = 'content', encoding = 'utf-8', de...` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.__init__(self, input = 'content', encoding = 'utf-8', decode_error = 'strict', strip_accents = None, lowercase = True, preprocessor = None, tokenizer = None, analyzer = 'word', stop_words = None, token_pattern = '(?u)\\b\\w\\w+\\b', ngram_range = (1, 1), max_df = 1.0, min_df = 1, max_features = None, vocabulary = None, binary = False, dtype = np.float64, norm = 'l2', use_idf = True, smooth_idf = True, sublinear_tf = False)` | complex | 48 | 魔术方法 |
| 2 | `idf_` | property | `self` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.idf_(self)` | medium | 13 | 抛异常, 有逻辑 |
| 3 | `idf_` | instance | `self, value` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.idf_(self, value)` | medium | 21 | 抛异常, 有逻辑 |
| 4 | `fit` | instance | `self, raw_documents, y = None` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.fit(self, raw_documents, y = None)` | medium | 27 | - |
| 5 | `fit_transform` | instance | `self, raw_documents, y = None` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.fit_transform(self, raw_documents, y = None)` | medium | 31 | - |
| 6 | `transform` | instance | `self, raw_documents` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.transform(self, raw_documents)` | medium | 20 | - |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_extraction.text.TfidfVectorizer.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `SelectorMixin`

**完全限定名**: `sklearn.feature_selection._base.SelectorMixin`

**文件路径**: `sklearn/feature_selection/_base.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_support` | instance | `self, indices = False` | `None` | `sklearn.feature_selection._base.SelectorMixin.get_support(self, indices = False)` | medium | 22 | 有逻辑 |
| 2 | `transform` | instance | `self, X` | `None` | `sklearn.feature_selection._base.SelectorMixin.transform(self, X)` | medium | 30 | - |
| 3 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.feature_selection._base.SelectorMixin.inverse_transform(self, X)` | complex | 39 | 抛异常, 有逻辑 |
| 4 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.feature_selection._base.SelectorMixin.get_feature_names_out(self, input_features = None)` | medium | 23 | 有逻辑 |

---

## 🔹 `SelectFromModel`

**完全限定名**: `sklearn.feature_selection._from_model.SelectFromModel`

**文件路径**: `sklearn/feature_selection/_from_model.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, threshold = None, prefit = Fal...` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.__init__(self, estimator, threshold = None, prefit = False, norm_order = 1, max_features = None, importance_getter = 'auto')` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, **fit_params` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.fit(self, X, y = None, **fit_params)` | complex | 56 | 抛异常, 有逻辑 |
| 3 | `threshold_` | property | `self` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.threshold_(self)` | simple | 9 | 有逻辑 |
| 4 | `partial_fit` | instance | `self, X, y = None, **partial_fit_params` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.partial_fit(self, X, y = None, **partial_fit_params)` | complex | 66 | 抛异常, 有逻辑 |
| 5 | `n_features_in_` | property | `self` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.n_features_in_(self)` | medium | 14 | 抛异常, 有逻辑 |
| 6 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.get_metadata_routing(self)` | medium | 21 | - |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._from_model.SelectFromModel.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `RFE`

**完全限定名**: `sklearn.feature_selection._rfe.RFE`

**文件路径**: `sklearn/feature_selection/_rfe.py`

**公共方法数**: 10

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_features_to_select = None, s...` | `None` | `sklearn.feature_selection._rfe.RFE.__init__(self, estimator, n_features_to_select = None, step = 1, verbose = 0, importance_getter = 'auto')` | medium | 14 | 魔术方法 |
| 2 | `classes_` | property | `self` | `None` | `sklearn.feature_selection._rfe.RFE.classes_(self)` | simple | 8 | - |
| 3 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.feature_selection._rfe.RFE.fit(self, X, y, **fit_params)` | medium | 33 | 有逻辑 |
| 4 | `predict` | instance | `self, X, **predict_params` | `None` | `sklearn.feature_selection._rfe.RFE.predict(self, X, **predict_params)` | medium | 34 | 有逻辑 |
| 5 | `score` | instance | `self, X, y, **score_params` | `None` | `sklearn.feature_selection._rfe.RFE.score(self, X, y, **score_params)` | complex | 39 | 有逻辑 |
| 6 | `decision_function` | instance | `self, X` | `None` | `sklearn.feature_selection._rfe.RFE.decision_function(self, X)` | medium | 20 | 有逻辑 |
| 7 | `predict_proba` | instance | `self, X` | `None` | `sklearn.feature_selection._rfe.RFE.predict_proba(self, X)` | medium | 18 | 有逻辑 |
| 8 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.feature_selection._rfe.RFE.predict_log_proba(self, X)` | medium | 16 | 有逻辑 |
| 9 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._rfe.RFE.__sklearn_tags__(self)` | medium | 14 | 魔术方法, 有逻辑 |
| 10 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.feature_selection._rfe.RFE.get_metadata_routing(self)` | medium | 22 | - |

---

## 🔹 `RFECV`

**完全限定名**: `sklearn.feature_selection._rfe.RFECV`

**文件路径**: `sklearn/feature_selection/_rfe.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, step = 1, min_features_to_sele...` | `None` | `sklearn.feature_selection._rfe.RFECV.__init__(self, estimator, step = 1, min_features_to_select = 1, cv = None, scoring = None, verbose = 0, n_jobs = None, importance_getter = 'auto')` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **params` | `None` | `sklearn.feature_selection._rfe.RFECV.fit(self, X, y, **params)` | complex | 137 | 有逻辑 |
| 3 | `score` | instance | `self, X, y, **score_params` | `None` | `sklearn.feature_selection._rfe.RFECV.score(self, X, y, **score_params)` | medium | 35 | 有逻辑 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.feature_selection._rfe.RFECV.get_metadata_routing(self)` | medium | 34 | - |

---

## 🔹 `SequentialFeatureSelector`

**完全限定名**: `sklearn.feature_selection._sequential.SequentialFeatureSelector`

**文件路径**: `sklearn/feature_selection/_sequential.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_features_to_select = 'auto',...` | `None` | `sklearn.feature_selection._sequential.SequentialFeatureSelector.__init__(self, estimator, n_features_to_select = 'auto', tol = None, direction = 'forward', scoring = None, cv = 5, n_jobs = None)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, **params` | `None` | `sklearn.feature_selection._sequential.SequentialFeatureSelector.fit(self, X, y = None, **params)` | complex | 99 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._sequential.SequentialFeatureSelector.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.feature_selection._sequential.SequentialFeatureSelector.get_metadata_routing(self)` | medium | 28 | - |

---

## 🔹 `GenericUnivariateSelect`

**完全限定名**: `sklearn.feature_selection._univariate_selection.GenericUnivariateSelect`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, score_func = f_classif, mode = 'percentil...` | `None` | `sklearn.feature_selection._univariate_selection.GenericUnivariateSelect.__init__(self, score_func = f_classif, mode = 'percentile', param = 1e-05)` | simple | 4 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._univariate_selection.GenericUnivariateSelect.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SelectFdr`

**完全限定名**: `sklearn.feature_selection._univariate_selection.SelectFdr`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, score_func = f_classif, alpha = 0.05` | `None` | `sklearn.feature_selection._univariate_selection.SelectFdr.__init__(self, score_func = f_classif, alpha = 0.05)` | simple | 3 | 魔术方法 |

---

## 🔹 `SelectFpr`

**完全限定名**: `sklearn.feature_selection._univariate_selection.SelectFpr`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, score_func = f_classif, alpha = 0.05` | `None` | `sklearn.feature_selection._univariate_selection.SelectFpr.__init__(self, score_func = f_classif, alpha = 0.05)` | simple | 3 | 魔术方法 |

---

## 🔹 `SelectFwe`

**完全限定名**: `sklearn.feature_selection._univariate_selection.SelectFwe`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, score_func = f_classif, alpha = 0.05` | `None` | `sklearn.feature_selection._univariate_selection.SelectFwe.__init__(self, score_func = f_classif, alpha = 0.05)` | simple | 3 | 魔术方法 |

---

## 🔹 `SelectKBest`

**完全限定名**: `sklearn.feature_selection._univariate_selection.SelectKBest`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, score_func = f_classif, k = 10` | `None` | `sklearn.feature_selection._univariate_selection.SelectKBest.__init__(self, score_func = f_classif, k = 10)` | simple | 3 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._univariate_selection.SelectKBest.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SelectPercentile`

**完全限定名**: `sklearn.feature_selection._univariate_selection.SelectPercentile`

**文件路径**: `sklearn/feature_selection/_univariate_selection.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, score_func = f_classif, percentile = 10` | `None` | `sklearn.feature_selection._univariate_selection.SelectPercentile.__init__(self, score_func = f_classif, percentile = 10)` | simple | 3 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._univariate_selection.SelectPercentile.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `VarianceThreshold`

**完全限定名**: `sklearn.feature_selection._variance_threshold.VarianceThreshold`

**文件路径**: `sklearn/feature_selection/_variance_threshold.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, threshold = 0.0` | `None` | `sklearn.feature_selection._variance_threshold.VarianceThreshold.__init__(self, threshold = 0.0)` | simple | 2 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.feature_selection._variance_threshold.VarianceThreshold.fit(self, X, y = None)` | complex | 49 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.feature_selection._variance_threshold.VarianceThreshold.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `FrozenEstimator`

**完全限定名**: `sklearn.frozen._frozen.FrozenEstimator`

**文件路径**: `sklearn/frozen/_frozen.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator` | `None` | `sklearn.frozen._frozen.FrozenEstimator.__init__(self, estimator)` | simple | 2 | 魔术方法 |
| 2 | `__getitem__` | instance | `self, *args, **kwargs` | `None` | `sklearn.frozen._frozen.FrozenEstimator.__getitem__(self, *args, **kwargs)` | simple | 5 | 魔术方法 |
| 3 | `__getattr__` | instance | `self, name` | `None` | `sklearn.frozen._frozen.FrozenEstimator.__getattr__(self, name)` | simple | 6 | 魔术方法, 抛异常, 有逻辑 |
| 4 | `__sklearn_clone__` | instance | `self` | `None` | `sklearn.frozen._frozen.FrozenEstimator.__sklearn_clone__(self)` | simple | 2 | 魔术方法 |
| 5 | `__sklearn_is_fitted__` | instance | `self` | `None` | `sklearn.frozen._frozen.FrozenEstimator.__sklearn_is_fitted__(self)` | simple | 6 | 魔术方法, 有逻辑 |
| 6 | `fit` | instance | `self, X, y, *args, **kwargs` | `None` | `sklearn.frozen._frozen.FrozenEstimator.fit(self, X, y, *args, **kwargs)` | medium | 28 | 有逻辑 |
| 7 | `set_params` | instance | `self, **kwargs` | `None` | `sklearn.frozen._frozen.FrozenEstimator.set_params(self, **kwargs)` | medium | 26 | 抛异常, 有逻辑 |
| 8 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.frozen._frozen.FrozenEstimator.get_params(self, deep = True)` | medium | 17 | 有逻辑 |
| 9 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.frozen._frozen.FrozenEstimator.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `GaussianProcessClassifier`

**完全限定名**: `sklearn.gaussian_process._gpc.GaussianProcessClassifier`

**文件路径**: `sklearn/gaussian_process/_gpc.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = None, optimizer = 'fmin_l_bfgs_b...` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.__init__(self, kernel = None, optimizer = 'fmin_l_bfgs_b', n_restarts_optimizer = 0, max_iter_predict = 100, warm_start = False, copy_X_train = True, random_state = None, multi_class = 'one_vs_rest', n_jobs = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.fit(self, X, y)` | complex | 73 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.predict(self, X)` | medium | 21 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.predict_proba(self, X)` | medium | 29 | 抛异常, 有逻辑 |
| 5 | `kernel_` | property | `self` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.kernel_(self)` | simple | 8 | 有逻辑 |
| 6 | `log_marginal_likelihood` | instance | `self, theta = None, eval_gradient = False, clon...` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.log_marginal_likelihood(self, theta = None, eval_gradient = False, clone_kernel = True)` | complex | 84 | 抛异常, 有逻辑 |
| 7 | `latent_mean_and_variance` | instance | `self, X` | `None` | `sklearn.gaussian_process._gpc.GaussianProcessClassifier.latent_mean_and_variance(self, X)` | medium | 38 | 抛异常, 有逻辑 |

---

## 🔹 `GaussianProcessRegressor`

**完全限定名**: `sklearn.gaussian_process._gpr.GaussianProcessRegressor`

**文件路径**: `sklearn/gaussian_process/_gpr.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = None, alpha = 1e-10, optimizer =...` | `None` | `sklearn.gaussian_process._gpr.GaussianProcessRegressor.__init__(self, kernel = None, alpha = 1e-10, optimizer = 'fmin_l_bfgs_b', n_restarts_optimizer = 0, normalize_y = False, copy_X_train = True, n_targets = None, random_state = None)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.gaussian_process._gpr.GaussianProcessRegressor.fit(self, X, y)` | complex | 141 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X, return_std = False, return_cov = False` | `None` | `sklearn.gaussian_process._gpr.GaussianProcessRegressor.predict(self, X, return_std = False, return_cov = False)` | complex | 131 | 抛异常, 有逻辑 |
| 4 | `sample_y` | instance | `self, X, n_samples = 1, random_state = 0` | `None` | `sklearn.gaussian_process._gpr.GaussianProcessRegressor.sample_y(self, X, n_samples = 1, random_state = 0)` | complex | 38 | 有逻辑 |
| 5 | `log_marginal_likelihood` | instance | `self, theta = None, eval_gradient = False, clon...` | `None` | `sklearn.gaussian_process._gpr.GaussianProcessRegressor.log_marginal_likelihood(self, theta = None, eval_gradient = False, clone_kernel = True)` | complex | 116 | 抛异常, 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.gaussian_process._gpr.GaussianProcessRegressor.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `CompoundKernel`

**完全限定名**: `sklearn.gaussian_process.kernels.CompoundKernel`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 10

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernels` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.__init__(self, kernels)` | simple | 2 | 魔术方法 |
| 2 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.get_params(self, deep = True)` | medium | 15 | 有逻辑 |
| 3 | `theta` | property | `self` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.theta(self)` | medium | 14 | 有逻辑 |
| 4 | `theta` | instance | `self, theta` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.theta(self, theta)` | medium | 11 | 有逻辑 |
| 5 | `bounds` | property | `self` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.bounds(self)` | simple | 9 | 有逻辑 |
| 6 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.__call__(self, X, Y = None, eval_gradient = False)` | complex | 42 | 魔术方法, 有逻辑 |
| 7 | `__eq__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.__eq__(self, b)` | simple | 6 | 魔术方法, 有逻辑 |
| 8 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.is_stationary(self)` | simple | 3 | 有逻辑 |
| 9 | `requires_vector_input` | property | `self` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.requires_vector_input(self)` | simple | 3 | 有逻辑 |
| 10 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.CompoundKernel.diag(self, X)` | medium | 18 | 有逻辑 |

---

## 🔹 `ConstantKernel`

**完全限定名**: `sklearn.gaussian_process.kernels.ConstantKernel`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, constant_value = 1.0, constant_value_boun...` | `None` | `sklearn.gaussian_process.kernels.ConstantKernel.__init__(self, constant_value = 1.0, constant_value_bounds = (1e-05, 100000.0))` | simple | 3 | 魔术方法 |
| 2 | `hyperparameter_constant_value` | property | `self` | `None` | `sklearn.gaussian_process.kernels.ConstantKernel.hyperparameter_constant_value(self)` | simple | 2 | - |
| 3 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.ConstantKernel.__call__(self, X, Y = None, eval_gradient = False)` | complex | 53 | 魔术方法, 抛异常, 有逻辑 |
| 4 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.ConstantKernel.diag(self, X)` | medium | 22 | - |
| 5 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.ConstantKernel.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `DotProduct`

**完全限定名**: `sklearn.gaussian_process.kernels.DotProduct`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sigma_0 = 1.0, sigma_0_bounds = (1e-05, 1...` | `None` | `sklearn.gaussian_process.kernels.DotProduct.__init__(self, sigma_0 = 1.0, sigma_0_bounds = (1e-05, 100000.0))` | simple | 3 | 魔术方法 |
| 2 | `hyperparameter_sigma_0` | property | `self` | `None` | `sklearn.gaussian_process.kernels.DotProduct.hyperparameter_sigma_0(self)` | simple | 2 | - |
| 3 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.DotProduct.__call__(self, X, Y = None, eval_gradient = False)` | complex | 45 | 魔术方法, 抛异常, 有逻辑 |
| 4 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.DotProduct.diag(self, X)` | medium | 18 | - |
| 5 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.DotProduct.is_stationary(self)` | simple | 3 | - |
| 6 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.DotProduct.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `ExpSineSquared`

**完全限定名**: `sklearn.gaussian_process.kernels.ExpSineSquared`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, length_scale = 1.0, periodicity = 1.0, le...` | `None` | `sklearn.gaussian_process.kernels.ExpSineSquared.__init__(self, length_scale = 1.0, periodicity = 1.0, length_scale_bounds = (1e-05, 100000.0), periodicity_bounds = (1e-05, 100000.0))` | medium | 11 | 魔术方法 |
| 2 | `hyperparameter_length_scale` | property | `self` | `None` | `sklearn.gaussian_process.kernels.ExpSineSquared.hyperparameter_length_scale(self)` | simple | 3 | - |
| 3 | `hyperparameter_periodicity` | property | `self` | `None` | `sklearn.gaussian_process.kernels.ExpSineSquared.hyperparameter_periodicity(self)` | simple | 2 | - |
| 4 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.ExpSineSquared.__call__(self, X, Y = None, eval_gradient = False)` | complex | 62 | 魔术方法, 抛异常, 有逻辑 |
| 5 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.ExpSineSquared.__repr__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `Exponentiation`

**完全限定名**: `sklearn.gaussian_process.kernels.Exponentiation`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 12

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel, exponent` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.__init__(self, kernel, exponent)` | simple | 3 | 魔术方法 |
| 2 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.get_params(self, deep = True)` | medium | 19 | 有逻辑 |
| 3 | `hyperparameters` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.hyperparameters(self)` | medium | 13 | 有逻辑 |
| 4 | `theta` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.theta(self)` | medium | 14 | 有逻辑 |
| 5 | `theta` | instance | `self, theta` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.theta(self, theta)` | medium | 9 | 有逻辑 |
| 6 | `bounds` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.bounds(self)` | simple | 9 | - |
| 7 | `__eq__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.__eq__(self, b)` | simple | 4 | 魔术方法, 有逻辑 |
| 8 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.__call__(self, X, Y = None, eval_gradient = False)` | medium | 35 | 魔术方法, 有逻辑 |
| 9 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.diag(self, X)` | medium | 18 | - |
| 10 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.__repr__(self)` | simple | 2 | 魔术方法 |
| 11 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.is_stationary(self)` | simple | 3 | - |
| 12 | `requires_vector_input` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Exponentiation.requires_vector_input(self)` | simple | 3 | - |

---

## 🔹 `GenericKernelMixin`

**完全限定名**: `sklearn.gaussian_process.kernels.GenericKernelMixin`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `requires_vector_input` | property | `self` | `None` | `sklearn.gaussian_process.kernels.GenericKernelMixin.requires_vector_input(self)` | simple | 3 | - |

---

## 🔹 `Hyperparameter`

**完全限定名**: `sklearn.gaussian_process.kernels.Hyperparameter`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__new__` | instance | `cls, name, value_type, bounds, n_elements = 1, ...` | `None` | `sklearn.gaussian_process.kernels.Hyperparameter.__new__(cls, name, value_type, bounds, n_elements = 1, fixed = None)` | medium | 16 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `__eq__` | instance | `self, other` | `None` | `sklearn.gaussian_process.kernels.Hyperparameter.__eq__(self, other)` | simple | 8 | 魔术方法 |

---

## 🔹 `Kernel`

**完全限定名**: `sklearn.gaussian_process.kernels.Kernel`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 19

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.gaussian_process.kernels.Kernel.get_params(self, deep = True)` | complex | 39 | 抛异常, 有逻辑 |
| 2 | `set_params` | instance | `self, **params` | `None` | `sklearn.gaussian_process.kernels.Kernel.set_params(self, **params)` | complex | 39 | 抛异常, 有逻辑 |
| 3 | `clone_with_theta` | instance | `self, theta` | `None` | `sklearn.gaussian_process.kernels.Kernel.clone_with_theta(self, theta)` | simple | 11 | - |
| 4 | `n_dims` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.n_dims(self)` | simple | 3 | - |
| 5 | `hyperparameters` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.hyperparameters(self)` | simple | 8 | 有逻辑 |
| 6 | `theta` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.theta(self)` | medium | 22 | 有逻辑 |
| 7 | `theta` | instance | `self, theta` | `None` | `sklearn.gaussian_process.kernels.Kernel.theta(self, theta)` | medium | 29 | 有逻辑 |
| 8 | `bounds` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.bounds(self)` | medium | 17 | 有逻辑 |
| 9 | `__add__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Kernel.__add__(self, b)` | simple | 4 | 魔术方法, 有逻辑 |
| 10 | `__radd__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Kernel.__radd__(self, b)` | simple | 4 | 魔术方法, 有逻辑 |
| 11 | `__mul__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Kernel.__mul__(self, b)` | simple | 4 | 魔术方法, 有逻辑 |
| 12 | `__rmul__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Kernel.__rmul__(self, b)` | simple | 4 | 魔术方法, 有逻辑 |
| 13 | `__pow__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Kernel.__pow__(self, b)` | simple | 2 | 魔术方法 |
| 14 | `__eq__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.Kernel.__eq__(self, b)` | simple | 9 | 魔术方法, 有逻辑 |
| 15 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.__repr__(self)` | simple | 4 | 魔术方法 |
| 16 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.Kernel.__call__(self, X, Y = None, eval_gradient = False)` | simple | 2 | 魔术方法, 抽象方法 |
| 17 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.Kernel.diag(self, X)` | medium | 17 | 抽象方法 |
| 18 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.is_stationary(self)` | simple | 2 | 抽象方法 |
| 19 | `requires_vector_input` | property | `self` | `None` | `sklearn.gaussian_process.kernels.Kernel.requires_vector_input(self)` | simple | 5 | 有逻辑 |

---

## 🔹 `KernelOperator`

**完全限定名**: `sklearn.gaussian_process.kernels.KernelOperator`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, k1, k2` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.__init__(self, k1, k2)` | simple | 3 | 魔术方法 |
| 2 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.get_params(self, deep = True)` | medium | 22 | 有逻辑 |
| 3 | `hyperparameters` | property | `self` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.hyperparameters(self)` | medium | 22 | 有逻辑 |
| 4 | `theta` | property | `self` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.theta(self)` | medium | 14 | 有逻辑 |
| 5 | `theta` | instance | `self, theta` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.theta(self, theta)` | medium | 11 | 有逻辑 |
| 6 | `bounds` | property | `self` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.bounds(self)` | medium | 13 | 有逻辑 |
| 7 | `__eq__` | instance | `self, b` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.__eq__(self, b)` | simple | 6 | 魔术方法, 有逻辑 |
| 8 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.is_stationary(self)` | simple | 3 | - |
| 9 | `requires_vector_input` | property | `self` | `None` | `sklearn.gaussian_process.kernels.KernelOperator.requires_vector_input(self)` | simple | 3 | - |

---

## 🔹 `Matern`

**完全限定名**: `sklearn.gaussian_process.kernels.Matern`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, length_scale = 1.0, length_scale_bounds =...` | `None` | `sklearn.gaussian_process.kernels.Matern.__init__(self, length_scale = 1.0, length_scale_bounds = (1e-05, 100000.0), nu = 1.5)` | simple | 3 | 魔术方法 |
| 2 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.Matern.__call__(self, X, Y = None, eval_gradient = False)` | complex | 102 | 魔术方法, 抛异常, 有逻辑 |
| 3 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Matern.__repr__(self)` | medium | 11 | 魔术方法, 有逻辑 |

---

## 🔹 `NormalizedKernelMixin`

**完全限定名**: `sklearn.gaussian_process.kernels.NormalizedKernelMixin`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.NormalizedKernelMixin.diag(self, X)` | medium | 18 | - |

---

## 🔹 `PairwiseKernel`

**完全限定名**: `sklearn.gaussian_process.kernels.PairwiseKernel`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, gamma = 1.0, gamma_bounds = (1e-05, 10000...` | `None` | `sklearn.gaussian_process.kernels.PairwiseKernel.__init__(self, gamma = 1.0, gamma_bounds = (1e-05, 100000.0), metric = 'linear', pairwise_kernels_kwargs = None)` | medium | 11 | 魔术方法 |
| 2 | `hyperparameter_gamma` | property | `self` | `None` | `sklearn.gaussian_process.kernels.PairwiseKernel.hyperparameter_gamma(self)` | simple | 2 | - |
| 3 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.PairwiseKernel.__call__(self, X, Y = None, eval_gradient = False)` | complex | 59 | 魔术方法, 有逻辑 |
| 4 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.PairwiseKernel.diag(self, X)` | medium | 19 | - |
| 5 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.PairwiseKernel.is_stationary(self)` | simple | 3 | - |
| 6 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.PairwiseKernel.__repr__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `Product`

**完全限定名**: `sklearn.gaussian_process.kernels.Product`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.Product.__call__(self, X, Y = None, eval_gradient = False)` | complex | 36 | 魔术方法, 有逻辑 |
| 2 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.Product.diag(self, X)` | medium | 18 | - |
| 3 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Product.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `RBF`

**完全限定名**: `sklearn.gaussian_process.kernels.RBF`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, length_scale = 1.0, length_scale_bounds =...` | `None` | `sklearn.gaussian_process.kernels.RBF.__init__(self, length_scale = 1.0, length_scale_bounds = (1e-05, 100000.0))` | simple | 3 | 魔术方法 |
| 2 | `anisotropic` | property | `self` | `None` | `sklearn.gaussian_process.kernels.RBF.anisotropic(self)` | simple | 2 | - |
| 3 | `hyperparameter_length_scale` | property | `self` | `None` | `sklearn.gaussian_process.kernels.RBF.hyperparameter_length_scale(self)` | simple | 9 | 有逻辑 |
| 4 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.RBF.__call__(self, X, Y = None, eval_gradient = False)` | complex | 58 | 魔术方法, 抛异常, 有逻辑 |
| 5 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.RBF.__repr__(self)` | simple | 10 | 魔术方法, 有逻辑 |

---

## 🔹 `RationalQuadratic`

**完全限定名**: `sklearn.gaussian_process.kernels.RationalQuadratic`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, length_scale = 1.0, alpha = 1.0, length_s...` | `None` | `sklearn.gaussian_process.kernels.RationalQuadratic.__init__(self, length_scale = 1.0, alpha = 1.0, length_scale_bounds = (1e-05, 100000.0), alpha_bounds = (1e-05, 100000.0))` | medium | 11 | 魔术方法 |
| 2 | `hyperparameter_length_scale` | property | `self` | `None` | `sklearn.gaussian_process.kernels.RationalQuadratic.hyperparameter_length_scale(self)` | simple | 2 | - |
| 3 | `hyperparameter_alpha` | property | `self` | `None` | `sklearn.gaussian_process.kernels.RationalQuadratic.hyperparameter_alpha(self)` | simple | 2 | - |
| 4 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.RationalQuadratic.__call__(self, X, Y = None, eval_gradient = False)` | complex | 66 | 魔术方法, 抛异常, 有逻辑 |
| 5 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.RationalQuadratic.__repr__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `StationaryKernelMixin`

**完全限定名**: `sklearn.gaussian_process.kernels.StationaryKernelMixin`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `is_stationary` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.StationaryKernelMixin.is_stationary(self)` | simple | 3 | - |

---

## 🔹 `Sum`

**完全限定名**: `sklearn.gaussian_process.kernels.Sum`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.Sum.__call__(self, X, Y = None, eval_gradient = False)` | medium | 34 | 魔术方法, 有逻辑 |
| 2 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.Sum.diag(self, X)` | medium | 18 | - |
| 3 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.Sum.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `WhiteKernel`

**完全限定名**: `sklearn.gaussian_process.kernels.WhiteKernel`

**文件路径**: `sklearn/gaussian_process/kernels.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, noise_level = 1.0, noise_level_bounds = (...` | `None` | `sklearn.gaussian_process.kernels.WhiteKernel.__init__(self, noise_level = 1.0, noise_level_bounds = (1e-05, 100000.0))` | simple | 3 | 魔术方法 |
| 2 | `hyperparameter_noise_level` | property | `self` | `None` | `sklearn.gaussian_process.kernels.WhiteKernel.hyperparameter_noise_level(self)` | simple | 2 | - |
| 3 | `__call__` | instance | `self, X, Y = None, eval_gradient = False` | `None` | `sklearn.gaussian_process.kernels.WhiteKernel.__call__(self, X, Y = None, eval_gradient = False)` | complex | 46 | 魔术方法, 抛异常, 有逻辑 |
| 4 | `diag` | instance | `self, X` | `None` | `sklearn.gaussian_process.kernels.WhiteKernel.diag(self, X)` | medium | 20 | - |
| 5 | `__repr__` | instance | `self` | `None` | `sklearn.gaussian_process.kernels.WhiteKernel.__repr__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `MissingIndicator`

**完全限定名**: `sklearn.impute._base.MissingIndicator`

**文件路径**: `sklearn/impute/_base.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, missing_values = np.nan, features = 'miss...` | `None` | `sklearn.impute._base.MissingIndicator.__init__(self, missing_values = np.nan, features = 'missing-only', sparse = 'auto', error_on_new = True)` | medium | 12 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.impute._base.MissingIndicator.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.impute._base.MissingIndicator.transform(self, X)` | complex | 40 | 抛异常, 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.impute._base.MissingIndicator.fit_transform(self, X, y = None)` | medium | 24 | 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.impute._base.MissingIndicator.get_feature_names_out(self, input_features = None)` | medium | 30 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.impute._base.MissingIndicator.__sklearn_tags__(self)` | simple | 7 | 魔术方法 |

---

## 🔹 `SimpleImputer`

**完全限定名**: `sklearn.impute._base.SimpleImputer`

**文件路径**: `sklearn/impute/_base.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, missing_values = np.nan, strategy = 'mean...` | `None` | `sklearn.impute._base.SimpleImputer.__init__(self, missing_values = np.nan, strategy = 'mean', fill_value = None, copy = True, add_indicator = False, keep_empty_features = False)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.impute._base.SimpleImputer.fit(self, X, y = None)` | complex | 41 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.impute._base.SimpleImputer.transform(self, X)` | complex | 88 | 抛异常, 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.impute._base.SimpleImputer.inverse_transform(self, X)` | complex | 61 | 抛异常, 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.impute._base.SimpleImputer.__sklearn_tags__(self)` | simple | 7 | 魔术方法 |
| 6 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.impute._base.SimpleImputer.get_feature_names_out(self, input_features = None)` | medium | 25 | 有逻辑 |

---

## 🔹 `IterativeImputer`

**完全限定名**: `sklearn.impute._iterative.IterativeImputer`

**文件路径**: `sklearn/impute/_iterative.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, missing_values = np.nan...` | `None` | `sklearn.impute._iterative.IterativeImputer.__init__(self, estimator = None, missing_values = np.nan, sample_posterior = False, max_iter = 10, tol = 0.001, n_nearest_features = None, initial_strategy = 'mean', fill_value = None, imputation_order = 'ascending', skip_complete = False, min_value = -np.inf, max_value = np.inf, verbose = 0, random_state = None, add_indicator = False, keep_empty_features = False)` | complex | 39 | 魔术方法 |
| 2 | `fit_transform` | instance | `self, X, y = None, **params` | `None` | `sklearn.impute._iterative.IterativeImputer.fit_transform(self, X, y = None, **params)` | complex | 151 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.impute._iterative.IterativeImputer.transform(self, X)` | complex | 53 | 有逻辑 |
| 4 | `fit` | instance | `self, X, y = None, **fit_params` | `None` | `sklearn.impute._iterative.IterativeImputer.fit(self, X, y = None, **fit_params)` | medium | 29 | 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.impute._iterative.IterativeImputer.get_feature_names_out(self, input_features = None)` | medium | 24 | 有逻辑 |
| 6 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.impute._iterative.IterativeImputer.get_metadata_routing(self)` | medium | 19 | - |

---

## 🔹 `KNNImputer`

**完全限定名**: `sklearn.impute._knn.KNNImputer`

**文件路径**: `sklearn/impute/_knn.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, missing_values = np.nan, n_neighbors = 5,...` | `None` | `sklearn.impute._knn.KNNImputer.__init__(self, missing_values = np.nan, n_neighbors = 5, weights = 'uniform', metric = 'nan_euclidean', copy = True, add_indicator = False, keep_empty_features = False)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.impute._knn.KNNImputer.fit(self, X, y = None)` | complex | 39 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.impute._knn.KNNImputer.transform(self, X)` | complex | 133 | 有逻辑 |
| 4 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.impute._knn.KNNImputer.get_feature_names_out(self, input_features = None)` | medium | 24 | 有逻辑 |

---

## 🔹 `DecisionBoundaryDisplay`

**完全限定名**: `sklearn.inspection._plot.decision_boundary.DecisionBoundaryDisplay`

**文件路径**: `sklearn/inspection/_plot/decision_boundary.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, xx0, xx1, response, multiclass_colors = N...` | `None` | `sklearn.inspection._plot.decision_boundary.DecisionBoundaryDisplay.__init__(self, xx0, xx1, response, multiclass_colors = None, xlabel = None, ylabel = None)` | simple | 9 | 魔术方法 |
| 2 | `plot` | instance | `self, plot_method = 'contourf', ax = None, xlab...` | `None` | `sklearn.inspection._plot.decision_boundary.DecisionBoundaryDisplay.plot(self, plot_method = 'contourf', ax = None, xlabel = None, ylabel = None, **kwargs)` | complex | 119 | 抛异常, 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, grid_resolution = 100, eps =...` | `None` | `sklearn.inspection._plot.decision_boundary.DecisionBoundaryDisplay.from_estimator(cls, estimator, X, grid_resolution = 100, eps = 1.0, plot_method = 'contourf', response_method = 'auto', class_of_interest = None, multiclass_colors = None, xlabel = None, ylabel = None, ax = None, **kwargs)` | complex | 268 | 抛异常, 有逻辑 |

---

## 🔹 `PartialDependenceDisplay`

**完全限定名**: `sklearn.inspection._plot.partial_dependence.PartialDependenceDisplay`

**文件路径**: `sklearn/inspection/_plot/partial_dependence.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, pd_results, features, feature_names, targ...` | `None` | `sklearn.inspection._plot.partial_dependence.PartialDependenceDisplay.__init__(self, pd_results, features, feature_names, target_idx, deciles, kind = 'average', subsample = 1000, random_state = None, is_categorical = None)` | medium | 22 | 魔术方法 |
| 2 | `from_estimator` | class | `cls, estimator, X, features, sample_weight = No...` | `None` | `sklearn.inspection._plot.partial_dependence.PartialDependenceDisplay.from_estimator(cls, estimator, X, features, sample_weight = None, categorical_features = None, feature_names = None, target = None, response_method = 'auto', n_cols = 3, grid_resolution = 100, percentiles = (0.05, 0.95), custom_values = None, method = 'auto', n_jobs = None, verbose = 0, line_kw = None, ice_lines_kw = None, pd_line_kw = None, contour_kw = None, ax = None, kind = 'average', centered = False, subsample = 1000, random_state = None)` | complex | 540 | 抛异常, 有逻辑 |
| 3 | `plot` | instance | `self, ax = None, n_cols = 3, line_kw = None, ic...` | `None` | `sklearn.inspection._plot.partial_dependence.PartialDependenceDisplay.plot(self, ax = None, n_cols = 3, line_kw = None, ice_lines_kw = None, pd_line_kw = None, contour_kw = None, bar_kw = None, heatmap_kw = None, pdp_lim = None, centered = False)` | complex | 358 | 抛异常, 有逻辑 |

---

## 🔹 `IsotonicRegression`

**完全限定名**: `sklearn.isotonic.IsotonicRegression`

**文件路径**: `sklearn/isotonic.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, y_min = None, y_max = None, increasing = ...` | `None` | `sklearn.isotonic.IsotonicRegression.__init__(self, y_min = None, y_max = None, increasing = True, out_of_bounds = 'nan')` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.isotonic.IsotonicRegression.fit(self, X, y, sample_weight = None)` | complex | 48 | 有逻辑 |
| 3 | `transform` | instance | `self, T` | `None` | `sklearn.isotonic.IsotonicRegression.transform(self, T)` | medium | 17 | - |
| 4 | `predict` | instance | `self, T` | `None` | `sklearn.isotonic.IsotonicRegression.predict(self, T)` | medium | 14 | - |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.isotonic.IsotonicRegression.get_feature_names_out(self, input_features = None)` | medium | 16 | 有逻辑 |
| 6 | `__getstate__` | instance | `self` | `None` | `sklearn.isotonic.IsotonicRegression.__getstate__(self)` | simple | 6 | 魔术方法 |
| 7 | `__setstate__` | instance | `self, state` | `None` | `sklearn.isotonic.IsotonicRegression.__setstate__(self, state)` | simple | 8 | 魔术方法, 有逻辑 |
| 8 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.isotonic.IsotonicRegression.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `AdditiveChi2Sampler`

**完全限定名**: `sklearn.kernel_approximation.AdditiveChi2Sampler`

**文件路径**: `sklearn/kernel_approximation.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, sample_steps = 2, sample_interval = None` | `None` | `sklearn.kernel_approximation.AdditiveChi2Sampler.__init__(self, sample_steps = 2, sample_interval = None)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.kernel_approximation.AdditiveChi2Sampler.fit(self, X, y = None)` | medium | 30 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.kernel_approximation.AdditiveChi2Sampler.transform(self, X)` | complex | 45 | 抛异常, 有逻辑 |
| 4 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.kernel_approximation.AdditiveChi2Sampler.get_feature_names_out(self, input_features = None)` | medium | 30 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.kernel_approximation.AdditiveChi2Sampler.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `Nystroem`

**完全限定名**: `sklearn.kernel_approximation.Nystroem`

**文件路径**: `sklearn/kernel_approximation.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = 'rbf', gamma = None, coef0 = Non...` | `None` | `sklearn.kernel_approximation.Nystroem.__init__(self, kernel = 'rbf', gamma = None, coef0 = None, degree = None, kernel_params = None, n_components = 100, random_state = None, n_jobs = None)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.kernel_approximation.Nystroem.fit(self, X, y = None)` | complex | 58 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.kernel_approximation.Nystroem.transform(self, X)` | medium | 29 | - |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.kernel_approximation.Nystroem.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `PolynomialCountSketch`

**完全限定名**: `sklearn.kernel_approximation.PolynomialCountSketch`

**文件路径**: `sklearn/kernel_approximation.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, gamma = 1.0, degree = 2, coef0 = 0, n_com...` | `None` | `sklearn.kernel_approximation.PolynomialCountSketch.__init__(self, gamma = 1.0, degree = 2, coef0 = 0, n_components = 100, random_state = None)` | simple | 8 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.kernel_approximation.PolynomialCountSketch.fit(self, X, y = None)` | medium | 35 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.kernel_approximation.PolynomialCountSketch.transform(self, X)` | complex | 62 | 抛异常, 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.kernel_approximation.PolynomialCountSketch.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `RBFSampler`

**完全限定名**: `sklearn.kernel_approximation.RBFSampler`

**文件路径**: `sklearn/kernel_approximation.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, gamma = 1.0, n_components = 100, random_s...` | `None` | `sklearn.kernel_approximation.RBFSampler.__init__(self, gamma = 1.0, n_components = 100, random_state = None)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.kernel_approximation.RBFSampler.fit(self, X, y = None)` | complex | 44 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.kernel_approximation.RBFSampler.transform(self, X)` | medium | 22 | - |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.kernel_approximation.RBFSampler.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `SkewedChi2Sampler`

**完全限定名**: `sklearn.kernel_approximation.SkewedChi2Sampler`

**文件路径**: `sklearn/kernel_approximation.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, skewedness = 1.0, n_components = 100, ran...` | `None` | `sklearn.kernel_approximation.SkewedChi2Sampler.__init__(self, skewedness = 1.0, n_components = 100, random_state = None)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.kernel_approximation.SkewedChi2Sampler.fit(self, X, y = None)` | medium | 36 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.kernel_approximation.SkewedChi2Sampler.transform(self, X)` | medium | 29 | 抛异常, 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.kernel_approximation.SkewedChi2Sampler.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `KernelRidge`

**完全限定名**: `sklearn.kernel_ridge.KernelRidge`

**文件路径**: `sklearn/kernel_ridge.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1, kernel = 'linear', gamma = Non...` | `None` | `sklearn.kernel_ridge.KernelRidge.__init__(self, alpha = 1, kernel = 'linear', gamma = None, degree = 3, coef0 = 1, kernel_params = None)` | medium | 16 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.kernel_ridge.KernelRidge.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.kernel_ridge.KernelRidge.fit(self, X, y, sample_weight = None)` | complex | 43 | 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.kernel_ridge.KernelRidge.predict(self, X)` | medium | 20 | 有逻辑 |

---

## 🔹 `LinearClassifierMixin`

**完全限定名**: `sklearn.linear_model._base.LinearClassifierMixin`

**文件路径**: `sklearn/linear_model/_base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `decision_function` | instance | `self, X` | `None` | `sklearn.linear_model._base.LinearClassifierMixin.decision_function(self, X)` | medium | 30 | 有逻辑 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.linear_model._base.LinearClassifierMixin.predict(self, X)` | medium | 22 | 有逻辑 |

---

## 🔹 `LinearModel`

**完全限定名**: `sklearn.linear_model._base.LinearModel`

**文件路径**: `sklearn/linear_model/_base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._base.LinearModel.fit(self, X, y)` | simple | 2 | 抽象方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.linear_model._base.LinearModel.predict(self, X)` | medium | 15 | - |

---

## 🔹 `LinearRegression`

**完全限定名**: `sklearn.linear_model._base.LinearRegression`

**文件路径**: `sklearn/linear_model/_base.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fit_intercept = True, copy_X = True, tol ...` | `None` | `sklearn.linear_model._base.LinearRegression.__init__(self, fit_intercept = True, copy_X = True, tol = 1e-06, n_jobs = None, positive = False)` | medium | 14 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._base.LinearRegression.fit(self, X, y, sample_weight = None)` | complex | 107 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._base.LinearRegression.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SparseCoefMixin`

**完全限定名**: `sklearn.linear_model._base.SparseCoefMixin`

**文件路径**: `sklearn/linear_model/_base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `densify` | instance | `self` | `None` | `sklearn.linear_model._base.SparseCoefMixin.densify(self)` | medium | 19 | 有逻辑 |
| 2 | `sparsify` | instance | `self` | `None` | `sklearn.linear_model._base.SparseCoefMixin.sparsify(self)` | medium | 30 | 有逻辑 |

---

## 🔹 `ARDRegression`

**完全限定名**: `sklearn.linear_model._bayes.ARDRegression`

**文件路径**: `sklearn/linear_model/_bayes.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, max_iter = 300, tol = 0.001, alpha_1 = 1e...` | `None` | `sklearn.linear_model._bayes.ARDRegression.__init__(self, max_iter = 300, tol = 0.001, alpha_1 = 1e-06, alpha_2 = 1e-06, lambda_1 = 1e-06, lambda_2 = 1e-06, compute_score = False, threshold_lambda = 10000.0, fit_intercept = True, copy_X = True, verbose = False)` | medium | 26 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._bayes.ARDRegression.fit(self, X, y)` | complex | 124 | 有逻辑 |
| 3 | `predict` | instance | `self, X, return_std = False` | `None` | `sklearn.linear_model._bayes.ARDRegression.predict(self, X, return_std = False)` | medium | 31 | 有逻辑 |

---

## 🔹 `BayesianRidge`

**完全限定名**: `sklearn.linear_model._bayes.BayesianRidge`

**文件路径**: `sklearn/linear_model/_bayes.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, max_iter = 300, tol = 0.001, alpha_1 = 1e...` | `None` | `sklearn.linear_model._bayes.BayesianRidge.__init__(self, max_iter = 300, tol = 0.001, alpha_1 = 1e-06, alpha_2 = 1e-06, lambda_1 = 1e-06, lambda_2 = 1e-06, alpha_init = None, lambda_init = None, compute_score = False, fit_intercept = True, copy_X = True, verbose = False)` | medium | 28 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._bayes.BayesianRidge.fit(self, X, y, sample_weight = None)` | complex | 156 | 有逻辑 |
| 3 | `predict` | instance | `self, X, return_std = False` | `None` | `sklearn.linear_model._bayes.BayesianRidge.predict(self, X, return_std = False)` | medium | 29 | 有逻辑 |

---

## 🔹 `ElasticNet`

**完全限定名**: `sklearn.linear_model._coordinate_descent.ElasticNet`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, l1_ratio = 0.5, fit_intercep...` | `None` | `sklearn.linear_model._coordinate_descent.ElasticNet.__init__(self, alpha = 1.0, l1_ratio = 0.5, fit_intercept = True, precompute = False, max_iter = 1000, copy_X = True, tol = 0.0001, warm_start = False, positive = False, random_state = None, selection = 'cyclic')` | medium | 26 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, check_input =...` | `None` | `sklearn.linear_model._coordinate_descent.ElasticNet.fit(self, X, y, sample_weight = None, check_input = True)` | complex | 200 | 抛异常, 有逻辑 |
| 3 | `sparse_coef_` | property | `self` | `None` | `sklearn.linear_model._coordinate_descent.ElasticNet.sparse_coef_(self)` | simple | 3 | - |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._coordinate_descent.ElasticNet.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `ElasticNetCV`

**完全限定名**: `sklearn.linear_model._coordinate_descent.ElasticNetCV`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, l1_ratio = 0.5, eps = 0.001, n_alphas = '...` | `None` | `sklearn.linear_model._coordinate_descent.ElasticNetCV.__init__(self, l1_ratio = 0.5, eps = 0.001, n_alphas = 'deprecated', alphas = 'warn', fit_intercept = True, precompute = 'auto', max_iter = 1000, tol = 0.0001, cv = None, copy_X = True, verbose = 0, n_jobs = None, positive = False, random_state = None, selection = 'cyclic')` | complex | 34 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **params` | `None` | `sklearn.linear_model._coordinate_descent.ElasticNetCV.fit(self, X, y, sample_weight = None, **params)` | complex | 39 | 有逻辑 |

---

## 🔹 `Lasso`

**完全限定名**: `sklearn.linear_model._coordinate_descent.Lasso`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, precom...` | `None` | `sklearn.linear_model._coordinate_descent.Lasso.__init__(self, alpha = 1.0, fit_intercept = True, precompute = False, copy_X = True, max_iter = 1000, tol = 0.0001, warm_start = False, positive = False, random_state = None, selection = 'cyclic')` | medium | 27 | 魔术方法 |

---

## 🔹 `LassoCV`

**完全限定名**: `sklearn.linear_model._coordinate_descent.LassoCV`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, eps = 0.001, n_alphas = 'deprecated', alp...` | `None` | `sklearn.linear_model._coordinate_descent.LassoCV.__init__(self, eps = 0.001, n_alphas = 'deprecated', alphas = 'warn', fit_intercept = True, precompute = 'auto', max_iter = 1000, tol = 0.0001, copy_X = True, cv = None, verbose = False, n_jobs = None, positive = False, random_state = None, selection = 'cyclic')` | complex | 34 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **params` | `None` | `sklearn.linear_model._coordinate_descent.LassoCV.fit(self, X, y, sample_weight = None, **params)` | complex | 39 | 有逻辑 |

---

## 🔹 `LinearModelCV`

**完全限定名**: `sklearn.linear_model._coordinate_descent.LinearModelCV`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, eps = 0.001, n_alphas = 'deprecated', alp...` | `None` | `sklearn.linear_model._coordinate_descent.LinearModelCV.__init__(self, eps = 0.001, n_alphas = 'deprecated', alphas = 'warn', fit_intercept = True, precompute = 'auto', max_iter = 1000, tol = 0.0001, copy_X = True, cv = None, verbose = False, n_jobs = None, positive = False, random_state = None, selection = 'cyclic')` | complex | 31 | 魔术方法, 抽象方法 |
| 2 | `path` | static | `X, y, **kwargs` | `None` | `sklearn.linear_model._coordinate_descent.LinearModelCV.path(X, y, **kwargs)` | simple | 2 | 抽象方法 |
| 3 | `fit` | instance | `self, X, y, sample_weight = None, **params` | `None` | `sklearn.linear_model._coordinate_descent.LinearModelCV.fit(self, X, y, sample_weight = None, **params)` | complex | 320 | 抛异常, 有逻辑 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.linear_model._coordinate_descent.LinearModelCV.get_metadata_routing(self)` | medium | 23 | - |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._coordinate_descent.LinearModelCV.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `MultiTaskElasticNet`

**完全限定名**: `sklearn.linear_model._coordinate_descent.MultiTaskElasticNet`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, l1_ratio = 0.5, fit_intercep...` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskElasticNet.__init__(self, alpha = 1.0, l1_ratio = 0.5, fit_intercept = True, copy_X = True, max_iter = 1000, tol = 0.0001, warm_start = False, random_state = None, selection = 'cyclic')` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskElasticNet.fit(self, X, y)` | complex | 89 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskElasticNet.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `MultiTaskElasticNetCV`

**完全限定名**: `sklearn.linear_model._coordinate_descent.MultiTaskElasticNetCV`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, l1_ratio = 0.5, eps = 0.001, n_alphas = '...` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskElasticNetCV.__init__(self, l1_ratio = 0.5, eps = 0.001, n_alphas = 'deprecated', alphas = 'warn', fit_intercept = True, max_iter = 1000, tol = 0.0001, cv = None, copy_X = True, verbose = 0, n_jobs = None, random_state = None, selection = 'cyclic')` | medium | 30 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskElasticNetCV.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y, **params` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskElasticNetCV.fit(self, X, y, **params)` | medium | 28 | 有逻辑 |

---

## 🔹 `MultiTaskLasso`

**完全限定名**: `sklearn.linear_model._coordinate_descent.MultiTaskLasso`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, copy_X...` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskLasso.__init__(self, alpha = 1.0, fit_intercept = True, copy_X = True, max_iter = 1000, tol = 0.0001, warm_start = False, random_state = None, selection = 'cyclic')` | medium | 21 | 魔术方法 |

---

## 🔹 `MultiTaskLassoCV`

**完全限定名**: `sklearn.linear_model._coordinate_descent.MultiTaskLassoCV`

**文件路径**: `sklearn/linear_model/_coordinate_descent.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, eps = 0.001, n_alphas = 'deprecated', alp...` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskLassoCV.__init__(self, eps = 0.001, n_alphas = 'deprecated', alphas = 'warn', fit_intercept = True, max_iter = 1000, tol = 0.0001, copy_X = True, cv = None, verbose = False, n_jobs = None, random_state = None, selection = 'cyclic')` | medium | 30 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskLassoCV.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y, **params` | `None` | `sklearn.linear_model._coordinate_descent.MultiTaskLassoCV.fit(self, X, y, **params)` | medium | 28 | 有逻辑 |

---

## 🔹 `NewtonCholeskySolver`

**完全限定名**: `sklearn.linear_model._glm._newton_solver.NewtonCholeskySolver`

**文件路径**: `sklearn/linear_model/_glm/_newton_solver.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `setup` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonCholeskySolver.setup(self, X, y, sample_weight)` | medium | 32 | 有逻辑 |
| 2 | `update_gradient_hessian` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonCholeskySolver.update_gradient_hessian(self, X, y, sample_weight)` | medium | 12 | - |
| 3 | `inner_solve` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonCholeskySolver.inner_solve(self, X, y, sample_weight)` | complex | 119 | 有逻辑 |
| 4 | `finalize` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonCholeskySolver.finalize(self, X, y, sample_weight)` | simple | 13 | 有逻辑 |

---

## 🔹 `NewtonSolver`

**完全限定名**: `sklearn.linear_model._glm._newton_solver.NewtonSolver`

**文件路径**: `sklearn/linear_model/_glm/_newton_solver.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, coef, linear_loss = LinearModelLoss(base_...` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.__init__(self, coef, linear_loss = LinearModelLoss(base_loss=HalfSquaredError(), fit_intercept=True), l2_reg_strength = 0.0, tol = 0.0001, max_iter = 100, n_threads = 1, verbose = 0)` | medium | 18 | 魔术方法 |
| 2 | `setup` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.setup(self, X, y, sample_weight)` | medium | 19 | - |
| 3 | `update_gradient_hessian` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.update_gradient_hessian(self, X, y, sample_weight)` | simple | 2 | 抽象方法 |
| 4 | `inner_solve` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.inner_solve(self, X, y, sample_weight)` | simple | 7 | 抽象方法 |
| 5 | `fallback_lbfgs_solve` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.fallback_lbfgs_solve(self, X, y, sample_weight)` | medium | 28 | - |
| 6 | `line_search` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.line_search(self, X, y, sample_weight)` | complex | 107 | 有逻辑 |
| 7 | `check_convergence` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.check_convergence(self, X, y, sample_weight)` | medium | 45 | 有逻辑 |
| 8 | `finalize` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.finalize(self, X, y, sample_weight)` | simple | 6 | - |
| 9 | `solve` | instance | `self, X, y, sample_weight` | `None` | `sklearn.linear_model._glm._newton_solver.NewtonSolver.solve(self, X, y, sample_weight)` | complex | 82 | 有逻辑 |

---

## 🔹 `GammaRegressor`

**完全限定名**: `sklearn.linear_model._glm.glm.GammaRegressor`

**文件路径**: `sklearn/linear_model/_glm/glm.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, solver...` | `None` | `sklearn.linear_model._glm.glm.GammaRegressor.__init__(self, alpha = 1.0, fit_intercept = True, solver = 'lbfgs', max_iter = 100, tol = 0.0001, warm_start = False, verbose = 0)` | medium | 20 | 魔术方法 |

---

## 🔹 `PoissonRegressor`

**完全限定名**: `sklearn.linear_model._glm.glm.PoissonRegressor`

**文件路径**: `sklearn/linear_model/_glm/glm.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, solver...` | `None` | `sklearn.linear_model._glm.glm.PoissonRegressor.__init__(self, alpha = 1.0, fit_intercept = True, solver = 'lbfgs', max_iter = 100, tol = 0.0001, warm_start = False, verbose = 0)` | medium | 20 | 魔术方法 |

---

## 🔹 `TweedieRegressor`

**完全限定名**: `sklearn.linear_model._glm.glm.TweedieRegressor`

**文件路径**: `sklearn/linear_model/_glm/glm.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, power = 0.0, alpha = 1.0, fit_intercept =...` | `None` | `sklearn.linear_model._glm.glm.TweedieRegressor.__init__(self, power = 0.0, alpha = 1.0, fit_intercept = True, link = 'auto', solver = 'lbfgs', max_iter = 100, tol = 0.0001, warm_start = False, verbose = 0)` | medium | 24 | 魔术方法 |

---

## 🔹 `HuberRegressor`

**完全限定名**: `sklearn.linear_model._huber.HuberRegressor`

**文件路径**: `sklearn/linear_model/_huber.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, epsilon = 1.35, max_iter = 100, alpha = 0...` | `None` | `sklearn.linear_model._huber.HuberRegressor.__init__(self, epsilon = 1.35, max_iter = 100, alpha = 0.0001, warm_start = False, fit_intercept = True, tol = 1e-05)` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._huber.HuberRegressor.fit(self, X, y, sample_weight = None)` | complex | 81 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._huber.HuberRegressor.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `Lars`

**完全限定名**: `sklearn.linear_model._least_angle.Lars`

**文件路径**: `sklearn/linear_model/_least_angle.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fit_intercept = True, verbose = False, pr...` | `None` | `sklearn.linear_model._least_angle.Lars.__init__(self, fit_intercept = True, verbose = False, precompute = 'auto', n_nonzero_coefs = 500, eps = np.finfo(float).eps, copy_X = True, fit_path = True, jitter = None, random_state = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, Xy = None` | `None` | `sklearn.linear_model._least_angle.Lars.fit(self, X, y, Xy = None)` | complex | 48 | 有逻辑 |

---

## 🔹 `LarsCV`

**完全限定名**: `sklearn.linear_model._least_angle.LarsCV`

**文件路径**: `sklearn/linear_model/_least_angle.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fit_intercept = True, verbose = False, ma...` | `None` | `sklearn.linear_model._least_angle.LarsCV.__init__(self, fit_intercept = True, verbose = False, max_iter = 500, precompute = 'auto', cv = None, max_n_alphas = 1000, n_jobs = None, eps = np.finfo(float).eps, copy_X = True)` | medium | 26 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._least_angle.LarsCV.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y, **params` | `None` | `sklearn.linear_model._least_angle.LarsCV.fit(self, X, y, **params)` | complex | 111 | 有逻辑 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.linear_model._least_angle.LarsCV.get_metadata_routing(self)` | medium | 19 | - |

---

## 🔹 `LassoLars`

**完全限定名**: `sklearn.linear_model._least_angle.LassoLars`

**文件路径**: `sklearn/linear_model/_least_angle.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, verbos...` | `None` | `sklearn.linear_model._least_angle.LassoLars.__init__(self, alpha = 1.0, fit_intercept = True, verbose = False, precompute = 'auto', max_iter = 500, eps = np.finfo(float).eps, copy_X = True, fit_path = True, positive = False, jitter = None, random_state = None)` | medium | 26 | 魔术方法 |

---

## 🔹 `LassoLarsCV`

**完全限定名**: `sklearn.linear_model._least_angle.LassoLarsCV`

**文件路径**: `sklearn/linear_model/_least_angle.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fit_intercept = True, verbose = False, ma...` | `None` | `sklearn.linear_model._least_angle.LassoLarsCV.__init__(self, fit_intercept = True, verbose = False, max_iter = 500, precompute = 'auto', cv = None, max_n_alphas = 1000, n_jobs = None, eps = np.finfo(float).eps, copy_X = True, positive = False)` | medium | 24 | 魔术方法 |

---

## 🔹 `LassoLarsIC`

**完全限定名**: `sklearn.linear_model._least_angle.LassoLarsIC`

**文件路径**: `sklearn/linear_model/_least_angle.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, criterion = 'aic', fit_intercept = True, ...` | `None` | `sklearn.linear_model._least_angle.LassoLarsIC.__init__(self, criterion = 'aic', fit_intercept = True, verbose = False, precompute = 'auto', max_iter = 500, eps = np.finfo(float).eps, copy_X = True, positive = False, noise_variance = None)` | medium | 23 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._least_angle.LassoLarsIC.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y, copy_X = None` | `None` | `sklearn.linear_model._least_angle.LassoLarsIC.fit(self, X, y, copy_X = None)` | complex | 89 | 抛异常, 有逻辑 |

---

## 🔹 `LinearModelLoss`

**完全限定名**: `sklearn.linear_model._linear_loss.LinearModelLoss`

**文件路径**: `sklearn/linear_model/_linear_loss.py`

**公共方法数**: 10

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, base_loss, fit_intercept` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.__init__(self, base_loss, fit_intercept)` | simple | 3 | 魔术方法 |
| 2 | `init_zero_coef` | instance | `self, X, dtype = None` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.init_zero_coef(self, X, dtype = None)` | medium | 27 | 有逻辑 |
| 3 | `weight_intercept` | instance | `self, coef` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.weight_intercept(self, coef)` | complex | 38 | 有逻辑 |
| 4 | `weight_intercept_raw` | instance | `self, coef, X` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.weight_intercept_raw(self, coef, X)` | medium | 31 | 有逻辑 |
| 5 | `l2_penalty` | instance | `self, weights, l2_reg_strength` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.l2_penalty(self, weights, l2_reg_strength)` | simple | 4 | 有逻辑 |
| 6 | `loss` | instance | `self, coef, X, y, sample_weight = None, l2_reg_...` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.loss(self, coef, X, y, sample_weight = None, l2_reg_strength = 0.0, n_threads = 1, raw_prediction = None)` | complex | 53 | 有逻辑 |
| 7 | `loss_gradient` | instance | `self, coef, X, y, sample_weight = None, l2_reg_...` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.loss_gradient(self, coef, X, y, sample_weight = None, l2_reg_strength = 0.0, n_threads = 1, raw_prediction = None)` | complex | 77 | 有逻辑 |
| 8 | `gradient` | instance | `self, coef, X, y, sample_weight = None, l2_reg_...` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.gradient(self, coef, X, y, sample_weight = None, l2_reg_strength = 0.0, n_threads = 1, raw_prediction = None)` | complex | 72 | 有逻辑 |
| 9 | `gradient_hessian` | instance | `self, coef, X, y, sample_weight = None, l2_reg_...` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.gradient_hessian(self, coef, X, y, sample_weight = None, l2_reg_strength = 0.0, n_threads = 1, gradient_out = None, hessian_out = None, raw_prediction = None)` | complex | 256 | 抛异常, 有逻辑 |
| 10 | `gradient_hessian_product` | instance | `self, coef, X, y, sample_weight = None, l2_reg_...` | `None` | `sklearn.linear_model._linear_loss.LinearModelLoss.gradient_hessian_product(self, coef, X, y, sample_weight = None, l2_reg_strength = 0.0, n_threads = 1)` | complex | 152 | 有逻辑 |

---

## 🔹 `OrthogonalMatchingPursuit`

**完全限定名**: `sklearn.linear_model._omp.OrthogonalMatchingPursuit`

**文件路径**: `sklearn/linear_model/_omp.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_nonzero_coefs = None, tol = None, fit_i...` | `None` | `sklearn.linear_model._omp.OrthogonalMatchingPursuit.__init__(self, n_nonzero_coefs = None, tol = None, fit_intercept = True, precompute = 'auto')` | medium | 12 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._omp.OrthogonalMatchingPursuit.fit(self, X, y)` | complex | 69 | 有逻辑 |

---

## 🔹 `OrthogonalMatchingPursuitCV`

**完全限定名**: `sklearn.linear_model._omp.OrthogonalMatchingPursuitCV`

**文件路径**: `sklearn/linear_model/_omp.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, copy = True, fit_intercept = True, max_it...` | `None` | `sklearn.linear_model._omp.OrthogonalMatchingPursuitCV.__init__(self, copy = True, fit_intercept = True, max_iter = None, cv = None, n_jobs = None, verbose = False)` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.linear_model._omp.OrthogonalMatchingPursuitCV.fit(self, X, y, **fit_params)` | complex | 70 | 有逻辑 |
| 3 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.linear_model._omp.OrthogonalMatchingPursuitCV.get_metadata_routing(self)` | medium | 20 | - |

---

## 🔹 `PassiveAggressiveClassifier`

**完全限定名**: `sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier`

**文件路径**: `sklearn/linear_model/_passive_aggressive.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, C = 1.0, fit_intercept = True, max_iter =...` | `None` | `sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier.__init__(self, C = 1.0, fit_intercept = True, max_iter = 1000, tol = 0.001, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, shuffle = True, verbose = 0, loss = 'hinge', n_jobs = None, random_state = None, warm_start = False, class_weight = None, average = False)` | complex | 39 | 魔术方法 |
| 2 | `partial_fit` | instance | `self, X, y, classes = None` | `None` | `sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier.partial_fit(self, X, y, classes = None)` | complex | 55 | 抛异常, 有逻辑 |
| 3 | `fit` | instance | `self, X, y, coef_init = None, intercept_init = ...` | `None` | `sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier.fit(self, X, y, coef_init = None, intercept_init = None)` | medium | 34 | 有逻辑 |

---

## 🔹 `PassiveAggressiveRegressor`

**完全限定名**: `sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor`

**文件路径**: `sklearn/linear_model/_passive_aggressive.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, C = 1.0, fit_intercept = True, max_iter =...` | `None` | `sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor.__init__(self, C = 1.0, fit_intercept = True, max_iter = 1000, tol = 0.001, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, shuffle = True, verbose = 0, loss = 'epsilon_insensitive', epsilon = DEFAULT_EPSILON, random_state = None, warm_start = False, average = False)` | complex | 37 | 魔术方法 |
| 2 | `partial_fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor.partial_fit(self, X, y)` | medium | 31 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y, coef_init = None, intercept_init = ...` | `None` | `sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor.fit(self, X, y, coef_init = None, intercept_init = None)` | medium | 34 | 有逻辑 |

---

## 🔹 `Perceptron`

**完全限定名**: `sklearn.linear_model._perceptron.Perceptron`

**文件路径**: `sklearn/linear_model/_perceptron.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, penalty = None, alpha = 0.0001, l1_ratio ...` | `None` | `sklearn.linear_model._perceptron.Perceptron.__init__(self, penalty = None, alpha = 0.0001, l1_ratio = 0.15, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, eta0 = 1.0, n_jobs = None, random_state = 0, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, class_weight = None, warm_start = False)` | complex | 41 | 魔术方法 |

---

## 🔹 `QuantileRegressor`

**完全限定名**: `sklearn.linear_model._quantile.QuantileRegressor`

**文件路径**: `sklearn/linear_model/_quantile.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, quantile = 0.5, alpha = 1.0, fit_intercep...` | `None` | `sklearn.linear_model._quantile.QuantileRegressor.__init__(self, quantile = 0.5, alpha = 1.0, fit_intercept = True, solver = 'highs', solver_options = None)` | medium | 14 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._quantile.QuantileRegressor.fit(self, X, y, sample_weight = None)` | complex | 154 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._quantile.QuantileRegressor.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `RANSACRegressor`

**完全限定名**: `sklearn.linear_model._ransac.RANSACRegressor`

**文件路径**: `sklearn/linear_model/_ransac.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, min_samples = None, res...` | `None` | `sklearn.linear_model._ransac.RANSACRegressor.__init__(self, estimator = None, min_samples = None, residual_threshold = None, is_data_valid = None, is_model_valid = None, max_trials = 100, max_skips = np.inf, stop_n_inliers = np.inf, stop_score = np.inf, stop_probability = 0.99, loss = 'absolute_error', random_state = None)` | medium | 28 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **fit_params` | `None` | `sklearn.linear_model._ransac.RANSACRegressor.fit(self, X, y, sample_weight = None, **fit_params)` | complex | 282 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X, **params` | `None` | `sklearn.linear_model._ransac.RANSACRegressor.predict(self, X, **params)` | complex | 45 | 有逻辑 |
| 4 | `score` | instance | `self, X, y, **params` | `None` | `sklearn.linear_model._ransac.RANSACRegressor.score(self, X, y, **params)` | complex | 45 | 有逻辑 |
| 5 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.linear_model._ransac.RANSACRegressor.get_metadata_routing(self)` | medium | 23 | - |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._ransac.RANSACRegressor.__sklearn_tags__(self)` | simple | 7 | 魔术方法, 有逻辑 |

---

## 🔹 `Ridge`

**完全限定名**: `sklearn.linear_model._ridge.Ridge`

**文件路径**: `sklearn/linear_model/_ridge.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, copy_X...` | `None` | `sklearn.linear_model._ridge.Ridge.__init__(self, alpha = 1.0, fit_intercept = True, copy_X = True, max_iter = None, tol = 0.0001, solver = 'auto', positive = False, random_state = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._ridge.Ridge.fit(self, X, y, sample_weight = None)` | medium | 33 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._ridge.Ridge.__sklearn_tags__(self)` | simple | 7 | 魔术方法 |

---

## 🔹 `RidgeCV`

**完全限定名**: `sklearn.linear_model._ridge.RidgeCV`

**文件路径**: `sklearn/linear_model/_ridge.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, y, sample_weight = None, **params` | `None` | `sklearn.linear_model._ridge.RidgeCV.fit(self, X, y, sample_weight = None, **params)` | complex | 41 | 有逻辑 |

---

## 🔹 `RidgeClassifier`

**完全限定名**: `sklearn.linear_model._ridge.RidgeClassifier`

**文件路径**: `sklearn/linear_model/_ridge.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, fit_intercept = True, copy_X...` | `None` | `sklearn.linear_model._ridge.RidgeClassifier.__init__(self, alpha = 1.0, fit_intercept = True, copy_X = True, max_iter = None, tol = 0.0001, class_weight = None, solver = 'auto', positive = False, random_state = None)` | medium | 24 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._ridge.RidgeClassifier.fit(self, X, y, sample_weight = None)` | medium | 27 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._ridge.RidgeClassifier.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `RidgeClassifierCV`

**完全限定名**: `sklearn.linear_model._ridge.RidgeClassifierCV`

**文件路径**: `sklearn/linear_model/_ridge.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alphas = (0.1, 1.0, 10.0), fit_intercept ...` | `None` | `sklearn.linear_model._ridge.RidgeClassifierCV.__init__(self, alphas = (0.1, 1.0, 10.0), fit_intercept = True, scoring = None, cv = None, class_weight = None, store_cv_results = False)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **params` | `None` | `sklearn.linear_model._ridge.RidgeClassifierCV.fit(self, X, y, sample_weight = None, **params)` | medium | 45 | 有逻辑 |

---

## 🔹 `BaseSGD`

**完全限定名**: `sklearn.linear_model._stochastic_gradient.BaseSGD`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss, penalty = 'l2', alpha = 0.0001, l1_...` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGD.__init__(self, loss, penalty = 'l2', alpha = 0.0001, l1_ratio = 0.15, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, epsilon = 0.1, random_state = None, learning_rate = 'optimal', eta0 = 0.01, power_t = 0.5, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, warm_start = False, average = False)` | complex | 42 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGD.fit(self, X, y)` | simple | 2 | 抽象方法 |

---

## 🔹 `BaseSGDClassifier`

**完全限定名**: `sklearn.linear_model._stochastic_gradient.BaseSGDClassifier`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'hinge', penalty = 'l2', alpha = 0...` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDClassifier.__init__(self, loss = 'hinge', penalty = 'l2', alpha = 0.0001, l1_ratio = 0.15, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, epsilon = DEFAULT_EPSILON, n_jobs = None, random_state = None, learning_rate = 'optimal', eta0 = 0.01, power_t = 0.5, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, class_weight = None, warm_start = False, average = False)` | complex | 48 | 魔术方法, 抽象方法 |
| 2 | `partial_fit` | instance | `self, X, y, classes = None, sample_weight = None` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDClassifier.partial_fit(self, X, y, classes = None, sample_weight = None)` | complex | 61 | 抛异常, 有逻辑 |
| 3 | `fit` | instance | `self, X, y, coef_init = None, intercept_init = ...` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDClassifier.fit(self, X, y, coef_init = None, intercept_init = None, sample_weight = None)` | complex | 40 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDClassifier.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `BaseSGDRegressor`

**完全限定名**: `sklearn.linear_model._stochastic_gradient.BaseSGDRegressor`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'squared_error', penalty = 'l2', a...` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDRegressor.__init__(self, loss = 'squared_error', penalty = 'l2', alpha = 0.0001, l1_ratio = 0.15, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, epsilon = DEFAULT_EPSILON, random_state = None, learning_rate = 'invscaling', eta0 = 0.01, power_t = 0.25, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, warm_start = False, average = False)` | complex | 44 | 魔术方法, 抽象方法 |
| 2 | `partial_fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDRegressor.partial_fit(self, X, y, sample_weight = None)` | complex | 39 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y, coef_init = None, intercept_init = ...` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDRegressor.fit(self, X, y, coef_init = None, intercept_init = None, sample_weight = None)` | medium | 37 | 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDRegressor.predict(self, X)` | medium | 14 | - |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._stochastic_gradient.BaseSGDRegressor.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SGDClassifier`

**完全限定名**: `sklearn.linear_model._stochastic_gradient.SGDClassifier`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'hinge', penalty = 'l2', alpha = 0...` | `None` | `sklearn.linear_model._stochastic_gradient.SGDClassifier.__init__(self, loss = 'hinge', penalty = 'l2', alpha = 0.0001, l1_ratio = 0.15, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, epsilon = DEFAULT_EPSILON, n_jobs = None, random_state = None, learning_rate = 'optimal', eta0 = 0.01, power_t = 0.5, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, class_weight = None, warm_start = False, average = False)` | complex | 48 | 魔术方法 |
| 2 | `predict_proba` | instance | `self, X` | `None` | `sklearn.linear_model._stochastic_gradient.SGDClassifier.predict_proba(self, X)` | complex | 79 | 抛异常, 有逻辑 |
| 3 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.linear_model._stochastic_gradient.SGDClassifier.predict_log_proba(self, X)` | medium | 23 | 有逻辑 |

---

## 🔹 `SGDOneClassSVM`

**完全限定名**: `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, nu = 0.5, fit_intercept = True, max_iter ...` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.__init__(self, nu = 0.5, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, random_state = None, learning_rate = 'optimal', eta0 = 0.01, power_t = 0.5, warm_start = False, average = False)` | complex | 36 | 魔术方法 |
| 2 | `partial_fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.partial_fit(self, X, y = None, sample_weight = None)` | medium | 33 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None, coef_init = None, offset_ini...` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.fit(self, X, y = None, coef_init = None, offset_init = None, sample_weight = None)` | complex | 46 | 有逻辑 |
| 4 | `decision_function` | instance | `self, X` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.decision_function(self, X)` | medium | 23 | 有逻辑 |
| 5 | `score_samples` | instance | `self, X` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.score_samples(self, X)` | medium | 15 | - |
| 6 | `predict` | instance | `self, X` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.predict(self, X)` | medium | 16 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.linear_model._stochastic_gradient.SGDOneClassSVM.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `SGDRegressor`

**完全限定名**: `sklearn.linear_model._stochastic_gradient.SGDRegressor`

**文件路径**: `sklearn/linear_model/_stochastic_gradient.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'squared_error', penalty = 'l2', a...` | `None` | `sklearn.linear_model._stochastic_gradient.SGDRegressor.__init__(self, loss = 'squared_error', penalty = 'l2', alpha = 0.0001, l1_ratio = 0.15, fit_intercept = True, max_iter = 1000, tol = 0.001, shuffle = True, verbose = 0, epsilon = DEFAULT_EPSILON, random_state = None, learning_rate = 'invscaling', eta0 = 0.01, power_t = 0.25, early_stopping = False, validation_fraction = 0.1, n_iter_no_change = 5, warm_start = False, average = False)` | complex | 44 | 魔术方法 |

---

## 🔹 `TheilSenRegressor`

**完全限定名**: `sklearn.linear_model._theil_sen.TheilSenRegressor`

**文件路径**: `sklearn/linear_model/_theil_sen.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fit_intercept = True, max_subpopulation =...` | `None` | `sklearn.linear_model._theil_sen.TheilSenRegressor.__init__(self, fit_intercept = True, max_subpopulation = 10000.0, n_subsamples = None, max_iter = 300, tol = 0.001, random_state = None, n_jobs = None, verbose = False)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.linear_model._theil_sen.TheilSenRegressor.fit(self, X, y)` | complex | 58 | 有逻辑 |

---

## 🔹 `ClassicalMDS`

**完全限定名**: `sklearn.manifold._classical_mds.ClassicalMDS`

**文件路径**: `sklearn/manifold/_classical_mds.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, metric = 'euclidean', m...` | `None` | `sklearn.manifold._classical_mds.ClassicalMDS.__init__(self, n_components = 2, metric = 'euclidean', metric_params = None)` | simple | 10 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.manifold._classical_mds.ClassicalMDS.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.manifold._classical_mds.ClassicalMDS.fit(self, X, y = None)` | medium | 21 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.manifold._classical_mds.ClassicalMDS.fit_transform(self, X, y = None)` | complex | 56 | 有逻辑 |

---

## 🔹 `Isomap`

**完全限定名**: `sklearn.manifold._isomap.Isomap`

**文件路径**: `sklearn/manifold/_isomap.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 5, radius = None, n_compone...` | `None` | `sklearn.manifold._isomap.Isomap.__init__(self, n_neighbors = 5, radius = None, n_components = 2, eigen_solver = 'auto', tol = 0, max_iter = None, path_method = 'auto', neighbors_algorithm = 'auto', n_jobs = None, metric = 'minkowski', p = 2, metric_params = None)` | medium | 28 | 魔术方法 |
| 2 | `reconstruction_error` | instance | `self` | `None` | `sklearn.manifold._isomap.Isomap.reconstruction_error(self)` | medium | 24 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.manifold._isomap.Isomap.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.manifold._isomap.Isomap.fit_transform(self, X, y = None)` | medium | 19 | 有逻辑 |
| 5 | `transform` | instance | `self, X` | `None` | `sklearn.manifold._isomap.Isomap.transform(self, X)` | complex | 50 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.manifold._isomap.Isomap.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `LocallyLinearEmbedding`

**完全限定名**: `sklearn.manifold._locally_linear.LocallyLinearEmbedding`

**文件路径**: `sklearn/manifold/_locally_linear.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 5, n_components = 2, reg = ...` | `None` | `sklearn.manifold._locally_linear.LocallyLinearEmbedding.__init__(self, n_neighbors = 5, n_components = 2, reg = 0.001, eigen_solver = 'auto', tol = 1e-06, max_iter = 100, method = 'standard', hessian_tol = 0.0001, modified_tol = 1e-12, neighbors_algorithm = 'auto', random_state = None, n_jobs = None)` | medium | 28 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.manifold._locally_linear.LocallyLinearEmbedding.fit(self, X, y = None)` | medium | 18 | 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.manifold._locally_linear.LocallyLinearEmbedding.fit_transform(self, X, y = None)` | medium | 18 | 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.manifold._locally_linear.LocallyLinearEmbedding.transform(self, X)` | medium | 30 | 有逻辑 |

---

## 🔹 `MDS`

**完全限定名**: `sklearn.manifold._mds.MDS`

**文件路径**: `sklearn/manifold/_mds.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, metric_mds = True, n_in...` | `None` | `sklearn.manifold._mds.MDS.__init__(self, n_components = 2, metric_mds = True, n_init = 'warn', init = 'warn', max_iter = 300, verbose = 0, eps = 1e-06, n_jobs = None, random_state = None, dissimilarity = 'deprecated', metric = 'euclidean', metric_params = None, normalized_stress = 'auto')` | medium | 30 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.manifold._mds.MDS.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y = None, init = None` | `None` | `sklearn.manifold._mds.MDS.fit(self, X, y = None, init = None)` | medium | 26 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None, init = None` | `None` | `sklearn.manifold._mds.MDS.fit_transform(self, X, y = None, init = None)` | complex | 119 | 抛异常, 有逻辑 |

---

## 🔹 `SpectralEmbedding`

**完全限定名**: `sklearn.manifold._spectral_embedding.SpectralEmbedding`

**文件路径**: `sklearn/manifold/_spectral_embedding.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, affinity = 'nearest_nei...` | `None` | `sklearn.manifold._spectral_embedding.SpectralEmbedding.__init__(self, n_components = 2, affinity = 'nearest_neighbors', gamma = None, random_state = None, eigen_solver = None, eigen_tol = 'auto', n_neighbors = None, n_jobs = None)` | medium | 20 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.manifold._spectral_embedding.SpectralEmbedding.__sklearn_tags__(self)` | simple | 8 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.manifold._spectral_embedding.SpectralEmbedding.fit(self, X, y = None)` | medium | 35 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.manifold._spectral_embedding.SpectralEmbedding.fit_transform(self, X, y = None)` | medium | 24 | 有逻辑 |

---

## 🔹 `TSNE`

**完全限定名**: `sklearn.manifold._t_sne.TSNE`

**文件路径**: `sklearn/manifold/_t_sne.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 2, perplexity = 30.0, earl...` | `None` | `sklearn.manifold._t_sne.TSNE.__init__(self, n_components = 2, perplexity = 30.0, early_exaggeration = 12.0, learning_rate = 'auto', max_iter = 1000, n_iter_without_progress = 300, min_grad_norm = 1e-07, metric = 'euclidean', metric_params = None, init = 'pca', verbose = 0, random_state = None, method = 'barnes_hut', angle = 0.5, n_jobs = None)` | complex | 34 | 魔术方法 |
| 2 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.manifold._t_sne.TSNE.fit_transform(self, X, y = None)` | medium | 25 | - |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.manifold._t_sne.TSNE.fit(self, X, y = None)` | medium | 23 | - |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.manifold._t_sne.TSNE.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `ArgKmin`

**完全限定名**: `sklearn.metrics._pairwise_distances_reduction._dispatcher.ArgKmin`

**文件路径**: `sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute` | class | `cls, X, Y, k, metric = 'euclidean', chunk_size ...` | `None` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.ArgKmin.compute(cls, X, Y, k, metric = 'euclidean', chunk_size = None, metric_kwargs = None, strategy = None, return_distance = False)` | complex | 119 | 抛异常, 有逻辑 |

---

## 🔹 `ArgKminClassMode`

**完全限定名**: `sklearn.metrics._pairwise_distances_reduction._dispatcher.ArgKminClassMode`

**文件路径**: `sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `valid_metrics` | class | `cls` | `List[str]` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.ArgKminClassMode.valid_metrics(cls)` | simple | 9 | 有逻辑 |
| 2 | `compute` | class | `cls, X, Y, k, weights, Y_labels, unique_Y_label...` | `None` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.ArgKminClassMode.compute(cls, X, Y, k, weights, Y_labels, unique_Y_labels, metric = 'euclidean', chunk_size = None, metric_kwargs = None, strategy = None)` | complex | 135 | 抛异常, 有逻辑 |

---

## 🔹 `BaseDistancesReductionDispatcher`

**完全限定名**: `sklearn.metrics._pairwise_distances_reduction._dispatcher.BaseDistancesReductionDispatcher`

**文件路径**: `sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `valid_metrics` | class | `cls` | `List[str]` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.BaseDistancesReductionDispatcher.valid_metrics(cls)` | simple | 15 | 有逻辑 |
| 2 | `is_usable_for` | class | `cls, X, Y, metric` | `bool` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.BaseDistancesReductionDispatcher.is_usable_for(cls, X, Y, metric)` | complex | 59 | 有逻辑 |
| 3 | `compute` | class | `cls, X, Y, **kwargs` | `None` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.BaseDistancesReductionDispatcher.compute(cls, X, Y, **kwargs)` | medium | 23 | 抽象方法, 有逻辑 |

---

## 🔹 `RadiusNeighbors`

**完全限定名**: `sklearn.metrics._pairwise_distances_reduction._dispatcher.RadiusNeighbors`

**文件路径**: `sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `compute` | class | `cls, X, Y, radius, metric = 'euclidean', chunk_...` | `None` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.RadiusNeighbors.compute(cls, X, Y, radius, metric = 'euclidean', chunk_size = None, metric_kwargs = None, strategy = None, return_distance = False, sort_results = False)` | complex | 127 | 抛异常, 有逻辑 |

---

## 🔹 `RadiusNeighborsClassMode`

**完全限定名**: `sklearn.metrics._pairwise_distances_reduction._dispatcher.RadiusNeighborsClassMode`

**文件路径**: `sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `valid_metrics` | class | `cls` | `List[str]` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.RadiusNeighborsClassMode.valid_metrics(cls)` | simple | 9 | 有逻辑 |
| 2 | `compute` | class | `cls, X, Y, radius, weights, Y_labels, unique_Y_...` | `None` | `sklearn.metrics._pairwise_distances_reduction._dispatcher.RadiusNeighborsClassMode.compute(cls, X, Y, radius, weights, Y_labels, unique_Y_labels, outlier_label, metric = 'euclidean', chunk_size = None, metric_kwargs = None, strategy = None)` | complex | 117 | 抛异常, 有逻辑 |

---

## 🔹 `ConfusionMatrixDisplay`

**完全限定名**: `sklearn.metrics._plot.confusion_matrix.ConfusionMatrixDisplay`

**文件路径**: `sklearn/metrics/_plot/confusion_matrix.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, confusion_matrix, display_labels = None` | `None` | `sklearn.metrics._plot.confusion_matrix.ConfusionMatrixDisplay.__init__(self, confusion_matrix, display_labels = None)` | simple | 3 | 魔术方法 |
| 2 | `plot` | instance | `self, include_values = True, cmap = 'viridis', ...` | `None` | `sklearn.metrics._plot.confusion_matrix.ConfusionMatrixDisplay.plot(self, include_values = True, cmap = 'viridis', xticks_rotation = 'horizontal', values_format = None, ax = None, colorbar = True, im_kw = None, text_kw = None)` | complex | 115 | 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, labels = None, sample_wei...` | `None` | `sklearn.metrics._plot.confusion_matrix.ConfusionMatrixDisplay.from_estimator(cls, estimator, X, y, labels = None, sample_weight = None, normalize = None, display_labels = None, include_values = True, xticks_rotation = 'horizontal', values_format = None, cmap = 'viridis', ax = None, colorbar = True, im_kw = None, text_kw = None)` | complex | 147 | 抛异常, 有逻辑 |
| 4 | `from_predictions` | class | `cls, y_true, y_pred, labels = None, sample_weig...` | `None` | `sklearn.metrics._plot.confusion_matrix.ConfusionMatrixDisplay.from_predictions(cls, y_true, y_pred, labels = None, sample_weight = None, normalize = None, display_labels = None, include_values = True, xticks_rotation = 'horizontal', values_format = None, cmap = 'viridis', ax = None, colorbar = True, im_kw = None, text_kw = None)` | complex | 146 | 有逻辑 |

---

## 🔹 `DetCurveDisplay`

**完全限定名**: `sklearn.metrics._plot.det_curve.DetCurveDisplay`

**文件路径**: `sklearn/metrics/_plot/det_curve.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fpr, fnr, estimator_name = None, pos_labe...` | `None` | `sklearn.metrics._plot.det_curve.DetCurveDisplay.__init__(self, fpr, fnr, estimator_name = None, pos_label = None)` | simple | 5 | 魔术方法 |
| 2 | `from_estimator` | class | `cls, estimator, X, y, sample_weight = None, dro...` | `None` | `sklearn.metrics._plot.det_curve.DetCurveDisplay.from_estimator(cls, estimator, X, y, sample_weight = None, drop_intermediate = True, response_method = 'auto', pos_label = None, name = None, ax = None, **kwargs)` | complex | 113 | 有逻辑 |
| 3 | `from_predictions` | class | `cls, y_true, y_score = None, sample_weight = No...` | `None` | `sklearn.metrics._plot.det_curve.DetCurveDisplay.from_predictions(cls, y_true, y_score = None, sample_weight = None, drop_intermediate = True, pos_label = None, name = None, ax = None, y_pred = 'deprecated', **kwargs)` | complex | 119 | 有逻辑 |
| 4 | `plot` | instance | `self, ax = None, name = None, **kwargs` | `None` | `sklearn.metrics._plot.det_curve.DetCurveDisplay.plot(self, ax = None, name = None, **kwargs)` | complex | 64 | 有逻辑 |

---

## 🔹 `PrecisionRecallDisplay`

**完全限定名**: `sklearn.metrics._plot.precision_recall_curve.PrecisionRecallDisplay`

**文件路径**: `sklearn/metrics/_plot/precision_recall_curve.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, precision, recall, average_precision = No...` | `None` | `sklearn.metrics._plot.precision_recall_curve.PrecisionRecallDisplay.__init__(self, precision, recall, average_precision = None, name = None, pos_label = None, prevalence_pos_label = None, estimator_name = 'deprecated')` | medium | 17 | 魔术方法 |
| 2 | `plot` | instance | `self, ax = None, name = None, plot_chance_level...` | `None` | `sklearn.metrics._plot.precision_recall_curve.PrecisionRecallDisplay.plot(self, ax = None, name = None, plot_chance_level = False, chance_level_kw = None, despine = False, **kwargs)` | complex | 130 | 抛异常, 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, sample_weight = None, dro...` | `None` | `sklearn.metrics._plot.precision_recall_curve.PrecisionRecallDisplay.from_estimator(cls, estimator, X, y, sample_weight = None, drop_intermediate = False, response_method = 'auto', pos_label = None, name = None, ax = None, plot_chance_level = False, chance_level_kw = None, despine = False, **kwargs)` | complex | 145 | 有逻辑 |
| 4 | `from_predictions` | class | `cls, y_true, y_score = None, sample_weight = No...` | `None` | `sklearn.metrics._plot.precision_recall_curve.PrecisionRecallDisplay.from_predictions(cls, y_true, y_score = None, sample_weight = None, drop_intermediate = False, pos_label = None, name = None, ax = None, plot_chance_level = False, chance_level_kw = None, despine = False, y_pred = 'deprecated', **kwargs)` | complex | 160 | 有逻辑 |

---

## 🔹 `PredictionErrorDisplay`

**完全限定名**: `sklearn.metrics._plot.regression.PredictionErrorDisplay`

**文件路径**: `sklearn/metrics/_plot/regression.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, y_true, y_pred` | `None` | `sklearn.metrics._plot.regression.PredictionErrorDisplay.__init__(self, y_true, y_pred)` | simple | 3 | 魔术方法 |
| 2 | `plot` | instance | `self, ax = None, kind = 'residual_vs_predicted'...` | `None` | `sklearn.metrics._plot.regression.PredictionErrorDisplay.plot(self, ax = None, kind = 'residual_vs_predicted', scatter_kwargs = None, line_kwargs = None)` | complex | 103 | 抛异常, 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, kind = 'residual_vs_predi...` | `None` | `sklearn.metrics._plot.regression.PredictionErrorDisplay.from_estimator(cls, estimator, X, y, kind = 'residual_vs_predicted', subsample = 1000, random_state = None, ax = None, scatter_kwargs = None, line_kwargs = None)` | complex | 103 | 有逻辑 |
| 4 | `from_predictions` | class | `cls, y_true, y_pred, kind = 'residual_vs_predic...` | `None` | `sklearn.metrics._plot.regression.PredictionErrorDisplay.from_predictions(cls, y_true, y_pred, kind = 'residual_vs_predicted', subsample = 1000, random_state = None, ax = None, scatter_kwargs = None, line_kwargs = None)` | complex | 119 | 抛异常, 有逻辑 |

---

## 🔹 `RocCurveDisplay`

**完全限定名**: `sklearn.metrics._plot.roc_curve.RocCurveDisplay`

**文件路径**: `sklearn/metrics/_plot/roc_curve.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, fpr, tpr, roc_auc = None, name = None, po...` | `None` | `sklearn.metrics._plot.roc_curve.RocCurveDisplay.__init__(self, fpr, tpr, roc_auc = None, name = None, pos_label = None, estimator_name = 'deprecated')` | medium | 15 | 魔术方法 |
| 2 | `plot` | instance | `self, ax = None, name = None, curve_kwargs = No...` | `None` | `sklearn.metrics._plot.roc_curve.RocCurveDisplay.plot(self, ax = None, name = None, curve_kwargs = None, plot_chance_level = False, chance_level_kw = None, despine = False, **kwargs)` | complex | 145 | 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, sample_weight = None, dro...` | `None` | `sklearn.metrics._plot.roc_curve.RocCurveDisplay.from_estimator(cls, estimator, X, y, sample_weight = None, drop_intermediate = True, response_method = 'auto', pos_label = None, name = None, ax = None, curve_kwargs = None, plot_chance_level = False, chance_level_kw = None, despine = False, **kwargs)` | complex | 146 | 有逻辑 |
| 4 | `from_predictions` | class | `cls, y_true, y_score = None, sample_weight = No...` | `None` | `sklearn.metrics._plot.roc_curve.RocCurveDisplay.from_predictions(cls, y_true, y_score = None, sample_weight = None, drop_intermediate = True, pos_label = None, name = None, ax = None, curve_kwargs = None, plot_chance_level = False, chance_level_kw = None, despine = False, y_pred = 'deprecated', **kwargs)` | complex | 158 | 有逻辑 |
| 5 | `from_cv_results` | class | `cls, cv_results, X, y, sample_weight = None, dr...` | `None` | `sklearn.metrics._plot.roc_curve.RocCurveDisplay.from_cv_results(cls, cv_results, X, y, sample_weight = None, drop_intermediate = True, response_method = 'auto', pos_label = None, ax = None, name = None, curve_kwargs = None, plot_chance_level = False, chance_level_kwargs = None, despine = False)` | complex | 166 | 有逻辑 |

---

## 🔹 `BaseMixture`

**完全限定名**: `sklearn.mixture._base.BaseMixture`

**文件路径**: `sklearn/mixture/_base.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components, tol, reg_covar, max_iter, n...` | `None` | `sklearn.mixture._base.BaseMixture.__init__(self, n_components, tol, reg_covar, max_iter, n_init, init_params, random_state, warm_start, verbose, verbose_interval)` | medium | 23 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.mixture._base.BaseMixture.fit(self, X, y = None)` | medium | 29 | 有逻辑 |
| 3 | `fit_predict` | instance | `self, X, y = None` | `None` | `sklearn.mixture._base.BaseMixture.fit_predict(self, X, y = None)` | complex | 110 | 抛异常, 有逻辑 |
| 4 | `score_samples` | instance | `self, X` | `None` | `sklearn.mixture._base.BaseMixture.score_samples(self, X)` | medium | 18 | - |
| 5 | `score` | instance | `self, X, y = None` | `None` | `sklearn.mixture._base.BaseMixture.score(self, X, y = None)` | medium | 19 | 有逻辑 |
| 6 | `predict` | instance | `self, X` | `None` | `sklearn.mixture._base.BaseMixture.predict(self, X)` | medium | 18 | 有逻辑 |
| 7 | `predict_proba` | instance | `self, X` | `None` | `sklearn.mixture._base.BaseMixture.predict_proba(self, X)` | medium | 19 | 有逻辑 |
| 8 | `sample` | instance | `self, n_samples = 1` | `None` | `sklearn.mixture._base.BaseMixture.sample(self, n_samples = 1)` | complex | 76 | 抛异常, 有逻辑 |

---

## 🔹 `BayesianGaussianMixture`

**完全限定名**: `sklearn.mixture._bayesian_mixture.BayesianGaussianMixture`

**文件路径**: `sklearn/mixture/_bayesian_mixture.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 1, covariance_type = 'full...` | `None` | `sklearn.mixture._bayesian_mixture.BayesianGaussianMixture.__init__(self, n_components = 1, covariance_type = 'full', tol = 0.001, reg_covar = 1e-06, max_iter = 100, n_init = 1, init_params = 'kmeans', weight_concentration_prior_type = 'dirichlet_process', weight_concentration_prior = None, mean_precision_prior = None, mean_prior = None, degrees_of_freedom_prior = None, covariance_prior = None, random_state = None, warm_start = False, verbose = 0, verbose_interval = 10)` | complex | 41 | 魔术方法 |

---

## 🔹 `GaussianMixture`

**完全限定名**: `sklearn.mixture._gaussian_mixture.GaussianMixture`

**文件路径**: `sklearn/mixture/_gaussian_mixture.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 1, covariance_type = 'full...` | `None` | `sklearn.mixture._gaussian_mixture.GaussianMixture.__init__(self, n_components = 1, covariance_type = 'full', tol = 0.001, reg_covar = 1e-06, max_iter = 100, n_init = 1, init_params = 'kmeans', weights_init = None, means_init = None, precisions_init = None, random_state = None, warm_start = False, verbose = 0, verbose_interval = 10)` | complex | 35 | 魔术方法 |
| 2 | `bic` | instance | `self, X` | `None` | `sklearn.mixture._gaussian_mixture.GaussianMixture.bic(self, X)` | medium | 22 | 有逻辑 |
| 3 | `aic` | instance | `self, X` | `None` | `sklearn.mixture._gaussian_mixture.GaussianMixture.aic(self, X)` | medium | 17 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.mixture._gaussian_mixture.GaussianMixture.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `BaseThresholdClassifier`

**完全限定名**: `sklearn.model_selection._classification_threshold.BaseThresholdClassifier`

**文件路径**: `sklearn/model_selection/_classification_threshold.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, response_method = 'auto'` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.__init__(self, estimator, response_method = 'auto')` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **params` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.fit(self, X, y, **params)` | medium | 38 | 抛异常, 有逻辑 |
| 3 | `classes_` | property | `self` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.classes_(self)` | simple | 3 | - |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.predict_proba(self, X)` | medium | 17 | 有逻辑 |
| 5 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.predict_log_proba(self, X)` | medium | 17 | 有逻辑 |
| 6 | `decision_function` | instance | `self, X` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.decision_function(self, X)` | medium | 17 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.model_selection._classification_threshold.BaseThresholdClassifier.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `FixedThresholdClassifier`

**完全限定名**: `sklearn.model_selection._classification_threshold.FixedThresholdClassifier`

**文件路径**: `sklearn/model_selection/_classification_threshold.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, threshold = 'auto', pos_label ...` | `None` | `sklearn.model_selection._classification_threshold.FixedThresholdClassifier.__init__(self, estimator, threshold = 'auto', pos_label = None, response_method = 'auto')` | medium | 11 | 魔术方法 |
| 2 | `classes_` | property | `self` | `None` | `sklearn.model_selection._classification_threshold.FixedThresholdClassifier.classes_(self)` | simple | 10 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.model_selection._classification_threshold.FixedThresholdClassifier.predict(self, X)` | medium | 33 | 有逻辑 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.model_selection._classification_threshold.FixedThresholdClassifier.get_metadata_routing(self)` | medium | 17 | - |

---

## 🔹 `TunedThresholdClassifierCV`

**完全限定名**: `sklearn.model_selection._classification_threshold.TunedThresholdClassifierCV`

**文件路径**: `sklearn/model_selection/_classification_threshold.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, scoring = 'balanced_accuracy',...` | `None` | `sklearn.model_selection._classification_threshold.TunedThresholdClassifierCV.__init__(self, estimator, scoring = 'balanced_accuracy', response_method = 'auto', thresholds = 100, cv = None, refit = True, n_jobs = None, random_state = None, store_cv_results = False)` | medium | 21 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.model_selection._classification_threshold.TunedThresholdClassifierCV.predict(self, X)` | medium | 25 | - |
| 3 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.model_selection._classification_threshold.TunedThresholdClassifierCV.get_metadata_routing(self)` | medium | 28 | - |

---

## 🔹 `LearningCurveDisplay`

**完全限定名**: `sklearn.model_selection._plot.LearningCurveDisplay`

**文件路径**: `sklearn/model_selection/_plot.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, train_sizes, train_scores, test_scores, s...` | `None` | `sklearn.model_selection._plot.LearningCurveDisplay.__init__(self, train_sizes, train_scores, test_scores, score_name = None)` | simple | 5 | 魔术方法 |
| 2 | `plot` | instance | `self, ax = None, negate_score = False, score_na...` | `None` | `sklearn.model_selection._plot.LearningCurveDisplay.plot(self, ax = None, negate_score = False, score_name = None, score_type = 'both', std_display_style = 'fill_between', line_kw = None, fill_between_kw = None, errorbar_kw = None)` | complex | 74 | 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, groups = None, train_size...` | `None` | `sklearn.model_selection._plot.LearningCurveDisplay.from_estimator(cls, estimator, X, y, groups = None, train_sizes = np.linspace(0.1, 1.0, 5), cv = None, scoring = None, exploit_incremental_learning = False, n_jobs = None, pre_dispatch = 'all', verbose = 0, shuffle = False, random_state = None, error_score = np.nan, fit_params = None, ax = None, negate_score = False, score_name = None, score_type = 'both', std_display_style = 'fill_between', line_kw = None, fill_between_kw = None, errorbar_kw = None)` | complex | 222 | 有逻辑 |

---

## 🔹 `ValidationCurveDisplay`

**完全限定名**: `sklearn.model_selection._plot.ValidationCurveDisplay`

**文件路径**: `sklearn/model_selection/_plot.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, param_name, param_range, train_scores, te...` | `None` | `sklearn.model_selection._plot.ValidationCurveDisplay.__init__(self, param_name, param_range, train_scores, test_scores, score_name = None)` | simple | 8 | 魔术方法 |
| 2 | `plot` | instance | `self, ax = None, negate_score = False, score_na...` | `None` | `sklearn.model_selection._plot.ValidationCurveDisplay.plot(self, ax = None, negate_score = False, score_name = None, score_type = 'both', std_display_style = 'fill_between', line_kw = None, fill_between_kw = None, errorbar_kw = None)` | complex | 74 | 有逻辑 |
| 3 | `from_estimator` | class | `cls, estimator, X, y, param_name, param_range, ...` | `None` | `sklearn.model_selection._plot.ValidationCurveDisplay.from_estimator(cls, estimator, X, y, param_name, param_range, groups = None, cv = None, scoring = None, n_jobs = None, pre_dispatch = 'all', verbose = 0, error_score = np.nan, fit_params = None, ax = None, negate_score = False, score_name = None, score_type = 'both', std_display_style = 'fill_between', line_kw = None, fill_between_kw = None, errorbar_kw = None)` | complex | 205 | 有逻辑 |

---

## 🔹 `BaseSearchCV`

**完全限定名**: `sklearn.model_selection._search.BaseSearchCV`

**文件路径**: `sklearn/model_selection/_search.py`

**公共方法数**: 14

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, scoring = None, n_jobs = None,...` | `None` | `sklearn.model_selection._search.BaseSearchCV.__init__(self, estimator, scoring = None, n_jobs = None, refit = True, cv = None, verbose = 0, pre_dispatch = '2*n_jobs', error_score = np.nan, return_train_score = True)` | medium | 22 | 魔术方法, 抽象方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.model_selection._search.BaseSearchCV.__sklearn_tags__(self)` | simple | 11 | 魔术方法 |
| 3 | `score` | instance | `self, X, y = None, **params` | `None` | `sklearn.model_selection._search.BaseSearchCV.score(self, X, y = None, **params)` | complex | 58 | 抛异常, 有逻辑 |
| 4 | `score_samples` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.score_samples(self, X)` | medium | 21 | 有逻辑 |
| 5 | `predict` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.predict(self, X)` | medium | 20 | 有逻辑 |
| 6 | `predict_proba` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.predict_proba(self, X)` | medium | 21 | 有逻辑 |
| 7 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.predict_log_proba(self, X)` | medium | 21 | 有逻辑 |
| 8 | `decision_function` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.decision_function(self, X)` | medium | 21 | 有逻辑 |
| 9 | `transform` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.transform(self, X)` | medium | 20 | 有逻辑 |
| 10 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.model_selection._search.BaseSearchCV.inverse_transform(self, X)` | medium | 20 | 有逻辑 |
| 11 | `n_features_in_` | property | `self` | `None` | `sklearn.model_selection._search.BaseSearchCV.n_features_in_(self)` | medium | 17 | 抛异常, 有逻辑 |
| 12 | `classes_` | property | `self` | `None` | `sklearn.model_selection._search.BaseSearchCV.classes_(self)` | simple | 7 | - |
| 13 | `fit` | instance | `self, X, y = None, **params` | `None` | `sklearn.model_selection._search.BaseSearchCV.fit(self, X, y = None, **params)` | complex | 190 | 抛异常, 有逻辑 |
| 14 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.model_selection._search.BaseSearchCV.get_metadata_routing(self)` | medium | 32 | - |

---

## 🔹 `GridSearchCV`

**完全限定名**: `sklearn.model_selection._search.GridSearchCV`

**文件路径**: `sklearn/model_selection/_search.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, param_grid, scoring = None, n_...` | `None` | `sklearn.model_selection._search.GridSearchCV.__init__(self, estimator, param_grid, scoring = None, n_jobs = None, refit = True, cv = None, verbose = 0, pre_dispatch = '2*n_jobs', error_score = np.nan, return_train_score = False)` | medium | 26 | 魔术方法 |

---

## 🔹 `ParameterGrid`

**完全限定名**: `sklearn.model_selection._search.ParameterGrid`

**文件路径**: `sklearn/model_selection/_search.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, param_grid` | `None` | `sklearn.model_selection._search.ParameterGrid.__init__(self, param_grid)` | complex | 38 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `__iter__` | instance | `self` | `None` | `sklearn.model_selection._search.ParameterGrid.__iter__(self)` | medium | 19 | 魔术方法, 有逻辑 |
| 3 | `__len__` | instance | `self` | `None` | `sklearn.model_selection._search.ParameterGrid.__len__(self)` | simple | 7 | 魔术方法, 有逻辑 |
| 4 | `__getitem__` | instance | `self, ind` | `None` | `sklearn.model_selection._search.ParameterGrid.__getitem__(self, ind)` | medium | 40 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `ParameterSampler`

**完全限定名**: `sklearn.model_selection._search.ParameterSampler`

**文件路径**: `sklearn/model_selection/_search.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, param_distributions, n_iter, random_state...` | `None` | `sklearn.model_selection._search.ParameterSampler.__init__(self, param_distributions, n_iter, random_state = None)` | medium | 29 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `__iter__` | instance | `self` | `None` | `sklearn.model_selection._search.ParameterSampler.__iter__(self)` | medium | 34 | 魔术方法, 有逻辑 |
| 3 | `__len__` | instance | `self` | `None` | `sklearn.model_selection._search.ParameterSampler.__len__(self)` | simple | 7 | 魔术方法, 有逻辑 |

---

## 🔹 `RandomizedSearchCV`

**完全限定名**: `sklearn.model_selection._search.RandomizedSearchCV`

**文件路径**: `sklearn/model_selection/_search.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, param_distributions, n_iter = ...` | `None` | `sklearn.model_selection._search.RandomizedSearchCV.__init__(self, estimator, param_distributions, n_iter = 10, scoring = None, n_jobs = None, refit = True, cv = None, verbose = 0, pre_dispatch = '2*n_jobs', random_state = None, error_score = np.nan, return_train_score = False)` | medium | 30 | 魔术方法 |

---

## 🔹 `BaseSuccessiveHalving`

**完全限定名**: `sklearn.model_selection._search_successive_halving.BaseSuccessiveHalving`

**文件路径**: `sklearn/model_selection/_search_successive_halving.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, scoring = None, n_jobs = None,...` | `None` | `sklearn.model_selection._search_successive_halving.BaseSuccessiveHalving.__init__(self, estimator, scoring = None, n_jobs = None, refit = True, cv = 5, verbose = 0, random_state = None, error_score = np.nan, return_train_score = True, max_resources = 'auto', min_resources = 'exhaust', resource = 'n_samples', factor = 3, aggressive_elimination = False)` | complex | 35 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, **params` | `None` | `sklearn.model_selection._search_successive_halving.BaseSuccessiveHalving.fit(self, X, y = None, **params)` | medium | 39 | 有逻辑 |

---

## 🔹 `HalvingGridSearchCV`

**完全限定名**: `sklearn.model_selection._search_successive_halving.HalvingGridSearchCV`

**文件路径**: `sklearn/model_selection/_search_successive_halving.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, param_grid, factor = 3, resour...` | `None` | `sklearn.model_selection._search_successive_halving.HalvingGridSearchCV.__init__(self, estimator, param_grid, factor = 3, resource = 'n_samples', max_resources = 'auto', min_resources = 'exhaust', aggressive_elimination = False, cv = 5, scoring = None, refit = True, error_score = np.nan, return_train_score = True, random_state = None, n_jobs = None, verbose = 0)` | complex | 36 | 魔术方法 |

---

## 🔹 `HalvingRandomSearchCV`

**完全限定名**: `sklearn.model_selection._search_successive_halving.HalvingRandomSearchCV`

**文件路径**: `sklearn/model_selection/_search_successive_halving.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, param_distributions, n_candida...` | `None` | `sklearn.model_selection._search_successive_halving.HalvingRandomSearchCV.__init__(self, estimator, param_distributions, n_candidates = 'exhaust', factor = 3, resource = 'n_samples', max_resources = 'auto', min_resources = 'smallest', aggressive_elimination = False, cv = 5, scoring = None, refit = True, error_score = np.nan, return_train_score = True, random_state = None, n_jobs = None, verbose = 0)` | complex | 38 | 魔术方法 |

---

## 🔹 `BaseCrossValidator`

**完全限定名**: `sklearn.model_selection._split.BaseCrossValidator`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.BaseCrossValidator.split(self, X, y = None, groups = None)` | medium | 30 | 有逻辑 |
| 2 | `get_n_splits` | instance | `self, X = None, y = None, groups = None` | `None` | `sklearn.model_selection._split.BaseCrossValidator.get_n_splits(self, X = None, y = None, groups = None)` | simple | 2 | 抽象方法 |
| 3 | `__repr__` | instance | `self` | `None` | `sklearn.model_selection._split.BaseCrossValidator.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `BaseShuffleSplit`

**完全限定名**: `sklearn.model_selection._split.BaseShuffleSplit`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 10, test_size = None, train_si...` | `None` | `sklearn.model_selection._split.BaseShuffleSplit.__init__(self, n_splits = 10, test_size = None, train_size = None, random_state = None)` | simple | 8 | 魔术方法 |
| 2 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.BaseShuffleSplit.split(self, X, y = None, groups = None)` | medium | 33 | 有逻辑 |
| 3 | `get_n_splits` | instance | `self, X = None, y = None, groups = None` | `None` | `sklearn.model_selection._split.BaseShuffleSplit.get_n_splits(self, X = None, y = None, groups = None)` | medium | 21 | 有逻辑 |
| 4 | `__repr__` | instance | `self` | `None` | `sklearn.model_selection._split.BaseShuffleSplit.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `GroupKFold`

**完全限定名**: `sklearn.model_selection._split.GroupKFold`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, shuffle = False, random_sta...` | `None` | `sklearn.model_selection._split.GroupKFold.__init__(self, n_splits = 5, shuffle = False, random_state = None)` | simple | 2 | 魔术方法 |
| 2 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.GroupKFold.split(self, X, y = None, groups = None)` | medium | 25 | 有逻辑 |

---

## 🔹 `GroupShuffleSplit`

**完全限定名**: `sklearn.model_selection._split.GroupShuffleSplit`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, test_size = None, train_siz...` | `None` | `sklearn.model_selection._split.GroupShuffleSplit.__init__(self, n_splits = 5, test_size = None, train_size = None, random_state = None)` | simple | 10 | 魔术方法 |
| 2 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.GroupShuffleSplit.split(self, X, y = None, groups = None)` | medium | 31 | 有逻辑 |

---

## 🔹 `KFold`

**完全限定名**: `sklearn.model_selection._split.KFold`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, shuffle = False, random_sta...` | `None` | `sklearn.model_selection._split.KFold.__init__(self, n_splits = 5, shuffle = False, random_state = None)` | simple | 2 | 魔术方法 |

---

## 🔹 `LeaveOneGroupOut`

**完全限定名**: `sklearn.model_selection._split.LeaveOneGroupOut`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_n_splits` | instance | `self, X = None, y = None, groups = None` | `None` | `sklearn.model_selection._split.LeaveOneGroupOut.get_n_splits(self, X = None, y = None, groups = None)` | medium | 26 | 抛异常, 有逻辑 |
| 2 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.LeaveOneGroupOut.split(self, X, y = None, groups = None)` | medium | 25 | 有逻辑 |

---

## 🔹 `LeaveOneOut`

**完全限定名**: `sklearn.model_selection._split.LeaveOneOut`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `get_n_splits` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.LeaveOneOut.get_n_splits(self, X, y = None, groups = None)` | medium | 23 | 抛异常, 有逻辑 |

---

## 🔹 `LeavePGroupsOut`

**完全限定名**: `sklearn.model_selection._split.LeavePGroupsOut`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_groups` | `None` | `sklearn.model_selection._split.LeavePGroupsOut.__init__(self, n_groups)` | simple | 2 | 魔术方法 |
| 2 | `get_n_splits` | instance | `self, X = None, y = None, groups = None` | `None` | `sklearn.model_selection._split.LeavePGroupsOut.get_n_splits(self, X = None, y = None, groups = None)` | medium | 26 | 抛异常, 有逻辑 |
| 3 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.LeavePGroupsOut.split(self, X, y = None, groups = None)` | medium | 25 | 有逻辑 |

---

## 🔹 `LeavePOut`

**完全限定名**: `sklearn.model_selection._split.LeavePOut`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, p` | `None` | `sklearn.model_selection._split.LeavePOut.__init__(self, p)` | simple | 2 | 魔术方法 |
| 2 | `get_n_splits` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.LeavePOut.get_n_splits(self, X, y = None, groups = None)` | medium | 18 | 抛异常, 有逻辑 |

---

## 🔹 `PredefinedSplit`

**完全限定名**: `sklearn.model_selection._split.PredefinedSplit`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, test_fold` | `None` | `sklearn.model_selection._split.PredefinedSplit.__init__(self, test_fold)` | simple | 5 | 魔术方法 |
| 2 | `split` | instance | `self, X = None, y = None, groups = None` | `None` | `sklearn.model_selection._split.PredefinedSplit.split(self, X = None, y = None, groups = None)` | medium | 28 | 有逻辑 |
| 3 | `get_n_splits` | instance | `self, X = None, y = None, groups = None` | `None` | `sklearn.model_selection._split.PredefinedSplit.get_n_splits(self, X = None, y = None, groups = None)` | medium | 20 | 有逻辑 |

---

## 🔹 `RepeatedKFold`

**完全限定名**: `sklearn.model_selection._split.RepeatedKFold`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, n_repeats = 10, random_stat...` | `None` | `sklearn.model_selection._split.RepeatedKFold.__init__(self, n_splits = 5, n_repeats = 10, random_state = None)` | simple | 4 | 魔术方法 |

---

## 🔹 `RepeatedStratifiedKFold`

**完全限定名**: `sklearn.model_selection._split.RepeatedStratifiedKFold`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, n_repeats = 10, random_stat...` | `None` | `sklearn.model_selection._split.RepeatedStratifiedKFold.__init__(self, n_splits = 5, n_repeats = 10, random_state = None)` | simple | 7 | 魔术方法 |
| 2 | `split` | instance | `self, X, y, groups = None` | `None` | `sklearn.model_selection._split.RepeatedStratifiedKFold.split(self, X, y, groups = None)` | medium | 36 | 有逻辑 |

---

## 🔹 `ShuffleSplit`

**完全限定名**: `sklearn.model_selection._split.ShuffleSplit`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 10, test_size = None, train_si...` | `None` | `sklearn.model_selection._split.ShuffleSplit.__init__(self, n_splits = 10, test_size = None, train_size = None, random_state = None)` | simple | 10 | 魔术方法 |

---

## 🔹 `StratifiedGroupKFold`

**完全限定名**: `sklearn.model_selection._split.StratifiedGroupKFold`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, shuffle = False, random_sta...` | `None` | `sklearn.model_selection._split.StratifiedGroupKFold.__init__(self, n_splits = 5, shuffle = False, random_state = None)` | simple | 2 | 魔术方法 |

---

## 🔹 `StratifiedKFold`

**完全限定名**: `sklearn.model_selection._split.StratifiedKFold`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, shuffle = False, random_sta...` | `None` | `sklearn.model_selection._split.StratifiedKFold.__init__(self, n_splits = 5, shuffle = False, random_state = None)` | simple | 2 | 魔术方法 |
| 2 | `split` | instance | `self, X, y, groups = None` | `None` | `sklearn.model_selection._split.StratifiedKFold.split(self, X, y, groups = None)` | complex | 41 | 有逻辑 |

---

## 🔹 `StratifiedShuffleSplit`

**完全限定名**: `sklearn.model_selection._split.StratifiedShuffleSplit`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 10, test_size = None, train_si...` | `None` | `sklearn.model_selection._split.StratifiedShuffleSplit.__init__(self, n_splits = 10, test_size = None, train_size = None, random_state = None)` | simple | 10 | 魔术方法 |
| 2 | `split` | instance | `self, X, y, groups = None` | `None` | `sklearn.model_selection._split.StratifiedShuffleSplit.split(self, X, y, groups = None)` | complex | 41 | 有逻辑 |

---

## 🔹 `TimeSeriesSplit`

**完全限定名**: `sklearn.model_selection._split.TimeSeriesSplit`

**文件路径**: `sklearn/model_selection/_split.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_splits = 5, max_train_size = None, test...` | `None` | `sklearn.model_selection._split.TimeSeriesSplit.__init__(self, n_splits = 5, max_train_size = None, test_size = None, gap = 0)` | simple | 5 | 魔术方法 |
| 2 | `split` | instance | `self, X, y = None, groups = None` | `None` | `sklearn.model_selection._split.TimeSeriesSplit.split(self, X, y = None, groups = None)` | medium | 29 | 有逻辑 |

---

## 🔹 `OneVsOneClassifier`

**完全限定名**: `sklearn.multiclass.OneVsOneClassifier`

**文件路径**: `sklearn/multiclass.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_jobs = None` | `None` | `sklearn.multiclass.OneVsOneClassifier.__init__(self, estimator, n_jobs = None)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.multiclass.OneVsOneClassifier.fit(self, X, y, **fit_params)` | complex | 70 | 抛异常, 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y, classes = None, **partial_fit_params` | `None` | `sklearn.multiclass.OneVsOneClassifier.partial_fit(self, X, y, classes = None, **partial_fit_params)` | complex | 86 | 抛异常, 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.multiclass.OneVsOneClassifier.predict(self, X)` | medium | 22 | 有逻辑 |
| 5 | `decision_function` | instance | `self, X` | `None` | `sklearn.multiclass.OneVsOneClassifier.decision_function(self, X)` | complex | 47 | 有逻辑 |
| 6 | `n_classes_` | property | `self` | `None` | `sklearn.multiclass.OneVsOneClassifier.n_classes_(self)` | simple | 3 | - |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.multiclass.OneVsOneClassifier.__sklearn_tags__(self)` | simple | 6 | 魔术方法, 有逻辑 |
| 8 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.multiclass.OneVsOneClassifier.get_metadata_routing(self)` | medium | 26 | - |

---

## 🔹 `OneVsRestClassifier`

**完全限定名**: `sklearn.multiclass.OneVsRestClassifier`

**文件路径**: `sklearn/multiclass.py`

**公共方法数**: 10

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_jobs = None, verbose = 0` | `None` | `sklearn.multiclass.OneVsRestClassifier.__init__(self, estimator, n_jobs = None, verbose = 0)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.multiclass.OneVsRestClassifier.fit(self, X, y, **fit_params)` | complex | 65 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y, classes = None, **partial_fit_params` | `None` | `sklearn.multiclass.OneVsRestClassifier.partial_fit(self, X, y, classes = None, **partial_fit_params)` | complex | 79 | 抛异常, 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.multiclass.OneVsRestClassifier.predict(self, X)` | complex | 39 | 有逻辑 |
| 5 | `predict_proba` | instance | `self, X` | `None` | `sklearn.multiclass.OneVsRestClassifier.predict_proba(self, X)` | medium | 40 | 有逻辑 |
| 6 | `decision_function` | instance | `self, X` | `None` | `sklearn.multiclass.OneVsRestClassifier.decision_function(self, X)` | medium | 28 | 有逻辑 |
| 7 | `multilabel_` | property | `self` | `None` | `sklearn.multiclass.OneVsRestClassifier.multilabel_(self)` | simple | 3 | - |
| 8 | `n_classes_` | property | `self` | `None` | `sklearn.multiclass.OneVsRestClassifier.n_classes_(self)` | simple | 3 | - |
| 9 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.multiclass.OneVsRestClassifier.__sklearn_tags__(self)` | simple | 6 | 魔术方法, 有逻辑 |
| 10 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.multiclass.OneVsRestClassifier.get_metadata_routing(self)` | medium | 26 | - |

---

## 🔹 `OutputCodeClassifier`

**完全限定名**: `sklearn.multiclass.OutputCodeClassifier`

**文件路径**: `sklearn/multiclass.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, code_size = 1.5, random_state ...` | `None` | `sklearn.multiclass.OutputCodeClassifier.__init__(self, estimator, code_size = 1.5, random_state = None, n_jobs = None)` | simple | 5 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **fit_params` | `None` | `sklearn.multiclass.OutputCodeClassifier.fit(self, X, y, **fit_params)` | complex | 76 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.multiclass.OutputCodeClassifier.predict(self, X)` | medium | 24 | 有逻辑 |
| 4 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.multiclass.OutputCodeClassifier.get_metadata_routing(self)` | medium | 20 | - |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.multiclass.OutputCodeClassifier.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `ClassifierChain`

**完全限定名**: `sklearn.multioutput.ClassifierChain`

**文件路径**: `sklearn/multioutput.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, order = None, cv = None...` | `None` | `sklearn.multioutput.ClassifierChain.__init__(self, estimator = None, order = None, cv = None, chain_method = 'predict', random_state = None, verbose = False, base_estimator = 'deprecated')` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, Y, **fit_params` | `None` | `sklearn.multioutput.ClassifierChain.fit(self, X, Y, **fit_params)` | medium | 29 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X` | `None` | `sklearn.multioutput.ClassifierChain.predict_proba(self, X)` | medium | 14 | - |
| 4 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.multioutput.ClassifierChain.predict_log_proba(self, X)` | medium | 14 | - |
| 5 | `decision_function` | instance | `self, X` | `None` | `sklearn.multioutput.ClassifierChain.decision_function(self, X)` | medium | 15 | 有逻辑 |
| 6 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.multioutput.ClassifierChain.get_metadata_routing(self)` | medium | 20 | - |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.multioutput.ClassifierChain.__sklearn_tags__(self)` | simple | 7 | 魔术方法 |

---

## 🔹 `MultiOutputClassifier`

**完全限定名**: `sklearn.multioutput.MultiOutputClassifier`

**文件路径**: `sklearn/multioutput.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_jobs = None` | `None` | `sklearn.multioutput.MultiOutputClassifier.__init__(self, estimator, n_jobs = None)` | simple | 2 | 魔术方法 |
| 2 | `fit` | instance | `self, X, Y, sample_weight = None, **fit_params` | `None` | `sklearn.multioutput.MultiOutputClassifier.fit(self, X, Y, sample_weight = None, **fit_params)` | medium | 29 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X` | `None` | `sklearn.multioutput.MultiOutputClassifier.predict_proba(self, X)` | medium | 26 | 抛异常, 有逻辑 |
| 4 | `score` | instance | `self, X, y` | `None` | `sklearn.multioutput.MultiOutputClassifier.score(self, X, y)` | medium | 30 | 抛异常, 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.multioutput.MultiOutputClassifier.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `MultiOutputRegressor`

**完全限定名**: `sklearn.multioutput.MultiOutputRegressor`

**文件路径**: `sklearn/multioutput.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator, n_jobs = None` | `None` | `sklearn.multioutput.MultiOutputRegressor.__init__(self, estimator, n_jobs = None)` | simple | 2 | 魔术方法 |
| 2 | `partial_fit` | instance | `self, X, y, sample_weight = None, **partial_fit...` | `None` | `sklearn.multioutput.MultiOutputRegressor.partial_fit(self, X, y, sample_weight = None, **partial_fit_params)` | medium | 31 | 有逻辑 |

---

## 🔹 `RegressorChain`

**完全限定名**: `sklearn.multioutput.RegressorChain`

**文件路径**: `sklearn/multioutput.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, X, Y, **fit_params` | `None` | `sklearn.multioutput.RegressorChain.fit(self, X, Y, **fit_params)` | medium | 24 | - |
| 2 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.multioutput.RegressorChain.get_metadata_routing(self)` | medium | 20 | - |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.multioutput.RegressorChain.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `BernoulliNB`

**完全限定名**: `sklearn.naive_bayes.BernoulliNB`

**文件路径**: `sklearn/naive_bayes.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, force_alpha = True, binarize...` | `None` | `sklearn.naive_bayes.BernoulliNB.__init__(self, alpha = 1.0, force_alpha = True, binarize = 0.0, fit_prior = True, class_prior = None)` | medium | 16 | 魔术方法 |

---

## 🔹 `CategoricalNB`

**完全限定名**: `sklearn.naive_bayes.CategoricalNB`

**文件路径**: `sklearn/naive_bayes.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, force_alpha = True, fit_prio...` | `None` | `sklearn.naive_bayes.CategoricalNB.__init__(self, alpha = 1.0, force_alpha = True, fit_prior = True, class_prior = None, min_categories = None)` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.naive_bayes.CategoricalNB.fit(self, X, y, sample_weight = None)` | medium | 26 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y, classes = None, sample_weight = None` | `None` | `sklearn.naive_bayes.CategoricalNB.partial_fit(self, X, y, classes = None, sample_weight = None)` | complex | 43 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.naive_bayes.CategoricalNB.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `ComplementNB`

**完全限定名**: `sklearn.naive_bayes.ComplementNB`

**文件路径**: `sklearn/naive_bayes.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, force_alpha = True, fit_prio...` | `None` | `sklearn.naive_bayes.ComplementNB.__init__(self, alpha = 1.0, force_alpha = True, fit_prior = True, class_prior = None, norm = False)` | medium | 16 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.naive_bayes.ComplementNB.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `GaussianNB`

**完全限定名**: `sklearn.naive_bayes.GaussianNB`

**文件路径**: `sklearn/naive_bayes.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, priors = None, var_smoothing = 1e-09` | `None` | `sklearn.naive_bayes.GaussianNB.__init__(self, priors = None, var_smoothing = 1e-09)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.naive_bayes.GaussianNB.fit(self, X, y, sample_weight = None)` | medium | 28 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y, classes = None, sample_weight = None` | `None` | `sklearn.naive_bayes.GaussianNB.partial_fit(self, X, y, classes = None, sample_weight = None)` | complex | 43 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.naive_bayes.GaussianNB.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `MultinomialNB`

**完全限定名**: `sklearn.naive_bayes.MultinomialNB`

**文件路径**: `sklearn/naive_bayes.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, alpha = 1.0, force_alpha = True, fit_prio...` | `None` | `sklearn.naive_bayes.MultinomialNB.__init__(self, alpha = 1.0, force_alpha = True, fit_prior = True, class_prior = None)` | simple | 9 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.naive_bayes.MultinomialNB.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `KNeighborsMixin`

**完全限定名**: `sklearn.neighbors._base.KNeighborsMixin`

**文件路径**: `sklearn/neighbors/_base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `kneighbors` | instance | `self, X = None, n_neighbors = None, return_dist...` | `None` | `sklearn.neighbors._base.KNeighborsMixin.kneighbors(self, X = None, n_neighbors = None, return_distance = True)` | complex | 203 | 抛异常, 有逻辑 |
| 2 | `kneighbors_graph` | instance | `self, X = None, n_neighbors = None, mode = 'con...` | `None` | `sklearn.neighbors._base.KNeighborsMixin.kneighbors_graph(self, X = None, n_neighbors = None, mode = 'connectivity')` | complex | 82 | 抛异常, 有逻辑 |

---

## 🔹 `NeighborsBase`

**完全限定名**: `sklearn.neighbors._base.NeighborsBase`

**文件路径**: `sklearn/neighbors/_base.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = None, radius = None, algori...` | `None` | `sklearn.neighbors._base.NeighborsBase.__init__(self, n_neighbors = None, radius = None, algorithm = 'auto', leaf_size = 30, metric = 'minkowski', p = 2, metric_params = None, n_jobs = None)` | medium | 19 | 魔术方法, 抽象方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._base.NeighborsBase.__sklearn_tags__(self)` | simple | 9 | 魔术方法 |

---

## 🔹 `RadiusNeighborsMixin`

**完全限定名**: `sklearn.neighbors._base.RadiusNeighborsMixin`

**文件路径**: `sklearn/neighbors/_base.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `radius_neighbors` | instance | `self, X = None, radius = None, return_distance ...` | `None` | `sklearn.neighbors._base.RadiusNeighborsMixin.radius_neighbors(self, X = None, radius = None, return_distance = True, sort_results = False)` | complex | 217 | 抛异常, 有逻辑 |
| 2 | `radius_neighbors_graph` | instance | `self, X = None, radius = None, mode = 'connecti...` | `None` | `sklearn.neighbors._base.RadiusNeighborsMixin.radius_neighbors_graph(self, X = None, radius = None, mode = 'connectivity', sort_results = False)` | complex | 89 | 抛异常, 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._base.RadiusNeighborsMixin.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `KNeighborsClassifier`

**完全限定名**: `sklearn.neighbors._classification.KNeighborsClassifier`

**文件路径**: `sklearn/neighbors/_classification.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 5, weights = 'uniform', alg...` | `None` | `sklearn.neighbors._classification.KNeighborsClassifier.__init__(self, n_neighbors = 5, weights = 'uniform', algorithm = 'auto', leaf_size = 30, p = 2, metric = 'minkowski', metric_params = None, n_jobs = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.neighbors._classification.KNeighborsClassifier.fit(self, X, y)` | medium | 19 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.neighbors._classification.KNeighborsClassifier.predict(self, X)` | complex | 68 | 抛异常, 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.neighbors._classification.KNeighborsClassifier.predict_proba(self, X)` | complex | 104 | 抛异常, 有逻辑 |
| 5 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.neighbors._classification.KNeighborsClassifier.score(self, X, y, sample_weight = None)` | medium | 30 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._classification.KNeighborsClassifier.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `RadiusNeighborsClassifier`

**完全限定名**: `sklearn.neighbors._classification.RadiusNeighborsClassifier`

**文件路径**: `sklearn/neighbors/_classification.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, radius = 1.0, weights = 'uniform', algori...` | `None` | `sklearn.neighbors._classification.RadiusNeighborsClassifier.__init__(self, radius = 1.0, weights = 'uniform', algorithm = 'auto', leaf_size = 30, p = 2, metric = 'minkowski', outlier_label = None, metric_params = None, n_jobs = None)` | medium | 24 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.neighbors._classification.RadiusNeighborsClassifier.fit(self, X, y)` | complex | 70 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.neighbors._classification.RadiusNeighborsClassifier.predict(self, X)` | complex | 43 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.neighbors._classification.RadiusNeighborsClassifier.predict_proba(self, X)` | complex | 119 | 抛异常, 有逻辑 |
| 5 | `score` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.neighbors._classification.RadiusNeighborsClassifier.score(self, X, y, sample_weight = None)` | medium | 30 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._classification.RadiusNeighborsClassifier.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `KNeighborsTransformer`

**完全限定名**: `sklearn.neighbors._graph.KNeighborsTransformer`

**文件路径**: `sklearn/neighbors/_graph.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, mode = 'distance', n_neighbors = 5, algor...` | `None` | `sklearn.neighbors._graph.KNeighborsTransformer.__init__(self, mode = 'distance', n_neighbors = 5, algorithm = 'auto', leaf_size = 30, metric = 'minkowski', p = 2, metric_params = None, n_jobs = None)` | medium | 23 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._graph.KNeighborsTransformer.fit(self, X, y = None)` | medium | 19 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.neighbors._graph.KNeighborsTransformer.transform(self, X)` | medium | 21 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._graph.KNeighborsTransformer.fit_transform(self, X, y = None)` | medium | 23 | 有逻辑 |

---

## 🔹 `RadiusNeighborsTransformer`

**完全限定名**: `sklearn.neighbors._graph.RadiusNeighborsTransformer`

**文件路径**: `sklearn/neighbors/_graph.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, mode = 'distance', radius = 1.0, algorith...` | `None` | `sklearn.neighbors._graph.RadiusNeighborsTransformer.__init__(self, mode = 'distance', radius = 1.0, algorithm = 'auto', leaf_size = 30, metric = 'minkowski', p = 2, metric_params = None, n_jobs = None)` | medium | 23 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._graph.RadiusNeighborsTransformer.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.neighbors._graph.RadiusNeighborsTransformer.transform(self, X)` | medium | 18 | 有逻辑 |
| 4 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._graph.RadiusNeighborsTransformer.fit_transform(self, X, y = None)` | medium | 23 | 有逻辑 |

---

## 🔹 `KernelDensity`

**完全限定名**: `sklearn.neighbors._kde.KernelDensity`

**文件路径**: `sklearn/neighbors/_kde.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, bandwidth = 1.0, algorithm = 'auto', kern...` | `None` | `sklearn.neighbors._kde.KernelDensity.__init__(self, bandwidth = 1.0, algorithm = 'auto', kernel = 'gaussian', metric = 'euclidean', atol = 0, rtol = 0, breadth_first = True, leaf_size = 40, metric_params = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.neighbors._kde.KernelDensity.fit(self, X, y = None, sample_weight = None)` | complex | 53 | 有逻辑 |
| 3 | `score_samples` | instance | `self, X` | `None` | `sklearn.neighbors._kde.KernelDensity.score_samples(self, X)` | complex | 37 | 有逻辑 |
| 4 | `score` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._kde.KernelDensity.score(self, X, y = None)` | medium | 21 | 有逻辑 |
| 5 | `sample` | instance | `self, n_samples = 1, random_state = None` | `None` | `sklearn.neighbors._kde.KernelDensity.sample(self, n_samples = 1, random_state = None)` | complex | 52 | 抛异常, 有逻辑 |

---

## 🔹 `LocalOutlierFactor`

**完全限定名**: `sklearn.neighbors._lof.LocalOutlierFactor`

**文件路径**: `sklearn/neighbors/_lof.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 20, algorithm = 'auto', lea...` | `None` | `sklearn.neighbors._lof.LocalOutlierFactor.__init__(self, n_neighbors = 20, algorithm = 'auto', leaf_size = 30, metric = 'minkowski', p = 2, metric_params = None, contamination = 'auto', novelty = False, n_jobs = None)` | medium | 24 | 魔术方法 |
| 2 | `fit_predict` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._lof.LocalOutlierFactor.fit_predict(self, X, y = None)` | medium | 26 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._lof.LocalOutlierFactor.fit(self, X, y = None)` | complex | 67 | 有逻辑 |
| 4 | `predict` | instance | `self, X = None` | `None` | `sklearn.neighbors._lof.LocalOutlierFactor.predict(self, X = None)` | medium | 21 | 有逻辑 |
| 5 | `decision_function` | instance | `self, X` | `None` | `sklearn.neighbors._lof.LocalOutlierFactor.decision_function(self, X)` | medium | 26 | 有逻辑 |
| 6 | `score_samples` | instance | `self, X` | `None` | `sklearn.neighbors._lof.LocalOutlierFactor.score_samples(self, X)` | complex | 46 | 有逻辑 |

---

## 🔹 `NeighborhoodComponentsAnalysis`

**完全限定名**: `sklearn.neighbors._nca.NeighborhoodComponentsAnalysis`

**文件路径**: `sklearn/neighbors/_nca.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = None, init = 'auto', warm_...` | `None` | `sklearn.neighbors._nca.NeighborhoodComponentsAnalysis.__init__(self, n_components = None, init = 'auto', warm_start = False, max_iter = 50, tol = 1e-05, callback = None, verbose = 0, random_state = None)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.neighbors._nca.NeighborhoodComponentsAnalysis.fit(self, X, y)` | complex | 121 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.neighbors._nca.NeighborhoodComponentsAnalysis.transform(self, X)` | medium | 23 | - |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._nca.NeighborhoodComponentsAnalysis.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `NearestCentroid`

**完全限定名**: `sklearn.neighbors._nearest_centroid.NearestCentroid`

**文件路径**: `sklearn/neighbors/_nearest_centroid.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, metric = 'euclidean', shrink_threshold = ...` | `None` | `sklearn.neighbors._nearest_centroid.NearestCentroid.__init__(self, metric = 'euclidean', shrink_threshold = None, priors = 'uniform')` | simple | 10 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.neighbors._nearest_centroid.NearestCentroid.fit(self, X, y)` | complex | 124 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.neighbors._nearest_centroid.NearestCentroid.predict(self, X)` | medium | 33 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._nearest_centroid.NearestCentroid.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `KNeighborsRegressor`

**完全限定名**: `sklearn.neighbors._regression.KNeighborsRegressor`

**文件路径**: `sklearn/neighbors/_regression.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 5, weights = 'uniform', alg...` | `None` | `sklearn.neighbors._regression.KNeighborsRegressor.__init__(self, n_neighbors = 5, weights = 'uniform', algorithm = 'auto', leaf_size = 30, p = 2, metric = 'minkowski', metric_params = None, n_jobs = None)` | medium | 22 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neighbors._regression.KNeighborsRegressor.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y` | `None` | `sklearn.neighbors._regression.KNeighborsRegressor.fit(self, X, y)` | medium | 19 | 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.neighbors._regression.KNeighborsRegressor.predict(self, X)` | complex | 44 | 有逻辑 |

---

## 🔹 `RadiusNeighborsRegressor`

**完全限定名**: `sklearn.neighbors._regression.RadiusNeighborsRegressor`

**文件路径**: `sklearn/neighbors/_regression.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, radius = 1.0, weights = 'uniform', algori...` | `None` | `sklearn.neighbors._regression.RadiusNeighborsRegressor.__init__(self, radius = 1.0, weights = 'uniform', algorithm = 'auto', leaf_size = 30, p = 2, metric = 'minkowski', metric_params = None, n_jobs = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.neighbors._regression.RadiusNeighborsRegressor.fit(self, X, y)` | medium | 19 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.neighbors._regression.RadiusNeighborsRegressor.predict(self, X)` | complex | 58 | 有逻辑 |

---

## 🔹 `NearestNeighbors`

**完全限定名**: `sklearn.neighbors._unsupervised.NearestNeighbors`

**文件路径**: `sklearn/neighbors/_unsupervised.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_neighbors = 5, radius = 1.0, algorithm ...` | `None` | `sklearn.neighbors._unsupervised.NearestNeighbors.__init__(self, n_neighbors = 5, radius = 1.0, algorithm = 'auto', leaf_size = 30, metric = 'minkowski', p = 2, metric_params = None, n_jobs = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.neighbors._unsupervised.NearestNeighbors.fit(self, X, y = None)` | medium | 18 | 有逻辑 |

---

## 🔹 `BaseMultilayerPerceptron`

**完全限定名**: `sklearn.neural_network._multilayer_perceptron.BaseMultilayerPerceptron`

**文件路径**: `sklearn/neural_network/_multilayer_perceptron.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, hidden_layer_sizes, activation, solver, a...` | `None` | `sklearn.neural_network._multilayer_perceptron.BaseMultilayerPerceptron.__init__(self, hidden_layer_sizes, activation, solver, alpha, batch_size, learning_rate, learning_rate_init, power_t, max_iter, loss, shuffle, random_state, tol, verbose, warm_start, momentum, nesterovs_momentum, early_stopping, validation_fraction, beta_1, beta_2, epsilon, n_iter_no_change, max_fun)` | complex | 51 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.neural_network._multilayer_perceptron.BaseMultilayerPerceptron.fit(self, X, y, sample_weight = None)` | medium | 23 | - |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neural_network._multilayer_perceptron.BaseMultilayerPerceptron.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `MLPClassifier`

**完全限定名**: `sklearn.neural_network._multilayer_perceptron.MLPClassifier`

**文件路径**: `sklearn/neural_network/_multilayer_perceptron.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, hidden_layer_sizes = (100,), activation =...` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPClassifier.__init__(self, hidden_layer_sizes = (100,), activation = 'relu', solver = 'adam', alpha = 0.0001, batch_size = 'auto', learning_rate = 'constant', learning_rate_init = 0.001, power_t = 0.5, max_iter = 200, shuffle = True, random_state = None, tol = 0.0001, verbose = False, warm_start = False, momentum = 0.9, nesterovs_momentum = True, early_stopping = False, validation_fraction = 0.1, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, n_iter_no_change = 10, max_fun = 15000)` | complex | 53 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPClassifier.predict(self, X)` | medium | 15 | - |
| 3 | `partial_fit` | instance | `self, X, y, sample_weight = None, classes = None` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPClassifier.partial_fit(self, X, y, sample_weight = None, classes = None)` | medium | 37 | 有逻辑 |
| 4 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPClassifier.predict_log_proba(self, X)` | medium | 17 | 有逻辑 |
| 5 | `predict_proba` | instance | `self, X` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPClassifier.predict_proba(self, X)` | medium | 24 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPClassifier.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `MLPRegressor`

**完全限定名**: `sklearn.neural_network._multilayer_perceptron.MLPRegressor`

**文件路径**: `sklearn/neural_network/_multilayer_perceptron.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, loss = 'squared_error', hidden_layer_size...` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPRegressor.__init__(self, loss = 'squared_error', hidden_layer_sizes = (100,), activation = 'relu', solver = 'adam', alpha = 0.0001, batch_size = 'auto', learning_rate = 'constant', learning_rate_init = 0.001, power_t = 0.5, max_iter = 200, shuffle = True, random_state = None, tol = 0.0001, verbose = False, warm_start = False, momentum = 0.9, nesterovs_momentum = True, early_stopping = False, validation_fraction = 0.1, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, n_iter_no_change = 10, max_fun = 15000)` | complex | 54 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPRegressor.predict(self, X)` | medium | 15 | - |
| 3 | `partial_fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.neural_network._multilayer_perceptron.MLPRegressor.partial_fit(self, X, y, sample_weight = None)` | medium | 22 | - |

---

## 🔹 `BernoulliRBM`

**完全限定名**: `sklearn.neural_network._rbm.BernoulliRBM`

**文件路径**: `sklearn/neural_network/_rbm.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 256, learning_rate = 0.1, ...` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.__init__(self, n_components = 256, learning_rate = 0.1, batch_size = 10, n_iter = 10, verbose = 0, random_state = None)` | medium | 16 | 魔术方法 |
| 2 | `transform` | instance | `self, X` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.transform(self, X)` | medium | 19 | - |
| 3 | `gibbs` | instance | `self, v` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.gibbs(self, v)` | medium | 20 | 有逻辑 |
| 4 | `partial_fit` | instance | `self, X, y = None` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.partial_fit(self, X, y = None)` | complex | 40 | 有逻辑 |
| 5 | `score_samples` | instance | `self, X` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.score_samples(self, X)` | complex | 40 | 有逻辑 |
| 6 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.fit(self, X, y = None)` | complex | 54 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.neural_network._rbm.BernoulliRBM.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `AdamOptimizer`

**完全限定名**: `sklearn.neural_network._stochastic_optimizers.AdamOptimizer`

**文件路径**: `sklearn/neural_network/_stochastic_optimizers.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, params, learning_rate_init = 0.001, beta_...` | `None` | `sklearn.neural_network._stochastic_optimizers.AdamOptimizer.__init__(self, params, learning_rate_init = 0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08)` | simple | 11 | 魔术方法, 有逻辑 |

---

## 🔹 `BaseOptimizer`

**完全限定名**: `sklearn.neural_network._stochastic_optimizers.BaseOptimizer`

**文件路径**: `sklearn/neural_network/_stochastic_optimizers.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, learning_rate_init = 0.1` | `None` | `sklearn.neural_network._stochastic_optimizers.BaseOptimizer.__init__(self, learning_rate_init = 0.1)` | simple | 3 | 魔术方法 |
| 2 | `update_params` | instance | `self, params, grads` | `None` | `sklearn.neural_network._stochastic_optimizers.BaseOptimizer.update_params(self, params, grads)` | medium | 16 | 有逻辑 |
| 3 | `iteration_ends` | instance | `self, time_step` | `None` | `sklearn.neural_network._stochastic_optimizers.BaseOptimizer.iteration_ends(self, time_step)` | simple | 5 | - |
| 4 | `trigger_stopping` | instance | `self, msg, verbose` | `None` | `sklearn.neural_network._stochastic_optimizers.BaseOptimizer.trigger_stopping(self, msg, verbose)` | medium | 19 | 有逻辑 |

---

## 🔹 `SGDOptimizer`

**完全限定名**: `sklearn.neural_network._stochastic_optimizers.SGDOptimizer`

**文件路径**: `sklearn/neural_network/_stochastic_optimizers.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, params, learning_rate_init = 0.1, lr_sche...` | `None` | `sklearn.neural_network._stochastic_optimizers.SGDOptimizer.__init__(self, params, learning_rate_init = 0.1, lr_schedule = 'constant', momentum = 0.9, nesterov = True, power_t = 0.5)` | medium | 16 | 魔术方法, 有逻辑 |
| 2 | `iteration_ends` | instance | `self, time_step` | `None` | `sklearn.neural_network._stochastic_optimizers.SGDOptimizer.iteration_ends(self, time_step)` | medium | 14 | 有逻辑 |
| 3 | `trigger_stopping` | instance | `self, msg, verbose` | `None` | `sklearn.neural_network._stochastic_optimizers.SGDOptimizer.trigger_stopping(self, msg, verbose)` | medium | 15 | 有逻辑 |

---

## 🔹 `FeatureUnion`

**完全限定名**: `sklearn.pipeline.FeatureUnion`

**文件路径**: `sklearn/pipeline.py`

**公共方法数**: 15

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, transformer_list, n_jobs = None, transfor...` | `None` | `sklearn.pipeline.FeatureUnion.__init__(self, transformer_list, n_jobs = None, transformer_weights = None, verbose = False, verbose_feature_names_out = True)` | medium | 14 | 魔术方法 |
| 2 | `set_output` | instance | `self, transform = None` | `None` | `sklearn.pipeline.FeatureUnion.set_output(self, transform = None)` | medium | 24 | 有逻辑 |
| 3 | `named_transformers` | property | `self` | `None` | `sklearn.pipeline.FeatureUnion.named_transformers(self)` | simple | 3 | - |
| 4 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.pipeline.FeatureUnion.get_params(self, deep = True)` | medium | 19 | 有逻辑 |
| 5 | `set_params` | instance | `self, **kwargs` | `None` | `sklearn.pipeline.FeatureUnion.set_params(self, **kwargs)` | medium | 21 | - |
| 6 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.pipeline.FeatureUnion.get_feature_names_out(self, input_features = None)` | medium | 27 | 抛异常, 有逻辑 |
| 7 | `fit` | instance | `self, X, y = None, **fit_params` | `None` | `sklearn.pipeline.FeatureUnion.fit(self, X, y = None, **fit_params)` | complex | 46 | 有逻辑 |
| 8 | `fit_transform` | instance | `self, X, y = None, **params` | `None` | `sklearn.pipeline.FeatureUnion.fit_transform(self, X, y = None, **params)` | complex | 54 | 有逻辑 |
| 9 | `transform` | instance | `self, X, **params` | `None` | `sklearn.pipeline.FeatureUnion.transform(self, X, **params)` | complex | 41 | 有逻辑 |
| 10 | `n_features_in_` | property | `self` | `None` | `sklearn.pipeline.FeatureUnion.n_features_in_(self)` | simple | 5 | - |
| 11 | `feature_names_in_` | property | `self` | `None` | `sklearn.pipeline.FeatureUnion.feature_names_in_(self)` | simple | 4 | - |
| 12 | `__sklearn_is_fitted__` | instance | `self` | `None` | `sklearn.pipeline.FeatureUnion.__sklearn_is_fitted__(self)` | simple | 5 | 魔术方法, 有逻辑 |
| 13 | `__getitem__` | instance | `self, name` | `None` | `sklearn.pipeline.FeatureUnion.__getitem__(self, name)` | simple | 5 | 魔术方法, 抛异常, 有逻辑 |
| 14 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.pipeline.FeatureUnion.get_metadata_routing(self)` | medium | 28 | 有逻辑 |
| 15 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.pipeline.FeatureUnion.__sklearn_tags__(self)` | medium | 14 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `Pipeline`

**完全限定名**: `sklearn.pipeline.Pipeline`

**文件路径**: `sklearn/pipeline.py`

**公共方法数**: 25

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, steps, transform_input = None, memory = N...` | `None` | `sklearn.pipeline.Pipeline.__init__(self, steps, transform_input = None, memory = None, verbose = False)` | simple | 5 | 魔术方法 |
| 2 | `set_output` | instance | `self, transform = None` | `None` | `sklearn.pipeline.Pipeline.set_output(self, transform = None)` | medium | 26 | 有逻辑 |
| 3 | `get_params` | instance | `self, deep = True` | `None` | `sklearn.pipeline.Pipeline.get_params(self, deep = True)` | medium | 18 | 有逻辑 |
| 4 | `set_params` | instance | `self, **kwargs` | `None` | `sklearn.pipeline.Pipeline.set_params(self, **kwargs)` | medium | 21 | - |
| 5 | `__len__` | instance | `self` | `None` | `sklearn.pipeline.Pipeline.__len__(self)` | simple | 5 | 魔术方法 |
| 6 | `__getitem__` | instance | `self, ind` | `None` | `sklearn.pipeline.Pipeline.__getitem__(self, ind)` | medium | 25 | 魔术方法, 抛异常, 有逻辑 |
| 7 | `named_steps` | property | `self` | `None` | `sklearn.pipeline.Pipeline.named_steps(self)` | simple | 7 | - |
| 8 | `fit` | instance | `self, X, y = None, **params` | `None` | `sklearn.pipeline.Pipeline.fit(self, X, y = None, **params)` | complex | 58 | 抛异常, 有逻辑 |
| 9 | `fit_transform` | instance | `self, X, y = None, **params` | `None` | `sklearn.pipeline.Pipeline.fit_transform(self, X, y = None, **params)` | complex | 59 | 有逻辑 |
| 10 | `predict` | instance | `self, X, **params` | `None` | `sklearn.pipeline.Pipeline.predict(self, X, **params)` | complex | 55 | 有逻辑 |
| 11 | `fit_predict` | instance | `self, X, y = None, **params` | `None` | `sklearn.pipeline.Pipeline.fit_predict(self, X, y = None, **params)` | complex | 55 | 有逻辑 |
| 12 | `predict_proba` | instance | `self, X, **params` | `None` | `sklearn.pipeline.Pipeline.predict_proba(self, X, **params)` | complex | 52 | 有逻辑 |
| 13 | `decision_function` | instance | `self, X, **params` | `None` | `sklearn.pipeline.Pipeline.decision_function(self, X, **params)` | complex | 45 | 有逻辑 |
| 14 | `score_samples` | instance | `self, X` | `None` | `sklearn.pipeline.Pipeline.score_samples(self, X)` | medium | 24 | 有逻辑 |
| 15 | `predict_log_proba` | instance | `self, X, **params` | `None` | `sklearn.pipeline.Pipeline.predict_log_proba(self, X, **params)` | complex | 53 | 有逻辑 |
| 16 | `transform` | instance | `self, X, **params` | `None` | `sklearn.pipeline.Pipeline.transform(self, X, **params)` | complex | 42 | 有逻辑 |
| 17 | `inverse_transform` | instance | `self, X, **params` | `None` | `sklearn.pipeline.Pipeline.inverse_transform(self, X, **params)` | complex | 39 | 有逻辑 |
| 18 | `score` | instance | `self, X, y = None, sample_weight = None, **params` | `None` | `sklearn.pipeline.Pipeline.score(self, X, y = None, sample_weight = None, **params)` | complex | 55 | 有逻辑 |
| 19 | `classes_` | property | `self` | `None` | `sklearn.pipeline.Pipeline.classes_(self)` | simple | 3 | 有逻辑 |
| 20 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.pipeline.Pipeline.__sklearn_tags__(self)` | medium | 39 | 魔术方法, 有逻辑 |
| 21 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.pipeline.Pipeline.get_feature_names_out(self, input_features = None)` | medium | 25 | 抛异常, 有逻辑 |
| 22 | `n_features_in_` | property | `self` | `None` | `sklearn.pipeline.Pipeline.n_features_in_(self)` | simple | 4 | - |
| 23 | `feature_names_in_` | property | `self` | `None` | `sklearn.pipeline.Pipeline.feature_names_in_(self)` | simple | 4 | - |
| 24 | `__sklearn_is_fitted__` | instance | `self` | `None` | `sklearn.pipeline.Pipeline.__sklearn_is_fitted__(self)` | medium | 28 | 魔术方法, 有逻辑 |
| 25 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.pipeline.Pipeline.get_metadata_routing(self)` | complex | 74 | 有逻辑 |

---

## 🔹 `Binarizer`

**完全限定名**: `sklearn.preprocessing._data.Binarizer`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, threshold = 0.0, copy = True` | `None` | `sklearn.preprocessing._data.Binarizer.__init__(self, threshold = 0.0, copy = True)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.Binarizer.fit(self, X, y = None)` | medium | 21 | - |
| 3 | `transform` | instance | `self, X, copy = None` | `None` | `sklearn.preprocessing._data.Binarizer.transform(self, X, copy = None)` | medium | 30 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.Binarizer.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `KernelCenterer`

**完全限定名**: `sklearn.preprocessing._data.KernelCenterer`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, K, y = None` | `None` | `sklearn.preprocessing._data.KernelCenterer.fit(self, K, y = None)` | medium | 30 | 抛异常, 有逻辑 |
| 2 | `transform` | instance | `self, K, copy = True` | `None` | `sklearn.preprocessing._data.KernelCenterer.transform(self, K, copy = True)` | medium | 36 | - |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.KernelCenterer.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `MaxAbsScaler`

**完全限定名**: `sklearn.preprocessing._data.MaxAbsScaler`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, copy = True, clip = False` | `None` | `sklearn.preprocessing._data.MaxAbsScaler.__init__(self, copy = True, clip = False)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.MaxAbsScaler.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.MaxAbsScaler.partial_fit(self, X, y = None)` | complex | 48 | 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.MaxAbsScaler.transform(self, X)` | complex | 45 | 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.MaxAbsScaler.inverse_transform(self, X)` | medium | 31 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.MaxAbsScaler.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `MinMaxScaler`

**完全限定名**: `sklearn.preprocessing._data.MinMaxScaler`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, feature_range = (0, 1), copy = True, clip...` | `None` | `sklearn.preprocessing._data.MinMaxScaler.__init__(self, feature_range = (0, 1), copy = True, clip = False)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.MinMaxScaler.fit(self, X, y = None)` | medium | 20 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.MinMaxScaler.partial_fit(self, X, y = None)` | complex | 70 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.MinMaxScaler.transform(self, X)` | complex | 40 | 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.MinMaxScaler.inverse_transform(self, X)` | medium | 28 | - |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.MinMaxScaler.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `Normalizer`

**完全限定名**: `sklearn.preprocessing._data.Normalizer`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, norm = 'l2', copy = True` | `None` | `sklearn.preprocessing._data.Normalizer.__init__(self, norm = 'l2', copy = True)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.Normalizer.fit(self, X, y = None)` | medium | 21 | 有逻辑 |
| 3 | `transform` | instance | `self, X, copy = None` | `None` | `sklearn.preprocessing._data.Normalizer.transform(self, X, copy = None)` | medium | 22 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.Normalizer.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `PowerTransformer`

**完全限定名**: `sklearn.preprocessing._data.PowerTransformer`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, method = 'yeo-johnson', standardize = Tru...` | `None` | `sklearn.preprocessing._data.PowerTransformer.__init__(self, method = 'yeo-johnson', standardize = True, copy = True)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.PowerTransformer.fit(self, X, y = None)` | medium | 21 | 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.PowerTransformer.fit_transform(self, X, y = None)` | medium | 18 | 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.PowerTransformer.transform(self, X)` | medium | 28 | 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.PowerTransformer.inverse_transform(self, X)` | complex | 58 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.PowerTransformer.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `QuantileTransformer`

**完全限定名**: `sklearn.preprocessing._data.QuantileTransformer`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_quantiles = 1000, output_distribution =...` | `None` | `sklearn.preprocessing._data.QuantileTransformer.__init__(self, n_quantiles = 1000, output_distribution = 'uniform', ignore_implicit_zeros = False, subsample = 10000, random_state = None, copy = True)` | medium | 16 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.QuantileTransformer.fit(self, X, y = None)` | complex | 47 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.QuantileTransformer.transform(self, X)` | medium | 20 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.QuantileTransformer.inverse_transform(self, X)` | medium | 22 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.QuantileTransformer.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `RobustScaler`

**完全限定名**: `sklearn.preprocessing._data.RobustScaler`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, with_centering = True, with_scaling = Tru...` | `None` | `sklearn.preprocessing._data.RobustScaler.__init__(self, with_centering = True, with_scaling = True, quantile_range = (25.0, 75.0), copy = True, unit_variance = False)` | medium | 14 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._data.RobustScaler.fit(self, X, y = None)` | complex | 66 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.RobustScaler.transform(self, X)` | complex | 34 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._data.RobustScaler.inverse_transform(self, X)` | medium | 32 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.RobustScaler.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `StandardScaler`

**完全限定名**: `sklearn.preprocessing._data.StandardScaler`

**文件路径**: `sklearn/preprocessing/_data.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, copy = True, with_mean = True, with_std =...` | `None` | `sklearn.preprocessing._data.StandardScaler.__init__(self, copy = True, with_mean = True, with_std = True)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.preprocessing._data.StandardScaler.fit(self, X, y = None, sample_weight = None)` | medium | 26 | 有逻辑 |
| 3 | `partial_fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.preprocessing._data.StandardScaler.partial_fit(self, X, y = None, sample_weight = None)` | complex | 147 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, X, copy = None` | `None` | `sklearn.preprocessing._data.StandardScaler.transform(self, X, copy = None)` | complex | 44 | 抛异常, 有逻辑 |
| 5 | `inverse_transform` | instance | `self, X, copy = None` | `None` | `sklearn.preprocessing._data.StandardScaler.inverse_transform(self, X, copy = None)` | complex | 43 | 抛异常, 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._data.StandardScaler.__sklearn_tags__(self)` | simple | 7 | 魔术方法 |

---

## 🔹 `KBinsDiscretizer`

**完全限定名**: `sklearn.preprocessing._discretization.KBinsDiscretizer`

**文件路径**: `sklearn/preprocessing/_discretization.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_bins = 5, encode = 'onehot', strategy =...` | `None` | `sklearn.preprocessing._discretization.KBinsDiscretizer.__init__(self, n_bins = 5, encode = 'onehot', strategy = 'quantile', quantile_method = 'warn', dtype = None, subsample = 200000, random_state = None)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.preprocessing._discretization.KBinsDiscretizer.fit(self, X, y = None, sample_weight = None)` | complex | 180 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._discretization.KBinsDiscretizer.transform(self, X)` | medium | 38 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._discretization.KBinsDiscretizer.inverse_transform(self, X)` | medium | 38 | 抛异常, 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.preprocessing._discretization.KBinsDiscretizer.get_feature_names_out(self, input_features = None)` | medium | 27 | 有逻辑 |

---

## 🔹 `OneHotEncoder`

**完全限定名**: `sklearn.preprocessing._encoders.OneHotEncoder`

**文件路径**: `sklearn/preprocessing/_encoders.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, categories = 'auto', drop = None, sparse_...` | `None` | `sklearn.preprocessing._encoders.OneHotEncoder.__init__(self, categories = 'auto', drop = None, sparse_output = True, dtype = np.float64, handle_unknown = 'error', min_frequency = None, max_categories = None, feature_name_combiner = 'concat')` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._encoders.OneHotEncoder.fit(self, X, y = None)` | medium | 26 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._encoders.OneHotEncoder.transform(self, X)` | complex | 86 | 抛异常, 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._encoders.OneHotEncoder.inverse_transform(self, X)` | complex | 118 | 抛异常, 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.preprocessing._encoders.OneHotEncoder.get_feature_names_out(self, input_features = None)` | medium | 34 | 有逻辑 |

---

## 🔹 `OrdinalEncoder`

**完全限定名**: `sklearn.preprocessing._encoders.OrdinalEncoder`

**文件路径**: `sklearn/preprocessing/_encoders.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, categories = 'auto', dtype = np.float64, ...` | `None` | `sklearn.preprocessing._encoders.OrdinalEncoder.__init__(self, categories = 'auto', dtype = np.float64, handle_unknown = 'error', unknown_value = None, encoded_missing_value = np.nan, min_frequency = None, max_categories = None)` | medium | 18 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._encoders.OrdinalEncoder.fit(self, X, y = None)` | complex | 107 | 抛异常, 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._encoders.OrdinalEncoder.transform(self, X)` | medium | 31 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._encoders.OrdinalEncoder.inverse_transform(self, X)` | complex | 85 | 抛异常, 有逻辑 |

---

## 🔹 `FunctionTransformer`

**完全限定名**: `sklearn.preprocessing._function_transformer.FunctionTransformer`

**文件路径**: `sklearn/preprocessing/_function_transformer.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, func = None, inverse_func = None, validat...` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.__init__(self, func = None, inverse_func = None, validate = False, accept_sparse = False, check_inverse = True, feature_names_out = None, kw_args = None, inv_kw_args = None)` | medium | 20 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.fit(self, X, y = None)` | medium | 29 | 有逻辑 |
| 3 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.transform(self, X)` | complex | 73 | 抛异常, 有逻辑 |
| 4 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.inverse_transform(self, X)` | medium | 17 | 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.get_feature_names_out(self, input_features = None)` | complex | 46 | 抛异常, 有逻辑 |
| 6 | `__sklearn_is_fitted__` | instance | `self` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.__sklearn_is_fitted__(self)` | simple | 3 | 魔术方法 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 8 | `set_output` | instance | `self, transform = None` | `None` | `sklearn.preprocessing._function_transformer.FunctionTransformer.set_output(self, transform = None)` | medium | 29 | 有逻辑 |

---

## 🔹 `LabelBinarizer`

**完全限定名**: `sklearn.preprocessing._label.LabelBinarizer`

**文件路径**: `sklearn/preprocessing/_label.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, neg_label = 0, pos_label = 1, sparse_outp...` | `None` | `sklearn.preprocessing._label.LabelBinarizer.__init__(self, neg_label = 0, pos_label = 1, sparse_output = False)` | simple | 4 | 魔术方法 |
| 2 | `fit` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelBinarizer.fit(self, y)` | complex | 48 | 抛异常, 有逻辑 |
| 3 | `fit_transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelBinarizer.fit_transform(self, y)` | medium | 21 | 有逻辑 |
| 4 | `transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelBinarizer.transform(self, y)` | complex | 42 | 抛异常, 有逻辑 |
| 5 | `inverse_transform` | instance | `self, Y, threshold = None` | `None` | `sklearn.preprocessing._label.LabelBinarizer.inverse_transform(self, Y, threshold = None)` | complex | 58 | 抛异常, 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._label.LabelBinarizer.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `LabelEncoder`

**完全限定名**: `sklearn.preprocessing._label.LabelEncoder`

**文件路径**: `sklearn/preprocessing/_label.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `fit` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelEncoder.fit(self, y)` | medium | 16 | - |
| 2 | `fit_transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelEncoder.fit_transform(self, y)` | medium | 16 | - |
| 3 | `transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelEncoder.transform(self, y)` | medium | 21 | 有逻辑 |
| 4 | `inverse_transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.LabelEncoder.inverse_transform(self, y)` | medium | 29 | 抛异常, 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._label.LabelEncoder.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `MultiLabelBinarizer`

**完全限定名**: `sklearn.preprocessing._label.MultiLabelBinarizer`

**文件路径**: `sklearn/preprocessing/_label.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, classes = None, sparse_output = False` | `None` | `sklearn.preprocessing._label.MultiLabelBinarizer.__init__(self, classes = None, sparse_output = False)` | simple | 3 | 魔术方法 |
| 2 | `fit` | instance | `self, y` | `None` | `sklearn.preprocessing._label.MultiLabelBinarizer.fit(self, y)` | medium | 31 | 抛异常, 有逻辑 |
| 3 | `fit_transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.MultiLabelBinarizer.fit_transform(self, y)` | medium | 42 | 有逻辑 |
| 4 | `transform` | instance | `self, y` | `None` | `sklearn.preprocessing._label.MultiLabelBinarizer.transform(self, y)` | medium | 25 | 有逻辑 |
| 5 | `inverse_transform` | instance | `self, yt` | `None` | `sklearn.preprocessing._label.MultiLabelBinarizer.inverse_transform(self, yt)` | complex | 40 | 抛异常, 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._label.MultiLabelBinarizer.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `PolynomialFeatures`

**完全限定名**: `sklearn.preprocessing._polynomial.PolynomialFeatures`

**文件路径**: `sklearn/preprocessing/_polynomial.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, degree = 2, interaction_only = False, inc...` | `None` | `sklearn.preprocessing._polynomial.PolynomialFeatures.__init__(self, degree = 2, interaction_only = False, include_bias = True, order = 'C')` | simple | 7 | 魔术方法 |
| 2 | `powers_` | property | `self` | `None` | `sklearn.preprocessing._polynomial.PolynomialFeatures.powers_(self)` | medium | 14 | 有逻辑 |
| 3 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.preprocessing._polynomial.PolynomialFeatures.get_feature_names_out(self, input_features = None)` | complex | 38 | 有逻辑 |
| 4 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.preprocessing._polynomial.PolynomialFeatures.fit(self, X, y = None)` | complex | 95 | 抛异常, 有逻辑 |
| 5 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._polynomial.PolynomialFeatures.transform(self, X)` | complex | 184 | 抛异常, 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._polynomial.PolynomialFeatures.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `SplineTransformer`

**完全限定名**: `sklearn.preprocessing._polynomial.SplineTransformer`

**文件路径**: `sklearn/preprocessing/_polynomial.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_knots = 5, degree = 3, knots = 'uniform...` | `None` | `sklearn.preprocessing._polynomial.SplineTransformer.__init__(self, n_knots = 5, degree = 3, knots = 'uniform', extrapolation = 'constant', include_bias = True, order = 'C', handle_missing = 'error', sparse_output = False)` | medium | 20 | 魔术方法 |
| 2 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.preprocessing._polynomial.SplineTransformer.get_feature_names_out(self, input_features = None)` | medium | 29 | 有逻辑 |
| 3 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.preprocessing._polynomial.SplineTransformer.fit(self, X, y = None, sample_weight = None)` | complex | 142 | 抛异常, 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._polynomial.SplineTransformer.transform(self, X)` | complex | 273 | 抛异常, 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._polynomial.SplineTransformer.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `TargetEncoder`

**完全限定名**: `sklearn.preprocessing._target_encoder.TargetEncoder`

**文件路径**: `sklearn/preprocessing/_target_encoder.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, categories = 'auto', target_type = 'auto'...` | `None` | `sklearn.preprocessing._target_encoder.TargetEncoder.__init__(self, categories = 'auto', target_type = 'auto', smooth = 'auto', cv = 5, shuffle = True, random_state = None)` | medium | 15 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.preprocessing._target_encoder.TargetEncoder.fit(self, X, y)` | medium | 26 | 有逻辑 |
| 3 | `fit_transform` | instance | `self, X, y` | `None` | `sklearn.preprocessing._target_encoder.TargetEncoder.fit_transform(self, X, y)` | complex | 79 | 有逻辑 |
| 4 | `transform` | instance | `self, X` | `None` | `sklearn.preprocessing._target_encoder.TargetEncoder.transform(self, X)` | complex | 44 | 有逻辑 |
| 5 | `get_feature_names_out` | instance | `self, input_features = None` | `None` | `sklearn.preprocessing._target_encoder.TargetEncoder.get_feature_names_out(self, input_features = None)` | medium | 28 | 有逻辑 |
| 6 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.preprocessing._target_encoder.TargetEncoder.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `BaseRandomProjection`

**完全限定名**: `sklearn.random_projection.BaseRandomProjection`

**文件路径**: `sklearn/random_projection.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 'auto', eps = 0.1, compute...` | `None` | `sklearn.random_projection.BaseRandomProjection.__init__(self, n_components = 'auto', eps = 0.1, compute_inverse_components = False, random_state = None)` | medium | 12 | 魔术方法, 抽象方法 |
| 2 | `fit` | instance | `self, X, y = None` | `None` | `sklearn.random_projection.BaseRandomProjection.fit(self, X, y = None)` | complex | 66 | 抛异常, 有逻辑 |
| 3 | `inverse_transform` | instance | `self, X` | `None` | `sklearn.random_projection.BaseRandomProjection.inverse_transform(self, X)` | medium | 28 | 有逻辑 |
| 4 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.random_projection.BaseRandomProjection.__sklearn_tags__(self)` | simple | 5 | 魔术方法 |

---

## 🔹 `GaussianRandomProjection`

**完全限定名**: `sklearn.random_projection.GaussianRandomProjection`

**文件路径**: `sklearn/random_projection.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 'auto', eps = 0.1, compute...` | `None` | `sklearn.random_projection.GaussianRandomProjection.__init__(self, n_components = 'auto', eps = 0.1, compute_inverse_components = False, random_state = None)` | medium | 14 | 魔术方法 |
| 2 | `transform` | instance | `self, X` | `None` | `sklearn.random_projection.GaussianRandomProjection.transform(self, X)` | medium | 23 | - |

---

## 🔹 `SparseRandomProjection`

**完全限定名**: `sklearn.random_projection.SparseRandomProjection`

**文件路径**: `sklearn/random_projection.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, n_components = 'auto', density = 'auto', ...` | `None` | `sklearn.random_projection.SparseRandomProjection.__init__(self, n_components = 'auto', density = 'auto', eps = 0.1, dense_output = False, compute_inverse_components = False, random_state = None)` | medium | 19 | 魔术方法 |
| 2 | `transform` | instance | `self, X` | `None` | `sklearn.random_projection.SparseRandomProjection.transform(self, X)` | medium | 24 | - |

---

## 🔹 `BaseLabelPropagation`

**完全限定名**: `sklearn.semi_supervised._label_propagation.BaseLabelPropagation`

**文件路径**: `sklearn/semi_supervised/_label_propagation.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = 'rbf', gamma = 20, n_neighbors =...` | `None` | `sklearn.semi_supervised._label_propagation.BaseLabelPropagation.__init__(self, kernel = 'rbf', gamma = 20, n_neighbors = 7, alpha = 1, max_iter = 30, tol = 0.001, n_jobs = None)` | medium | 23 | 魔术方法 |
| 2 | `predict` | instance | `self, X` | `None` | `sklearn.semi_supervised._label_propagation.BaseLabelPropagation.predict(self, X)` | medium | 19 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X` | `None` | `sklearn.semi_supervised._label_propagation.BaseLabelPropagation.predict_proba(self, X)` | complex | 40 | 有逻辑 |
| 4 | `fit` | instance | `self, X, y` | `None` | `sklearn.semi_supervised._label_propagation.BaseLabelPropagation.fit(self, X, y)` | complex | 103 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.semi_supervised._label_propagation.BaseLabelPropagation.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `LabelPropagation`

**完全限定名**: `sklearn.semi_supervised._label_propagation.LabelPropagation`

**文件路径**: `sklearn/semi_supervised/_label_propagation.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = 'rbf', gamma = 20, n_neighbors =...` | `None` | `sklearn.semi_supervised._label_propagation.LabelPropagation.__init__(self, kernel = 'rbf', gamma = 20, n_neighbors = 7, max_iter = 1000, tol = 0.001, n_jobs = None)` | medium | 19 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.semi_supervised._label_propagation.LabelPropagation.fit(self, X, y)` | medium | 20 | - |

---

## 🔹 `LabelSpreading`

**完全限定名**: `sklearn.semi_supervised._label_propagation.LabelSpreading`

**文件路径**: `sklearn/semi_supervised/_label_propagation.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = 'rbf', gamma = 20, n_neighbors =...` | `None` | `sklearn.semi_supervised._label_propagation.LabelSpreading.__init__(self, kernel = 'rbf', gamma = 20, n_neighbors = 7, alpha = 0.2, max_iter = 30, tol = 0.001, n_jobs = None)` | medium | 21 | 魔术方法 |

---

## 🔹 `SelfTrainingClassifier`

**完全限定名**: `sklearn.semi_supervised._self_training.SelfTrainingClassifier`

**文件路径**: `sklearn/semi_supervised/_self_training.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, estimator = None, threshold = 0.75, crite...` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.__init__(self, estimator = None, threshold = 0.75, criterion = 'threshold', k_best = 10, max_iter = 10, verbose = False)` | medium | 15 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, **params` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.fit(self, X, y, **params)` | complex | 134 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X, **params` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.predict(self, X, **params)` | complex | 40 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X, **params` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.predict_proba(self, X, **params)` | complex | 41 | 有逻辑 |
| 5 | `decision_function` | instance | `self, X, **params` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.decision_function(self, X, **params)` | complex | 43 | 有逻辑 |
| 6 | `predict_log_proba` | instance | `self, X, **params` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.predict_log_proba(self, X, **params)` | complex | 43 | 有逻辑 |
| 7 | `score` | instance | `self, X, y, **params` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.score(self, X, y, **params)` | complex | 43 | 有逻辑 |
| 8 | `get_metadata_routing` | instance | `self` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.get_metadata_routing(self)` | medium | 29 | - |
| 9 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.semi_supervised._self_training.SelfTrainingClassifier.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `BaseLibSVM`

**完全限定名**: `sklearn.svm._base.BaseLibSVM`

**文件路径**: `sklearn/svm/_base.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel, degree, gamma, coef0, tol, C, nu,...` | `None` | `sklearn.svm._base.BaseLibSVM.__init__(self, kernel, degree, gamma, coef0, tol, C, nu, epsilon, shrinking, probability, cache_size, class_weight, verbose, max_iter, random_state)` | complex | 38 | 魔术方法, 抽象方法, 抛异常, 有逻辑 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.svm._base.BaseLibSVM.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |
| 3 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.svm._base.BaseLibSVM.fit(self, X, y, sample_weight = None)` | complex | 140 | 抛异常, 有逻辑 |
| 4 | `predict` | instance | `self, X` | `None` | `sklearn.svm._base.BaseLibSVM.predict(self, X)` | medium | 19 | 有逻辑 |
| 5 | `coef_` | property | `self` | `None` | `sklearn.svm._base.BaseLibSVM.coef_(self)` | medium | 21 | 抛异常, 有逻辑 |
| 6 | `n_support_` | property | `self` | `None` | `sklearn.svm._base.BaseLibSVM.n_support_(self)` | medium | 14 | 抛异常, 有逻辑 |

---

## 🔹 `BaseSVC`

**完全限定名**: `sklearn.svm._base.BaseSVC`

**文件路径**: `sklearn/svm/_base.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel, degree, gamma, coef0, tol, C, nu,...` | `None` | `sklearn.svm._base.BaseSVC.__init__(self, kernel, degree, gamma, coef0, tol, C, nu, shrinking, probability, cache_size, class_weight, verbose, max_iter, decision_function_shape, random_state, break_ties)` | complex | 38 | 魔术方法, 抽象方法 |
| 2 | `decision_function` | instance | `self, X` | `None` | `sklearn.svm._base.BaseSVC.decision_function(self, X)` | medium | 31 | 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.svm._base.BaseSVC.predict(self, X)` | medium | 32 | 抛异常, 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.svm._base.BaseSVC.predict_proba(self, X)` | complex | 35 | 抛异常, 有逻辑 |
| 5 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.svm._base.BaseSVC.predict_log_proba(self, X)` | medium | 28 | 有逻辑 |
| 6 | `probA_` | property | `self` | `None` | `sklearn.svm._base.BaseSVC.probA_(self)` | simple | 8 | - |
| 7 | `probB_` | property | `self` | `None` | `sklearn.svm._base.BaseSVC.probB_(self)` | simple | 8 | - |
| 8 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.svm._base.BaseSVC.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `LinearSVC`

**完全限定名**: `sklearn.svm._classes.LinearSVC`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, penalty = 'l2', loss = 'squared_hinge', d...` | `None` | `sklearn.svm._classes.LinearSVC.__init__(self, penalty = 'l2', loss = 'squared_hinge', dual = 'auto', tol = 0.0001, C = 1.0, multi_class = 'ovr', fit_intercept = True, intercept_scaling = 1, class_weight = None, verbose = 0, random_state = None, max_iter = 1000)` | medium | 28 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.svm._classes.LinearSVC.fit(self, X, y, sample_weight = None)` | complex | 70 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.svm._classes.LinearSVC.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `LinearSVR`

**完全限定名**: `sklearn.svm._classes.LinearSVR`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, epsilon = 0.0, tol = 0.0001, C = 1.0, los...` | `None` | `sklearn.svm._classes.LinearSVR.__init__(self, epsilon = 0.0, tol = 0.0001, C = 1.0, loss = 'epsilon_insensitive', fit_intercept = True, intercept_scaling = 1.0, dual = 'auto', verbose = 0, random_state = None, max_iter = 1000)` | medium | 24 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.svm._classes.LinearSVR.fit(self, X, y, sample_weight = None)` | complex | 62 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.svm._classes.LinearSVR.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `NuSVC`

**完全限定名**: `sklearn.svm._classes.NuSVC`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, nu = 0.5, kernel = 'rbf', degree = 3, gam...` | `None` | `sklearn.svm._classes.NuSVC.__init__(self, nu = 0.5, kernel = 'rbf', degree = 3, gamma = 'scale', coef0 = 0.0, shrinking = True, probability = False, tol = 0.001, cache_size = 200, class_weight = None, verbose = False, max_iter = -1, decision_function_shape = 'ovr', break_ties = False, random_state = None)` | complex | 37 | 魔术方法 |

---

## 🔹 `NuSVR`

**完全限定名**: `sklearn.svm._classes.NuSVR`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, nu = 0.5, C = 1.0, kernel = 'rbf', degree...` | `None` | `sklearn.svm._classes.NuSVR.__init__(self, nu = 0.5, C = 1.0, kernel = 'rbf', degree = 3, gamma = 'scale', coef0 = 0.0, shrinking = True, tol = 0.001, cache_size = 200, verbose = False, max_iter = -1)` | complex | 32 | 魔术方法 |

---

## 🔹 `OneClassSVM`

**完全限定名**: `sklearn.svm._classes.OneClassSVM`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = 'rbf', degree = 3, gamma = 'scal...` | `None` | `sklearn.svm._classes.OneClassSVM.__init__(self, kernel = 'rbf', degree = 3, gamma = 'scale', coef0 = 0.0, tol = 0.001, nu = 0.5, shrinking = True, cache_size = 200, verbose = False, max_iter = -1)` | complex | 31 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y = None, sample_weight = None` | `None` | `sklearn.svm._classes.OneClassSVM.fit(self, X, y = None, sample_weight = None)` | medium | 28 | 有逻辑 |
| 3 | `decision_function` | instance | `self, X` | `None` | `sklearn.svm._classes.OneClassSVM.decision_function(self, X)` | medium | 17 | 有逻辑 |
| 4 | `score_samples` | instance | `self, X` | `None` | `sklearn.svm._classes.OneClassSVM.score_samples(self, X)` | medium | 14 | - |
| 5 | `predict` | instance | `self, X` | `None` | `sklearn.svm._classes.OneClassSVM.predict(self, X)` | medium | 19 | 有逻辑 |

---

## 🔹 `SVC`

**完全限定名**: `sklearn.svm._classes.SVC`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, C = 1.0, kernel = 'rbf', degree = 3, gamm...` | `None` | `sklearn.svm._classes.SVC.__init__(self, C = 1.0, kernel = 'rbf', degree = 3, gamma = 'scale', coef0 = 0.0, shrinking = True, probability = False, tol = 0.001, cache_size = 200, class_weight = None, verbose = False, max_iter = -1, decision_function_shape = 'ovr', break_ties = False, random_state = None)` | complex | 37 | 魔术方法 |

---

## 🔹 `SVR`

**完全限定名**: `sklearn.svm._classes.SVR`

**文件路径**: `sklearn/svm/_classes.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, kernel = 'rbf', degree = 3, gamma = 'scal...` | `None` | `sklearn.svm._classes.SVR.__init__(self, kernel = 'rbf', degree = 3, gamma = 'scale', coef0 = 0.0, tol = 0.001, C = 1.0, epsilon = 0.1, shrinking = True, cache_size = 200, verbose = False, max_iter = -1)` | complex | 32 | 魔术方法 |

---

## 🔹 `BaseDecisionTree`

**完全限定名**: `sklearn.tree._classes.BaseDecisionTree`

**文件路径**: `sklearn/tree/_classes.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, criterion, splitter, max_depth, min_sampl...` | `None` | `sklearn.tree._classes.BaseDecisionTree.__init__(self, criterion, splitter, max_depth, min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_features, max_leaf_nodes, random_state, min_impurity_decrease, class_weight = None, ccp_alpha = 0.0, monotonic_cst = None)` | medium | 30 | 魔术方法, 抽象方法 |
| 2 | `get_depth` | instance | `self` | `None` | `sklearn.tree._classes.BaseDecisionTree.get_depth(self)` | medium | 13 | - |
| 3 | `get_n_leaves` | instance | `self` | `None` | `sklearn.tree._classes.BaseDecisionTree.get_n_leaves(self)` | simple | 10 | - |
| 4 | `predict` | instance | `self, X, check_input = True` | `None` | `sklearn.tree._classes.BaseDecisionTree.predict(self, X, check_input = True)` | complex | 50 | 有逻辑 |
| 5 | `apply` | instance | `self, X, check_input = True` | `None` | `sklearn.tree._classes.BaseDecisionTree.apply(self, X, check_input = True)` | medium | 27 | 有逻辑 |
| 6 | `decision_path` | instance | `self, X, check_input = True` | `None` | `sklearn.tree._classes.BaseDecisionTree.decision_path(self, X, check_input = True)` | medium | 24 | 有逻辑 |
| 7 | `cost_complexity_pruning_path` | instance | `self, X, y, sample_weight = None` | `None` | `sklearn.tree._classes.BaseDecisionTree.cost_complexity_pruning_path(self, X, y, sample_weight = None)` | complex | 38 | 有逻辑 |
| 8 | `feature_importances_` | property | `self` | `None` | `sklearn.tree._classes.BaseDecisionTree.feature_importances_(self)` | medium | 20 | - |
| 9 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.tree._classes.BaseDecisionTree.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `DecisionTreeClassifier`

**完全限定名**: `sklearn.tree._classes.DecisionTreeClassifier`

**文件路径**: `sklearn/tree/_classes.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, criterion = 'gini', splitter = 'best', ma...` | `None` | `sklearn.tree._classes.DecisionTreeClassifier.__init__(self, criterion = 'gini', splitter = 'best', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = None, random_state = None, max_leaf_nodes = None, min_impurity_decrease = 0.0, class_weight = None, ccp_alpha = 0.0, monotonic_cst = None)` | complex | 32 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, check_input =...` | `None` | `sklearn.tree._classes.DecisionTreeClassifier.fit(self, X, y, sample_weight = None, check_input = True)` | complex | 37 | 有逻辑 |
| 3 | `predict_proba` | instance | `self, X, check_input = True` | `None` | `sklearn.tree._classes.DecisionTreeClassifier.predict_proba(self, X, check_input = True)` | complex | 36 | 有逻辑 |
| 4 | `predict_log_proba` | instance | `self, X` | `None` | `sklearn.tree._classes.DecisionTreeClassifier.predict_log_proba(self, X)` | medium | 27 | 有逻辑 |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.tree._classes.DecisionTreeClassifier.__sklearn_tags__(self)` | simple | 12 | 魔术方法, 有逻辑 |

---

## 🔹 `DecisionTreeRegressor`

**完全限定名**: `sklearn.tree._classes.DecisionTreeRegressor`

**文件路径**: `sklearn/tree/_classes.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, criterion = 'squared_error', splitter = '...` | `None` | `sklearn.tree._classes.DecisionTreeRegressor.__init__(self, criterion = 'squared_error', splitter = 'best', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = None, random_state = None, max_leaf_nodes = None, min_impurity_decrease = 0.0, ccp_alpha = 0.0, monotonic_cst = None)` | medium | 30 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, check_input =...` | `None` | `sklearn.tree._classes.DecisionTreeRegressor.fit(self, X, y, sample_weight = None, check_input = True)` | medium | 36 | 有逻辑 |
| 3 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.tree._classes.DecisionTreeRegressor.__sklearn_tags__(self)` | simple | 11 | 魔术方法, 有逻辑 |

---

## 🔹 `ExtraTreeClassifier`

**完全限定名**: `sklearn.tree._classes.ExtraTreeClassifier`

**文件路径**: `sklearn/tree/_classes.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, criterion = 'gini', splitter = 'random', ...` | `None` | `sklearn.tree._classes.ExtraTreeClassifier.__init__(self, criterion = 'gini', splitter = 'random', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = 'sqrt', random_state = None, max_leaf_nodes = None, min_impurity_decrease = 0.0, class_weight = None, ccp_alpha = 0.0, monotonic_cst = None)` | complex | 32 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.tree._classes.ExtraTreeClassifier.__sklearn_tags__(self)` | simple | 12 | 魔术方法, 有逻辑 |

---

## 🔹 `ExtraTreeRegressor`

**完全限定名**: `sklearn.tree._classes.ExtraTreeRegressor`

**文件路径**: `sklearn/tree/_classes.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, criterion = 'squared_error', splitter = '...` | `None` | `sklearn.tree._classes.ExtraTreeRegressor.__init__(self, criterion = 'squared_error', splitter = 'random', max_depth = None, min_samples_split = 2, min_samples_leaf = 1, min_weight_fraction_leaf = 0.0, max_features = 1.0, random_state = None, min_impurity_decrease = 0.0, max_leaf_nodes = None, ccp_alpha = 0.0, monotonic_cst = None)` | medium | 30 | 魔术方法 |
| 2 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.tree._classes.ExtraTreeRegressor.__sklearn_tags__(self)` | simple | 11 | 魔术方法, 有逻辑 |

---

## 🔹 `Sentinel`

**完全限定名**: `sklearn.tree._export.Sentinel`

**文件路径**: `sklearn/tree/_export.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__repr__` | instance | `self` | `None` | `sklearn.tree._export.Sentinel.__repr__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `DrawTree`

**完全限定名**: `sklearn.tree._reingold_tilford.DrawTree`

**文件路径**: `sklearn/tree/_reingold_tilford.py`

**公共方法数**: 8

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, tree, parent = None, depth = 0, number = 1` | `None` | `sklearn.tree._reingold_tilford.DrawTree.__init__(self, tree, parent = None, depth = 0, number = 1)` | medium | 15 | 魔术方法, 有逻辑 |
| 2 | `left` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.left(self)` | simple | 2 | - |
| 3 | `right` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.right(self)` | simple | 2 | - |
| 4 | `lbrother` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.lbrother(self)` | simple | 9 | 有逻辑 |
| 5 | `get_lmost_sibling` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.get_lmost_sibling(self)` | simple | 4 | 有逻辑 |
| 6 | `__str__` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.__str__(self)` | simple | 2 | 魔术方法 |
| 7 | `__repr__` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.__repr__(self)` | simple | 2 | 魔术方法 |
| 8 | `max_extents` | instance | `self` | `None` | `sklearn.tree._reingold_tilford.DrawTree.max_extents(self)` | simple | 4 | 有逻辑 |

---

## 🔹 `Tree`

**完全限定名**: `sklearn.tree._reingold_tilford.Tree`

**文件路径**: `sklearn/tree/_reingold_tilford.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, label = '', node_id = -1, *children` | `None` | `sklearn.tree._reingold_tilford.Tree.__init__(self, label = '', node_id = -1, *children)` | simple | 7 | 魔术方法, 有逻辑 |

---

## 🔹 `Bunch`

**完全限定名**: `sklearn.utils._bunch.Bunch`

**文件路径**: `sklearn/utils/_bunch.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, **kwargs` | `None` | `sklearn.utils._bunch.Bunch.__init__(self, **kwargs)` | simple | 5 | 魔术方法 |
| 2 | `__getitem__` | instance | `self, key` | `None` | `sklearn.utils._bunch.Bunch.__getitem__(self, key)` | simple | 7 | 魔术方法, 有逻辑 |
| 3 | `__setattr__` | instance | `self, key, value` | `None` | `sklearn.utils._bunch.Bunch.__setattr__(self, key, value)` | simple | 2 | 魔术方法 |
| 4 | `__dir__` | instance | `self` | `None` | `sklearn.utils._bunch.Bunch.__dir__(self)` | simple | 2 | 魔术方法 |
| 5 | `__getattr__` | instance | `self, key` | `None` | `sklearn.utils._bunch.Bunch.__getattr__(self, key)` | simple | 5 | 魔术方法, 抛异常, 有逻辑 |
| 6 | `__setstate__` | instance | `self, state` | `None` | `sklearn.utils._bunch.Bunch.__setstate__(self, state)` | simple | 10 | 魔术方法 |

---

## 🔹 `MissingValues`

**完全限定名**: `sklearn.utils._encode.MissingValues`

**文件路径**: `sklearn/utils/_encode.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `to_list` | instance | `self` | `None` | `sklearn.utils._encode.MissingValues.to_list(self)` | simple | 8 | 有逻辑 |

---

## 🔹 `MetadataRequest`

**完全限定名**: `sklearn.utils._metadata_requests.MetadataRequest`

**文件路径**: `sklearn/utils/_metadata_requests.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, owner` | `None` | `sklearn.utils._metadata_requests.MetadataRequest.__init__(self, owner)` | simple | 8 | 魔术方法, 有逻辑 |
| 2 | `consumes` | instance | `self, method, params` | `None` | `sklearn.utils._metadata_requests.MetadataRequest.consumes(self, method, params)` | medium | 24 | 有逻辑 |
| 3 | `__getattr__` | instance | `self, name` | `None` | `sklearn.utils._metadata_requests.MetadataRequest.__getattr__(self, name)` | medium | 29 | 魔术方法, 抛异常, 有逻辑 |
| 4 | `__repr__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MetadataRequest.__repr__(self)` | simple | 2 | 魔术方法 |
| 5 | `__str__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MetadataRequest.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `MetadataRouter`

**完全限定名**: `sklearn.utils._metadata_requests.MetadataRouter`

**文件路径**: `sklearn/utils/_metadata_requests.py`

**公共方法数**: 9

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, owner` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.__init__(self, owner)` | simple | 8 | 魔术方法, 有逻辑 |
| 2 | `add_self_request` | instance | `self, obj` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.add_self_request(self, obj)` | complex | 35 | 抛异常, 有逻辑 |
| 3 | `add` | instance | `self, method_mapping, **objs` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.add(self, method_mapping, **objs)` | medium | 29 | 有逻辑 |
| 4 | `consumes` | instance | `self, method, params` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.consumes(self, method, params)` | medium | 37 | 有逻辑 |
| 5 | `route_params` | instance | `self, caller, params` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.route_params(self, caller, params)` | complex | 43 | 有逻辑 |
| 6 | `validate_metadata` | instance | `self, method, params` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.validate_metadata(self, method, params)` | medium | 31 | 抛异常, 有逻辑 |
| 7 | `__iter__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.__iter__(self)` | medium | 11 | 魔术方法, 有逻辑 |
| 8 | `__repr__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.__repr__(self)` | simple | 2 | 魔术方法 |
| 9 | `__str__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MetadataRouter.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `MethodMapping`

**完全限定名**: `sklearn.utils._metadata_requests.MethodMapping`

**文件路径**: `sklearn/utils/_metadata_requests.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MethodMapping.__init__(self)` | simple | 2 | 魔术方法 |
| 2 | `__iter__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MethodMapping.__iter__(self)` | simple | 2 | 魔术方法 |
| 3 | `add` | instance | `self, caller, callee` | `None` | `sklearn.utils._metadata_requests.MethodMapping.add(self, caller, callee)` | medium | 29 | 抛异常, 有逻辑 |
| 4 | `__repr__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MethodMapping.__repr__(self)` | simple | 2 | 魔术方法 |
| 5 | `__str__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MethodMapping.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `MethodMetadataRequest`

**完全限定名**: `sklearn.utils._metadata_requests.MethodMetadataRequest`

**文件路径**: `sklearn/utils/_metadata_requests.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, owner, method, requests = None` | `None` | `sklearn.utils._metadata_requests.MethodMetadataRequest.__init__(self, owner, method, requests = None)` | simple | 4 | 魔术方法 |
| 2 | `requests` | property | `self` | `None` | `sklearn.utils._metadata_requests.MethodMetadataRequest.requests(self)` | simple | 3 | - |
| 3 | `add_request` | instance | `self, param, alias` | `None` | `sklearn.utils._metadata_requests.MethodMetadataRequest.add_request(self, param, alias)` | complex | 48 | 抛异常, 有逻辑 |
| 4 | `__repr__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MethodMetadataRequest.__repr__(self)` | simple | 2 | 魔术方法 |
| 5 | `__str__` | instance | `self` | `None` | `sklearn.utils._metadata_requests.MethodMetadataRequest.__str__(self)` | simple | 2 | 魔术方法 |

---

## 🔹 `RequestMethod`

**完全限定名**: `sklearn.utils._metadata_requests.RequestMethod`

**文件路径**: `sklearn/utils/_metadata_requests.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, name, keys, validate_keys = True` | `None` | `sklearn.utils._metadata_requests.RequestMethod.__init__(self, name, keys, validate_keys = True)` | simple | 4 | 魔术方法 |
| 2 | `__get__` | instance | `self, instance, owner` | `None` | `sklearn.utils._metadata_requests.RequestMethod.__get__(self, instance, owner)` | complex | 80 | 魔术方法, 抛异常, 有逻辑 |

---

## 🔹 `ArraySlicingWrapper`

**完全限定名**: `sklearn.utils._mocking.ArraySlicingWrapper`

**文件路径**: `sklearn/utils/_mocking.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, array` | `None` | `sklearn.utils._mocking.ArraySlicingWrapper.__init__(self, array)` | simple | 2 | 魔术方法 |
| 2 | `__getitem__` | instance | `self, aslice` | `None` | `sklearn.utils._mocking.ArraySlicingWrapper.__getitem__(self, aslice)` | simple | 2 | 魔术方法 |

---

## 🔹 `CheckingClassifier`

**完全限定名**: `sklearn.utils._mocking.CheckingClassifier`

**文件路径**: `sklearn/utils/_mocking.py`

**公共方法数**: 7

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, check_y = None, check_y_params = None, ch...` | `None` | `sklearn.utils._mocking.CheckingClassifier.__init__(self, check_y = None, check_y_params = None, check_X = None, check_X_params = None, methods_to_check = 'all', foo_param = 0, expected_sample_weight = None, expected_fit_params = None, random_state = None)` | medium | 22 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y, sample_weight = None, **fit_params` | `None` | `sklearn.utils._mocking.CheckingClassifier.fit(self, X, y, sample_weight = None, **fit_params)` | complex | 47 | 抛异常, 有逻辑 |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.utils._mocking.CheckingClassifier.predict(self, X)` | medium | 17 | 有逻辑 |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.utils._mocking.CheckingClassifier.predict_proba(self, X)` | medium | 23 | 有逻辑 |
| 5 | `decision_function` | instance | `self, X` | `None` | `sklearn.utils._mocking.CheckingClassifier.decision_function(self, X)` | medium | 26 | 有逻辑 |
| 6 | `score` | instance | `self, X = None, Y = None` | `None` | `sklearn.utils._mocking.CheckingClassifier.score(self, X = None, Y = None)` | medium | 26 | 有逻辑 |
| 7 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.utils._mocking.CheckingClassifier.__sklearn_tags__(self)` | simple | 6 | 魔术方法 |

---

## 🔹 `MockDataFrame`

**完全限定名**: `sklearn.utils._mocking.MockDataFrame`

**文件路径**: `sklearn/utils/_mocking.py`

**公共方法数**: 6

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, array` | `None` | `sklearn.utils._mocking.MockDataFrame.__init__(self, array)` | simple | 7 | 魔术方法 |
| 2 | `__len__` | instance | `self` | `None` | `sklearn.utils._mocking.MockDataFrame.__len__(self)` | simple | 2 | 魔术方法 |
| 3 | `__array__` | instance | `self, dtype = None` | `None` | `sklearn.utils._mocking.MockDataFrame.__array__(self, dtype = None)` | simple | 5 | 魔术方法 |
| 4 | `__eq__` | instance | `self, other` | `None` | `sklearn.utils._mocking.MockDataFrame.__eq__(self, other)` | simple | 2 | 魔术方法 |
| 5 | `__ne__` | instance | `self, other` | `None` | `sklearn.utils._mocking.MockDataFrame.__ne__(self, other)` | simple | 2 | 魔术方法 |
| 6 | `take` | instance | `self, indices, axis = 0` | `None` | `sklearn.utils._mocking.MockDataFrame.take(self, indices, axis = 0)` | simple | 2 | - |

---

## 🔹 `NoSampleWeightWrapper`

**完全限定名**: `sklearn.utils._mocking.NoSampleWeightWrapper`

**文件路径**: `sklearn/utils/_mocking.py`

**公共方法数**: 5

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, est = None` | `None` | `sklearn.utils._mocking.NoSampleWeightWrapper.__init__(self, est = None)` | simple | 2 | 魔术方法 |
| 2 | `fit` | instance | `self, X, y` | `None` | `sklearn.utils._mocking.NoSampleWeightWrapper.fit(self, X, y)` | simple | 2 | - |
| 3 | `predict` | instance | `self, X` | `None` | `sklearn.utils._mocking.NoSampleWeightWrapper.predict(self, X)` | simple | 2 | - |
| 4 | `predict_proba` | instance | `self, X` | `None` | `sklearn.utils._mocking.NoSampleWeightWrapper.predict_proba(self, X)` | simple | 2 | - |
| 5 | `__sklearn_tags__` | instance | `self` | `None` | `sklearn.utils._mocking.NoSampleWeightWrapper.__sklearn_tags__(self)` | simple | 4 | 魔术方法 |

---

## 🔹 `HasMethods`

**完全限定名**: `sklearn.utils._param_validation.HasMethods`

**文件路径**: `sklearn/utils/_param_validation.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, methods` | `None` | `sklearn.utils._param_validation.HasMethods.__init__(self, methods)` | simple | 5 | 魔术方法, 有逻辑 |
| 2 | `is_satisfied_by` | instance | `self, val` | `None` | `sklearn.utils._param_validation.HasMethods.is_satisfied_by(self, val)` | simple | 2 | 有逻辑 |
| 3 | `__str__` | instance | `self` | `None` | `sklearn.utils._param_validation.HasMethods.__str__(self)` | simple | 9 | 魔术方法, 有逻辑 |

---

## 🔹 `Hidden`

**完全限定名**: `sklearn.utils._param_validation.Hidden`

**文件路径**: `sklearn/utils/_param_validation.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, constraint` | `None` | `sklearn.utils._param_validation.Hidden.__init__(self, constraint)` | simple | 2 | 魔术方法 |

---

## 🔹 `Interval`

**完全限定名**: `sklearn.utils._param_validation.Interval`

**文件路径**: `sklearn/utils/_param_validation.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, type, left, right, closed` | `None` | `sklearn.utils._param_validation.Interval.__init__(self, type, left, right, closed)` | simple | 8 | 魔术方法 |
| 2 | `__contains__` | instance | `self, val` | `None` | `sklearn.utils._param_validation.Interval.__contains__(self, val)` | medium | 15 | 魔术方法, 有逻辑 |
| 3 | `is_satisfied_by` | instance | `self, val` | `None` | `sklearn.utils._param_validation.Interval.is_satisfied_by(self, val)` | simple | 5 | 有逻辑 |
| 4 | `__str__` | instance | `self` | `None` | `sklearn.utils._param_validation.Interval.__str__(self)` | medium | 17 | 魔术方法, 有逻辑 |

---

## 🔹 `MissingValues`

**完全限定名**: `sklearn.utils._param_validation.MissingValues`

**文件路径**: `sklearn/utils/_param_validation.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, numeric_only = False` | `None` | `sklearn.utils._param_validation.MissingValues.__init__(self, numeric_only = False)` | medium | 14 | 魔术方法, 有逻辑 |
| 2 | `is_satisfied_by` | instance | `self, val` | `None` | `sklearn.utils._param_validation.MissingValues.is_satisfied_by(self, val)` | simple | 2 | 有逻辑 |
| 3 | `__str__` | instance | `self` | `None` | `sklearn.utils._param_validation.MissingValues.__str__(self)` | simple | 5 | 魔术方法, 有逻辑 |

---

## 🔹 `Options`

**完全限定名**: `sklearn.utils._param_validation.Options`

**文件路径**: `sklearn/utils/_param_validation.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, type, options, deprecated = None` | `None` | `sklearn.utils._param_validation.Options.__init__(self, type, options, deprecated = None)` | simple | 8 | 魔术方法, 抛异常, 有逻辑 |
| 2 | `is_satisfied_by` | instance | `self, val` | `None` | `sklearn.utils._param_validation.Options.is_satisfied_by(self, val)` | simple | 2 | - |
| 3 | `__str__` | instance | `self` | `None` | `sklearn.utils._param_validation.Options.__str__(self)` | simple | 5 | 魔术方法, 有逻辑 |

---

## 🔹 `StrOptions`

**完全限定名**: `sklearn.utils._param_validation.StrOptions`

**文件路径**: `sklearn/utils/_param_validation.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, options, deprecated = None` | `None` | `sklearn.utils._param_validation.StrOptions.__init__(self, options, deprecated = None)` | simple | 2 | 魔术方法 |

---

## 🔹 `KeyValTuple`

**完全限定名**: `sklearn.utils._pprint.KeyValTuple`

**文件路径**: `sklearn/utils/_pprint.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__repr__` | instance | `self` | `None` | `sklearn.utils._pprint.KeyValTuple.__repr__(self)` | simple | 3 | 魔术方法, 有逻辑 |

---

## 🔹 `ParamsDict`

**完全限定名**: `sklearn.utils._repr_html.params.ParamsDict`

**文件路径**: `sklearn/utils/_repr_html/params.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, params = None, non_default = tuple(), est...` | `None` | `sklearn.utils._repr_html.params.ParamsDict.__init__(self, params = None, non_default = tuple(), estimator_class = None, doc_link = '')` | simple | 7 | 魔术方法 |

---

## 🔹 `ContainerAdapterProtocol`

**完全限定名**: `sklearn.utils._set_output.ContainerAdapterProtocol`

**文件路径**: `sklearn/utils/_set_output.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `create_container` | instance | `self, X_output, X_original, columns, inplace = ...` | `None` | `sklearn.utils._set_output.ContainerAdapterProtocol.create_container(self, X_output, X_original, columns, inplace = False)` | medium | 27 | 有逻辑 |
| 2 | `is_supported_container` | instance | `self, X` | `None` | `sklearn.utils._set_output.ContainerAdapterProtocol.is_supported_container(self, X)` | medium | 13 | 有逻辑 |
| 3 | `rename_columns` | instance | `self, X, columns` | `None` | `sklearn.utils._set_output.ContainerAdapterProtocol.rename_columns(self, X, columns)` | medium | 16 | - |
| 4 | `hstack` | instance | `self, Xs` | `None` | `sklearn.utils._set_output.ContainerAdapterProtocol.hstack(self, Xs)` | medium | 13 | - |

---

## 🔹 `ContainerAdaptersManager`

**完全限定名**: `sklearn.utils._set_output.ContainerAdaptersManager`

**文件路径**: `sklearn/utils/_set_output.py`

**公共方法数**: 3

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self` | `None` | `sklearn.utils._set_output.ContainerAdaptersManager.__init__(self)` | simple | 2 | 魔术方法 |
| 2 | `supported_outputs` | property | `self` | `None` | `sklearn.utils._set_output.ContainerAdaptersManager.supported_outputs(self)` | simple | 2 | - |
| 3 | `register` | instance | `self, adapter` | `None` | `sklearn.utils._set_output.ContainerAdaptersManager.register(self, adapter)` | simple | 2 | - |

---

## 🔹 `PandasAdapter`

**完全限定名**: `sklearn.utils._set_output.PandasAdapter`

**文件路径**: `sklearn/utils/_set_output.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `create_container` | instance | `self, X_output, X_original, columns, inplace = ...` | `None` | `sklearn.utils._set_output.PandasAdapter.create_container(self, X_output, X_original, columns, inplace = True)` | medium | 23 | 有逻辑 |
| 2 | `is_supported_container` | instance | `self, X` | `None` | `sklearn.utils._set_output.PandasAdapter.is_supported_container(self, X)` | simple | 3 | - |
| 3 | `rename_columns` | instance | `self, X, columns` | `None` | `sklearn.utils._set_output.PandasAdapter.rename_columns(self, X, columns)` | simple | 5 | - |
| 4 | `hstack` | instance | `self, Xs` | `None` | `sklearn.utils._set_output.PandasAdapter.hstack(self, Xs)` | simple | 3 | - |

---

## 🔹 `PolarsAdapter`

**完全限定名**: `sklearn.utils._set_output.PolarsAdapter`

**文件路径**: `sklearn/utils/_set_output.py`

**公共方法数**: 4

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `create_container` | instance | `self, X_output, X_original, columns, inplace = ...` | `None` | `sklearn.utils._set_output.PolarsAdapter.create_container(self, X_output, X_original, columns, inplace = True)` | simple | 12 | 有逻辑 |
| 2 | `is_supported_container` | instance | `self, X` | `None` | `sklearn.utils._set_output.PolarsAdapter.is_supported_container(self, X)` | simple | 3 | - |
| 3 | `rename_columns` | instance | `self, X, columns` | `None` | `sklearn.utils._set_output.PolarsAdapter.rename_columns(self, X, columns)` | simple | 5 | - |
| 4 | `hstack` | instance | `self, Xs` | `None` | `sklearn.utils._set_output.PolarsAdapter.hstack(self, Xs)` | simple | 3 | - |

---

## 🔹 `deprecated`

**完全限定名**: `sklearn.utils.deprecation.deprecated`

**文件路径**: `sklearn/utils/deprecation.py`

**公共方法数**: 2

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__init__` | instance | `self, extra = ''` | `None` | `sklearn.utils.deprecation.deprecated.__init__(self, extra = '')` | simple | 2 | 魔术方法 |
| 2 | `__call__` | instance | `self, obj` | `None` | `sklearn.utils.deprecation.deprecated.__call__(self, obj)` | medium | 20 | 魔术方法, 有逻辑 |

---

## 🔹 `Parallel`

**完全限定名**: `sklearn.utils.parallel.Parallel`

**文件路径**: `sklearn/utils/parallel.py`

**公共方法数**: 1

| # | 方法名 | 方法类型 | 参数 | 返回类型 | 完整签名 | 复杂度 | 行数 | 特征 |
|---|--------|---------|------|----------|----------|--------|------|------|
| 1 | `__call__` | instance | `self, iterable` | `None` | `sklearn.utils.parallel.Parallel.__call__(self, iterable)` | medium | 38 | 魔术方法, 有逻辑 |

---

