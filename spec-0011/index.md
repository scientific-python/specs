---
title: "SPEC 11 — Vulnerability disclosure"
number: 11
date: 2025-05-13
author:
  - "Juanita Gomez <juanitagomezr2112@gmail.com>"
  - "Mihai Maruseac <mihai.maruseac@gmail.com>"
is-draft: true
endorsed-by:
---

## Description

This SPEC outlines the process for vulnerability disclosure. It aims to
provide clear guidelines for the identification, reporting, and remediation of
security vulnerabilities within projects.

### Core Project Endorsement

### Ecosystem Adoption

TODO: Risks in smaller projects vs risks in larger projects. This might change
strict adherence to the implementation here.

## Implementation

Security vulnerabilities should be handled quickly, and sometimes privately.
The primary goal of this process is to reduce the total time users are
vulnerable to both publicly and privately known reports.

To achieve this goal, the project should provide well-defined ways to report
vulnerabilities (e.g., special email address such as `security@<project>.com`,
forum, GitHub private security reporting, vulnerability reward programs). All
suspected vulnerabilities should be handled in accordance with
[Responsible Disclosure model](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure).
The project should provide a mechanism for researchers to submit GPG encrypted
vulnerability reports, for vulnerabilities with a higher degree of
sensitivity.

The project should ensure that a _Security Incident Response Team_ (SIRT) exists. This
team could be shared with other projects in the same organization, or within
the same ecosystem. The SIRT has the following responsibilities:

- Triage: assess the impact of any vulnerability. Can the vulnerability be
  replicated? Which projects are affected? What is the blast radius? Who is
  responsible for the fix? Is there a need for coordinated disclosure between
  multiple projects?
- Command: create security advisories, ensure teams working on fixing a
  vulnerability can work in private, create tests for the vulnerability and
  its variants.
- Disclosure: handle public messaging around the vulnerability by drafting an
  advisory to document the impact, how to upgrade, how to mitigate if upgrading
  is not possible.
- Release: create patch releases containing the fix and notify the public.

For each vulnerability, the SIRT should follow these steps:

1. **Acknowledge the report**: The SIRT should respond to any report in at most
   48 hours. For this, there should be inventory of all the places where
   vulnerabilities can be reported, and SIRT should monitor all of these (via
   automation and dashboards where possible). The SIRT will handle
   communication with the reporter throughout the vulnerability remediation
   process, updating the reporter on the disclosure timeline.
2. **Triage the vulnerability**: The SIRT should attempt to reproduce the
   vulnerabiltiy and analyze its impact. The SIRT should rate the impact and
   consider coordinated disclosure based on
   [the traffic light protocol (TLP)](https://www.cisa.gov/news-events/news/traffic-light-protocol-tlp-definitions-and-usage).
3. **Assign the vulnerability fix to fixing team**: The SIRT is not responsible
   for fixing all vulnerabilities themselves. They should delegate to a team
   that has the most accurate knowledge of the affected codebase. In general,
   the fixing team should include maintainers from the affected projects.
   Depending on TLP level, other members of the project could be brought in,
   as needed, but only after consulting the SIRT.
4. **Prepare a disclosure timeline**: Judging based on severity, complexity of
   the code base, development time, release work, upstream dependencies,
   the SIRT should create a timeline for when the vulnerability fix should be
   released and the public would be notified about the vulnerability. If the
   vulnerability has a low severity, the timeline can be extended to slow the
   release process to account for holidays, developer bandwidth, etc.
5. **Request and prepare a CVE**: The SIRT should prepare a
   [security advisory](https://docs.github.com/en/code-security/security-advisories)
   in the affected repositories and obtain CVE numbers for the
   vulnerabilities. As many details as possible should be entered into the
   advisory. Each time new information is discovered, the advisory should be
   updated. A vulnerability severity score, computed using
   [CVSS](https://www.first.org/cvss/) should be added. Members of the remediation
   team should be added to the advisory, to contribute details.
6. **Create a private fork[^1]** for the remediation team to fix the vulnerability
   in private. This is a temporary fork and should be deleted once the
   vulnerability is fixed. It should only be created to ensure CI can run on
   code fixing the vulnerability without accidentally disclosing the
   vulnerability[^2].
7. **Plan and perform the patch release**. Once the fixing team has submitted
   all necessary fixes for the vulnerability and its variants and the SIRT has
   verified that the work is completed, the two teams agree on a release
   timeline and perform the release as well as announce the vulnerability to
   the public[^3].

On the release day, the SIRT and the remediation team:

1. merge all the commits from the private fork onto the project repository
2. start patch releases for all affected versions in the supported range
3. publish all release binaries and packages
4. publish the security advisory
5. publish an announcement that is actionable, contains mitigation steps for
   users that cannot upgrade to the newly released patched versions, and is
   distributed to a wide audience.

A template of the announcement could be:

```
Subject: Security release of $PROJECT $VERSION is now available
To: ...

Hello $PROJECT Community,

The Security Incident Response Team and maintainers of $PROJECT would like
to announce the availability of $PROJECT $VERSION.

This addresses the following CVE(s):

* CVE-YEAR-ABCDEF (CVSS score $CVSS): $CVESUMMARY
...

Upgrading to $VERSION is encouraged to fix these issues.

**Am I vulnerable?**

Run `$PROJECT --version` and if it indicates a base version of $OLDVERSION or
older that means it is a vulnerable version.

<!-- Update this for libraries that don't have a CLI capable of running
`--version` to extract version information -->

<!-- Provide details on features, extensions, configuration that make it
likely that a system is vulnerable in practice. -->

**How do I mitigate the vulnerability?**

<!-- This is an optional section. Remove if there are no mitigations. -->

**How do I upgrade?**

<!-- Outline upgrade steps (e.g., use `uv install`) -->

**Vulnerability Details**

<!-- For each CVE, provide some details of the vulnerability and link to the
advisory. -->
```

## Notes

A few days after the release, the SIRT could write a retrospective of the
vulnerability and the remediation process, with details on everyone involved, links to
PRs, and other relevant information. This is to encourage learning, preventing
future similar vulnerabilities and providing opportunities for improving the
disclosure process.

[^1]: All communication between the people involved in the fix must happen only on the advisory and the private fork, to prevent accidental disclosure.

[^2]: The [`act`](https://github.com/nektos/act) project could be used to run CI locally if needed.

[^3]: To ensure that the release and the announcement are seen in an adequate time-frame, it is recommend to use 4PM UTC on a non-Friday weekend as the disclosure time. This ensures that the announcement would be seen at morning time in APAC, early evening in EMEA and late evening in Asia.
