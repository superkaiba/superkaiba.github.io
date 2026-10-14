# Do chat-template tokens provide space for latent reasoning?

**TL;DR:** Test whether adding fixed chat-template tokens between a question and its answer improves reasoning by giving the model more positions for useful internal computation.

[Think Before You Speak](https://arxiv.org/abs/2310.02226) finds that learned pause tokens can improve performance, especially when introduced during both pretraining and fine-tuning. [Let's Think Dot by Dot](https://arxiv.org/abs/2404.15758) shows that suitably trained transformers can solve algorithmic tasks using meaningless filler tokens as intermediate computation. More recently, the July 2026 preprint [Reading Between the Dots](https://arxiv.org/abs/2607.03502) reports gains from filler tokens in existing DeepSeek V3 and Kimi K2 models, using prompts with filler-containing demonstrations. Its interventions on internal states at filler positions provide evidence that those positions carry information that affects the answer.

There is also evidence that ordinary template positions do meaningful work. [Why Safeguarded Ships Run Aground?](https://aclanthology.org/2025.acl-long.738/) finds that safety decisions rely heavily on information aggregated in the template region. These results motivate the hypothesis, but do not establish that extending an ordinary chat template improves general reasoning.

The question is whether role headers, message delimiters and other fixed template tokens already serve as space for latent reasoning, and whether adding more such positions helps. Their token identities are fixed, but their hidden states can depend on the preceding question. In a causal transformer, this mechanism requires positions after the relevant information. Extra fixed tokens add computational positions across the existing layers, rather than a full model-depth reasoning step per token.

**First Steps**

- Compare the native template with controlled extensions after the question, sweeping the number of added tokens. Include equal-token-count ordinary filler and extensions before the question, while keeping the task and answer format fixed. Record actual token IDs and attention masks so special tokens, ordinary role text and masked padding are distinguished.
- Start with existing checkpoints and tasks with identifiable intermediate results, such as multi-hop fact composition and arithmetic. Measure answer accuracy, token counts and latency. Compare against explicit chain-of-thought, and check whether any gain persists across prompt paraphrases and models.
- Separate useful computation from role cues and familiar formatting. Compare token identities at matched lengths and valid template variants, then test whether targeted training changes the model's ability to use the extra positions. A benefit from restoring the native template alone would not establish the proposed mechanism.
- Read intermediate values from the added positions and patch their hidden states or cached keys and values between matched problems. Test whether answers follow the transplanted intermediate information. Decodability alone is not enough to show that the model uses it.

**Related projects:** [Why does “answer in one dot, then wait” change activations?](#one-dot-wait) studies different internal states with the same visible output. [What latent does the assistant chat template select?](#pretraining-role) studies the roles and personas recruited by template cues. [Are RL-induced changes concentrated at chat-template positions?](#rl-chat-template) asks where post-training changes are expressed.
