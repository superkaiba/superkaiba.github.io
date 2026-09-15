---
title: Which cognitive biases do language models exhibit?
category: personas
status: Not started
order: 12
---

# Which cognitive biases do language models exhibit?

Human cognitive biases provide concrete tests of how judgments change with irrelevant information, framing and prior beliefs. But resemblance should be measured: [recent causal-judgment experiments](https://arxiv.org/abs/2602.02983) found that many LLMs did not reproduce characteristic human biases, and that chain-of-thought changed their robustness. The relevant question is which specific patterns transfer to models, under which conditions.

It would be useful to build a controlled picture of these biases across model families and training stages, and determine whether an observed bias reflects a stable decision tendency, a prompt artifact or a learned conversational role.

- Start with a small set of anchoring, framing, base-rate and causal-judgment tasks, defining a comparison standard for each.
- Use matched wording, reversed answer orders and fresh scenarios to test whether effects survive surface changes.
- Compare base, instruction-tuned and reasoning models under matched response budgets.
- Test whether persona or user cues alter the measured biases, then investigate internal representations associated with the changes.
