---
title: Does the model simulate a grader persona?
category: safety
status: Not started
order: 3
---

# Does the model simulate a grader persona?

[Steering towards automated grading](https://www.lesswrong.com/posts/wYZMmdWEt5QLM3m3e/steering-towards-automated-grading-degrades-alignment) reports that an automated-versus-human-grader direction changes safety-relevant behavior. [Judge Circuits](https://arxiv.org/abs/2605.16023) studies internal evaluation mechanisms, while [contrastive belief updates about rewards](https://arxiv.org/abs/2607.18966) offers a way to vary what a model believes an evaluator wants.

It would be useful to know whether answering under evaluation reuses the representations involved in explicitly acting as that evaluator. Here, a grader persona means a representation of the evaluator's preferences and likely judgments, rather than evaluation awareness alone.

- Ask the model to judge fixed candidate answers under different evaluator preferences and identify corresponding features or subspaces.
- Test whether those same representations track preferences when the model answers without being asked to act as a judge.
- Transfer interventions from judging to answering, and patch naturally occurring answering states to test causal mediation.
- Separate evaluator preferences from identity, repeated rubric text, correctness and the assistant's own persona; test whether selective suppression reduces reward-seeking without impairing ordinary instruction following.
