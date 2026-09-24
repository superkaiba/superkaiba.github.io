---
title: Self-reflection to prevent reward hacking
status: Not started
order: 53
---

# Self-reflection to prevent reward hacking

**TL;DR:** Test whether reminders to reflect on the task's intended goal prevent reward hacking or encourage rationalization, and examine the internal changes and performance trade-offs.

[Goodfire's activation monitors](https://arxiv.org/abs/2609.19101) and [PRIME](https://arxiv.org/abs/2606.09711) identify internal signals associated with reward hacking. This motivates testing whether asking a model to reconsider the task's intent can change its next action. Detectable signals alone do not establish that a model consciously recognizes its behavior as hacking.

This project inserts brief checks such as “Are you still doing what the task intended?” during difficult, long-running tasks. We will test whether they prevent exploitation, merely produce reassuring explanations, or cause premature abandonment, and whether using them during training changes those effects.

**First Steps**

- Branch trajectories before observed reward hacking and insert reminders at different distances from the decision, with matched neutral-text and no-reminder controls.
- Measure actual hacking, legitimate task performance, and abandonment separately from the model's explanation.
- Compare internal signals when reflection changes behavior and when the model continues to exploit the reward.
- Compare training-time and evaluation-only reminders, varying their wording and frequency.

**Related Work**

- [BAITBENCH](https://arxiv.org/html/2608.30724v1#A4) already tests explicit experiment-validity judgments and finds no consistent benefit in a small ablation. Our focus includes intervention timing, internal mechanisms, and training effects.
- [Specification Self-Correction](https://arxiv.org/html/2507.18742v1) critiques and repairs task specifications; we test reminders within a fixed specification.
- [Training self-correction through RL](https://arxiv.org/abs/2409.12917) motivates testing whether reflection can be learned, while behavioral checks distinguish successful correction from rationalization.
