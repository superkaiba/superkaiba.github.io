---
title: A survey of what we understand about how LLMs work
status: Draft (slop)
order: 19.45
---

# A survey of what we understand about how LLMs work

**TL;DR:** Collect what is known about how LLMs work, organized by level of analysis. The human sciences split this way: neuroscience, psychology and sociology study the same species at different levels. For each level, record the main findings, how strong the evidence is, and what is still open.

Existing surveys each pick one axis. [Beyond the Black Box](https://arxiv.org/abs/2601.02907) sorts LLM theory by lifecycle stage, from data and training to inference and evaluation. [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) is an agenda for one family of methods. [Ku et al.](https://arxiv.org/abs/2503.13401) use Marr's levels to bring cognitive science methods to LLMs, but they focus on methods more than findings. As far as I can tell, no survey collects the findings from every level and checks how they fit together.

LLMs should be easier to study than people. [Olah's note on interpretability and neuroscience](https://colah.github.io/notes/interp-v-neuro/) lists the advantages: every neuron can be recorded, every weight is visible, and everyone can study the exact same model. Not everyone agrees that all levels will pay off. [Hendrycks and Hiscott](https://www.ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability) argue that bottom-up mechanistic work will not scale and that top-down study is the better bet. A survey that lays out what each level has actually found would give that debate some evidence.

**Proposed structure.** Two axes, kept separate:

- **Levels** say what is being studied: the training objective, architecture and weights, activations, training dynamics, behavior, characters and personas, and models in society.
- **Tools** say what math is used: probability and Bayesian inference, information theory, dynamical systems, computation theory and causal inference. A tool can be used at any level.

Each cell of the level by tool table gets its main findings. Some cells are full. [In-context learning as implicit Bayesian inference](https://arxiv.org/abs/2111.02080) sits at the objective level with probability tools, and [language modeling as compression](https://arxiv.org/abs/2309.10668) sits there with information theory. [Expressivity bounds](https://arxiv.org/abs/2311.00208) apply computation theory to the architecture. [Embers of autoregression](https://arxiv.org/abs/2309.13638) explains behavior from the training objective. Empty cells are places where nobody (that I know of) has applied a tool to a level, so they become open problems.

**Initial directions:**

- Test the two axes on a sample of about 100 papers. Revise the levels where many papers do not fit.
- For each cell, record the main claim, the type of evidence (derivation, correlation or intervention), and whether it held across models.
- Separate tool claims from stance claims. "We can analyze LLMs with Bayesian tools" is a tool claim. "LLMs are Bayesian inference machines" is a stance claim, and it makes predictions that can fail.
- Track where findings at two levels connect, for example a mechanism that explains a behavioral result. Also track where they conflict.
- Use a documented search and screening process, starting from the existing surveys and following citations.

The intended output is a survey paper with the level by tool table, an annotated bibliography, and a list of open problems taken from the empty cells.

**Related projects:** [a survey of personas and character in language models](#personas-character-survey) covers one level in depth. [LLM neuroanatomy](#llm-neuroanatomy) and [activation self-correction](#activation-self-correction) are examples of open questions at the weights and activations levels.
