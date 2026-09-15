---
title: What distillation changes inside a model
category: training
status: In progress
order: 2
---

# What distillation changes inside a model

[Distilled Circuits](https://arxiv.org/abs/2505.10822) studies how distillation reorganizes and compresses internal computation. [Linear feature transfer between models](https://arxiv.org/abs/2506.06609) shows that some representation alignment can also exist without distillation, giving us an important baseline.

It would be useful to extend this analysis to larger modern models and establish what extra alignment distillation produces. We are working on whether a smaller, inspectable student can serve as a useful guide to its teacher's behavior.

- Compare teacher and student representations before and after distillation on matched text.
- Vary model size and family, and compare text-only distillation with matching output probabilities.
- Track which features and circuits are preserved, reorganized or lost.
- Test whether student activations predict teacher-specific failures or intervention effects beyond what their output similarity explains.
