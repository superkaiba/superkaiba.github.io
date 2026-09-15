---
title: How synthetic and real training data change representations
category: training
status: Not started
order: 1
---

# How synthetic and real training data change representations

Work on [model collapse](https://arxiv.org/abs/2305.17493) and [retaining real data during repeated training](https://arxiv.org/abs/2404.01413) shows that the source and reuse of training data can affect performance. [Demystifying Synthetic Data in LLM Pre-training](https://aclanthology.org/2025.emnlp-main.544/) provides further baselines for comparing synthetic-data settings.

It would be useful to understand these differences inside the model: which representations change when human-written data is replaced by generated text, and which of those changes matter for behavior?

- Train comparable models on real data, synthetic data and mixtures while matching task and training budget.
- Compare feature diversity, behavioral directions and representations of people or conversational roles.
- Test whether internal changes predict failures on held-out real data.
- Add real data back and examine which representational and behavioral changes recover.
