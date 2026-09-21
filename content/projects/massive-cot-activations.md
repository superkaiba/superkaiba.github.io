---
title: Massive activations during reasoning and at its end
status: Not started
order: 37
---

# Massive activations during reasoning and at its end

[Massive Activations in Large Language Models](https://arxiv.org/abs/2402.17762) identifies a few unusually large hidden-state values that often behave like input-independent biases. Meanwhile, [DeepSeek-R1](https://arxiv.org/html/2501.12948v1) demonstrates that reinforcement learning can produce substantial changes in reasoning behavior.

I have some results showing that a few massive activation coordinates dominate the difference between prompt-end and end-of-CoT states. [Read the concise report (PDF)](/assets/docs/massive-cot-activations-summary.pdf?v=20260920).

It would be useful to compare activation extremes before and after reasoning training, particularly around the transition from reasoning to the final answer. The question is whether there is a distinctive computation at this boundary, rather than assuming that a large activation necessarily encodes a meaningful thought or stopping decision.

- Compare matched base, instruction-tuned, and reasoning-tuned checkpoints across the same tasks.
- Measure activation magnitudes around reasoning delimiters and matched ordinary tokens.
- Control for token identity, answer position, sequence length, and normalization.
- Ablate or patch the relevant activations to test effects on stopping, answer quality, and reasoning length.
