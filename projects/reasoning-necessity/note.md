# Predicting when a task needs chain-of-thought

[AdaptThink](https://arxiv.org/abs/2505.13417) already trains reasoning models to choose between thinking and answering directly. This makes the useful question more specific than whether adaptive reasoning is possible: can the model's state before generation predict how much an explicit reasoning trace will improve its answer?

It would be useful to build a predictor of the benefit of reasoning, rather than just a predictor of task difficulty. A difficult question might remain unsolved after a long trace, while a short calculation might benefit substantially from a few extra steps.

- Compare direct answers and several reasoning budgets on the same prompts across repeated samples.
- Predict the improvement from reasoning using only prompt text or pre-generation activations.
- Compare simple probes with adaptive-thinking policies and basic difficulty heuristics.
- Test transfer across task families and report both error rates and the tokens spent to avoid them.
