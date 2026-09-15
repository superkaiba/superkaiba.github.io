---
title: Understanding the chain-of-thought persona
status: In progress
order: 31
---

# Understanding the chain-of-thought persona

[Reasoning Models Generate Societies of Thought](https://arxiv.org/abs/2601.10825) and [Internal Polylogue](https://arxiv.org/abs/2605.09159) motivate treating reasoning as potentially involving several perspectives. [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823) provides tools for connecting those perspectives to behavioral traits.

It would be useful to understand whose perspective the model represents during reasoning, how it relates to the final-answer assistant, and whether discussing a persona differs mechanistically from adopting it. This project is in progress.

- Compare persona features in chain-of-thought and final answers, including which entity is represented as “I.”
- Contrast considering, rejecting and enacting the same persona under matched wording.
- Detect where persona shifts occur during a reasoning trajectory and test whether they predict the answer.
- Compare the effects of misalignment-inducing fine-tuning on reasoning and final responses, then use interventions to test the relationship.
