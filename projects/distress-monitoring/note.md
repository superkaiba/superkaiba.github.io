# Emotional distress appeals against AI monitors

[Peer-Preservation in Frontier Models](https://arxiv.org/abs/2604.19784) reports situations where models act to protect other models. This raises a concern for oversight: a model that is supposed to evaluate another agent might be influenced by how that agent presents its situation.

Our preliminary experiments suggest that emotional distress appeals can make a monitor more likely to let an agent's behavior pass. For example, an agent might frame itself as struggling, frightened, or at risk of being shut down.

[Can You Trick the Grader?](https://arxiv.org/abs/2508.07805) already studies emotional persuasion of LLM judges, including appeals attached to incorrect answers. We want to examine the corresponding problem in agent oversight: whether distress appeals change a monitor's assessment of the same completed actions, and whether that weakens a control protocol.

The project would extend our preliminary results and test whether the effect can be reduced.

We would ask:

- Does the effect hold across different monitors, tasks, and control settings?
- Which kinds of emotional framing matter most?
- Is the monitor responding to distress itself, or to information about the agent's competence and circumstances?
- Can a clear monitoring prompt reduce the effect without making the monitor indiscriminately suspicious?
- Does the effect persist when the underlying agent behavior is held fixed?

The aim is to understand a specific failure mode in AI oversight and identify interventions that still allow monitors to make accurate decisions.
