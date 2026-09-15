# Persona selection as Bayesian inference

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) is a useful way to think about language-model behavior, but I would like a more precise account of what a persona is and how the model selects one.

A promising possibility is to treat the model as maintaining beliefs about which persona fits the context, and updating those beliefs as new evidence arrives. [In-context learning as Bayesian inference](https://arxiv.org/abs/2111.02080) develops the broader connection, while [PICLe](https://arxiv.org/abs/2405.02501) applies Bayesian persona elicitation to selecting demonstrations. [Belief Dynamics](https://arxiv.org/abs/2511.00617) models context as accumulated evidence and activation steering as a change in concept priors.

There is also evidence that transformers can represent [belief-state geometry in their residual stream](https://arxiv.org/abs/2405.15943). [The Shape of Beliefs](https://arxiv.org/abs/2602.02315) and [Stories in Space](https://arxiv.org/abs/2605.12412) connect belief updates and narratives to internal geometry. These provide concrete models and intervention methods that we can compare against.

The project aims to turn this into a formal, testable account of persona selection. We would work on:

- Defining personas through observable distributions over traits and behaviors.
- Creating contexts where we can measure how the model's beliefs about a character change.
- Testing Bayesian predictions when evidence is contradictory, unreliable, or presented in a different order.
- Looking for an internal geometry that tracks both the inferred persona and uncertainty about it.
- Using interventions to distinguish a causal representation from a convenient behavioral description.

There is already work underway on the formalization and behavioral experiments. The broader goal is to understand whether this account can help us predict and control persona changes.
