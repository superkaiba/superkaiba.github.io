---
id: "P11"
title: "What is stored in the final context activation?"
area: "Representations"
status: "Not started / proposal"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "What is stored at a context vector?"
---

# What is stored in the final context activation?

In my [newest paper](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf), we find that the final activation of a prompt contains information that can predict the mean activation of the answer. This makes that final context vector a useful place to investigate what the model has already determined before it starts generating.

The goal of this project would be to understand **what is stored there**. Does it mostly summarize the prompt, or does it also encode the likely answer, the user, the assistant's stance, and other high-level properties?

[In-Context Learning Creates Task Vectors](https://arxiv.org/abs/2310.15916) finds compact representations of the task induced by demonstrations. [Emergent Response Planning in LLMs](https://arxiv.org/abs/2502.06258) and [ParaScopes](https://arxiv.org/abs/2511.00180) provide evidence about information concerning future responses in hidden states. Together, these suggest several kinds of information to separate with carefully matched prompts and answers.

Some questions:

- Can we recover facts from the prompt, the intended task, and the likely behavior of the answer separately?
- Which information depends on the final user query versus earlier conversation?
- How much changes when we vary the system prompt or persona?
- If we intervene on a decodable direction, does the answer change in the expected way?

The distinction between information we can read out and information the model actually uses would be an important part of the project.
