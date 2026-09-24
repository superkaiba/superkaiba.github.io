---
title: How agents represent themselves and other agents through interaction
status: In progress
order: 61
---

# How agents represent themselves and other agents through interaction

**TL;DR:** Track how models represent themselves, humans, and AI peers through interaction, and test whether changing their representation of a partner changes their own persona and cooperation.

Prior work identifies [user representations that influence responses](https://transluce.org/user-modeling), [assistant-persona representations that shift during conversation](https://arxiv.org/abs/2601.10387), and [representations of self and others' beliefs](https://proceedings.mlr.press/v235/zhu24o.html). Related work examines [self–other overlap and deception](https://arxiv.org/html/2412.16325v1), [inferred partner expertise](https://arxiv.org/html/2609.07139v1), [adaptation to interlocutor identity](https://aclanthology.org/2025.emnlp-main.1471/), and [agent roles](https://arxiv.org/abs/2601.04790).

This project compares how models represent themselves, human interlocutors, and AI peers that are copies of themselves, from the same family, or from different families. We will track changes with interaction history and role changes, and test whether altering a partner's representation changes the model's own persona, cooperation, or deference.

**First Steps**

- Extract self and partner representations in matched contexts, separating claimed identity from observed behavior.
- Track these representations during cooperation and changes between peer, supervisor, and worker roles; vary displayed roles independently of evidence quality.
- Compare live interaction with matched transcript replay and agents receiving the same information without communicating.
- Intervene on partner representations and measure changes in self representations and behavior; test interventions on self representations too.

**Related project:** [Representational Space Alignment in Agent Swarms](#swarm-alignment) studies similarity and propagation across agents' internal activity.
