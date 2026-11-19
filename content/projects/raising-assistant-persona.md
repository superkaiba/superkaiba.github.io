---
title: '"Raising" the assistant persona throughout pretraining'
status: Fleshed out
order: 19.7
---

# "Raising" the assistant persona throughout pretraining

Current LLMs undergo pretraining, where they learn all their knowledge about the world, then post training, where their persona/character/self within that world is introduced and shaped. We know that plasticity falls during pretraining, leading to a decrease in the ability to acquire and retain new knowledge (extended pretraining makes models harder to fine-tune: [Springer et al., 2025](https://arxiv.org/abs/2503.19206); see also critical learning periods in deep networks: [Achille et al., 2019](https://arxiv.org/abs/1711.08856)).

This is similar to how humans lose plasticity throughout their lives, and how things we learn/happen to us in early childhood can leave lifelong marks (early interventions produce more lasting improvements in ethical behavior: [Kosse et al., 2020](https://doi.org/10.1086/704386); [Luo et al., 2018](https://doi.org/10.1038/s41467-018-07138-5)). It is therefore perhaps not surprising that post-training only provides shallow alignment ([Qi et al., 2025](https://arxiv.org/abs/2406.05946)) since it is done at the end of pretraining when the model's plasticity is at its lowest point.

Though there has been prior work on introducing alignment data in the chat template throughout pretraining ([Korbak et al., 2023](https://proceedings.mlr.press/v202/korbak23a.html); [Maini et al., 2025](https://arxiv.org/abs/2504.16980); [Minder et al., 2026](https://arxiv.org/abs/2608.13482)), I think this prior work fails to take into account that at the point in pretraining where they introduce the data, the model probably is "too stupid" to really understand what it means and therefore probably doesn't really learn what we want to learn.

Instead, I think that something that makes more sense is to introduce the assistant persona (and chat template) gradually throughout pretraining (potentially with a curriculum starting with simple knowledge about the world and moving to more complex), with data adapted to its current level of capabilities, and potentially also try to do only on-policy training (which has been shown to generalize better and forget less: [Chu et al., 2025](https://arxiv.org/abs/2501.17161); [Shenfeld et al., 2026](https://arxiv.org/abs/2509.04259)). Thus we would "raise" the model similarly to how we raise a baby, teaching it about itself, morals, and the world at the same time, and hope that alignment taught in such a way would be much deeper than alignment only provided in post-training.

Related: [On-policy alignment RL during pretraining](#alignment-rl-pretraining).
