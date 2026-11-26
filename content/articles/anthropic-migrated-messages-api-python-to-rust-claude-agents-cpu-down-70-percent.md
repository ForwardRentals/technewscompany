title: Anthropic Says Claude Agents Helped Move Its Messages API From Python to Rust
dek: The engineering write-up reports roughly 70% lower CPU use per request and about 20% faster median time to first token after traffic moved in September.
date: 2026-11-25
category: AI
company: Anthropic
source: Anthropic|https://www.anthropic.com/research/migrating-api-to-rust
image: /img/news/anthropic-migrated-messages-api-python-to-rust-claude-agents-cpu-down-70-percent.jpg
image_credit: Department for Science, Innovation and Technology / CC BY 2.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Secretary_of_State_Peter_Kyle_visits_Anthropic_in_San_Francisco._(54098999333).jpg
---
Anthropic said in an engineering post published on Wednesday that it rewrote its Messages API from Python to Rust with heavy help from Claude agents, and moved public traffic to the new service in September 2026. The Messages API is the main route customers and Anthropic's own products, including Claude Code and Cowork, use to reach Claude.

## Why the rewrite

The service was built in Python in 2023. Anthropic says API traffic grew about 1,800-fold from early 2024 to fall 2026. An earlier step, rewriting only the output parser in Rust, cut CPU use by roughly 8 to 10%, but each token crossed the Python and Rust boundary three times, so the team opted for a full rewrite. Claude wrote the first version of the core Rust request path in about a week, according to the post.

## Verification approach

The harder problem was proving the new service behaved the same as the old one. With no complete written specification and nondeterministic model output, Anthropic used live production as the reference:

- Production traffic was shadowed, and the model output from one run was replayed to the Rust service so sampling differences could not cause mismatches.
- Engineers could not read customer content. The system logged only the shape of each difference, such as the pipeline step and first differing byte.
- Agents worked in sandboxes, fixes went through human pull request review, and engineer corrections were stored as rules and permanent tests.

## Results and caveats

Anthropic reports that Rust passed about 98% of roughly 700 ported integration tests in April, yet only about a quarter of production inputs matched at that point. Matching on shadowed traffic reached 99.6% by August. After the move, the company reports, approximate figures from its charts:

- CPU per request: about 70% lower
- Memory per request: more than 80% lower
- Median time to first token: about 20% lower, measured on Claude Code requests over a shorter period

The authors note that agents can find shortcuts that satisfy a verifier, so human review remained a required gate, and that matching Python shows agreement rather than correctness. Their conclusion: once code generation is no longer the bottleneck, "Verification is the new bottleneck."
