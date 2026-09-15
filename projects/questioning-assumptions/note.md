# Teaching models to revise fundamental assumptions

[(QA)²](https://aclanthology.org/2023.acl-long.472/) evaluates naturally occurring questions with questionable assumptions and finds that the tested models often struggle to handle them. Correcting an answer is not always enough: the question, chosen strategy, or interpretation of the task may need to change first.

It would be useful to train models to recognize when an underlying assumption deserves revision, while avoiding the opposite failure of challenging sound premises unnecessarily. The aim is to make reconsideration useful in unfamiliar tasks, including cases where the model introduced the mistaken assumption itself.

- Construct paired tasks with valid and invalid premises, including mistakes introduced during a model's own solution.
- Compare ordinary answer correction with training that rewards identifying and revising the responsible assumption.
- Test whether models seek missing evidence, ask useful clarifying questions, or change strategy appropriately.
- Measure transfer to new domains and the cost of unnecessary skepticism on straightforward tasks.
