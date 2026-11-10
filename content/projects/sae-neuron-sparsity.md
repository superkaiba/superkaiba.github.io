---
title: Are SAE features sparse in the neuron basis?
status: Not started
order: 10.25
math: true
---

# Are SAE features sparse in the neuron basis?

**TL;DR:** Measure how many neurons each SAE feature uses, across the large public SAE releases, layers and model sizes. Then test whether the features that use few neurons are more interpretable or more causally important. This gives a direct, cheap measurement for the current debate on whether neurons are already clean or whether SAEs are needed to undo superposition.

The evidence so far is thin and mostly from small models. In [Neel Nanda's replication](https://www.lesswrong.com/posts/fKuugaxt2XLTkASkk/open-source-replication-and-commentary-on-anthropic-s) of Anthropic's dictionary learning work on a one-layer GELU model, about 92% of MLP SAE features were dense in the neuron basis, about 4% were explained by one neuron, and about 4% by two to ten. The neuron basis was still privileged: almost all features had higher kurtosis in the neuron basis than a random direction would. In a [two-layer TinyStories model](https://www.lesswrong.com/posts/LBaTQGD5KyXcbTtKt/how-polysemantic-can-one-neuron-be-investigating-features-in), one neuron was the closest neuron for over 400 features, and the most interpretable features were not mostly aligned with any neuron. In the residual stream, the axes are privileged only because of training: Anthropic found [outlier dimensions](https://transformer-circuits.pub/2023/privileged-basis/) and blamed Adam's per-dimension normalization, and a follow-up showed that [models trained with SGD have no privileged basis](https://www.lesswrong.com/posts/yrhu6MeFddnGRSLtQ/adam-optimizer-causes-privileged-basis-in-transformer). The other side of the debate is Goodfire's [Neural Networks Are Already Clean](https://already-clean.goodfire.com), which estimates that about 90% of neurons in Qwen3-32B have one main job and argues that SAEs can split clean neurons into pieces. As far as I can tell, nobody has measured neuron sparsity on the large modern SAE releases.

**Measures of neuron sparsity.** Let $d \in \mathbb{R}^n$ be a feature's decoder vector, written in the basis of the $n$ neurons. Three measures:

- The fraction of its squared norm on the top neuron, $f_1 = \max_i d_i^2 / \|d\|^2$, and on the top ten, $f_{10}$.
- The participation ratio, the effective number of neurons used:
$$
\mathrm{PR}(d) = \frac{\big(\sum_i d_i^2\big)^2}{\sum_i d_i^4}.
$$
It is 1 for a vector on one neuron and $n$ for a vector spread evenly over all of them.
- The kurtosis of the entries, which for zero-mean entries is linked to the participation ratio:
$$
\kappa(d) = \frac{\tfrac{1}{n}\sum_i d_i^4}{\big(\tfrac{1}{n}\sum_i d_i^2\big)^2} = \frac{n}{\mathrm{PR}(d)}.
$$
For a random direction the entries are roughly Gaussian, so $\kappa \approx 3$ and $\mathrm{PR} \approx n/3$. This gives the baseline: a feature is neuron-sparse to the extent that its participation ratio is far below $n/3$.

**Initial directions:**

- **Measure the public SAEs.** Compute $f_1$, $f_{10}$ and the participation ratio for every feature in large releases such as Gemma Scope and Llama Scope, for MLP and residual SAEs, by layer and model size. Compare each with the random-direction baseline.
- **Interpretability against sparsity.** Use automated interpretability scores and check whether neuron-sparse features are more interpretable than dense ones.
- **Causal importance against sparsity.** Measure each feature's effect on the loss when ablated, and check whether the important features tend to be neuron-sparse or dense.
- **Do SAEs split neurons?** For neurons that Goodfire-style audits call clean, find all SAE features that load mostly on that neuron. Check whether the features are pieces of one meaning or genuinely different meanings.
- **Effect of training choices.** Train small models with Adam and with SGD, and with different MLP activations, and train SAEs on each. Check how much neuron sparsity in both the MLP and residual stream depends on these choices.

**Related projects:** [are GLP neurons broadly interpretable](#glp-neuron-interpretability), [semantic structure in native residual coordinates](#native-coordinates), and [do LLM neurons grow by recursive generalization during training](#recursive-generalization-training).
