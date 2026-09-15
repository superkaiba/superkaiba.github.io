---
id: "P21"
title: "Predicting answer activations from context"
area: "Representations"
status: "Follow-up scope to confirm"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Predicting answer activations from context"
---

# Predicting answer activations from context

An LLM turns a context into an answer through many nonlinear steps. Nevertheless, my [recent paper](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) finds that a linear map can predict the answer's mean residual-stream activation from the final context activation.

This is different from [speculative decoding](https://arxiv.org/abs/2211.17192), which aims to accelerate generation by proposing tokens. Here, the interesting possibility is that we can predict something about the answer's internal representation before generating it.

The follow-up would be to understand what we can do with this prediction.

Some directions:

- Apply behavioral probes to predicted activations to anticipate what the model will do.
- Characterize which kinds of answer information are predictable and which are not.
- Study how the context-to-answer map changes during fine-tuning.
- Test whether this helps predict how training data will affect behavior.
- Compare with richer models of activation distributions, such as [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964).

The core mapping result already exists, so we would choose a specific extension rather than simply repeat that analysis.
