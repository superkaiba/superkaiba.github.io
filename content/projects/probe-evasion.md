---
title: Can models learn to evade probes in context?
status: Not started
order: 39
---

# Can models learn to evade probes in context?

[Obfuscated Activations](https://arxiv.org/abs/2412.09565) shows that some internal defenses can be evaded while the underlying behavior persists. In-context adaptation has also been studied: [You Can't Escape Your Own Activations](https://arxiv.org/abs/2609.03035) tests monitoring awareness and probe-score feedback with Qwen3-32B-AWQ and GPT-OSS-20B, and finds that its strongest probes remain accurate.

It seems important to check whether that result holds for larger, more capable models. Improved ability to interpret feedback might help evasion, but it might also make the relevant behavior easier to detect.

- Reproduce the fixed-probe setup, then extend it to larger open models with accessible activations.
- Vary feedback detail and interaction budget while independently verifying whether the monitored behavior still occurs.
- Test transfer of an evasion strategy to new probes, tasks and prompts.
- Compare performance across model sizes using matched tasks and reporting both detection and task success.
