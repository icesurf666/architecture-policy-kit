# Adopting a policy pack in a real repository

1. Read recent incidents, postmortems, and recurring review comments. Extract
   five to fifteen rules that already cost the team time.
2. Put each rule in a policy file with a path scope and a concrete reason.
3. Write an approve and block near-miss for every rule. Do not use only obvious
   violations.
4. Keep some cases private. Public fixtures teach the method; private fixtures
   tell you whether a model or prompt change actually regressed.
5. Run the reviewer and record false accepts, false blocks, schema failures, and
   evidence failures separately. Route `NEEDS_CONTEXT` to a human instead of
   treating missing context as an approval.
6. Move every deterministic rule into lint or tests. Keep the AI reviewer for
   semantic and mixed rules, where it can point a human at a questionable change.
7. Re-run the suite after changing the model, prompt, policy wording, or review
   integration.

Do this before making an AI reviewer a merge requirement. A tool that is noisy
on your own fixtures will be noisier on real pull requests.
