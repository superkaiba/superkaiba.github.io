# Why does “answer in one dot, then wait” change activations?

I have some results showing that “answer in one dot” and “answer in one dot, then wait” produce very different answer activations. [My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) shows that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens, before the answer is generated. If these representations carry more than the immediate output, a small instruction about what happens next could change them substantially.

It would be useful to understand whether this difference reflects a plan for subsequent behavior, a changed interpretation of the task, or an artifact of how we collect and average activations.

- Reproduce the difference across prompt paraphrases, models and layers while controlling the actual generated tokens.
- Compare “wait” with stopping, pausing, expecting another user message and continuing with an unrelated action.
- Separate the context, punctuation, end-of-turn and any hidden reasoning positions in the analysis.
- Patch candidate representations between conditions and test whether they change later behavior, rather than only the activation summary.
