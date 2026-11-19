---
title: 'Goals in LLMs: how they are represented, how long they persist, and whether they define personas'
status: Draft (slop)
order: 13.75
math: true
aliases: [bdi-persistence, goal-personas]
---

# Goals in LLMs: how they are represented, how long they persist, and whether they define personas

**TL;DR:** Look for a representation of the goal itself in LLM agents, separate from the model's beliefs about the world and from its current plan. Measure how long beliefs, goals and planned tokens persist in the residual stream, and whether later tokens read a stored decision or recompute it. Then test whether goals give a better account of personas than trait labels.

Many arguments about AI risk depend on whether models have goals, so it would help to be able to read goals out of activations instead of guessing them from behavior. Behavior alone is a weak basis. [Everitt et al.](https://arxiv.org/abs/2504.11844) measure goal-directedness as how fully a model uses its capabilities toward a given goal, and find that current models are often not fully goal-directed. A failure to reach a goal can mean low capability, a different goal, or a wrong belief, and behavior cannot always tell these apart.

The clearest internal evidence comes from a small RL agent. In a [maze-solving policy network](https://arxiv.org/abs/2310.08043), a few channels track the cheese location, and editing them moves the agent toward a new target. In LLMs the evidence is thinner. [Arghal et al.](https://arxiv.org/abs/2602.08964) probe GPT-OSS-20B as it navigates grid worlds and decode the agent and goal positions plus multi-step plans, but that decodes *where* the goal is, which is a fact about the world. [Auditing work on hidden objectives](https://arxiv.org/abs/2503.10965) shows that a model trained with a hidden objective can be caught with interpretability tools, but it does not describe the general format of goals. As far as I can tell, nobody has looked for a goal representation that is shared across tasks and kept apart from beliefs and plans.

### What would count as a goal representation

Write the model's decision as depending on its belief $b$ about the world, its goal $g$, and its plan $\pi$. A goal representation is a site $z_g$ in the activations with three properties:

1. **Invariance.** $z_g$ is about the same for two tasks with the same goal and different surface details.
2. **Separation from belief.** Changing where the target is changes $z_b$ but not $z_g$. Changing which target the agent wants changes $z_g$ but not $z_b$.
3. **Coherent retargeting.** Patching $z_g$ from a run with goal $g'$ makes the agent pursue $g'$ using its *current* beliefs, so it takes a new route that it never saw in the source run.

The third property separates a goal from a copied plan. One way to score it is

$$
S_{\text{retarget}} = \Pr\big[\text{reach } g' \mid \text{patch } z_g \leftarrow z_g^{(g')}\big] - \Pr\big[\text{reach } g' \mid \text{no patch}\big],
$$

computed only on episodes where the source run's action sequence would fail in the target layout. A 2×2 design crosses the goal (fetch the key or the coin) with the belief (the key is in the left or right room) and patches the goal and belief sites separately.

### How long beliefs, goals and intentions persist

In the [BDI model](https://users.cs.utah.edu/~tch/notes/refs/Rao-Georgeff1995.pdf), an agent keeps beliefs about the world, goals it would like to reach, and intentions it has committed to. Following Bratman, commitment lets an agent with limited computation reuse an earlier decision instead of recomputing it, at the cost of sometimes pursuing a plan after it stops making sense. Each part has some evidence in LLMs: transformers [linearly represent optimal belief states](https://arxiv.org/abs/2405.15943), Claude 3.5 Haiku [selects a rhyme word at the newline](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) before writing the line, and [goal drift in LM agents](https://arxiv.org/abs/2505.02709) grows as the context gets longer.

A transformer has no recurrent state between tokens apart from the KV cache, so a persisting decision can be carried (written once and read through attention) or re-derived from the original cue at each position. Only the first matches commitment, and behavior alone cannot tell them apart. Two measures separate them. The **persistence time** $\tau$ comes from training a probe at the decision site and applying it $d$ tokens later:

$$
P(d) - c \approx A\, e^{-d/\tau},
$$

where $c$ is chance accuracy. The **carried fraction** $R = E_{\text{site}} / (E_{\text{site}} + E_{\text{cue}})$ compares how often the output follows a counterfactual when only the decision site is patched versus when only the original cue is changed. $R$ is close to 1 when later tokens read the stored decision and close to 0 when they recompute it.

### Can personas be defined by goals?

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) describes simulated characters through their beliefs, goals and personality traits, and [persona vectors](https://www.anthropic.com/research/persona-vectors) identify trait directions that predict and influence behavior. These are two ways to describe the same persona: what it is like, and what it is trying to achieve. If a clean goal representation exists, it can be used to test whether goals give a more transferable account of personas than trait labels, or whether both are needed.

**Initial directions:**

- **Build matched agent tasks.** Use text grid worlds, tool-use tasks and short coding tasks with the same abstract goals, given in the system prompt, the user turn, or only through examples.
- **Find candidate goal sites.** Train goal probes at each layer and position and keep only those that transfer across tasks and across how the goal was given. Run the 2×2 separation test and compute $S_{\text{retarget}}$ for patches and steering vectors.
- **Measure persistence.** For beliefs, goals and planned tokens, vary what follows (filler, distractors, relevant evidence) and fit $\tau$ and $R$. Count both failure types: dropping a commitment after irrelevant text, and keeping it after evidence that should end it.
- **Compare stated goals and the model's own goals.** Repeat the analysis when the goal comes from the model's defaults or from fine-tuning, and check whether it uses the same site and format.
- **Goals versus traits for personas.** Construct scenarios where the same goal produces different surface traits and the same trait serves different goals, then compare goal-based and trait-based descriptions at predicting held-out choices.
- **Compare base and instruction-tuned models,** and test whether $\tau$ and $R$ from short controlled tasks predict goal drift in long agentic transcripts.

**Related projects:** [how agents represent themselves and other agents](#agents-modeling-agents), [personas as persistent features](#persistent-personas), [how much of an LLM's behavior is decided in advance](#behavior-commitment), and [whether LLMs do distributional RL](#distributional-rl).
