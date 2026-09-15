---
id: "P28"
title: "Nonlinear geometry of persona representations"
area: "Personas"
status: "In progress"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Persona manifolds"
---

# Nonlinear geometry of persona representations

A lot of work on personas represents them using linear directions, as in [persona features](https://arxiv.org/abs/2506.19823) and the [assistant axis](https://arxiv.org/abs/2601.10387). These tools are useful, but they may miss structure if persona representations lie on a curved surface rather than in a simple linear subspace.

[Goodfire's work on neural geometry](https://www.goodfire.ai/research/neural-geometry) motivates investigating curved representation spaces. [Manifold steering](https://arxiv.org/abs/2605.05115) explores interventions that respect that geometry, while [Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/abs/2604.28119) examines how sparse features describe curved concepts. [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964) also uses a learned activation prior for nonlinear steering, including persona directions. These give us concrete alternatives to compare with fixed linear steering.

The goal is to characterize both individual personas and the broader structure of persona space.

We could begin with role representations collected across many questions, then:

- Compare linear dimension estimates with methods that allow curved structure.
- Look for clusters and relationships between roles.
- Track how representations move as a conversation supplies new information.
- Study whether misalignment-inducing fine-tuning moves a persona along the structure or changes the structure itself.
- Compare steering along the estimated manifold with steering in a fixed linear direction.

Ultimately, I would like to know whether understanding this geometry gives us more precise behavioral control, more natural generations, or a better account of persona drift.
