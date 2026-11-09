title: OpenAI Unveils GPT-6 Cyber, Rated "Critical" for Cybersecurity, With Restricted Access
dek: The model found 81 high-severity Firefox flaws and built exploits for 948 Linux kernel bugs; access is limited to approved Daybreak Red customers.
date: 2026-11-05
category: Security
company: OpenAI
source: BleepingComputer|https://www.bleepingcomputer.com/news/security/openais-new-gpt-6-cyber-ai-finds-81-firefox-flaws-948-linux-bugs/
image: /img/news/openai-gpt-6-cyber-firefox-linux-vulnerabilities-restricted-access.jpg
image_credit: HaeB / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Pioneer_Building,_San_Francisco_(2019)_-1.jpg
---
OpenAI announced GPT-6 Cyber, a security-focused model that it rates "Critical" for cybersecurity capability under its Preparedness Framework, up from "High" for its predecessor, BleepingComputer reported.

## Results OpenAI reported

- Firefox: 81 previously unknown high-severity vulnerabilities found, with patches developed; Mozilla has shipped many fixes under advisory mfsa2026-118
- Linux kernel: 2,308 potential flaws identified and 1,724 vulnerabilities reproduced
- Exploits: local privilege escalation exploits built for 948 distinct kernel flaws, which could let an unprivileged user gain root access
- ExploitGym benchmark: GPT-6 Cyber exploited 48.5% of vulnerabilities, against 32.1% for GPT-5.6 Cyber

## Who can use it

The model is not publicly available. Access is limited to a select group of approved customers in OpenAI's Daybreak Red program, which supports advanced exploit development and authorized testing. OpenAI plans to widen access to all Daybreak Red customers "soon." A companion program, Daybreak Blue, lets verified defenders investigate vulnerabilities and validate fixes with fewer restrictions. OpenAI said it intends to extend both programs to organizations of all sizes, independent researchers and open-source maintainers.

## OpenAI's warning

OpenAI said, "It is clear that we have a limited window to use frontier models to secure software," arguing defenders have limited time before similar capabilities reach attackers.

## Context

BleepingComputer linked the announcement to a run of AI-assisted security findings, including researchers using AI models to find two critical PHP flaws in October that attackers began targeting before patches, and an OpenSSH authentication bypass found this week by a researcher running AI agents through about 17,600 authentication tests.
