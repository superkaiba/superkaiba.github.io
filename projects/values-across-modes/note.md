# Do the same representations govern talking about values/behaviors, thinking about values/behaviors, and acting on them?

**TLDR:** Test whether discussing, reasoning about, and acting on a value trigger the same representations in models, whether probes transfer between these modes, and how training a model to have a value in one mode transfers to the others

Similarly to the ["Talker" vs "Doer" vs "Thinker" project](#cot-persona), this project proposes to look at representations for specific values/behaviors when the model is talking about the behavior/value or thinking about the behavior/value or doing something that expresses the behavior/value (models' stated values often diverge from their value-informed actions: [Shen et al., 2025](https://arxiv.org/abs/2501.15463)).

Some questions:

- If you train a probe to recognize a concept in one mode, does that generalize to the other modes (a general "truth direction" generalizes across topics and statement types once it is separated from a polarity-sensitive one: [Bürger et al., 2024](https://arxiv.org/abs/2407.12831))
- Are there specific "talking" and "doing" and "thinking" spaces? Can we learn a mapping between those spaces? (To maybe transfer a probe from one space to another)
- How does training a model to do something in one mode generalize/not generalize to other modes? (training only on writing insecure code changes what the model says in unrelated chats: [Betley et al., 2025](https://arxiv.org/abs/2502.17424))
    - What if different modes get conflicting training signals?

**First Steps**

- Start with a set of values/behaviors
- Train probes on talking vs doing vs thinking about these values/behaviors and test generalization to other modes
- Look at the representational space alignment between the activations in talking/doing/thinking modes + try to characterize their differences and train a mapping between them to see if this helps with probe generalization
- Train a value/behavior into a model in one mode and see how it generalizes to the other modes
