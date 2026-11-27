title: 1Password Says Attacker Used Employee GitHub Account to Reach Customer Names and Email Addresses
dek: The company says intrusion was detected November 19 and that customer vaults were not accessed, and its apps and browser extensions were unaffected.
date: 2026-11-25
category: Security
company: 1Password
source: TechCrunch|https://techcrunch.com/2026/11/25/1password-said-hackers-broke-into-its-internal-systems-but-customer-passwords-are-safe/
image: /img/news/1password-says-attacker-accessed-employee-github-account-customer-names-emails-exposed.jpg
image_credit: AgileBits / Public domain via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:1Password_icon.png
---
1Password said on November 25 that an attacker broke into its internal systems after gaining access to an employee's corporate GitHub account, according to TechCrunch, which cited a company blog post. The company said it detected the intrusion on November 19.

## What 1Password disclosed

The password manager uses GitHub to store and share source code. According to the report, the attacker used the compromised account to push malicious code to internal servers, and that access allowed customer data to be downloaded.

The exposed data was limited to:

- Customer names
- The email addresses used to sign in
- When each account was created
- When each user last logged in

## What was not affected

1Password said customer vaults were "at no point" accessible to the attacker. It said it cannot see customers' account passwords or secret keys, which are used to encrypt vault contents, and that its apps and browser extensions were not affected.

## Open questions

Several details were not available when TechCrunch published:

- How the attacker obtained access to the employee's GitHub account.
- How many customers are affected.
- Whether affected customers have been notified.
- Whether the attackers made any demands.

A company spokesperson did not immediately answer TechCrunch's questions. 1Password says it serves millions of customers and more than 200,000 businesses.

## Context

Attacks that target developer accounts and code repositories have become a recurring route into software companies, because source-control access can lead to internal systems. Names and email addresses can still be used in phishing attempts, so users of any affected service are generally advised to be cautious about unsolicited messages.
