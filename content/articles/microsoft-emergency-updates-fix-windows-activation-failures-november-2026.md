title: Microsoft Releases Emergency Updates for Windows Activation Failures
dek: Out-of-band patches address licensing errors caused by the November 2026 security updates for organizations that automate activation with SLMGR.
priority: 2
date: 2026-11-13
category: Security
company: Microsoft
source: BleepingComputer|https://www.bleepingcomputer.com/news/microsoft/microsoft-new-windows-emergency-updates-fix-activation-licensing-failures/
image: /img/news/microsoft-emergency-updates-fix-windows-activation-failures-november-2026.jpg
image_credit: Coolcaesar / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Building92microsoft.jpg
---
Microsoft has released out-of-band updates for several Windows and Windows Server versions to fix activation and licensing failures introduced by its November 2026 security updates, BleepingComputer reported on November 16.

## What went wrong

Microsoft confirmed the problem in a service alert on Wednesday and shipped the emergency fixes on Friday, according to the report. The failures affect organizations that use the Software Licensing Management Tool, `slmgr.vbs`, to automate activation and licensing. Enterprise customers who do not use the tool and have the KMS client key in their image are not affected.

Microsoft said devices that are already activated remain activated. The report does not state the technical root cause.

## The fixes

- **Windows Server 2025:** KB5136489
- **Windows Server 2022:** KB5136487
- **Windows Server 2019 and Windows 10 Enterprise LTSC 2019:** KB5136490
- **Windows 11, version 23H2:** KB5136483
- **Windows 10, version 22H2 (ESU) and Windows 10 Enterprise LTSC 2021:** KB5136493

Each update is cumulative and includes the November 2026 security fixes, per Microsoft. The Windows Server and Windows 10 updates are available only through the Microsoft Update Catalog. The Windows 11 23H2 update is optional and appears under Windows Update > Advanced options > Optional updates, as well as in the Catalog.

## Other November issues

The activation bug is one of several problems Microsoft has acknowledged this month. The company has also linked the updates to printing problems for documents with complex formatting, installation failures on systems that have the October 2026 preview update, and SQL Server performance and stability issues tied to updates released since October Patch Tuesday, BleepingComputer noted.

Administrators who have not yet deployed the November security updates can apply the new cumulative packages instead.
