---
title: "SPEC 6 — Keys to the Castle"
number: 6
date: 2022-12-19
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Pamphile Roy <roy.pamphile@gmail.com>"
  - "Lars Grüter <lagru@mailbox.org>"
endorsed-by:
  - ipython
  - networkx
  - numpy
  - scikit-image
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

Projects engage with restricted resources all the time.
Examples include access to add & remove team members, grant commit rights, or make uploads to certain hosts.

**Documenting resources** is critical to ensuring uninterrupted operations.
It is important that team members know _who_ have access to resources, and how to _gain access_ to resources.
For example, if updated project documentation needs to be uploaded to a remote server via SSH, who are the team members that can do that, and by which process can a release manager request access?

Furthermore, project developers sometimes have to **share secrets**, such as server passwords and social media logins.
Typically, such secrets are distributed among those who need them, without any centralized system for tracking the secrets or who has access to them.
When a server needs to be accessed, there is often a scramble to find someone with credentials.

This SPEC discusses the requirements for a system to distribute secrets, provides an example implementation, and lists suitable hosted services.

It should be noted that, in many cases, secrets & passwords can be avoided.
Most online services (GitHub, PyPI, etc.), have permissioning systems through which developers can be given the required access.
Access to servers can be given through SSH keys, which each developer has to safeguard.
This document deals with the situation in which that is not possible, and secrets have to be shared.

### Principles

1. Restricted project resources must be documented.

   Examples include servers that host services or web pages, and the processes for adding/removing project members on GitHub, chat, mailing lists, etc.

2. Assign the lowest privileges needed for a developer to do their work meaningfully.

   Review permissions regularly (say, every year) to maintain minimal permissions.

   _Tokens_ are a typical example of a stored secret that should be scoped (minimal necessary permissions), and set to expire after a reasonable time period (a year, typically).
   Instructions for rotating and revoking such tokens must be documented.

3. Project assets should, wherever possible, be accessible by at least two maintainers.
   This ensures access to assets, even when a key team member leaves the project or becomes indisposed.

4. A system for distributing project secrets must have the following properties:

   - Secrets are stored encrypted in a central (remote) location.
   - It must be possible to grant access to the secrets to a select group of team members.
   - It must be possible to revoke future access to the secrets.[^future-access]
   - The system must not rely on closed source or commercial encryption facilities, that
     can later disappear or be made unavailable, although such a solution can be considered if it allows for all data to be exported.

   Whichever system is chosen, its user interface should match the capabilities of the intended users.
   This reduces the risk of passwords being copied out to less secure mechanisms such as sticky notes or text files.
   If the target audience is not used to GPG or the command prompt, for example, the `pass` implementation below may not work, and an alternative like 1password or bitwarden should be considered.

[^future-access]: Revoking access to a service implies both (a) revoking access to secrets and (b) re-generating those secrets, since the actor could have copied them.

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

#### Badges

Projects can highlight their adoption of this SPEC by including a SPEC badge.
{{< spec_badge number="6" title="Keys to the Castle" >}}
To indicate adoption of multiple SPECS with one badge, see [this](../purpose-and-process/#badges).

## Implementation

### Password storage: hosted

The following hosted solutions conform to the principles in (2) above.

Self-hosted solutions:

- [vaultwarden](https://github.com/dani-garcia/vaultwarden); open source

Paid solutions:

- [bitwarden](https://bitwarden.com/) provides a non-profit discount of 25%; hosted open source

Sponsored solutions:

- [1password](https://github.com/1Password/1password-teams-open-source); closed source

#### Password storage: offline

[Pass](https://www.passwordstore.org/) is the standard unix password manager, which stores passwords as encrypted files on disk.
[password vault](https://github.com/scientific-python/vault-template) is an example implementation that satisfies the principles listed above.
The secrets are stored, encrypted, in a public Git repository.
The vault uses [gopass](https://github.com/gopasspw/gopass), a more user friendly implementation of pass, to manage access via GPG keys.
Each secret is encrypted using the public keys of all developers that should have access.
If a developer's access is removed, the vault is re-encrypted so that that developer cannot read future copies of the repository (but secrets are considered compromised and must, thus, be rotated).

### Other common scenarios

- **Publishing packages**: PyPi provides a [trusted publisher](https://docs.pypi.org/trusted-publishers/using-a-publisher/) mechanism for avoiding passwords

### Other security recommendations

- **2FA**: Developers must use two-factor authentication for service logins.
  This reduces the risk of account takeovers and subsequent fraudulent software releases.
- **Passwords** must be generated by a password manager.
  This ensures that they are of sufficient length and complexity.
- **SSH keys** must have a password. Ed25519 is the current recommended key type, and can be generated with `ssh-keygen -t ed25519`.

## Notes

See [gopass's security goals](https://github.com/gopasspw/gopass/blob/master/docs/security.md#security-goals).

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
