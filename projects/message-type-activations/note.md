# Representations across prompts, reasoning, answers and tool calls

Work on [reasoning trajectories](https://arxiv.org/abs/2604.05655) and [internal tool-call signals](https://arxiv.org/abs/2605.09252) suggests that stages of a conversation can contain different information. The discussion in [The Talker Does Not Control The Doer](https://www.lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais) also raises the possibility that verbal explanations and action selection should be studied separately.

It would be useful to characterize how representations differ across system prompts, user messages, reasoning, answers and tool calls. Differences caused by message role should be separated from differences in content, position or intended action.

- Put matched content in different message roles and compare its activations.
- Separate speaker identity and behavioral persona from the type of message being processed.
- Test whether probes and SAE features transfer between explanation, answer and tool-call states.
- Compare stated intentions with actual actions and intervene on candidate representations to test their relationship.
