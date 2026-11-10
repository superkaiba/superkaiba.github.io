---
title: How do J-lens token directions relate to token embeddings across layers?
status: Not started
order: 32.37
math: true
---

# How do J-lens token directions relate to token embeddings across layers?

**TL;DR:** For each token, follow two things across layers: the direction the J-lens uses to read that token at each layer, and what happens to the token's own input embedding as it moves up the residual stream. Check where the two meet, where they part, and whether J-space has the geometry of the input embeddings, the output embeddings, or neither.

The [J-lens](https://www.transformer-circuits.pub/2026/workspace/index.html) scores token $w$ at layer $\ell$ with the row $W_U[w]^\top J_\ell$, where $J_\ell$ is the average Jacobian of the final residual stream with respect to the layer-$\ell$ residual stream. As a vector in residual space this is

$$
u_\ell(w) = J_\ell^\top\, W_U[w].
$$

At the last layer $J_L = I$, so $u_L(w)$ is just the unembedding of $w$. The logit lens uses $u_L(w)$ at every layer, and the J-lens corrects it by pulling the unembedding back through the average effect of the later layers. Each token also has an input embedding $E[w]$, which is what enters the residual stream at layer 0 when $w$ is in the prompt. Nothing forces $u_\ell(w)$ and $E[w]$ to be related, even in models with tied embeddings, because $J_\ell$ can rotate and rescale directions. The paper does not report how the J-lens vectors change with depth or how they relate to the embeddings.

**What to measure.**

- **Alignment with the embedding.** $a_\ell(w) = \cos\big(u_\ell(w), E[w]\big)$ for every token and layer. If early J-lens vectors point along the input embedding, "thinking of $w$" in early layers looks like "having just read $w$".
- **Drift.** $\cos\big(u_\ell(w), u_{\ell+1}(w)\big)$, to find the layers where the reading direction for a token changes fastest.
- **Geometry.** For a fixed set of tokens, compare the similarity matrix of $\{u_\ell(w)\}$ with the similarity matrices of $\{E[w]\}$ and $\{W_U[w]\}$ (representational similarity analysis). This shows whether J-space is organized by input form (spelling, tokenization) or by meaning and use.
- **What happens to the current token.** When $w$ is the input at position $t$, track $h_{\ell,t}^\top u_\ell(w)$ and the J-lens rank of $w$ itself across layers. Check whether the model keeps the token it just read in J-space or removes it, and in which layers.

**Initial directions:**

- **Compute the curves.** On an open model with J-lens matrices available, compute $a_\ell(w)$, drift and the geometry comparison for the whole vocabulary. Split tokens by type: whole words, word pieces, numbers, punctuation, and tokens that start with a space.
- **Tied and untied embeddings.** Repeat on models with tied embeddings (where $E = W_U$) and untied ones. With tied embeddings the logit lens and the input embedding coincide at the last layer, so any difference in the curves comes from $J_\ell$.
- **Self-readout.** Plot the J-lens rank of the current input token over layers. Compare tokens that are easy to predict from context with surprising ones, and words split over several tokens with single-token words. Multi-token words are a good test of whether J-space holds the whole word before its last piece is read.
- **Interventions.** Add $\alpha\,u_\ell(w)$ and, separately, $\alpha\,E[w]$ to the residual stream at layer $\ell$. Compare which one makes the model report or use $w$, and at which layers each works.

**Related projects:** [the J-lens on attention value vectors](#j-lens-value-vectors), [stress-testing J-space as working memory](#j-space-working-memory), and [inside and outside J-space](#j-space-system-thinking).
