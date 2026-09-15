---
id: "P01"
title: "Can models learn to evade probes in context?"
area: "Monitoring"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Can the model learn to evade probes in context?"
---

# Can models learn to evade probes in context?

Probes are small classifiers that read a model's internal activations to detect a behavior of interest. They could be useful monitors, but only if the model cannot easily work around them. [Obfuscated Activations](https://arxiv.org/abs/2412.09565) shows that attacks can change activations enough to evade some internal defenses while preserving the behavior those defenses are meant to catch.

Learning to evade probes **in context**, without changing model weights, has already been studied. [You Can't Escape Your Own Activations](https://arxiv.org/abs/2609.03035) compares agents that receive no monitoring information, monitoring awareness, or feedback from the previous round's probe score. In its experiments with Qwen3-32B-AWQ and GPT-OSS-20B, the strongest probes remain accurate even when the agents know about the monitor and receive feedback.

I propose to test whether that result holds for **larger, more capable models**. A model that is better at using feedback or understanding its own behavior might find strategies that the models studied so far do not. This is an empirical question; greater capability could also make the monitored behavior easier to detect.

We would reproduce the fixed-probe setup and extend it to larger open models whose activations we can inspect. We would then check:

- Does detection get worse as models become larger or receive more feedback?
- Is the model still carrying out the monitored behavior, or did it simply stop?
- Does evasion transfer to a new probe or task?
- How much information and interaction time does the model need?

Comparing the same tasks, feedback budgets, and independently checked behavior across model sizes would help establish whether the existing result survives scaling.
