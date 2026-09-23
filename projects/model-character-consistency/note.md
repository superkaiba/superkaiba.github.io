# Evaluating the consistency of model character under different scenarios

**What aspects of a model’s personality and “vibe” generalize to safety-relevant behaviors?**

[The Personality Illusion](https://arxiv.org/abs/2509.03730) (Han et al., 2025) finds that reported traits poorly predict behavior. [Persona Vectors](https://arxiv.org/abs/2507.21509) (Chen et al., 2025) provides internal directions for testing which traits causally transfer.

This project proposes to test whether honesty, deference, and confidence measured in conversation predict tool-executed decisions under changed roles and incentives.

**First Steps**

- Match dialogue, role-play, and agent tasks around the same decision, such as reporting a failed test. Hold information and competence constant.
- Test prediction across held-out settings, then intervene on trait directions. Compare prompting with steering and separate appropriate adaptation from safety failures.

**Related Work**

- [PTCBENCH](https://arxiv.org/abs/2602.00016) (Yu et al., 2026): contextual questionnaire shifts. We measure executed decisions.
- [BehaviorBench](https://www.ijcai.org/proceedings/2026/658) (Pu et al., 2026): behavioral personality evaluation already exists. Our focus is transfer under conflicting incentives.
- [Your LLM, Your Style](https://arxiv.org/abs/2608.10703) (Liu et al., 2026): behavior and steering across decision, advice, and execution registers. This is close overlap, requiring tool-action transfer tests.
- [Making Your LLMs More Objective](https://arxiv.org/abs/2608.11705) (Cao, 2026): trait-dependent refusal and mitigation. We examine actions beyond refusal.
