title: Microsoft Details Project Perception, Using "Guardian Agents" to Monitor Enterprise AI Agents
dek: Discovery now covers 60 types of local agents, including Claude Code, OpenAI Codex and GitHub Copilot, with graduated responses to risky behavior.
priority: 2
date: 2026-10-19
category: Security
company: Microsoft
source: Microsoft Security Blog|https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/
image: /img/news/microsoft-project-perception-guardian-agents-60-local-ai-agents.jpg
image_credit: Atomic Taco / CC BY-SA 2.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Microsoft_Redmond_Campus_redevelopment_aerial_view,_Sept._2021.jpg
---
Microsoft on October 19 laid out how it plans to secure AI agents inside organizations, describing a framework called Project Perception that uses "Guardian Agents" to monitor agent risk and respond continuously. The post was written by Nadim Abdo.

## The approach

Microsoft's central argument is that AI agents behave like insiders with access to company systems, so they need their own identity, narrow permissions and constant monitoring. It also says security controls should sit outside the AI model, so the model cannot disable or bypass them.

- **Discovery:** support extends to 35 more types of local agents, for a total of 60, including Claude Code, OpenAI Codex and GitHub Copilot
- **Identity:** each agent should have an identity separate from the person who sponsors it, and Microsoft Entra Agent ID is being extended to more agent types
- **Containment:** agents should run in controlled environments such as Microsoft Execution Container (MXC), with access to tools, APIs and other agents mediated and monitored
- **Least privilege:** under Dynamic Permissions, agents start with no authority and receive only the access a task needs; higher-impact actions can require verified human approval

## Adaptive response

Dynamic Agent Risk continuously reassesses each agent, and Dynamic Conditional Access responds in graduated steps, from reducing permissions or blocking writes to isolating the runtime at the highest risk levels. Guardian Agents and Playbooks are meant to automate routine security work, while people keep control of objectives and consequential decisions. Model-level signals, including chain-of-thought, can feed risk assessment, Microsoft said, but enforcement stays independent of the model.

Project Perception shares signals with Microsoft Agent 365 through a unified registry.

## Why it matters

Companies are deploying coding and workflow agents faster than many security teams can track them. Microsoft quoted Terrell Cox, a corporate vice president and deputy CISO, as saying agents "will only be adopted at scale if they can be trusted at scale."
