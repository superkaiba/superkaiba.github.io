---
title: A general mechanistic understanding of LLM introspection
status: Not started
order: 34.5
---

# A general mechanistic understanding of LLM introspection

**TL;DR:** Identify how language models read and report their own internal states, and test whether different forms of introspection use a shared mechanism or separate circuits.

[Mechanisms of Introspective Awareness](https://arxiv.org/abs/2603.21396) traces a pathway from injected concepts through evidence-carrier features to gates that control detection reports. This explains a specific experimental behavior. A broader account would explain how a model judges its own uncertainty, anticipates its decisions, or checks whether an output matches its prior internal state under ordinary conditions.

There are useful starting points beyond concept injection. [Causal evidence that language models use confidence to drive behaviour](https://www.nature.com/articles/s42256-026-01293-x) links internal confidence representations to decisions to answer or abstain. [Me, Myself, and pi](https://arxiv.org/abs/2603.20276) studies self-prediction and proposes attention diffusion as a partial mechanism in an ethical-dilemma task. Neither establishes a general circuit for introspection. [Anthropic's discussion of possible mechanisms](https://transformer-circuits.pub/2025/introspection/index.html) also considers several specialized circuits that could reuse computations learned for other purposes.

The central question is whether the model constructs a reusable representation of its own processing that supports different judgments, or whether apparent introspection comes from task-specific readouts, recomputing an answer, and interpreting visible text. Finding information with an external probe is insufficient: the model must itself use that information to make an accurate judgment about its state.

**First Steps**

- Build matched tasks for reporting confidence, predicting one's own choices, checking intended versus produced outputs, and detecting controlled activation perturbations. Measure self-report accuracy separately from primary-task performance.
- Trace the attention and MLP computations connecting task representations to self-reports. Distinguish original model neurons from features extracted by transcoders or sparse autoencoders, and look for shared intermediate representations across tasks.
- Ablate and patch candidate components across tasks. Test whether an intervention changes introspective accuracy while preserving the underlying ability, and control for generic changes in answer preference, refusal, and reporting style.
- Compare with observers given only the text, matched non-introspective questions, and unrelated internal interventions. Test transfer across prompts, concepts, and model checkpoints, including natural internal variation as well as injected signals.

This complements [training models to predict their own activations](#self-latent-prediction): the focus here is explaining existing introspective mechanisms and their limits, rather than introducing a new training objective.
