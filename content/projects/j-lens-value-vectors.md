---
title: Reading attention value vectors with the J-lens
status: Not started
order: 32.35
math: true
---

# Reading attention value vectors with the J-lens

**TL;DR:** Apply the J-lens to what each attention head moves between positions, not only to the residual stream. This shows in words what a past token offers to later tokens, and which heads carry J-space content.

The [J-lens](https://www.transformer-circuits.pub/2026/workspace/index.html) reads a residual activation $h_\ell$ through the average Jacobian $J_\ell$ of the final residual stream with respect to layer $\ell$. The paper analyzes the residual stream and does not study attention keys, values or the KV cache. But much of what a later token "knows" about earlier text arrives through attention values. A residual readout at a position mixes what was computed there with what was copied in.

**The readout.** For head $h$ in layer $\ell$, the value at source position $s$ is $v^h_s = W_V^h\,\mathrm{LN}(x_{\ell,s})$, and its write into the residual stream at destination $t$ is $A^h_{ts}\,W_O^h v^h_s$. Define the head's output vector at $s$ as $o^h_s = W_O^h v^h_s$. This is a vector in residual space, so it can be read with the lens for the layer it is written into:

$$
\mathrm{lens}(o^h_s) = \mathrm{softmax}\!\big(W_U\, J_{\ell+1}\, o^h_s\big).
$$

Because $o^h_s$ does not depend on $t$, this readout says what position $s$ offers through head $h$ to any later position. The attention weights $A^h_{ts}$ then say who takes it. Two cautions. First, $J_\ell$ is an average over contexts, and a single head output is a much smaller vector than a full activation, so the normalization in the original lens may not apply. Compare raw logits with the normalized version. Second, the readout ignores the effect of later layer norms on a small addition, so check it against direct patching.

**Initial directions:**

- **Build the readout.** Compute $\mathrm{lens}(o^h_s)$ for every head and source position on an open model where J-lens matrices are available. Sanity-check it on known heads: an induction head should offer the token after the previous occurrence, and a name-mover head should offer a name.
- **Find J-space heads.** Decompose each $o^h_s$ into J-lens vectors and measure how much of it lies in J-space. Check whether a small set of heads carries most of the J-space content between positions.
- **Unspoken intermediates.** In two-hop prompts ("the animal that spins webs has how many legs"), check which head first offers "spider" and from which position.
- **Compare offered and received.** At destination $t$, compare $\sum_{h,s} A^h_{ts}\,\mathrm{lens}(o^h_s)$ with the residual readout at $t$. The gap measures how much J-space content is computed in place instead of copied.
- **Hidden reasoning.** Apply the readout to models with known hidden objectives and check whether value vectors reveal the objective earlier or more clearly than the residual stream.

**Related projects:** [inside and outside J-space](#j-space-system-thinking), [stress-testing J-space as working memory](#j-space-working-memory), [steering and patching the KV cache instead of the residual stream](#kv-steering), and [whether secrets are stored in values or the residual stream](#secrets-values-vs-residual).
