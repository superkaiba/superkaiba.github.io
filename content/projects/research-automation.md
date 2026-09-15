---
id: "P18"
title: "Evaluating research automation"
area: "Evaluation"
status: "Not started / proposal"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Formal evaluation of research automation"
---

# Evaluating research automation

We have benchmarks for coding and for carrying out machine-learning tasks, such as [MLAgentBench](https://arxiv.org/abs/2310.03302). But successfully running code is only one part of doing research.

I want to build a more explicit evaluation of the different skills involved in research:

- Designing an experiment that answers an important question.
- Interpreting results and noticing alternative explanations.
- Choosing the next experiment.
- Consolidating several results into a coherent picture.
- Identifying a promising next project.

The difficult part is deciding what makes an answer good. A proposal can sound convincing while failing to reduce any real uncertainty.

I propose to start with one skill and a collection of concrete research situations where we have enough information to assess the answer. For example, give a model an experiment and its results, then ask what it would run next.

We would compare its choices with simple baselines and researcher judgments, and investigate whether the evaluation rewards genuinely useful decisions or merely plausible research language.
