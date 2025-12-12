---
title: "SPEC Steering Committee"
date: 2021-01-06
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
---

## Description

The SPEC process is managed by the Steering Committee.
The Steering Committee represents the interests of the ecosystem and the community.
The Steering Committee also represent the interests of the
[Core Projects](/specs/core-projects)
and is composed partially of individuals who are active Core Project contributors.
In particular, the Steering Committee members

- monitor the
  [SPECs discussion forum](https://discuss.scientific-python.org/c/specs/6),
- determine which proposed SPECs are accepted as described in the [SPEC
  Purpose and Process](/specs/purpose-and-process),
- approve changes to the SPEC process including to the
  [SPEC Purpose and Process](/specs/purpose-and-process),
  [SPEC Steering Committee](/specs/steering-committee), and
  [SPEC Core Projects](/specs/core-projects), as well as
- serve as a communication channel to and from projects they contribute to as
  well as the larger ecosystem.

The SPEC Committee is led by the SPEC Steering Committee Chair.
The SPEC Steering Committee Chair is a designated member of the Steering Committee, selected by the Steering Committee.
The Chair serves at the discretion of the Steering Committee and may be replaced by the committee at any time.
The primary responsibility of the Chair is to organize and facilitate the SPEC Planning Meetings.
In addition to coordinating these meetings, the Chair may assist in managing meeting agendas and ensuring effective communication within the committee.
The Chair is also responsible for ensuring the Steering Committee is familiar with and following the SPEC Process.

### SPEC Steering Committee Chair

{{< grid file="spec-steering-committee-chair.toml" columns="2 3 4 5" />}}

### SPEC Steering Committee

{{< grid file="spec-steering-committee.toml" columns="2 3 4 5" />}}

### Emeritus SPEC Steering Committee

{{< grid file="emeritus-spec-steering-committee.toml" columns="2 3 4 5" />}}

## SPEC Planning Meetings

SPEC Planning Meetings are regular gatherings organized to discuss ongoing and upcoming SPEC proposals, procedural updates, and any other matters relevant to the Steering Committee or the broader community.
The Chair is responsible for scheduling and coordinating these meetings.
Information about upcoming SPEC Planning Meetings, including dates and details for joining, can be found on the [SPEC Steering Committee](https://scientific-python.org/calendars/specs.ics) calendar hosted at the [Scientific Python Calendars](https://scientific-python.org/calendars/).

The meetings are open to all community members.
[Meeting notes](https://hackmd.io/@stefanv/SPEC-meetings/edit) and outcomes are documented and shared via public community channels as appropriate.

## Implementation

Public communication takes place in the
[`specs` GitHub repository](https://github.com/scientific-python/specs/)
and the [SPECs discussion forum](https://discuss.scientific-python.org/c/specs/6).
Private communication within the Steering Committee takes place on
[Steering Committee private mailing list](mailto:spec-steering-committee@discuss.scientific-python.org).
Steering Committee members are expected to be aware of conversations on this list to lend validity
to consensus-seeking and voting.

### How are SPECs accepted?

<!-- This is a focused distillation of purpose-and-process#decision-points for the SPEC committee. -->

Also refer to [SPEC Purpose and Process: New
Proposals](/specs/purpose-and-process/#new-spec-proposals), a summary
of steps for SPEC authors.

To accept a SPEC requires two members of the Steering Committee to
approve and no members objecting.

Verify that:

1. The SPEC has two authors from two projects; and
2. that the idea is widely applicable to the ecosystem (i.e., it makes sense to
   write this up as a SPEC).

Assign the SPEC a number, and ask the authors to submit a draft PR
with a preliminary write-up.

The role of the Steering Committee is mainly to ensure that SPEC
proposals are appropriate, so objections should be rare.

### How does the SPEC Committee make decisions?

The Steering Committee makes decisions about changing the SPEC process documents
([SPEC Purpose and Process](/specs/purpose-and-process),
[SPEC Steering Committee](/specs/steering-committee), and
[SPEC Core Projects](/specs/core-projects))
through group consensus and, in the very rare instance
where no consensus can be reached, by two-thirds majority vote of those
available to cast a vote within ten days.

<!--
The vote "within ten days" is not clear. "ten days" after what?
Maybe:

Voting starts with an email to the
[Steering Committee private mailing list](mailto:spec-steering-committee@discuss.scientific-python.org).
-->

### Who should be a member?

Members of the Steering Committee should be active in the scientific Python ecosystem and
should have a demonstrated interest in the Core Projects and the SPEC process.
Examples of demonstrated interest include submitting SPECs, engaging in SPEC
discussions, reviewing SPEC pull requests, or advocating for wider SPEC participation.
Members of the steering committee do not have to belong to a core project.

### How many members should there be?

This is up to the Steering Committee.
However, if the Steering Committee is unable to quickly handle new SPEC proposals and new ideas arising
in the discussions aren't addressed in a timely manner, the Steering Committee should try to
recruit new members.

### How do you add a member?

If the Steering Committee decides to admit a new member and that person agrees,
then they should be added to the
(1) the Steering Committee member listing above,
(2) the [Steering Committee Team](https://github.com/orgs/scientific-python/teams/spec-steering-committee/members), and
(3) the [Steering Committee Discourse Group](https://discuss.scientific-python.org/g/spec-steering-committee).

### How do you remove a member?

If a member wishes to resign or if the Steering Committee decides to remove a member,
then they should
(1) be moved to the list of Emeritus Steering Committee members (below the list of active members),
(2) be removed from the
[Steering Committee Team](https://github.com/orgs/scientific-python/teams/spec-steering-committee/members), and
(3) be removed from the
[Steering Committee Discourse Group](https://discuss.scientific-python.org/g/spec-steering-committee).
