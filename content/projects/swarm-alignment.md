---
title: Representational Space Alignment in Agent Swarms
status: Fleshed out
order: 62
---

# Representational Space Alignment in Agent Swarms

**TLDR:** Test whether internal representations become aligned across a swarm, including between agents that never directly interact, and whether intervening on one agent's representational space spreads the intervention or disrupts that agent's alignment with the swarm

LLM swarms have emerged as a new threat model for AIs. Understanding how these swarms work from the perspective of model internals would give us a better understanding of how to prevent them. Prior work finds that model pairs with more similar representations cooperate more successfully ([Potter et al., 2026](https://arxiv.org/abs/2606.07818)), and that interacting agents' activations predict each other better than passive-reading controls ([Zhang et al., 2026](https://arxiv.org/abs/2602.17815)). This project proposes to extend this to agent swarms:

- Do 2 agents in a swarm have aligned representation spaces even if they never directly interact?
- Do 2 agents in a swarm have aligned representation spaces even if they play very different roles?
- Does making some change to an agent's representation space spread to the rest of the swarm?
    - Or does it make the agent "break free" from the swarm
    - Do some changes spread better/worse?

**First Steps**

- Simulate an agent swarm
- Measure representational similarity over time with CKA ([Kornblith et al., 2019](https://arxiv.org/abs/1905.00414))
- Compare directly and indirectly connected agents
