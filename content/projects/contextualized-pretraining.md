---
title: Contextualized pretraining for more robust alignment
category: training
status: In progress
order: 3
---

# Contextualized pretraining for more robust alignment

[Source-reliability learning](https://arxiv.org/abs/2310.15047) and [inoculation prompting](https://arxiv.org/abs/2510.04340) suggest that the context surrounding training examples can affect how their information generalizes. The [Scientist AI proposal](https://lawzero.org/en/publication/scientist-ai-safe-design-not-desiring) also motivates giving models explicit information about the provenance and reliability of what they read.

It would be useful to test whether source attribution during pretraining creates better-separated representations and more robust behavior under later fine-tuning. Our preliminary attribution experiments provide a starting point; the pretraining extension needs a carefully chosen scale.

- Compare meaningful source and reliability labels with arbitrary labels and unlabeled data.
- Measure how attribution changes persona, source and belief representations.
- Apply matched later fine-tuning and test whether alignment is more robust.
- Evaluate missing, misleading and unreliable source labels to identify what the model actually learns to trust.
