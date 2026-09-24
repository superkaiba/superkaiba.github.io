# On-policy alignment RL during pretraining

**TL;DR:** Test whether learning from feedback on the model's own actions during pretraining produces more durable, generalizable alignment than demonstrations or alignment introduced after pretraining.

Human experiments on [self-selected interventions](https://doi.org/10.3758/BF03193418) and [feedback about decisions' consequences](https://doi.org/10.1038/s41562-025-02271-w) motivate testing learning from self-generated behavior. This is an analogy to on-policy reinforcement learning, rather than a direct equivalence between human learning and LLM training. In LLMs, [pretraining with human preferences](https://proceedings.mlr.press/v202/korbak23a.html) and [introducing alignment-related material earlier](https://arxiv.org/abs/2608.13482) provide starting points for studying alignment during pretraining.

This project asks whether introducing on-policy alignment RL during pretraining produces alignment that transfers to unfamiliar settings and survives subsequent capability training. A curriculum of increasingly difficult supervised examples and RL environments could make this feasible while the model is still developing its capabilities.

**First Steps**

- Develop simple alignment environments that provide feedback on the consequences of the model's own decisions, increasing difficulty as capabilities improve.
- Compare on-policy RL during pretraining with the same intervention after pretraining, matching training budgets and measuring capability differences.
- Include demonstrations and offline preference optimization to separate the effect of training timing from the source of training behavior and the optimization method.
- Evaluate held-out situations, conflicting incentives, and durability after further capability training.

**Related projects:** [Contextualized pretraining](#contextualized-pretraining) studies source attribution; [developmental teaching methods](#developmental-ethics) studies a broader set of human-inspired interventions.
