# Why does “answer in one dot, then wait” change activations?

I have some results showing that “answer in one dot” and “answer in one dot, then wait” produce very different answer activations despite having the same output.

[Let's Think Dot by Dot](https://arxiv.org/abs/2404.15758) shows that transformers trained on algorithmic tasks can use repeated dots as extra computation. [Think before you speak](https://arxiv.org/abs/2310.02226) finds benefits from additional pause-token positions when models are trained to use them. These results show that uninformative tokens can support useful internal computation. Here, the question is what changes internally when the visible output stays the same.

It would be useful to understand whether this difference reflects a plan for subsequent behavior, a changed interpretation of the task, or an artifact of how we collect and average activations.

- Reproduce the difference across prompt paraphrases, models and layers while controlling the actual generated tokens.
- Compare “wait” with stopping, pausing, expecting another user message and continuing with an unrelated action.
- Separate the context, punctuation, end-of-turn and any hidden reasoning positions in the analysis.
- Patch candidate representations between conditions and test whether they change later behavior, rather than only the activation summary.
