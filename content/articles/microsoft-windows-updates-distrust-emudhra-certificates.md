title: Microsoft Ships Out-of-Band Windows Updates to Distrust eMudhra Certificates
dek: Updates KB5134133 and KB5134125 remove seven certificates from the Windows trust list after researchers found weak private keys in eight eMudhra intermediate CAs.
date: 2026-10-26
category: Security
company: Microsoft
source: BleepingComputer|https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-oob-updates-to-distrust-emudhra-certificates/
---
Microsoft released out-of-band Windows updates on October 26 that remove trust in several certificates issued by the certificate authority eMudhra, BleepingComputer reported.

## The updates

- **KB5134133** covers Windows 11 24H2, 25H2 and 26H2.
- **KB5134125** covers Windows 10 21H2 and 22H2.

The updates target machines without Internet access, devices that cannot reach Microsoft's certificate-update service, and devices where automatic Certificate Trust List (CTL) updates are disabled. They remove seven certificates from the Windows trust list: six eMudhra G3 roots and an AAA Certificate Services cross-sign. Microsoft said the same seven will be removed from the Edge trust list on October 27.

## The underlying flaw

Researchers found that eight eMudhra intermediate CA private keys, all generated in April 2025, had values smaller than 256, so anyone could recover them by testing just 256 possible numbers. Such keys could let attackers forge certificates for legitimate websites and intercept encrypted traffic.

eMudhra revoked the eight intermediates, and Mozilla, Google, Apple and other vendors began revoking them as well. Microsoft had earlier blocked the intermediates in the Windows Disallowed CTL, six used for TLS and two for code signing, and shipped a CRLSet update for Edge and WebView2.

## Guidance

Microsoft advises installing the update on disconnected systems and identifying certificates that depend on the removed roots, since they may need replacing. Organizations with compatibility needs can choose to trust a certificate locally after their own assessment.

The company noted that "removing a root from a trust list is not the same as revoking the known impacted intermediate certificate authorities." It said it is investigating the remaining eMudhra roots and may make further trust changes.
