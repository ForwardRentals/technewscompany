title: Microsoft's October Patch Tuesday Fixes More Than 1,400 Flaws, a New Record
dek: One Windows Shell zero-day is under active attack, and the monthly load keeps climbing as Microsoft credits AI-assisted bug discovery.
priority: 4
date: 2026-10-13
category: Security
company: Microsoft
source: Krebs on Security|https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/
image: /img/news/microsoft-october-2026-patch-tuesday-1400-flaws.jpg
image_credit: Jiaqian AirplaneFan / CC BY 3.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Building_92_of_Microsoft_Redmond_Campus_-_panoramio.jpg
---
Microsoft released fixes for more than 1,400 security vulnerabilities on October 13, 2026, its largest monthly Patch Tuesday yet, according to security journalist Brian Krebs. The batch exceeds September's record of nearly 1,000 fixes, which was itself roughly ten times Microsoft's usual monthly volume.

## The exploited flaw

Only one vulnerability in the release is described as already exploited in the wild:

- **CVE-2026-96951:** a security feature bypass in Windows Shell
- **Affected products:** Windows 10, Windows 11 and some versions of Windows Server

A separate flaw, CVE-2026-108398, is a security feature bypass in the .NET Framework. Microsoft says it has not seen exploitation, but the issue was publicly disclosed before the patch, which can give attackers a head start on building an exploit.

## Scale of the release

- At least 78 of the flaws are rated critical, meaning they can be exploited with little or no user action. Most allow remote code execution.
- Tenable's Satnam Narang said the month surpasses 2020, when Microsoft patched 1,261 CVEs, adding: "We've now crossed the 4,000 CVE mark with two months left to go."
- Microsoft credits large language models for the increased pace of bug discovery, and Krebs presumes AI also contributed to many of the fixes.

## Why it matters

Large batches strain administrators, who must test updates before rolling them out across a network. Tyler Reguly of Fortra noted that only 26 Microsoft vulnerabilities have appeared in the U.S. Cybersecurity and Infrastructure Security Agency's Known Exploited Vulnerabilities catalog this year, and recommended patching those first. He said, "Security leaders should focus on exploitable risk."

## Windows 10 support

Microsoft had planned to end Windows 10 updates in October 2025, then added a free extra year after pushback. According to Krebs, it later extended that support again, through October 2027.

Cisco Talos and the SANS Internet Storm Center have each published roundups of the more noteworthy flaws, sorted by severity and affected software. Administrators should consult Microsoft's Security Update Guide for the full list of affected products.
