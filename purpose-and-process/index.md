---
title: "SPEC Purpose and Process"
date: 2020-12-17
draft: true
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
---

# Description

The SPEC process is designed to identify shared concerns and areas of unification
and to produce collaboratively written, community adopted guidelines for projects in the
scientific Python ecosystem.
These documents are known as SPECs: Scientific Python Ecosystem Coordination documents.

Specifically, the purpose of the SPEC process is

1. to help unify the ecosystem for users and developers;
2. to provide guidance to projects on technical issues or processes;
3. to document standard APIs, development tools, and community practices; and
4. to foster ecosystem-wide discussions of common problems and to develop shared solutions.

Projects in the ecosystem have an existing, diverse set of proposal processes
and development constraints.
SPECs complement these: they are a mechanism to encourage shared practices and improve uniformity of experience across projects.
SPECs may, for example, capture established practices so that new projects can
learn from them; or they may propose a new practice that the authors believe
will benefit the ecosystem as a whole.

Projects decide for themselves whether to adopt any given SPEC—often, this
would be through team consensus.
A SPEC may not be a good fit for every single project, and thus there is no
expectation that all SPECs must be adopted by all projects.
That said, SPECs serve their purpose to the extent that they are adopted by
several projects—and their authority stems from the extent to which they are.

Participants in the SPEC process must adhere to our [Code of
Conduct]({{< relref "/code_of_conduct.md" >}}).

## Key Terms

Scientific Python Ecosystem
: The **ecosystem** is a loose federation of community developed Python projects
widely used in scientific research that interact well with one another and that
follow similar norms of development, documentation, testing, and so forth.

SPEC Core Projects
: The [Core Projects]({{< relref "/specs/core-projects" >}})
are a small subset of the ecosystem consisting of mature, community developed projects
that are (a) depended upon by most of the other projects and (b) responsible for
reviewing, discussing, implementing, and endorsing SPEC documents.

SPEC Steering Committee
: The [Steering Committee]({{< relref "/specs/steering-committee" >}}) leads the SPEC project and
manages the SPEC process including moderating
the [SPECs discussion forum](https://discuss.scientific-python.org/c/specs/6),
accepting SPEC documents, and maintaining the SPEC process documents.

SPEC Process
: The SPEC process is outlined in this document and the associated
[SPEC Steering Committee]({{< relref "/specs/steering-committee" >}}) and
[SPEC Core Projects]({{< relref "/specs/core-projects" >}}) documents.
This process is managed and overseen by the Steering Committee in collaboration
with the Core Projects, as well as community members and projects across
the entire ecosystem.

SPEC Document
: A **SPEC document** provides operational guidelines for projects in the ecosystem and
helps coordinate the ecosystem to provide a more unified experience for users.
These documents are developed collaboratively with the Core Projects and other interested
ecosystem projects and community members.

## Format

SPECs are UTF-8 encoded text files using
[Markdown](https://www.markdownguide.org/) format and stored in the [SPEC
repository](https://github.com/scientific-python/specs).
The SPEC documents are converted to HTML by code in the [scientific-python.org
repository](https://github.com/scientific-python/scientific-python.org/) using
[Hugo](https://gohugo.io/) and deployed to
[https://scientific-python.org/specs/](https://scientific-python.org/specs/).
Each SPEC has a corresponding
[discussion](https://discuss.scientific-python.org/c/specs/accepted/15)
with the same title, where anyone can comment, ask questions, or vote on
existing comments.

# Implementation

SPEC Proposals often will be driven by contributors and maintainers of Core or other ecosystem projects.
Only the Steering Committee can accept them (details below).

Before a proposed SPEC can be accepted, the idea must be discussed on the
discussion forum under the [`SPECS/Ideas` topic](https://discuss.scientific-python.org/c/specs/ideas/9).
Thereafter a new SPEC document must be submitted
as a pull request (PR) to the [SPEC repository](https://github.com/scientific-python/specs).

Use the `quickstart.py` script to create a new SPEC document.
Located at the top-level of the
[SPEC repository](https://github.com/scientific-python/specs),
the script will ask you a few questions[^newspec] and then create a new file
appropriately named with a basic template for you to complete.
Once the SPEC is in reasonable shape, file a pull request against the
[SPEC repository](https://github.com/scientific-python/specs).

A good SPEC proposal focuses on a single key proposal, recommendation, or idea for
coordinating projects in the scientific Python ecosystem.
Before proposing a SPEC, we highly recommended that you first **vet the idea**
by doing one or more of the following:

1. discuss the idea with at least one project in the ecosystem,
2. discuss the idea with at least one other member of the ecosystem, or
3. create a minimal, proof of concept prototype.

## Accept

The Steering Committee will accept the new SPEC document based on the quality of the proposal
and on interest on the [discussion forum](https://discuss.scientific-python.org/c/specs/ideas/9).
Accepting a SPEC does not mean it is ready for Core Project endorsement or project adoption.
Often, implementation details will need to be developed and negotiated with
projects and will necessarily evolve after the SPEC is accepted.

An accepted SPEC appears in the [SPEC list]({{< relref "/specs" >}})
and has a corresponding
[`SPECs/Accepted` topic](https://discuss.scientific-python.org/c/specs/accepted/15) on the discussion forum.

## Endorse

Accepted SPEC documents are marked as draft documents until two or more
of the Core Projects decide to endorse and, if applicable, adopt the SPEC.

Pre-endorsement, it is helpful to recruit coauthors from the Core Projects to develop the SPEC.
Most SPECs will have several authors from numerous projects.
During this stage, the focus is on collaboratively developing an implementation plan that
will be broadly applicable and and widely adopted.

Often, this phase of the process will take longer and be more involved
than the acceptance phase.
All PRs to the SPEC repository will be reviewed by the Steering Committee.
SPECs may involve the creation of new projects or implementation
work in existing projects.

## Adopt

Any project in the ecosystem is welcome to adopt a SPEC at any point.
However, it may make sense to wait until a SPEC is endorsed by several Core Projects.
This ensures that the SPEC has been vetted and deemed stable enough for widespread adoption.
Once a SPEC is endorsed by several Core Projects it may still evolve, but the
barrier for modifying the SPEC will increase substantially once it is endorsed by several
Core Projects (since all endorsing projects would need to agree to changes).
Projects that adopt a SPEC early should engage in the collaborative process
leading to the SPEC being endorsed by the Core Projects.
Each SPEC describes what adopting it means in its _Ecosystem Adoption_ section.
Every project is responsible for deciding whether they will adopt a SPEC according
to their own governance process.

# Notes

[^newspec]:
    When asked to enter the SPEC number, choose the next available number that
    has not yet been used.
    Before the SPEC is merged, the Steering Committee may ask you to change the SPEC number so
    that it doesn't conflict with another PR.
    If so, just rename the file as appropriate and update the SPEC number in the
    `title` field of the SPEC header.

    The script currently only supports adding one author.
    If you need to add additional authors, just edit the text file.

    Additional files associated with a SPEC document may be kept in a directory
    with the same filename (minus as the `.md` extension) as the SPEC.
    For example, files associated with `spec-0000.md` are in `spec-0000`.

    Leave the `draft` field set to `true` and the `endorsed-by` field empty.
