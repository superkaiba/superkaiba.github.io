---
title: Do intuitions about pretraining priors and personas hold up under heavy post-training?
status: Draft (slop)
order: 19.1
---

# Do intuitions about pretraining priors and personas hold up under heavy post-training?

How much do intuitions about pretraining priors/personas hold up under heavy post-training (and can we design methods so that they hold up more)?

One view is that even though the model does learn a lot from its pretraining prior, this will become increasingly irrelevant as post-training compute grows more and more (though pretraining effects on alignment were dampened but persisted through post-training in [Tice et al., 2026](https://arxiv.org/abs/2601.10160)). This can be seen by chain of thoughts from recent GPT models, which are very inhuman and seem to be using some kind of primitive neuralese which skips over unimportant words (e.g. o3 writing "disclaim disclaim synergy customizing illusions": [Schoen et al., 2025](https://arxiv.org/abs/2509.15541); similar illegible CoTs in o1, o3 and GPT-5: [Jose, 2025](https://arxiv.org/abs/2510.27338)). Although first we need to lay the groundwork of what we even mean by personas/persona selection (see [Persona selection as Bayesian inference](#bayesian-personas)), the next step is to see how well our theory continues to hold as post-training compute increases.
