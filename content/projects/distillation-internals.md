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

[Knowledge distillation](https://arxiv.org/abs/1503.02531) trains one model to imitate another, often transferring useful behavior from a larger model to a smaller one. But matching outputs does not tell us how much of the teacher's internal computation the student preserves.

This question has already been studied in [Distilled Circuits](https://arxiv.org/abs/2505.10822), which examines how student models reorganize, compress, and discard teacher components. I want to extend this kind of analysis to **larger modern language models**, and test whether the relationships between teacher and student representations change with scale.

One possible application is a smaller, inspectable “sidecar” model that helps us understand a larger model whose internals we cannot access. [Transferring Linear Features Across Language Models](https://arxiv.org/abs/2506.06609) shows that representations can align even without distillation, so we would measure how much distillation adds beyond that existing similarity.

We would use a larger open teacher and smaller students, treating the teacher as a black box during sidecar construction while retaining its activations to check our conclusions afterward.

First steps:

- Compare teacher and student representations on the same text before distillation.
- Distill the teacher into the students and track how their representations and circuits change.
- Compare text-only distillation with matching the teacher's output probabilities.
- Vary teacher and student size, and compare models from the same and different families.
- Test whether student activations predict teacher-specific failures or intervention effects beyond what the generated text reveals.

The goal is to understand what survives distillation at larger scales, and when a student's internals are a useful guide to its teacher.
