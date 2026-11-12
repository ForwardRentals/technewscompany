title: Microsoft's November Patch Tuesday Fixes a Record 1,235 Flaws, Including an Exploited Outlook Zero-Day
dek: BleepingComputer's count puts the release above October's 1,411 on its own tally basis, with 66 critical bugs and one actively exploited Outlook spoofing flaw.
date: 2026-11-10
category: Security
company: Microsoft
source: BleepingComputer|https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/
image: /img/news/microsoft-november-2026-patch-tuesday-1235-flaws-outlook-zero-day.jpg
image_credit: Ajatodekh / CC0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Microsoft_Outlook-Logo.wine.png
---
Microsoft's November 2026 Patch Tuesday update fixes 1,235 vulnerabilities, including one zero-day that attackers are already exploiting in Outlook, according to BleepingComputer's tally of the release. The outlet's count excludes 108 flaws Microsoft fixed earlier in the month.

## The exploited zero-day

The actively exploited bug is CVE-2026-124194, an Outlook spoofing vulnerability. BleepingComputer reported that attackers used it to steal NTLM account hashes: a specially crafted message file can make Outlook connect to an attacker-controlled network location without the usual warning about external content. Exploitation requires network connectivity and user interaction.

## By the numbers

- 1,235 flaws fixed, about 639 of them in Windows products or components
- 66 rated Critical: 48 remote code execution, 15 elevation of privilege and 3 use-after-free bugs in Microsoft Edge
- 536 elevation-of-privilege, 296 remote code execution, 157 information disclosure and 142 Edge flaws
- 46 denial-of-service, 27 security-feature-bypass and 22 spoofing flaws

BleepingComputer listed several critical examples, though its table was not complete:

- CVE-2026-118146: Active Directory Domain Services remote code execution
- CVE-2026-118207: Exchange Server remote code execution
- CVE-2026-122194: Microsoft Defender remote code execution
- CVE-2026-120003 and CVE-2026-111289: Microsoft Office remote code execution
- CVE-2026-119990: Azure OpenAI elevation of privilege

## Context

The previous record on the same tally was 1,411 flaws in October 2026. The totals are far above those of earlier years, and BleepingComputer's count is its own tabulation of fixes released on Patch Tuesday rather than a figure published by Microsoft.

Windows 11 received cumulative updates KB5132061 and KB5131087, and Windows 10 extended security update KB5131096 was also released. Administrators typically prioritize the exploited Outlook flaw and the critical remote-code-execution bugs in identity and mail infrastructure such as Active Directory and Exchange.

Other vendors also shipped fixes around the same time, including Cisco, SAP and N-able, according to the same report.
