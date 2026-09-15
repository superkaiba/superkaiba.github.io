---
title: Persona selection as Bayesian inference
status: In progress
order: 19
---

# Persona selection as Bayesian inference

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) suggests that context helps select among learned personas. [PICLe](https://arxiv.org/abs/2405.02501) already connects persona elicitation with Bayesian inference, and work on [belief-state geometry](https://arxiv.org/abs/2405.15943) provides a concrete account of how uncertainty about a text-generating process can appear in representations.

It would be useful to turn this into a testable account of persona selection: what evidence is the model using, what uncertainty does it retain, and when do Bayesian predictions fail? Work on the formalization and behavioral experiments is underway.

- Use a known text-generating process so the intended persona and evidence are controlled.
- Vary evidence reliability, order and contradiction, and compare observed updates with explicit Bayesian baselines.
- Prompt combinations of traits and test how their effects relate to singular directions of a specified representation matrix.
- Intervene on candidate belief representations to distinguish a causal mechanism from a descriptive fit.
