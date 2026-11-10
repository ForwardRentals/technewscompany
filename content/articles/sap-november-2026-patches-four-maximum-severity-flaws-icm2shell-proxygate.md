title: SAP's November Patch Day Fixes 35 Flaws, Four Rated 10 out of 10
dek: The critical bugs affect NetWeaver AS ABAP, Web Dispatcher and Gateway; the report does not say any are exploited yet.
date: 2026-11-10
category: Security
company: SAP
source: BleepingComputer|https://www.bleepingcomputer.com/news/security/sap-patches-four-maximum-severity-security-vulnerabilities/
---
SAP patched 35 vulnerabilities in its November 2026 security updates, four of them rated 10 out of 10 on the CVSS scale, BleepingComputer reported on November 10. SAP says unauthenticated attackers could exploit the four flaws to fully compromise affected systems remotely.

## The four flaws

- **CVE-2026-76964** (NetWeaver AS ABAP, Internet Communication Manager): memory corruption.
- **CVE-2026-89126** (SAP Web Dispatcher): memory corruption. Together with CVE-2026-76964 it is nicknamed ICM2SHELL.
- **CVE-2026-120017** (NetWeaver AS ABAP, SAML2 Service Provider): missing authentication.
- **CVE-2026-89103** (SAP Gateway): broken access control, nicknamed PROXYGATE.

Security firm Onapsis, which found and reported three of the issues, describes ICM2SHELL as remote code execution against the network-facing component with no credentials or user interaction. It says PROXYGATE tricks SAP Gateway into treating an outside attacker as an internal application server, giving control of the system as the installation's owner account. The report does not say who found the fourth flaw.

## Exploitation status

BleepingComputer did not report active exploitation of these four bugs.

## Context

SAP has had several maximum-severity fixes in recent months:

- CVE-2026-58231 in SAP Commerce Cloud (August), which Defused reported as exploited days after the patch.
- CVE-2026-44756 in SAP Kernel (September), dubbed OVERPASS by Onapsis.
- CVE-2026-89111, an OAuth2 SSRF affecting multi-tenant BTP applications (October).

CISA has listed 14 SAP flaws as actively exploited since November 2021, three of which ransomware groups have abused, according to the report. Administrators should consult SAP's security notes for the affected versions.
