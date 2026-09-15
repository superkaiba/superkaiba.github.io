---
title: Do different layers perform different stages of belief updating?
status: Not started
order: 13
---

# Do different layers perform different stages of belief updating?

[Belief-state geometry experiments](https://arxiv.org/abs/2405.15943) show that transformers trained on controlled sequence processes can represent uncertainty about hidden states. [Constrained belief-updating work](https://arxiv.org/abs/2502.01954) connects attention to partial Bayesian updates and studies how later layers refine them. These findings offer a concrete starting point for interpreting what changes from early to late layers.

It would be useful to determine whether layers have distinct roles in forming, updating and using beliefs, and whether that organization extends beyond the controlled settings already studied.

- Train small models on processes with known latent states and exact posterior probabilities.
- Decode prior beliefs, incoming evidence and updated beliefs at each layer, including information distributed across several layers.
- Intervene on specific layers to distinguish evidence accumulation from simply re-expressing the same information.
- Test whether the resulting predictions hold in larger models on controlled natural-language evidence, conflicting reports and changes in source reliability.
