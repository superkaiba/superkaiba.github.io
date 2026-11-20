---
title: 'LLM neuroanatomy: why are so many layers redundant?'
status: Draft (slop)
order: 10.1
math: true
---

# LLM neuroanatomy: why are so many layers redundant?

**TL;DR:** Many middle layers of an LLM can be deleted, swapped or run twice with little change to next-token predictions. Yet removing a single layer can break multi-step reasoning. Map what each layer does, and test why training leaves layers that look redundant.

Deleting or swapping adjacent layers at inference, with no fine-tuning, keeps 72 to 95% of the original model's prediction accuracy ([Lad et al.](https://arxiv.org/abs/2406.19384)). The first layer is fragile in every model they tested. Middle layers can also be skipped, reordered or run in parallel with gradual loss, except on math ([Transformer Layers as Painters](https://arxiv.org/abs/2407.09298)). Pruning studies remove a quarter or more of the layers with modest loss on multiple-choice benchmarks ([ShortGPT](https://arxiv.org/abs/2403.03853); [Gromov et al.](https://arxiv.org/abs/2403.17887)).

Running layers twice can even help. In his [LLM Neuroanatomy blog post](https://dnhkng.github.io/posts/rys/), David Ng ran layers 45 to 51 of Qwen2-72B a second time, with no weight changes, and the model reached the top of the Open LLM Leaderboard at the time. A [follow-up post](https://dnhkng.github.io/posts/sapir-whorf/) finds that early and late layers group sentences by language, while middle layers group them by topic across languages. His reading is that middle layers share one representation space, so an extra pass stays roughly in distribution.

The redundancy shrinks under harder tests. When answers are generated instead of scored by log-likelihood, middle and deep layers matter much more ([Song et al.](https://arxiv.org/abs/2510.02091)). Math depends on a few critical layers whose removal cuts accuracy by up to 80%, while factual recall has no critical layers ([Nepal et al.](https://arxiv.org/abs/2506.22638)). Generative tasks degrade far more than classification under layer pruning ([Shrestha et al.](https://arxiv.org/abs/2602.01997)).

**Why would training leave redundant layers?** Several explanations exist, and they predict different things:

- **Variance growth in Pre-LN models.** The residual stream's norm grows with depth, so each deep block adds a small update and its Jacobian approaches the identity ([The Curse of Depth](https://arxiv.org/abs/2502.05795)). On this view, much of the redundancy comes from the normalization scheme.
- **Iterative refinement.** Residual networks behave like ensembles of shallower paths ([Veit et al.](https://arxiv.org/abs/1605.06431)) and refine shared features a little at each block ([Jastrzebski et al.](https://arxiv.org/abs/1710.04773)). Deeper models seem to spread the same computation over more layers in smaller steps ([Csordás et al.](https://arxiv.org/abs/2505.13898)).
- **Self-repair.** After a layer is removed, later layers compensate for part of the loss ([McGrath et al.](https://arxiv.org/abs/2307.15771)). Deletion then understates what the layer normally contributes.
- **Specialization.** A layer might matter a lot for a small slice of inputs, such as math, code or rare facts, and barely at all elsewhere. Averages over all tokens would hide this.

The last two cases look alike in averaged metrics. For a deleted layer $\ell$ and an input $x$, let

$$
\Delta_\ell(x) = \mathcal{L}_{\setminus \ell}(x) - \mathcal{L}(x),
$$

the change in loss when layer $\ell$ is removed. Specialization predicts a heavy-tailed distribution of $\Delta_\ell(x)$ across inputs: a few inputs lose a lot. A layer that refines every input slightly predicts a narrow distribution where most inputs lose a little.

Small per-token losses also explain why generation breaks first. Suppose deleting a layer lowers each token's chance of being correct by a fraction $\delta$. A solution of $T$ tokens then succeeds with probability reduced by a factor of

$$
(1-\delta)^T \approx e^{-\delta T}.
$$

With $\delta = 0.01$ and $T = 200$, this factor is about $e^{-2} \approx 0.14$. Multiple choice only needs the correct option to stay ranked first, so the same blur rarely changes the answer. This toy model assumes independent errors.

**Initial directions:**

- **Break down deletion damage by input.** For each deleted layer, measure $\Delta_\ell(x)$ per example and per domain of the pretraining data (code, math, web text, other languages). I could not find a paper that reports this breakdown.
- **Compare deletion with duplication.** On the same model, check whether the layers that are safe to delete are the ones that help when run twice.
- **Look inside a repeated block.** Compare neuron activations on the first and second pass. If most neurons repeat their first-pass behavior, the second pass is refining. If second-pass activations look unlike any normal forward pass, the gains are harder to explain.
- **Change the normalization.** Repeat the deletion sweeps on models trained with LayerNorm Scaling or Peri-LN, and on models grown in depth during training. This tests how much redundancy the normalization scheme causes.
- **Follow redundancy over training.** Run the sweeps on Pythia or OLMo checkpoints. Check whether redundancy appears early, and whether it grows with more training tokens.
- **Separate redundancy from compensation.** Freeze later components at their clean outputs when a layer is removed. The gap between frozen and free deletion measures how much later layers compensate.

**Related projects:** [understanding the general structure of the residual stream](#residual-stream-structure), [activation self-correction](#activation-self-correction), [safety implications of looped transformers](#looped-transformers), [which nonlinearities can a model do without?](#nonlinearity-removal), and [do different layers perform different stages of belief updating?](#layerwise-belief-updating).
