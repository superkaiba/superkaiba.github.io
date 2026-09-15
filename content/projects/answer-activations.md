---
id: "P21"
title: "Predicting answer activations from context"
area: "Representations"
status: "In progress"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Predicting answer activations from context"
---

# Predicting answer activations from context

An LLM turns a context into an answer through many nonlinear steps. Nevertheless, my [recent paper](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) finds that a linear map can predict the answer's mean residual-stream activation from the final context activation.

This is different from [speculative decoding](https://arxiv.org/abs/2211.17192), which aims to accelerate generation by proposing tokens. Here, the interesting possibility is that we can predict something about the answer's internal representation before generating it.

[Language Models Can Predict Their Own Behavior](https://arxiv.org/abs/2502.13329) and [Predicting Future Behaviors in Reasoning Models Enables Better Steering](https://arxiv.org/abs/2606.11172) show how internal states can support behavioral forecasts. My paper already tests some applications of predicted answer activations; the follow-up would be to understand how far this approach can go, including uncertainty about multiple possible answers.

Some directions:

- Apply behavioral probes to predicted activations to anticipate what the model will do.
- Characterize which kinds of answer information are predictable and which are not.
- Study how the context-to-answer map changes during fine-tuning.
- Test whether this helps predict how training data will affect behavior.
- Compare a predicted mean with a distribution over possible answer activations, using [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964) as a starting point for generative modeling. Its activation prior would need to be extended to condition on a context and predict future answers.

The core mapping result already exists, so we would choose a specific extension rather than simply repeat that analysis.
