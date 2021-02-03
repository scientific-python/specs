---
title: "MetaSPEC 1 — Governance and Decision Making"
date: 2021-01-06
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
discussion: https://github.com/scientific-python/specs/discussions/12
---

# Description

The Scientific Python Ecosystem Coordination (SPEC) process is managed by
the SPEC Steering Committee (SSC).
The SSC does not decide which SPECs are adopted—that choice resides with
individual projects.
Similarly, the SSC does not decide which SPECs are endorsed—that choice resides
with individual core projects.
They do, however,

- monitor and discuss new ideas for SPEC documents in the
  [Discussions](https://github.com/scientific-python/specs/discussions/categories/ideas)
  forum,
- determine which new ideas are assigned a SPEC number as described in
  [MetaSPEC 0 — Purpose and Process]({{< relref "/specs/meta-spec-0000.md" >}}),
- decide whether new MetaSPECs (i.e., SPECs about SPECs)
  are accepted and approve any changes to them, and
- serve as a communication channel to and from their projects as well
  as the larger ecosystem.

## Steering Committee

<!-- prettier-ignore-start -->
{{< gallery >}}

{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="ipython"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="numpy"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="pandas"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="scikit-learn"
>}}

{{< /gallery >}}

{{< gallery >}}

{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="jupyter"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="scipy"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="statsmodels"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="NetworkX"
>}}

{{< /gallery >}}

{{< gallery >}}

{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="spyder"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="matplotlib"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="scikit-image"
>}}
{{< person
      name="?"
      github_handle=""
      avatar=""
      projects="community"
>}}

{{< /gallery >}}
<!-- prettier-ignore-end -->

# Implementation

To accept a SPEC proposal (i.e., to assign it a SPEC number and merge the PR)
requires two members of the SSC to approve and no members objecting.
Since the role of the SSC is to mainly ensure that SPEC proposals are
appropriate, objections should be rare.

To add members, remove members, or modify the MetaSPECs, the SSC
makes decisions through group consensus and, in the very rare instance
where no consensus can be reached, by two-thirds majority vote of those
available to cast a vote within ten days.

Public communication takes place on this GitHub repository.
Private communication within the SSC takes place on [SSC private mailing list](https://groups.io/g/spec-steering-committee/).
SSC members are expected to be aware of conversations on this list to lend validity
to consensus-seeking and voting.

## Who should be a member?

Members of the SSC should be active in the scientific Python ecosystem and
should have a demonstrated interest in the SPECs.
Examples of demonstrated interest include submitting SPECs, engaging in SPEC
discussions, reviewing SPEC PRs, or advocating SPEC adoption in ecosystem
projects.
Individuals can request to join the SSC and the SSC can ask individuals
if they are willing to serve on the SSC.

## How many members should there be?

This is up to the SSC.
However, if the SSC is unable to quickly handle new SPEC proposals and new ideas arising
in the discussions aren't addressed in a timely manner, the SSC should try to
recruit new members.

## How do you add a member?

Anyone on the SSC can propose inviting a new member to join the SSC.
And, as previously mentioned, anyone can ask to join the SSC.

If the SSC decides to admit a new member and that person agrees, then they
should
(1) be added to the SSC member listing above,
(2) be added to the [SSC
Team](https://github.com/orgs/scientific-python/teams/spec-steering-committee/members),
(3) be added to the [SSC private mailing list](https://groups.io/g/spec-steering-committee/members).

## How do you remove a member?

If a member wishes to resign or if the SSC decides to remove a member, then
they should
(1) be moved to the list of Emeritus SSC members (below the list of active members),
(2) be removed from the [SSC
Team](https://github.com/orgs/scientific-python/teams/spec-steering-committee/members),
(3) be removed from the [SSC private mailing list](https://groups.io/g/spec-steering-committee/members).
