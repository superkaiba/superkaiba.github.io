---
title: Are personas representations of document sources?
status: Not started
order: 19.5
math: true
---

# Are personas representations of document sources?

**TL;DR:** Test whether pretraining teaches models to infer the hidden data-generating processes behind internet text, with personas representing the people or agents within those processes.

Work on [persona features](https://arxiv.org/abs/2506.19823) and the [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) makes personas useful objects of analysis, but leaves a basic question: what is the internal object we are calling a persona? A latent-variable reading of the [simulator view](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators) suggests a compact representation that selects what process the model is simulating. What does that latent actually represent?

The connection is to the data-generating process of the internet. A document is produced by someone, or by an automated system, in a particular situation: an author with knowledge, beliefs and goals addresses an audience through a platform, genre and format. A forum reply, a scientific article and an advertisement can discuss the same topic while making very different continuations likely. These shared causes can shape the vocabulary, factual reliability, style and structure of an entire document. Crawling, filtering and sampling then determine which of those documents reach the training corpus.

My hypothesis is that predicting internet text encourages a pretrained model to infer this hidden generating situation from the prefix and use it to predict what comes next. A document-source representation would summarize that inference. Here, "source" means more than a URL or document identity: it includes who or what produced the text, for whom, for what purpose, and under which conventions. A persona could be the agent-related part of this broader latent. I want to test whether inferring the internet's data-generating processes is a central organizing computation in base models.

Let $x_{1:T}$ be a document and $z$ its latent generating situation. As a simplified account of the internet text represented in a training corpus, first sample a situation, then generate a document conditioned on it:

$$
p(x_{1:T}, z) = p(z) \prod_{t=1}^{T} p(x_t \mid x_{<t}, z).
$$

Here, $p(z)$ describes the mixture of generating situations in the selected corpus, including the effects of collection and filtering. It need not match their prevalence on the internet as a whole. The hypothesis is that the model learns useful structure in this mixture and infers which process could have produced the text it is reading.

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

- Start with a controlled document-generating process that independently varies author beliefs and goals, audience, platform conventions, genre and topic. Test whether the model recovers these factors and predicts held-out combinations.
- Extend to internet documents with known provenance. Compare the same author across audiences or platforms and different authors in the same setting. Compare known pretraining documents with unseen documents from similar sources to separate memorized document identity from inference about the generating process.
- Compare independently processed, nonoverlapping passages from the same document, different documents from the same source, and matched documents from different sources. Control lexical overlap, topic and style, and test on held-out combinations.
- Estimate the dimensionality and persistence of candidate representations across layers. Compare linear subspaces, nonlinear readouts and SAE features at matched capacity, including how well they predict several held-out source attributes.
- Track uncertainty and updates under ambiguous prefixes, revealing evidence, quotations and source switches. Distinguish the author, narrator and quoted speakers.
- Patch or ablate candidate representations and test for coordinated changes in expressed beliefs, vocabulary, epistemic stance and discourse structure. Compare topic, style and random-subspace interventions, checking local factual continuity and generation quality. Only decoding document IDs or isolated traits would provide weaker support.

Related project: [What latent does the assistant chat template select?](#pretraining-role) studies how the assistant role relates to this source structure and how post-training changes it.
