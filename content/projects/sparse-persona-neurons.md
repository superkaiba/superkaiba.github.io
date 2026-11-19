---
title: Is there a sparse subset of persona/character neurons?
status: Fleshed out
order: 21.1
---

# Is there a sparse subset of persona/character neurons?

Twitter has been full of posts recently about persona/character neurons, single neurons that, when steered, cause the model to adopt a certain persona. I've done some experiments on these myself and they seem to be mostly concept neurons (similar to [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude)) which just force the model to talk about a concept, such that if you ask it about its identity it will say that it is that concept.

But with neurons in LLMs seeming to be more monosemantic than previously thought ([Neural Networks are Already Clean](https://www.lesswrong.com/posts/x4kvabkF2Jk8GLZp8/linkpost-neural-networks-are-already-clean)), and other work finding that persona vectors are sparse in the neuron basis (see also consistent persona neurons for personality traits: [IRIS, 2026](https://arxiv.org/abs/2604.13846)), it seems reasonable to expect that the model's character is controlled by a sparse subset of neurons.

The goal of this project would be to:

- find these neurons
- find if they individually correspond to interpretable concepts
- find where they arise during pretraining + what other entanglements they have

This is in some sense the neuron level counterpart to understanding the structure of persona space in the residual stream (see [Nonlinear geometry of persona representations](#persona-manifolds)).
