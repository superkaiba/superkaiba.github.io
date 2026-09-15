---
id: "P17"
title: "What distillation changes inside a model"
area: "Training"
status: "Not started / proposal"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Understanding What Distillation Does to Model Internals"
---

# What distillation changes inside a model

[Knowledge distillation](https://arxiv.org/abs/1503.02531) trains one model to imitate another, often transferring useful behavior from a larger model to a smaller one. But what does it do to their internal representations?

One possibility is that a smaller, inspectable model could help us understand a larger model whose internals we cannot access. People sometimes call this a “sidecar” model. [Work on transferring linear features across models](https://arxiv.org/abs/2506.06609) provides a useful comparison for how much representation alignment is possible.

I propose to start with two open models, treating the larger one as a stand-in for a black box so that we can still check our conclusions.

First steps:

- Generate text from the larger model and feed the same text through the smaller model.
- Compare their representations before any distillation.
- Distill the larger model into the smaller one and track how that relationship changes.
- Compare distillation from text alone with matching the teacher's output probabilities.

We would then test whether the smaller model's internals tell us something about the teacher that we could not learn from the text alone, and whether this depends on the models being from the same family.
