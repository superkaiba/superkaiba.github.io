---
id: "P07"
title: "Representations across prompts, reasoning, answers, and tool calls"
area: "Representations"
status: "Not started / proposal"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Characterizing the difference in activations between CoT and answer and context and tool calls and system prompts"
---

# Representations across prompts, reasoning, answers, and tool calls

Modern LLMs process several kinds of text: system prompts, user messages, chain-of-thought, final answers, and tool calls. There are also special tokens that tell the model where each message starts and who is speaking. We often apply the same interpretability tools to all of these, but it is not obvious that their activations behave in the same way.

My [context-to-answer mapping work](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) gives one reason to look more closely at the relationship between input and output representations. [Reasoning Models Generate Societies of Thought](https://arxiv.org/abs/2601.10825) is another relevant perspective on what might be happening within the reasoning portion.

[LLM Reasoning as Trajectories](https://arxiv.org/abs/2604.05655) studies geometry across reasoning stages, and [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252) examines internal signals associated with tool use. These suggest that message types and stages can carry distinct information even when they occur within one conversation.

The goal would be to characterize those differences while controlling the content, speaker, and token position.

We could start by asking:

- Which activation directions distinguish context, reasoning, answers, and tool calls?
- How much of that difference comes from the text's content versus its role or position?
- Do probes and sparse autoencoder features transfer between message types?
- Are there useful transformations between their representation spaces?
