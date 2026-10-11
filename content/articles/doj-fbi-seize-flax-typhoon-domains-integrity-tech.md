title: FBI Seizes Seven Domains Tied to Flax Typhoon Hacking Tools Linked to Chinese Firm
dek: The Justice Department says Integrity Technology Group provided the MicroScan scanner and FishHub phishing platform used against critical infrastructure.
date: 2026-10-08
category: Security
company: Integrity Technology Group
source: BleepingComputer|https://bleepingcomputer.com/news/security/fbi-disrupts-chinese-hacking-tools-used-to-breach-critical-infrastructure
---
The U.S. Justice Department and FBI announced on October 8 that they seized seven domains tied to two hacking tools used by the China-linked group Flax Typhoon, according to BleepingComputer. U.S. authorities say the tools were operated by Integrity Technology Group, a China-based company with Chinese government contracts. China has rejected the allegations, per other reports.

## The tools

- **MicroScan:** a Python-based vulnerability scanner with more than 1,300 scripts, used alongside a Mirai botnet to scan targets
- **FishHub:** a spear-phishing and post-compromise platform for delivering malware, remote access and data exfiltration

The domain c0cc.cc provided access to MicroScan. Five domains delivered malware: 98aicai.com, 98aicode.com, outlook3650.com, youtubecard.com and linkedinns.net. A seventh, 98aiblog.com, was tied to SoftEther VPN software used to keep remote access to victims.

## Targets

MicroScan was used to scan a South Carolina power company, airports in Japan and Poland, Taiwanese gas and electricity companies and universities. Two Taiwanese universities scanned in 2022 and 2023 were later breached. The FBI did not say whether the named infrastructure operators were compromised.

A joint advisory from the DOJ, FBI, CISA, NSA and international partners lists indicators of compromise and recommends patching, disabling unnecessary exposed services and enforcing multifactor authentication.

## Context

FBI Cyber Division assistant director Brett Leatherman said Integrity Technology Group "provided China-linked threat actors" with capabilities. In September 2024 the DOJ disrupted an Integrity Tech-operated Mirai botnet of more than 200,000 devices, and the UK and EU have since sanctioned the company. Seizing domains disrupts operations but does not remove malware already on victim systems.
