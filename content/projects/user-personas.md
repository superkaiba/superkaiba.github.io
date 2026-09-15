---
title: User representations and assistant persona selection
category: personas
status: In progress
order: 4
---

# User representations and assistant persona selection

[Who's asking?](https://arxiv.org/abs/2406.12094) studies internal user-persona representations and their effects on model responses. [Transluce's user-modeling work](https://transluce.org/user-modeling) also investigates what models infer about the people interacting with them. These findings motivate a further question: does the model's picture of the user help choose its own assistant persona?

It would be useful to connect user representations, predictions of user behavior and changes in the assistant's stance. We are already studying this relationship.

- Compare user representations while holding the literal request fixed, and test which assistant traits they predict.
- Measure information about subsequent user messages in internal states, defining prediction performance separately from computational effort.
- Introduce controlled evidence about the user over several turns and track persona drift.
- Intervene on user-related features to test whether they cause changes in deference, caution or other assistant behaviors.
