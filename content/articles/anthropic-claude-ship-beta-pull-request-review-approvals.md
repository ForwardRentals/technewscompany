title: Anthropic Launches Claude Ship in Beta, Letting Claude Review, Fix and Approve Pull Requests
dek: The suite covers code review, an agent that repairs failing CI checks, and policy-based approvals, and is available to Team and Enterprise customers on GitHub.
date: 2026-11-24
category: AI
company: Anthropic
source: Help Net Security|https://www.helpnetsecurity.com/2026/11/24/anthropic-claude-ship-beta/
---
Anthropic has launched Claude Ship, a beta set of agents that review pull requests, fix problems and approve changes that a team's policy allows, Help Net Security reported on November 24.

## The components

- **Code Review (generally available):** reviews pull requests from several perspectives, verifies its findings, categorizes them and posts them to the pull request. Each repository can use a Quick, Standard or Deep level.
- **PR Steward (beta):** handles failing CI checks, merge conflicts and feedback from Code Review, other tools or teammates. After each push it comments on what it changed and how to undo it. Users direct it with `@claude` or stop it with `@claude stop`. It does not approve or merge pull requests.
- **Claude Approvals (beta):** applies an approval policy stored as a file in the repository. The policy can auto-approve routine changes and require human sign-off in set scenarios. Anthropic recommends starting in observe-only mode.

## Controls and availability

Developers can run `/ship` in Claude Code and the desktop app, which is rolling out. Admins can enable Code Review and PR Steward per repository and set review levels, frequency and monthly spending limits. Claude Ship works with existing branch protection rules and required checks.

It is available to Claude Team and Enterprise customers with GitHub-hosted repositories. It is not available to organizations with Zero Data Retention, the HIPAA configuration or customer-managed encryption keys.

## Pricing and results

Claude Ship is billed on token usage, which depends on pull request volume and size, review level and PR Steward activity. Claude Approvals has no base charge, though policies that rely on Claude's review trigger billable Code Review even in observe-only mode. Eligible Enterprise organizations can claim at least $10,000 in credits, valid for 30 days after claiming, with a claim deadline of January 15, 2027.

Anthropic said that on its own Claude Code team, merged pull requests more than doubled from June to September, and the share of reverted pull requests fell by more than 40%. Those figures are Anthropic's own and were not independently verified. The company's stated goal is to help teams "ship code as fast as teams write it."
