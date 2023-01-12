---
title: "SPEC 6 — Keys to the Castle"
date: 2022-12-19
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion:
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

Project developers often have to share secrets, such as server passwords and social media logins.
Typically, such secrets are distributed among those who need them, without any centralized system for tracking the secrets or who has access to them.
When a server needs to be accessed, there is often a scramble to find someone with credentials.
This SPEC discusses the requirements for a system to distribute secrets, and provides an example implementation.

## Implementation

### Principles

A system for distributing project secrets must have the following properties:

- Secrets are stored encrypted in a central (remote) location.
- It must be possible to grant access to the secrets to a select group of team members.
- It must be possible to revoke future access to the secrets.
- The system must not rely on closed source or commercial encryption facilities, that
  can later disappear or be made unavailable.

### Example

The [NumPy password vault](https://github.com/numpy/vault) is an example of an implementation that satisfies the above principles.
The secrets are stored, encrypted, in a public Git repository.
The vault uses [gopass](https://github.com/gopasspw/gopass) to manage access via GPG keys.
Each secret is encrypted using the public keys of all developers that should have access.
If a developer's access is removed, the vault is re-encrypted so that that developer cannot read future copies of the repository.

### Alternative implementations

Unknown

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Notes

See [gopass's security goals](https://github.com/gopasspw/gopass/blob/master/docs/security.md#security-goals).

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
