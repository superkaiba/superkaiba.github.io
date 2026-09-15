---
title: Which judge scores are linearly readable from activations?
category: safety
status: Not started
order: 6
---

# Which judge scores are linearly readable from activations?

[Calibrating LLM Judges](https://arxiv.org/abs/2512.22245) uses linear probes on a reasoning judge's hidden states to estimate uncertainty. This is encouraging, but confidence in a judgment is different from the judgment itself: a model can be certain about a low score, and different criteria may require different internal information.

It would be useful to characterize which scores and preferences admit simple readouts, where those readouts work, and what additional reasoning actually contributes. This could make some evaluations cheaper while identifying cases where a linear substitute loses important distinctions.

- Fit readouts for factual correctness, task success, preferences, and individual rubric criteria.
- Compare the evaluated model's activations with the judge's activations before and after deliberation.
- Separate predicting a judge's score from matching independently established correctness or human assessments.
- Test transfer across prompts, rubrics, and judges, comparing linear and nonlinear readouts at matched data budgets.
