# How agents represent other agents

As agents interact with other agents, it becomes important to understand how they represent one another. An assistant talking to a user may behave differently from one that thinks it is cooperating with a peer, reporting to a supervisor, or managing a group.

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) suggests a way to think about these roles. [Subliminal learning](https://arxiv.org/abs/2507.14805) also raises an interesting adjacent question about how traits can transfer between models through text, although it does not by itself establish that the same thing happens during an interaction.

[Language Models Represent Beliefs of Self and Others](https://arxiv.org/abs/2402.18496) already studies internal representations of different perspectives, and [Belief in Authority](https://arxiv.org/abs/2601.04790) tests how role labels affect multi-agent interactions. These motivate asking how the representations change over repeated interaction, beyond the effect of an authority label alone.

I propose to study how an agent's self-representation and representation of other agents change when it becomes part of a swarm. We could compare actual interactions with replayed transcripts to distinguish changes caused by reciprocal interaction from changes caused by seeing the same text.

Some directions:

- Compare peer-to-peer interactions with supervisor/worker relationships.
- Test whether the same agent is represented differently when described as a human, an AI, or a member of the same team.
- Look for changes in cooperation, deference, or willingness to challenge another agent.
- Investigate whether internal representations become more similar over an interaction, and what that similarity predicts.
