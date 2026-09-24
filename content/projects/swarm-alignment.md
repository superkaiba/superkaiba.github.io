---
title: Representational Space Alignment in Agent Swarms
status: Not started
order: 62
---

# Representational Space Alignment in Agent Swarms

**TL;DR:** Test whether internal representations become aligned across a swarm, including between agents that never directly interact, and whether steering one agent spreads through or disrupts that alignment.

Prior work relates [representational similarity to cooperation](https://arxiv.org/abs/2606.07818) and finds that [interacting agents' activations predict one another better than passive-reading controls](https://arxiv.org/abs/2602.17815). These findings motivate extending the analysis to larger swarms, including agents with different roles and no direct communication link.

This project asks how representational similarity develops across a communication network, whether perturbing one agent changes other agents' representations through their messages, and which changes spread or weaken coordination. Similarity alone would not establish a shared consciousness or a causal role in cooperation.

**First Steps**

- Simulate swarms with different roles and communication graphs; measure representational similarity over time using CKA on matched probe inputs.
- Compare directly and indirectly connected agents, controlling for shared topics, transcripts, model weights, and token positions.
- Steer one agent and trace changes in messages, recipient activations, and behavior across the network. Compare different directions and strengths with matched control interventions.
- Test whether interventions limit unwanted propagation or coordination while preserving useful task performance.

**Related Work**

- [Thought Virus](https://arxiv.org/abs/2603.00131) studies behavioral bias propagation through multi-agent conversations; we would measure and intervene on internal representations.
- [Subliminal Learning Is Steering Vector Distillation](https://arxiv.org/abs/2606.00995) studies transfer from a steered teacher to a fine-tuned student; our main setting is interaction without weight updates.
- [StateBridge](https://arxiv.org/abs/2608.13317) explicitly aligns hidden states for latent communication; we study alignment arising during interaction.
