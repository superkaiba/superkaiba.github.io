---
title: Structure in attention keys and values
status: Not started
order: 32.33
math: true
---

# Structure in attention keys and values

**TL;DR:** Most interpretability work studies the residual stream. But later tokens only see earlier positions through attention keys and values. Map the structure of keys and values: how many dimensions each head uses, which directions heads share, what features they contain, and how known residual-stream geometry (belief states, persona directions) survives the projection into them.

At each layer, a position offers two things to later tokens through each head. Its key decides when a later query retrieves it, and its value decides what gets moved ([the QK and OV circuits](https://transformer-circuits.pub/2021/framework/index.html)). Both are linear projections of the residual stream, so they contain no new information. They are a selection, though. Each head keeps at most $d_{\text{head}}$ directions of the residual stream (often 128). So the structure of keys and values decides which parts of the residual stream later positions can see at all.

Several findings, mostly from work on KV-cache compression, suggest that keys and values are organized differently:

- [KIVI](https://arxiv.org/abs/2402.02750) finds outlier channels in the key cache and no clear outlier pattern in the value cache. So keys are quantized per channel and values per token.
- [Loki](https://arxiv.org/abs/2406.02542) finds that keys lie in a much lower-dimensional space, consistently across models and datasets. Rotary embeddings (RoPE) raise their dimensionality.
- [Jin et al.](https://arxiv.org/abs/2502.01563) find very large entries concentrated in specific dimensions of queries and keys, with no such pattern in values. RoPE causes the concentration, and these entries matter more for using information in the context than for recalling facts stored in the weights.
- [Barbero et al.](https://arxiv.org/abs/2410.06205) find that Gemma 7B uses the highest RoPE frequencies to build purely positional heads. It mostly uses the lowest frequencies, which they suspect carry semantic information.
- [Ma et al.](https://arxiv.org/abs/2512.10547) train Top-K SAEs on keys and values. Keys saturate at about 8 active features. Values in deep layers need a larger budget.
- [Shaikh et al.](https://arxiv.org/abs/2603.13314) predict a head's keys from a few other heads in the same layer with a linear map (mean $R^2 \approx 0.76$ for keys with five reference heads on C4). This predictability is absent at initialization and grows during pretraining, as the key projection subspaces of heads in a layer align. Reconstructing keys costs much less accuracy than reconstructing values.
- [Guo et al.](https://arxiv.org/abs/2410.13835) find that the tokens that attract attention sinks have much smaller value vectors than other tokens.

Together these suggest that keys form a shared, low-dimensional addressing code, and values carry denser content that differs more between heads. Most of this work aims at compression. As far as I can tell, nobody has asked what the shared key directions represent, or how structure already known in the residual stream appears in keys and values.

**Setup.** For head $h$ at layer $\ell$ and position $s$, with $\tilde{x}_s = \mathrm{LN}(x_{\ell,s})$:

$$
k^h_s = R_s\, W_K^h\, \tilde{x}_s, \qquad v^h_s = W_V^h\, \tilde{x}_s,
$$

where $R_s$ is the RoPE rotation at position $s$. A later position $t$ receives $\sum_s a^h_{ts}\, W_O^h v^h_s$, with $a^h_{ts} = \mathrm{softmax}_s\big(q^{h\top}_t k^h_s / \sqrt{d_{\text{head}}}\big)$. In models with grouped-query attention, $h$ indexes the key-value heads.

**Shared subspaces.** Compare heads in whitened coordinates, so that directions the data never uses do not count. Let $C$ be the covariance of $\tilde{x}$ on a reference corpus and $z = C^{-1/2}\tilde{x}$. Then the pre-RoPE key is $W_K^h C^{1/2} z$, with $z$ isotropic. Let $U^h_K$ hold the top $r$ right singular vectors of $W_K^h C^{1/2}$. These are the directions that most affect head $h$'s keys. The overlap between heads $h$ and $h'$ is

$$
O_K(h, h') = \frac{1}{r}\,\big\| U^{h\top}_K\, U^{h'}_K \big\|_F^2,
$$

the mean squared cosine of the principal angles between the two subspaces. It is 1 for identical subspaces and about $r / d_{\text{model}}$ for random ones. Define $O_V$ the same way with $W_V^h$. If keys are a shared addressing code, $O_K$ should be well above $O_V$ within a layer.

**Initial directions:**

- **Dimensionality per head.** Measure the participation ratio $\mathrm{PR} = (\sum_i \lambda_i)^2 / \sum_i \lambda_i^2$ of the covariance eigenvalues, and the TwoNN intrinsic dimension, for keys (before and after RoPE) and values in every head and layer. Compare with the residual stream at the same layer. Report sink tokens separately, since their small values would distort the statistics.
- **What the shared key code encodes.** Compute $O_K$ and $O_V$ for all head pairs in each layer, and cluster heads by key subspace. Probe the shared key directions for position, token identity, part of speech, syntactic role, and position in the chat template (role tokens, turn boundaries).
- **Position and content in keys.** Split each key into RoPE frequency bands. Measure how much variance and how much decodable information each band holds. Check whether the low-frequency semantic channels from Barbero et al. are the same directions that heads share.
- **Features in keys and values.** Train SAEs on the keys and values of a few layers, and compare their features with residual-stream SAE features at the same layer. Map each residual feature through $W_K^h$ and $W_V^h$ and check which ones each head keeps. This gives, for each head, the residual features it can retrieve on and the ones it can move.
- **Known geometry after the projection.** Take structure already found in the residual stream: [belief-state simplices](https://arxiv.org/abs/2405.15943) in models trained on hidden Markov processes, persona directions, and [truth directions](https://arxiv.org/abs/2310.06824). A linear map keeps a simplex's shape (up to an affine transformation) unless it collapses some of the directions the simplex spans. Measure, for each head, how much of each structure survives in its keys and in its values. Heads whose values keep the belief simplex are candidates for carrying belief state to later positions. Heads whose keys keep it would retrieve earlier positions by their belief state.
- **Training dynamics.** Track these measures across Pythia or OLMo-2 checkpoints. Check whether the shared key subspace forms before, during or after the [induction head phase change](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html).
- **Post-training.** Compare base and instruction-tuned versions of the same model. Check whether post-training mostly changes the key code (what gets retrieved) or the value content (what gets moved).

A useful result would be a map of keys and values for a few open models: how many dimensions each head uses, which directions heads share, and what those directions encode. It would also tell other methods where to look. Probes and SAEs on values would find content that later positions can read, and the shared key directions would show what decides retrieval.

**Related projects:** [the J-lens on attention value vectors](#j-lens-value-vectors), [steering and patching the KV cache instead of the residual stream](#kv-steering), [whether secrets are stored in values or the residual stream](#secrets-values-vs-residual), [nonlinear geometry of persona representations](#persona-manifolds), and [trajectory straightening and belief-state geometry](#belief-geometry-straightening).
