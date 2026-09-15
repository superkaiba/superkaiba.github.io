---
id: "P08"
title: "Mapping context SAE features to answer SAE features"
area: "Representations"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Maps from context SAE features to answer SAE features"
---

# Mapping context SAE features to answer SAE features

My [recent context-to-answer work](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) finds that a simple map can predict aspects of the answer's activations from the final context activation. This is useful, but a prediction in the residual stream can still be difficult to interpret.

Sparse autoencoders (SAEs) try to express activations in terms of a larger set of features. I propose to investigate whether we can map **context features to answer features**, so that a prediction tells us something more understandable about what the model is likely to do.

We would begin with paired context and answer activations, encode them with SAEs, and compare a direct feature-to-feature map against mapping in the residual stream first.

We would then check:

- Which answer features are predictable before generation starts?
- Are persona and behavioral features easier to predict than details of the answer?
- Does the feature-space map make the relationship easier to explain?
- Do apparent prediction failures come from the model, or from the SAE representation?
