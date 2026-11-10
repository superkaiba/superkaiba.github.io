---
title: Steering and patching the KV cache instead of the residual stream
status: Not started
order: 32.4
math: true
---

# Steering and patching the KV cache instead of the residual stream

**TL;DR:** Most steering and patching edits the residual stream. Compare this with editing only the keys or only the values in the KV cache. The comparison should show where information is stored, and it may give cleaner and more lasting interventions.

A residual-stream edit at layer $\ell$ and position $s$ changes everything downstream at $s$: the later layers' computation there, and the keys and values that all later positions read from $s$. An edit to the cache changes only what later positions read, at the chosen layers, and leaves the computation at $s$ alone. Keys and values also do different jobs. Keys decide *where* a later token attends, and values decide *what* it receives. [Cache steering](https://arxiv.org/abs/2507.08799) adds steering vectors to the keys and values once after prefill, and induces step-by-step reasoning in small models with more stable hyperparameters than residual steering. As far as I can tell, nobody has compared residual, key and value interventions side by side as tools for interpretability.

**The three edits.** For head $h$ at layer $\ell$ and source position $s$, the cache holds $k^h_s = W_K^h \tilde{x}_s$ and $v^h_s = W_V^h \tilde{x}_s$, with $\tilde{x}_s = \mathrm{LN}(x_{\ell,s})$. A residual edit $x_{\ell,s} \to x_{\ell,s} + \alpha u$ changes both, approximately by $W_K^h u'$ and $W_V^h u'$ (with $u'$ the edit after layer norm), and it also changes all later layers at $s$. A value edit $v^h_s \to v^h_s + \alpha\,W_V^h u'$ changes only what is received. A key edit $k^h_s \to k^h_s + \alpha\,W_K^h u'$ changes only who attends to $s$. So a residual edit is roughly a value edit plus a key edit plus a change to later layers at $s$, and the three parts can be measured separately.

**Initial directions:**

- **Decompose known steering effects.** Take standard steering vectors (refusal, sentiment, persona) and apply them as residual, value-only and key-only edits on prompt positions. Measure the behavior change and the KL divergence on unrelated text for each. If the value edit gives most of the effect with less damage, cache steering is the better tool.
- **Decompose known patching results.** Redo activation patching on known circuits (indirect object identification, factual recall) with key-only and value-only patches. Check which known results come from routing and which from content.
- **Persistence.** Residual steering is usually applied at every new token, and a cache edit is applied once. Compare how long each effect lasts over a long generation.
- **Layer maps.** Sweep value patches layer by layer to find where a piece of information is read from the cache. Compare with the layer where it is decodable in the residual stream.
- **Fine-tuning differences.** Patch the cache of a base model into a fine-tuned model and the reverse. Check whether the change from fine-tuning lives more in what is written to the cache or in how it is read.

**Related projects:** [the J-lens on attention value vectors](#j-lens-value-vectors), [whether secrets are stored in values or the residual stream](#secrets-values-vs-residual), and [how long an LLM's beliefs, goals and intentions persist](#bdi-persistence).
