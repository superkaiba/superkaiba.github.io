---
title: Why do probes do badly at the last layer?
status: Not started
order: 15.5
math: true
---

# Why do probes do badly at the last layer?

**TL;DR:** Linear probes on LLMs usually work best in the middle layers and get worse toward the last layer. Find out why. Test whether the information is actually gone, still there but no longer linear, hidden by a few huge activation dimensions, or moved to describe the next token instead of the current one.

The drop is well documented. [Skean et al.](https://arxiv.org/abs/2502.02013) find that intermediate layers beat the final layer on 32 embedding tasks, across transformers and state-space models. [Numbers](https://arxiv.org/abs/2401.03735) are encoded most linearly in middle layers, and probe errors grow again in late layers. Token identity is [least linearly decodable in the middle](https://arxiv.org/abs/2606.02750), partly recovers in later layers, then drops near the end. In [Sparse Feature Circuits](https://arxiv.org/abs/2403.19647), a probe on the last layer of Pythia-70M could not beat chance on a profession classification task, so the authors used the second-to-last layer. In vision transformers, the [final-layer drop appears mainly under distribution shift](https://arxiv.org/abs/2603.05280). Most papers explain the drop by saying the last layers "specialize for next-token prediction". That is a description, not a mechanism.

**Accessible versus present.** A probe measures whether information is *linearly accessible*, not whether it is *present*. These come apart. Let $y$ be the probed property and $h_\ell$ the residual stream at layer $\ell$. A linear probe's accuracy tracks how well $y$ can be read with $w^\top h_\ell$. A probe with enough capacity (an MLP, or the model's own later computation) tracks how much information $h_\ell$ carries about $y$. If the gap between the two grows in the last layers, the information is still there but has been re-encoded. If both drop, it was removed. One useful reference point: at the last layer the J-lens Jacobian is the identity, $J_L = I$, so the residual stream there is read only through $W_U\,\mathrm{LN}(h_L)$. Any property the model still needs must survive that map, and anything that does not affect the next-token logits is free to be overwritten.

**Hypotheses:**

1. **Removal.** The last layers erase information that does not help predict the next token. Both linear and nonlinear probes should fail.
2. **Re-encoding.** The information is still present but mixed into the vocabulary-shaped geometry of the output. Nonlinear probes, or linear probes on the logits $W_U\,\mathrm{LN}(h_L)$, should recover it.
3. **Scale artifacts.** A few dimensions with very large activations dominate the last layer, and an unnormalized logistic regression fits badly. Standardizing features, applying the final layer norm, or removing the outlier dimensions should recover accuracy.
4. **Shift to the next token.** The last layer at position $t$ describes token $t+1$, so a property of the current text is replaced by a property of the prediction. Probes for properties of the next token should improve at the last layer while probes for the current text get worse.
5. **Distribution shift.** Last-layer features are more specific to the pretraining distribution, so they transfer worse to probing datasets.

**Initial directions:**

- **Layer curves with several probes.** For a set of properties (sentiment, truth, part of speech, entity type, numbers), plot accuracy against layer for a linear probe, an MLP probe and a linear probe on the logits.
- **Test scale artifacts directly.** Repeat the linear curves after standardization, after the final layer norm, and after removing the top few outlier dimensions.
- **Current versus next token.** Probe each property for the current token and for the next token at every layer, and check where the curves cross.
- **Causal check for removal.** Patch the last-layer residual stream from an input with a different value of $y$, and check whether any output that depends on $y$ (for example, a later answer about it) changes. If nothing changes, the model no longer uses $y$ at the last layer.
- **In and out of distribution.** Compare the drop on text close to pretraining data with text far from it.
- **Effect of post-training.** Compare base and instruction-tuned models, since post-training may change what the last layers keep.

**Related projects:** [what determines the right probe](#probe-selection), [when model behavior is internally detectable](#internal-detectability), and [how J-lens token directions relate to token embeddings across layers](#j-lens-token-embeddings).
