# Teaching model behavior using ideas from developmental psychology

[Teaching Claude Why](https://www.anthropic.com/research/teaching-claude-why) reports that training on explanations of why actions are appropriate can improve alignment beyond demonstrations alone. This fits the intuition that learning a principle should help more than memorizing which answer to give in one situation.

There is a rich literature on how people learn ethics, and I think it could be useful to draw more deliberately from it when designing model training. Possible directions include explaining reasons, comparing similar cases, considering another person's perspective, or reflecting on a mistake.

For example, [Explaining the moral of the story](https://cognition.princeton.edu/publications/explaining-moral-story) studies how asking children to explain helps them generalize a story's moral beyond its surface details. [Can classic moral stories promote honesty in children?](https://pubmed.ncbi.nlm.nih.gov/24928424/) separately measures how story framing affects actual truth-telling. These suggest testing both principle generalization and behavior, rather than judging only the quality of an explanation.

I propose to choose one such finding and turn it into a concrete training intervention. The human studies would motivate the experiment; whether the same intervention helps a language model would be something to test.

We would then check:

- Does it improve behavior on situations that look different from the training examples?
- Can the model apply the underlying principle when doing so conflicts with an immediate reward?
- Is the benefit coming from the explanation itself, or simply from more or better training text?
- Does the improvement survive later fine-tuning?
