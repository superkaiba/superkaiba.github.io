---
title: Nonlinear geometry of persona representations
status: In progress
order: 21
---

# Nonlinear geometry of persona representations

[Persona features](https://arxiv.org/abs/2506.19823) and the [assistant axis](https://arxiv.org/abs/2601.10387) describe useful linear directions. [Generative modeling of LLM activations](https://arxiv.org/abs/2602.06964) supplies a way to investigate more complex geometry and interventions that stay closer to typical model states.

It would be useful to understand when personas lie along approximately linear directions and when curved structure matters for predicting or controlling behavior. This project is already in progress.

- Compare principal components with independently measured persona and belief directions.
- Diagnose negative assistant-axis scores before any conversation, separating coordinate conventions from behavioral differences.
- Track whether post-training moves representations along an existing manifold or changes its structure.
- Collect graded persona examples, fit spline-based steering paths and compare them with fixed linear interventions.
- Measure behavioral control and generation quality on prompts not used to estimate the geometry.
