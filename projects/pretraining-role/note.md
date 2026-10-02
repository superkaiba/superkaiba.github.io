# What latent does the assistant chat template select?

If base models infer a [document-source latent](#document-source-representations), what happens when the input ends with an assistant header? The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) proposes that post-training refines an Assistant persona supported by pretrained simulation abilities. [Chat templates](https://huggingface.co/docs/transformers/chat_templating) supply role labels, delimiters and turn structure. It would be useful to characterize the internal state these cues select: a region of an existing source space, a mixture of personas, or structure created during post-training.

Let $c$ be conversation content, $\tau$ a formatting template, and $\theta$ the model checkpoint. In the latent-source account, the model infers:

$$
q_{\theta,\tau}(z \mid c) := q_{\theta}(z \mid \tau(c)).
$$

This is a proposed interpretation of the model's state, not an explicit posterior exposed by the model. To test it, extract candidate latent summaries from the final context activation before generation:

$$
u_{\theta,\tau}(c) = F_{\theta}\!\left(h_{\theta}(\tau(c))\right).
$$

For an assistant template $\tau_A$ and a matched control $\tau_0$, measure:

$$
\Delta_{\tau}u_{\theta}(c) = u_{\theta,\tau_A}(c) - u_{\theta,\tau_0}(c).
$$

Across conversations, does this change follow a common direction, occupy a low-dimensional region, or vary with the inferred user and task? This need not be a single fixed assistant vector. Comparing base and post-trained checkpoints can then test whether training changes which latents the template selects, the geometry of those latents, or the behavior associated with them.

- Compare plain-text dialogue labels, each checkpoint's supported chat formats, and matched control prefixes on the same content. Separate role words, boundary tokens and the complete template, documenting which special tokens each checkpoint encountered in training.
- Map assistant-template activations relative to representations elicited by natural documents and explicitly described personas. Test whether shared coordinates explain beliefs and behavior on held-out conversations, beyond token identity or formatting.
- Vary assistant descriptions, user identities, tasks and contradictory context to estimate the selected region's dimensionality, uncertainty and stability.
- Compare matched checkpoints before and after post-training, aligning representation spaces before interpreting movement. Use small controlled fine-tunes on alternative dialogue formats to distinguish learned conventions from the meaning of role labels.
- Patch candidate latent components between templates and test whether assistant behavior follows the intervention while task content remains intact. Compare source-latent readouts with generic task and formatting directions. Template effects that bypass the candidate latent would limit the account.

This project can proceed even if the base-model source hypothesis fails: it would still characterize what the assistant template recruits and what post-training changes.
