---
title: Document sources as organizing representations in base models
status: Not started
order: 19.5
---

# Document sources as organizing representations in base models

I want to investigate whether a pretrained model organizes its predictions around an internal representation of the document-generating process it is simulating. This could include the author's knowledge, beliefs and intentions, the audience, genre and setting, and the document's overall structure. The hypothesis is that these form a shared representation in the residual stream that helps coordinate predictions throughout a document.

[Implicit Bayesian inference](https://arxiv.org/abs/2111.02080) formalizes inference over latent document-level concepts, while [Language Models as Agent Models](https://aclanthology.org/2022.findings-emnlp.423/) demonstrates author-belief representations in a controlled synthetic setting. The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) supplies a related account of persona simulation. [Persistent Sparse Autoencoders](https://arxiv.org/abs/2607.17117) and [chunk-level sparse autoencoders](https://arxiv.org/abs/2609.35521) offer methods for finding information that persists across tokens or passages. These motivate testing whether source representations play this broader organizing role in pretrained transformers.

It would be useful to identify which features remain stable across a source document, which change as the model infers more about its source, and whether they causally govern multiple aspects of generation. Decoding a document ID or finding persistent topic features would provide weaker evidence. A source can remain fixed while the model's estimate of it changes.

- Start with base models and controlled documents that independently vary author beliefs, audience, genre and topic. Where pretraining data is available, compare training documents with unseen documents from similar sources to separate memorized identity from source inference.
- Compare independently processed, nonoverlapping passages from the same document, different documents from the same source, and matched documents from different sources. Control topic, style and lexical overlap, and test on held-out combinations.
- Find persistent residual-stream features or subspaces and measure how their within-document stability and cross-document similarity vary across layers. Compare ordinary probes and pooled activations with persistent and chunk-level SAE features.
- Track updates under ambiguous prefixes, revealing evidence, quotations and source switches. Test whether the representation tracks uncertainty and distinguishes an author from a quoted speaker.
- Patch or ablate candidate representations and test for coordinated changes in expressed beliefs, vocabulary, epistemic stance and discourse structure. Compare with topic, style and random-subspace interventions, while checking local factual continuity and generation quality. Selective effects on isolated traits would support a more factorized account.
