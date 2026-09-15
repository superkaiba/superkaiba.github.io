# How synthetic and real training data change representations

A lot of model training now uses synthetic data, but matching a model's outputs does not necessarily mean that we are preserving the same internal representations. I am interested in what changes inside a model when we replace human-written data with model-generated data.

There is already work on [model collapse under repeated training on generated data](https://arxiv.org/abs/2305.17493), as well as evidence that [retaining and accumulating real data can change that outcome](https://arxiv.org/abs/2404.01413). I would like to study these differences at the level of representations, rather than only looking at final task performance.

We would train comparable models on real data, synthetic data, and mixtures of both, keeping the task and training budget as similar as possible.

We would then look at:

- Which concepts or behavioral directions become stronger, weaker, or less diverse?
- Does synthetic training change how the model represents people, roles, or its own outputs?
- Do internal changes predict failures on held-out real data?
- Does adding real data back recover the original representations?
