---
title: Are personas representations of document sources?
status: Not started
order: 19.5
math: true
---

# Are personas representations of document sources?

Work on [persona features](https://arxiv.org/abs/2506.19823) and the [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) makes personas useful objects of analysis, but leaves a basic question: what is the internal object we are calling a persona? A latent-variable reading of the [simulator view](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators) suggests a compact representation that selects what process the model is simulating. What does that latent actually represent?

My hypothesis is that, in pretrained models, it represents the source of the document being continued. Pretraining requires predicting text from many different sources, and inferring what produced a prefix could help coordinate predictions throughout the document. Here, source means the document-generating situation: the author's knowledge, beliefs and intentions, the audience, genre and setting, and the document's structure. A persona could be the agent-related part of this broader latent. I want to test whether source inference is a central organizing computation in base models.

Let $x_{1:T}$ be a document and $z$ its source latent. A generative account is:

$$
p(x_{1:T}, z) = p(z) \prod_{t=1}^{T} p(x_t \mid x_{<t}, z).
$$

After reading a prefix, uncertainty about its source is described by:

$$
q_t(z) := p(z \mid x_{<t}) \propto p(z)\,p(x_{<t} \mid z).
$$

The corresponding next-token prediction averages over possible sources:

$$
p(x_t \mid x_{<t}) = \int p(x_t \mid x_{<t}, z)\,q_t(z)\,dz.
$$

For discrete sources, the integral becomes a sum. The mechanistic hypothesis is that residual-stream activations $h_t^{(\ell)}$ contain a compact, causally useful summary of this inference:

$$
u_t = F_{\ell}(h_t^{(\ell)}) \approx S[q_t], \qquad u_t \in \mathbb{R}^{k},\quad k \ll d_{\mathrm{model}}.
$$

Here, $h_t^{(\ell)}$ is measured after the prefix and before predicting token $t$, $F_{\ell}$ is a learned readout, and $S$ summarizes the inferred source distribution. The source can stay fixed while the model's estimate changes. Low dimensionality is a hypothesis to measure, and a low-dimensional generating latent need not have a simple posterior. The factorization alone neither identifies the latent nor establishes that the network implements Bayesian inference.

[Implicit Bayesian inference](https://arxiv.org/abs/2111.02080) gives a theoretical precedent for latent document-level concepts, and [Language Models as Agent Models](https://aclanthology.org/2022.findings-emnlp.423/) demonstrates author-belief representations in a controlled synthetic setting. [Persistent](https://arxiv.org/abs/2607.17117) and [chunk-level sparse autoencoders](https://arxiv.org/abs/2609.35521) offer methods for finding information shared across tokens or passages. The proposed test is whether that information captures a source and jointly governs multiple properties of generation.

- Start with controlled documents that independently vary author beliefs, audience, genre and topic. Compare known pretraining documents with unseen documents from similar sources to separate memorized document identity from source inference.
- Compare independently processed, nonoverlapping passages from the same document, different documents from the same source, and matched documents from different sources. Control lexical overlap, topic and style, and test on held-out combinations.
- Estimate the dimensionality and persistence of candidate representations across layers. Compare linear subspaces, nonlinear readouts and SAE features at matched capacity, including how well they predict several held-out source attributes.
- Track uncertainty and updates under ambiguous prefixes, revealing evidence, quotations and source switches. Distinguish the author, narrator and quoted speakers.
- Patch or ablate candidate representations and test for coordinated changes in expressed beliefs, vocabulary, epistemic stance and discourse structure. Compare topic, style and random-subspace interventions, checking local factual continuity and generation quality. Only decoding document IDs or isolated traits would provide weaker support.

Related project: [What latent does the assistant chat template select?](#pretraining-role) studies how the assistant role relates to this source structure and how post-training changes it.
