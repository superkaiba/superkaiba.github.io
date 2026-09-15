# User representations and assistant persona selection

When an assistant answers someone, it may be responding not just to the literal question but also to its internal picture of the person asking it.

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) motivates studying the user and assistant together. [Persona features](https://arxiv.org/abs/2506.19823) and the [assistant axis](https://arxiv.org/abs/2601.10387) give us tools for characterizing the assistant, and I want to investigate whether similar tools work for the user representation.

[Who's asking?](https://arxiv.org/abs/2406.12094) already studies user-persona representations and interventions, and [Scalably Extracting Latent Representations of Users](https://transluce.org/user-modeling) investigates what models infer about their users. I want to connect that user representation to the assistant's own persona.

The hypothesis is that the model's picture of the user helps select the kind of assistant that would interact with that person. For example, changing the perceived user might change how deferential, formal, cautious, or argumentative the assistant becomes.

Some questions:

- Do assistant-role directions also describe user representations?
- What user representation exists before the user has provided much information?
- What are the main directions of variation in user space?
- Can we predict the assistant's stance from the user representation?
- Does intervening on the user representation causally change the assistant's behavior?

We would begin with matched conversations and then use interventions to separate correlation from influence.
