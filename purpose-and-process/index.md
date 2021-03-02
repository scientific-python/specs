---
title: "SPEC Purpose and Process"
date: 2020-12-17
draft: true
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
---

# Description

The SPEC process is designed to identify areas of shared concern between projects
in the scientific Python ecosystem and to produce collaboratively written,
community adopted guidelines for addressing these.
Such guidelines are known as SPECs: Scientific Python Ecosystem Coordination documents.

Specifically, the purpose of the SPEC process is

1. to help unify the ecosystem for users and developers;
2. to provide guidance to projects on technical issues or processes;
3. to document standard APIs, development tools, and community practices; and
4. to foster ecosystem-wide discussions of common problems and to develop shared solutions.

Projects in the ecosystem have an existing, diverse set of proposal processes
and development constraints.
SPECs complement these: they are a mechanism to encourage shared practices and
improve uniformity of experience across projects.
SPECs may, for example, capture established practices so that new projects can
learn from them; or they may propose a new practice that the authors believe
will benefit the ecosystem as a whole.

Projects decide for themselves whether to adopt any given SPEC—often, this
would be through team consensus.
A SPEC may not be a good fit for every single project, and thus there is no
expectation that all SPECs must be adopted by all projects.
That said, SPECs serve their purpose through being adopted by
several projects—and their authority stems from the extent to which they are.

Participants in the SPEC process must adhere to our
[Code of Conduct]({{< relref "/code_of_conduct.md" >}}).

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
This process is managed and overseen by the Steering Committee, and functions in collaboration
with the Core Projects, community members, and projects across the ecosystem.

SPEC Document
: A **SPEC document** provides operational guidelines for projects and helps
coordinate the ecosystem to provide a more unified experience for users and developers.
These documents are developed collaboratively with the Core Projects and other interested
ecosystem projects and community members.

## Format

SPECs are UTF-8 encoded text files using
[Markdown](https://www.markdownguide.org/) format and stored in the
[SPEC repository](https://github.com/scientific-python/specs).
The SPEC documents are converted to HTML by code in the
[scientific-python.org repository](https://github.com/scientific-python/scientific-python.org/) using
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
as a pull request to the [SPEC repository](https://github.com/scientific-python/specs).

Use the `quickstart.py` script to create a new SPEC document.
Located at the top-level of the
[SPEC repository](https://github.com/scientific-python/specs),
the script will ask you a few questions[^newspec] and then create a new file
appropriately named with a basic template for you to complete.
Once the SPEC is in reasonable shape, file a pull request against the
[SPEC repository](https://github.com/scientific-python/specs).

A good SPEC proposal focuses on a single key recommendation or idea for
coordinating projects in the scientific Python ecosystem.
Before proposing a SPEC, we highly recommended that you first **vet the idea**
by doing one or more of the following:

1. discuss the idea with at least one project in the ecosystem,
2. discuss the idea with at least one other member of the ecosystem, or
3. create a minimal, proof of concept prototype.

A SPEC passes through three decision points over the course of
its development and implementation:
**Accept**, **Endorse**, and **Adopt**.

<!-- prettier-ignore-start -->
{{<mermaid>}}
graph LR

START[ ]--> |Propose| A[Accept]
A--> |Draft| B[Endorse]
B--> |Recommend| C[Adopt]

click A callback "Steering Committee Action"
click B callback "Core Project Action"
click C callback "Ecosystem Action"

style START fill:#FFFFFF, stroke:#FFFFFF;

{{</mermaid>}}
<!-- prettier-ignore-end -->

The **accept decision** is made by the Steering Committee and means the proposed SPEC is
accepted as a draft and added to the main branch of the
[SPEC repository](https://github.com/scientific-python/specs).
Proposed SPECs are accepted once (a) the draft is written to clearly explain the area of
common concern and a general approach to a shared solution and (b) there
are contributors (from at least two Core Projects) interested in working on the new SPEC
and in championing it to their projects as well as the larger community.
Additional details may be found in
[Steering Committee documentation]({{< relref "/specs/steering-committee" >}}).

The **endorse decision** is made by the Core Projects.
The Core Projects and interested community members revise the accepted SPEC in a
collabortive and iterative process focused on ensuring the SPEC implementation plan that
is broadly applicable and likely to be widely adopted.
Often, getting a SPEC endorsed will take longer and be more involved
than having it accepted.
Most SPECs will have several authors from numerous projects including several Core Projects.
A SPEC is recommended for wide-spread adoption once it is endorsed by two (or more) Core Projects.
Once a SPEC is recommended, further changes require the approval of all endorsing
Core Projects.
Additional details may be found in
[Core Project documentation]({{< relref "/specs/core-projects" >}}).

The **adopt decision** is made by individual projects according to their own decision-making
processes.
Any project in the ecosystem is welcome to adopt a SPEC at any point.
However, it may make sense to wait until a SPEC is endorsed by several Core Projects.
This ensures that the SPEC has been vetted and deemed stable enough for widespread adoption.
Once a SPEC is endorsed by several Core Projects it may still evolve,
but the barrier for modifying the SPEC will increase substantially
(since all endorsing projects would need to agree to changes).
Projects that adopt a SPEC early should engage in the collaborative process
leading to the SPEC being endorsed by the Core Projects.
Each SPEC describes what adopting it means in its _Ecosystem Adoption_ section.

# Notes

[^newspec]:
    When asked to enter the SPEC number, choose the next available number that
    has not yet been used.
    Before the SPEC is merged, the Steering Committee may ask you to change the SPEC number so
    that it doesn't conflict with another pull request.
    If so, just rename the file as appropriate and update the SPEC number in the
    `title` field of the SPEC header.

    The script currently only supports adding one author.
    If you need to add additional authors, just edit the text file.

    Additional files associated with a SPEC document may be kept in a directory
    with the same filename (minus as the `.md` extension) as the SPEC.
    For example, files associated with `spec-0000.md` are in `spec-0000`.

    Leave the `draft` field set to `true` and the `endorsed-by` field empty.
