title: ConnectWise Suspends Cloud Backup After Attackers Abuse Its Access to Microsoft 365 Tenants
dek: Huntress counted at least 162 affected tenants, and Microsoft classified the activity as an active supply-chain attack.
date: 2026-10-18
category: Security
company: Microsoft
source: BleepingComputer|https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
---
ConnectWise has suspended its Cloud Backup service, formerly SkyKick Cloud Backup, after attackers used the product's application credentials to reach customers' Microsoft 365 tenants, according to BleepingComputer. Microsoft confirmed malicious activity involving the service and classified it as an active supply-chain attack.

## What is known

- Security firm Huntress identified at least 162 compromised tenants in its own environment, and saw service-principal role assignments in nearly 50 tenants it monitors.
- Huntress linked scripted sign-in attempts from one IP address to October 13 and 14, with activity from that address beginning October 15. Microsoft flagged unauthorized authentication attempts from the same address on October 15.
- ConnectWise announced the service interruption on October 17, then said on October 18 that it had disabled seven application identities and taken SaaS Security and Cloud Management offline as a precaution.
- Scheduled backups have stopped and restore access is unavailable. ConnectWise says backup archives remain encrypted and isolated, with no sign they were compromised.
- The total victim count, the extent of any data theft and how the attacker obtained the credentials remain unknown.

## How the access worked

Microsoft said it observed a backdoor after successful service-principal authentication, followed by Microsoft Graph reconnaissance and attempts to add credentials. It assessed that the attacker likely abused permissions customers had already granted the app, including Directory.ReadWrite.All.

Security firm Todyl said the attacker authenticated directly as the application using its secret, so multi-factor authentication did not apply because no user signed in. Todyl, which analyzed nine intrusions, found only sign-in activity in those cases, with no evidence of new accounts or persistence.

## Recommended steps

- ConnectWise advises reviewing service-principal sign-ins in Microsoft Entra for the Cloud Backup application ID and checking unexpected source addresses.
- Huntress recommends disabling the affected ConnectWise applications and checking for credentials added since October 13.
- ConnectWise says the affected shared credentials are no longer valid, but previously issued tokens may remain usable until they expire.
