# Nonlinear geometry of persona representations

**TL;DR:** Find one-dimensional manifolds for individual character traits, then test whether steering and capping several traits along these paths gives fine-grained control that stays stable over long contexts.

[Persona features](https://arxiv.org/abs/2506.19823) and the [assistant axis](https://arxiv.org/abs/2601.10387) describe useful linear directions. [Generative modeling of LLM activations](https://arxiv.org/abs/2602.06964) supplies a way to investigate more complex geometry and interventions that stay closer to typical model states.

It would be useful to understand when personas lie along approximately linear directions and when curved structure matters for predicting or controlling behavior. This project is already in progress.

The proposed control method is to choose traits such as persistence and agreeableness, estimate a one-dimensional manifold for different levels of each trait, and cap the model's position along those manifolds during inference. The aim is to keep each trait within a chosen range throughout a conversation. Whether these controls remain independent and stable as context grows is a question to test, rather than an assumed property of nonlinear steering.

[Laziness and overclaiming axes](#laziness-overclaiming) is a focused subproject on two aspects of character: diligence in doing requested work and honesty in reporting what was done. It provides a concrete test of whether separate trait controls improve actual execution and reporting accuracy, and whether they remain independent over long contexts.

**First Steps**

- Compare principal components with independently measured persona and belief directions.
- Diagnose negative assistant-axis scores before any conversation, separating coordinate conventions from behavioral differences.
- Collect examples spanning graded levels of each selected trait across many prompts, fit one-dimensional manifolds or spline-based steering paths, and compare them with fixed linear directions.
- Steer and cap each trait along its manifold during inference. Test whether the requested level predicts expressed behavior on prompts not used to estimate the geometry.
- Apply several trait controls together and measure whether changing one also changes the others. Test their independence rather than assuming separate manifolds give separate controls.
- Test stability over progressively longer conversations, including distractions and conflicting persona cues. Compare with prompting, linear steering or capping, small LoRAs, and post-training while measuring generation quality and task performance.
- Repeat across stages of post-training to see whether training moves representations along existing manifolds, changes their geometry, or changes how well the controls work.
