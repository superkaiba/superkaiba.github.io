---
id: "P22"
title: "Persona selection as Bayesian inference"
area: "Personas"
status: "In progress"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Understanding personas from the perspective of Bayesian inference"
---

# Persona selection as Bayesian inference

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) is a useful way to think about language-model behavior, but I would like a more precise account of what a persona is and how the model selects one.

A promising possibility is to treat the model as maintaining beliefs about which persona fits the context, and updating those beliefs as new evidence arrives. This connects to [in-context learning as Bayesian inference](https://arxiv.org/abs/2111.02080) and work showing that transformers can represent [belief-state geometry in their residual stream](https://arxiv.org/abs/2405.15943).

The project aims to turn this into a formal, testable account of persona selection.

We would work on:

- Defining personas through observable distributions over traits and behaviors.
- Creating contexts where we can measure how the model's beliefs about a character change.
- Testing whether those changes follow the predictions of a Bayesian model.
- Looking for an internal geometry that tracks the same beliefs and uncertainty.
- Using interventions to distinguish a causal representation from a convenient description.

Related starting points include [Belief Dynamics](https://arxiv.org/abs/2511.00617), [constrained belief updates](https://arxiv.org/abs/2502.01954), [Stories in Space](https://arxiv.org/abs/2605.12412), and [The Shape of Beliefs](https://arxiv.org/abs/2602.02315).

There is already work underway on the formalization and behavioral experiments. The broader goal is to understand whether this account can help us predict and control persona changes.
