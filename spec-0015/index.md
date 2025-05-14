---
title: "SPEC 15 — Security Policy"
number: 15
date: 2025-05-13
author:
  - "Juanita Gomez <juanitagomezr2112@gmail.com>"
  - "Mihai Maruseac <mihai.maruseac@gmail.com>"
is-draft: true
endorsed-by:
---

## Description

A security policy in a GitHub repository helps users know how to report vulnerabilities responsibly and enables maintainers to respond effectively to security issues. This prevents senstive issues from being disclosed publicly before they are addressed.
 
This spec provides guidance for creating and maintaining a clear and accessible `SECURITY.md ` file in the repository, which serves as the project's security policy.

### Core Project Endorsement

Endorsing this SPEC means agreeing, in principle, with the importance of having a clear `SECURITY.md ` file to describe how to responsibly report vulnerabilities.

### Ecosystem Adoption

Adopting this SPEC means implementing a security policy by including a `SECURITY.md ` file in the repository root. At a minimum, this file should describe how to report a security vulnerability and provide an expected response timeline.

Other details of the security might vary depending on the project's size and attack surface.

#### Badges

Projects can highlight their adoption of this SPEC by including a SPEC badge.
{{< spec_badge number="15" title="Security Policy" >}}
To indicate adoption of multiple SPECS with one badge, see [this](../purpose-and-process/#badges).


## Implementation

To add a security policy:
- For a single repository: create a `SECURITY.md `file in the root of the repo.
- For all repositories in an organization: create a `.github` repository and add a `SECURITY.md` file there. It will automatically apply to all repos without their own policy. 

> [!NOTE]
> With this approach individual repositories can edit the `SECURITY.md` as needed.)
 
Once added, GitHub displays the security policy under the "Security" tab of each repository, making it easy for users to find and follow. 
 
A good `SECURITY.md` file should include the following sections:
- **Supported Versions**: Specify the range of versions that your project currently supports with security updates. 
- **Contact information**: List an email address or other method users can use to reach the security team or maintainer.  Ideally, use a dedicated address like `security@{PROJECT_NAME}.com` to manage security reports separately from general inquiries. *

> [!NOTE]
> Sometimes the security contact is an external vendor or a vulnerability program.

- **Reporting a Vulnerability**: Document how can users report a security issue (e.g., email address or link to a form). You can also enable [private vulnerability reporting on GitHub](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository), which allows users to create private issues to report vulnerabilities directly and securely through the GitHub interface. In this case, your security policy should document how users can [privately report a vulnerability using GitHub](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).
- **Expected Response Time**: Let users know how quickly you plan to respond (e.g., "within 72 hours").

### Template

```
# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | ✅        |
| 1.x     | ⚠️ Security fixes only |
| < 1.0   | ❌ Not supported |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, we strongly encourage you to report it as soon as possible. Please include as much detail as possible to help us reproduce and address the issue quickly.

- Email us at: [security@{PROJECT_NAME}.com]

## Expected Response Time

We aim to respond to vulnerability reports within **72 hours**, and follow [Responsible Disclosure model](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure).
```

## Notes

- [More information on adding a security policy to a GitHub repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)

