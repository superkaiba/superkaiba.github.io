---
title: Distributional RL in LLMs
status: Fleshed out
order: 13.8
---

# Distributional RL in LLMs

Large-scale RL has let LLMs do a lot of tasks that seemed out of reach a few years ago. It also comes with a lot of problems, and most of them can be seen as some form of reward hacking.

RL was partly inspired by how animals learn, and the brain turned out to implement something very close to it. [Schultz, Dayan and Montague (1997)](https://pubmed.ncbi.nlm.nih.gov/9054347/) showed that the activity of dopamine neurons in monkeys matches the reward prediction error used in temporal difference (TD) learning. These neurons fire above baseline when a reward is better than expected and below baseline when it is worse.

People have found similar machinery in LLMs. [Demircan et al. (2025)](https://arxiv.org/abs/2410.01280) found sparse autoencoder features in Llama 3 70B that track TD errors and Q-values while the model solves RL tasks in context, and removing those features hurts its performance. [Xu et al. (2026)](https://arxiv.org/abs/2602.00986) found that fewer than 1% of neurons in reasoning models act as "value neurons" and "dopamine neurons", the second group tracking step-level TD errors.

One variant of RL that has also been found in the brain is distributional RL. Standard RL learns one number for each situation: the average reward it expects. Distributional RL learns the whole range of rewards that could follow.

For example, an option that pays 0 or 10 with equal chance and an option that always pays 5 have the same average. Standard RL gives them the same value, while distributional RL can tell them apart.

A simple way to learn the distribution is to keep many value estimates that learn at different rates from good and bad surprises. An estimate that learns more from good surprises settles near the top of the range (optimistic), and one that learns more from bad surprises settles near the bottom (pessimistic). Together they describe the distribution.

[Dabney et al. (2020)](https://www.nature.com/articles/s41586-019-1924-6) found this pattern in mouse dopamine neurons. Each neuron had its own level of optimism, and the reward distribution could be decoded from the whole population. Similar codes have since been found in [monkey prefrontal cortex](https://www.nature.com/articles/s41593-023-01535-w) and [mouse striatum](https://www.nature.com/articles/s41586-024-08488-5).

This raises two questions, which I'd split into two projects:

- **Project 1** asks whether LLMs already implement distributional RL internally.
- **Project 2** asks whether training LLMs with distributional RL can reduce reward hacking.
