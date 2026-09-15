---
title: Does predicting internal activations improve introspection?
status: Not started
order: 34
---

# Does predicting internal activations improve introspection?

Training a network to predict its own representations is a different objective from predicting the next token. [Work on learning from one's own latents](https://arxiv.org/abs/2605.27734) gives sample-efficiency results in a simplified hierarchical setting. Separately, [concept-injection experiments](https://transformer-circuits.pub/2025/introspection/index.html) suggest that some LLMs can identify certain changes to their internal states, although this ability is unreliable.

It would be useful to test whether an auxiliary activation-prediction objective improves a model's ability to report its own states and anticipate its behavior. Better prediction by an external head would not, by itself, establish better introspection by the model.

- Train matched models with and without a loss for predicting later-layer or future-token activations.
- Test whether models can identify controlled internal interventions and predict their own errors.
- Compare self-prediction with an external observer given the same text.
- Measure transfer to unseen interventions, calibration, and ordinary task performance.
