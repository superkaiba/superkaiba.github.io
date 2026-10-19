---
title: "Inside and outside J-space: System 1 and System 2 thinking"
status: Not started
order: 32.25
---

# Inside and outside J-space: System 1 and System 2 thinking

**TL;DR:** Study what is represented and computed inside and outside J-space, and test how this distinction relates to automatic System 1 thinking, deliberate System 2 thinking, and action selection.

[Verbalizable Representations Form a Global Workspace in Language Models](https://www.transformer-circuits.pub/2026/workspace/index.html) identifies J-space representations that support verbal report and flexible internal reasoning, while some routine processing can proceed without them. Its analysis of features outside J-space finds examples involving syntax and formatting.

The question is whether this distinction helps explain System 1 and System 2 thinking. Does processing outside J-space support an automatic “doer,” and when does deliberate reasoning change what it does? These are hypotheses to test. J-space is a sparse set of representations, so its remainder is not a fixed orthogonal subspace; answering without written reasoning also need not mean bypassing J-space.

**First Steps**

- Characterize features inside J-space and in the remaining activations across layers, tasks, and models.
- Compare routine tasks with matched tasks that require reporting or flexibly using the same information. Ablate or patch each component to test its causal role.
- Study action selection when a model's stated intention conflicts with its behavior, testing which representations influence the final action.
- Use [System 2-to-System 1 distillation](https://arxiv.org/abs/2407.06023) to test whether learned skills become less dependent on J-space as they become more automatic.

**Related project:** [Understanding the thinker, talker, and doer personas](#cot-persona).
