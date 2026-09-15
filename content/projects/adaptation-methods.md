---
title: What can prompting, steering, LoRA, and fine-tuning change?
category: training
status: Not started
order: 7
---

# What can prompting, steering, LoRA, and fine-tuning change?

[LoRA](https://arxiv.org/abs/2106.09685) shows that low-rank weight updates can efficiently adapt large models. [Steer Like the LLM](https://arxiv.org/html/2605.03907v1) connects prompting to activation interventions and learns token-dependent steering that imitates prompt effects. These connections suggest common structure, but do not establish that the methods can induce the same behaviors under comparable constraints.

It would be useful to map which changes each method can achieve, when one can reproduce another, and where apparent equivalence breaks down. The comparison should include reliability and preservation of existing abilities, alongside success on the requested behavior.

- Compare prompting, fixed and conditional steering, LoRA, and full fine-tuning on matched behavioral targets.
- Vary data, compute, intervention size, and access to training examples explicitly.
- Test whether interventions transfer across contexts, tasks, and conversational roles.
- Compare internal representation changes, then use counterexamples to identify behavior that one method changes reliably and another cannot reproduce within its budget.
