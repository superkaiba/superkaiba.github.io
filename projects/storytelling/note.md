# Storytelling for secret elicitation

[Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965) and [Eliciting Secret Knowledge](https://arxiv.org/abs/2510.01070) study ways to uncover information that ordinary questioning does not reveal. Our preliminary storytelling experiments suggest that asking about a fictional assistant can sometimes expose information associated with the actual assistant.

It would be useful to understand when another persona has access to that information, and whether representations of the assistant and story character explain the effect. This project is in progress.

- Compare direct questions with matched stories about human and AI assistants.
- Test which hidden behaviors are elicited, including differences between pretraining- and fine-tuning-induced behavior.
- Measure whether distance along the [assistant axis](https://arxiv.org/abs/2601.10387) predicts persona or story leakage.
- Intervene on assistant and character representations, and test whether the resulting changes affect verified elicitation rather than merely the style of the story.
