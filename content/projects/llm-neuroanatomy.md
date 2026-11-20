---
title: Understanding LLM neuroanatomy
status: Fleshed out
order: 10.1
---

# Understanding LLM neuroanatomy

**TLDR:** Explain why many layers of an LLM can be deleted with little effect while repeating some of them improves performance: why it happens, when in training it arises, under what conditions, and how it links to functionally specific neurons.

There has been a bunch of work showing that:

- you can delete layers from an LLM without changing behavior much
- you can duplicate layers in an LLM and increase performance significantly

This is weird! Our intuitions assume that the model is using its capacity fully and so it shouldn't necessarily have redundant layers. Also the duplication results indicate that the transformer layers might be developing some kind of "general reasoning" machinery similar to cortical columns in the neocortex (repeated units that share the same basic circuit across brain areas; [Mountcastle 1997](https://pubmed.ncbi.nlm.nih.gov/9153131/)), but this goes against the picture painted by [Neural Networks Are Already Clean](https://already-clean.goodfire.com/) (Cammarata 2026) where each neuron has a specific function.

The previous work has mostly characterized this:

- **Deleting layers.** Deleting one layer or swapping two neighbours keeps 72–95% of next-token accuracy ([Lad et al. 2024](https://arxiv.org/abs/2406.19384)). Up to about half the layers can be pruned before QA accuracy collapses ([Gromov et al. 2024](https://arxiv.org/abs/2403.17887); [ShortGPT](https://arxiv.org/abs/2403.03853)), and middle layers can even be reordered or run in parallel ([Sun et al. 2024](https://arxiv.org/abs/2407.09298)). Most of the block-level redundancy is in attention sublayers ([He et al. 2024](https://arxiv.org/abs/2406.15786)).
- **The redundancy shrinks under harder tests.** It mostly shows up with likelihood or multiple-choice scoring. Generation, math and long reasoning depend on specific middle and deep layers ([Song et al. 2025](https://arxiv.org/abs/2510.02091); [Nepal et al. 2025](https://arxiv.org/abs/2506.22638)), and some deletions remove skills like arithmetic that fine-tuning can't bring back ([Shrestha et al. 2026](https://arxiv.org/abs/2602.01997)).
- **Duplicating layers.** Running layers 45–51 of Qwen2-72B twice, with no weight changes, topped the Open LLM Leaderboard ([Ng 2026](https://dnhkng.github.io/posts/rys/)). It only seems to work for contiguous middle blocks, and the best block differs between math and EQ ([Ng, Part II](https://dnhkng.github.io/posts/rys-ii)). Per-input programs that skip or repeat layers fix many wrong answers, and harder questions need more repeats ([Li et al. 2025](https://arxiv.org/abs/2507.07996); [Westerhoff et al. 2026](https://arxiv.org/abs/2609.31360)).
- **Partial explanations.** Pre-LN normalization pushes deep layers toward the identity ([Sun et al. 2025](https://arxiv.org/abs/2502.05795)). Most layers seem to act like an ensemble of similar estimators, which gives loss roughly ∝ 1/depth ([Liu et al. 2026](https://arxiv.org/abs/2602.05970)). Later layers partly compensate when an earlier one is removed ([McGrath et al. 2023](https://arxiv.org/abs/2307.15771); [Rushing & Nanda 2024](https://arxiv.org/abs/2402.15390)), and models don't seem to use more layers on harder inputs ([Csordás et al. 2025](https://arxiv.org/abs/2505.13898)).

As far as I can tell, each of these explains one piece, and none of them explains both why layers can be deleted and why repeating some of them helps.

The goal of this project would be to provide a unified explanation for:

- why this happens
- when in training this arises
- under what conditions it arises
- how does it link to functionally specific neurons

This would provide us a lot of understanding as to how LLMs work + why they work so well.
