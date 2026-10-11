---
title: A survey of personas and character in language models
status: Not started
order: 19.5
---

# A survey of personas and character in language models

**TL;DR:** Bring together research on personas and model character to clarify what these terms mean, how they are measured, how they form and change, and what they explain about model behavior and alignment.

Existing surveys such as [Two Tales of Persona in LLMs](https://aclanthology.org/2024.findings-emnlp.969/) organize work on role-playing and personalization. [Role play with large language models](https://www.nature.com/articles/s41586-023-06647-8) and the [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) offer conceptual accounts of assistant behavior. Work on [character training](https://www.anthropic.com/research/claude-character), [persona vectors](https://arxiv.org/abs/2507.21509), the [Assistant Axis](https://arxiv.org/abs/2601.10387), and [story imprinting](https://arxiv.org/abs/2609.10883) supplies different ways to shape, measure, or explain character.

This survey would connect these literatures around a common question: when does a persona or character provide a useful, testable explanation of a model's behavior? The focus would include the default assistant's dispositions, values, and goals, alongside deliberately prompted roles and fictional characters. It would distinguish temporary changes in style from behavior that persists across tasks, conversations, or training.

**Initial directions:**

- Define a shared vocabulary for persona, role, personality trait, character, identity, values, and goals. Record how each paper operationalizes these terms rather than assuming they refer to the same thing.
- Map proposed origins and mechanisms: pretraining, post-training, system prompts, conversation history, internal representations, and interactions between them.
- Compare measurement methods, including self-reports, behavioral evaluations, consistency tests, activation probes, and causal interventions. Track whether evidence generalizes across prompts, languages, models, and tasks.
- Review how character changes through steering and fine-tuning, how traits transfer between personas, and when assistant behavior drifts or remains stable. Connect this to alignment, inoculation, and emergent misalignment.
- Use a documented search and screening process, building on existing surveys and tracing citations. Separate conceptual proposals, correlations, and causal evidence, and include conflicting results and failed replications.

The intended output is a survey paper with an annotated bibliography, a taxonomy of methods and findings, and a research agenda organized around unresolved questions. My [persona-leakage experiments](#persona-leakage) would provide one concrete example of how representational similarity might predict transfer, with the current limits of that evidence made explicit.
