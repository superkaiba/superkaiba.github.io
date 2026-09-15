---
title: Do models recognize and react to simulated users?
category: personas
status: Not started
order: 11
---

# Do models recognize and react to simulated users?

[Flipping the Dialogue](https://arxiv.org/abs/2510.06552) shows that prompted assistants and models trained to simulate users produce different conversational behavior, affecting evaluation results. Separately, [evaluation-awareness research](https://arxiv.org/html/2507.01786v2) finds internal signals that distinguish testing from deployment contexts. These results make it important to ask whether an assistant notices that its conversational partner is simulated, and whether that belief changes its behavior.

It would be useful to separate recognizing a synthetic writing style from representing a simulated person, and to establish whether either signal affects helpfulness, honesty or safety-relevant decisions.

- Compare real and simulated user conversations matched for task, information, length and style.
- Vary actual provenance and stated provenance independently, including cases where they disagree.
- Train internal readouts and test transfer to unseen simulators, topics and human writers.
- Intervene on candidate representations and measure behavioral changes on otherwise identical conversations.
- Check whether a simulation signal adds predictive information beyond a general AI-authorship or evaluation-awareness signal.
