---
id: "P03"
title: "How synthetic and real training data change representations"
area: "Training"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "How does training on synthetic data + training on real data change what the model thinks?"
---

# How synthetic and real training data change representations

A lot of model training now uses synthetic data, but matching a model's outputs does not necessarily mean that we are preserving the same internal representations. I am interested in what changes inside a model when we replace human-written data with model-generated data.

There is already work on [model collapse under repeated training on generated data](https://arxiv.org/abs/2305.17493), as well as evidence that [retaining and accumulating real data can change that outcome](https://arxiv.org/abs/2404.01413). I would like to study these differences at the level of representations, rather than only looking at final task performance.

[Demystifying Synthetic Data in LLM Pre-training](https://aclanthology.org/2025.emnlp-main.544/) already compares benefits and pitfalls across synthetic-data training settings. [How to Synthesize Text Data without Model Collapse?](https://arxiv.org/abs/2412.14689) provides a further baseline for preserving useful information in generated data. These suggest studying how the data-generation method changes representations, alongside the proportion of synthetic text.

We would train comparable models on real data, synthetic data, and mixtures of both, keeping the task and training budget as similar as possible.

We would then look at:

- Which concepts or behavioral directions become stronger, weaker, or less diverse?
- Does synthetic training change how the model represents people, roles, or its own outputs?
- Do internal changes predict failures on held-out real data?
- Does adding real data back recover the original representations?
