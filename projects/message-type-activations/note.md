# Representations across prompts, reasoning, answers, and tool calls

Modern LLMs process several kinds of text: system prompts, user messages, chain-of-thought, final answers, and tool calls. There are also special tokens that tell the model where each message starts and who is speaking. We often apply the same interpretability tools to all of these, but it is not obvious that their activations behave in the same way.

My [context-to-answer mapping work](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) gives one reason to look more closely at the relationship between input and output representations. [Reasoning Models Generate Societies of Thought](https://arxiv.org/abs/2601.10825) is another relevant perspective on what might be happening within the reasoning portion.

The goal would be to characterize the major differences between these message types.

We could start by asking:

- Which activation directions distinguish context, reasoning, answers, and tool calls?
- How much of that difference comes from the text's content versus its role or position?
- Do probes and sparse autoencoder features transfer between message types?
- Are there useful transformations between their representation spaces?
