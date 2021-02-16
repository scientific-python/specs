---
title: "SPEC Purpose and Process"
date: 2020-12-17
draft: true
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
---

# Description

SPEC documents or SPECs, for short, provide operational guidelines
for projects in the scientific Python ecosystem.
Their goal is to coordinate the ecosystem and to provide a more unified
experience for users.

Projects in the ecosystem have an existing, diverse set of proposal processes
and development constraints.
SPECs, therefore, are not meant to be prescriptive: rather, they are a
mechanism to encourage shared practices and improve uniformity of experience.
SPECs may, for example, capture established practices so that new projects can
learn from them; or they may propose a new practice that the authors believe
will benefit the ecosystem as a whole.

Projects decide for themselves whether to adopt any given SPEC—often, this
would be through team consensus.
A SPEC may not be a good fit for every single project, and thus there is no
expectation that all SPECs must be adopted by all projects.
Different SPECs may even recommend differing approaches to the same problem for
the sake of discussion and consensus-building among the projects.
However, it is often better to capture the various approaches to one problem
in one SPEC.

That said, the purpose of the SPEC process is

1. to help unify the ecosystem for users;
2. to provide guidance to projects on technical issues or processes;
3. to document standard APIs, development tools, and community practices; and
4. to serve as a mechanism for ecosystem contributors to discuss common problems and develop shared solutions.

SPECs serve their purpose to the extent that they are discussed and adopted by
several projects—and their authority stems from the extent to which they are.

## Key Concepts

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
[`specs` discussions](https://discuss.scientific-python.org/c/specs/6),
accepting SPEC documents, and maintaining the SPEC process documents.

SPEC Document
: A **SPEC document** provides operational guidelines for projects in the ecosystem.

<!-- prettier-ignore-start -->
SPEC Process
: The **SPEC process** is described in the
  [SPEC Purpose and Process]({{< relref "/specs/purpose-and-process" >}}),
  [SPEC Steering Committee]({{< relref "/specs/steering-committee" >}}), or
  [SPEC Core Projects]({{< relref "/specs/core-projects" >}}) documents.
  During the SPEC process, a SPEC can be

  Proposed
  : Anyone can propose a SPEC.  Often, proposals are driven by contributors and
  maintainers of Core Projects or other ecosystem projects. 
  Before a proposed SPEC can be accepted, it must be discussed as a 
  [`specs/ideas` discussion topic](https://discuss.scientific-python.org/c/specs/ideas/9).

  Accepted
  : The Steering Committee determines whether a SPEC is accepted.
  The main criterion for acceptance is some agreement among the Steering Committee that the SPEC
  describes a useful proposal, recommendation, or idea for coordinating projects.
  Often, implementation details will need to be developed and negotiated with
  projects and will necessarily develop and evolve after the SPEC is accepted.
  An accepted SPEC appears in the [SPEC list]({{< relref "/specs" >}})
  and has a corresponding
  [`specs/accepted` discussion topic](https://discuss.scientific-python.org/c/specs/accepted/15).
  Accepted SPECs are marked as a `draft document` until there is a consensus
  that it ready for widespread project adoption through endorsement from two
  or more Core Projects.
  
  Adopted
  : Any project in the ecosystem can adopt any SPEC.
  Each SPEC describes what adopting it means in its _Ecosystem Adoption_ section.
  Every project is responsible for deciding whether they will adopt a SPEC according
  to their own governance process.
  
  Endorsed
  : Each Core Project independently decides whether to endorse a SPEC.
  Endorsements signal to the ecosystem that the core projects not only adopt
  the SPEC (when applicable), but that after carefully reviewing the SPEC
  that they want to use their reputation in the ecosystem to publicly encourage
  other projects to adopt a SPEC.
  When applicable, an endorsement also mean that the Core Project provides the
  necessary infrastructure required by other projects wishing to adopt the SPEC.
  Often, as part of the collaborative effort, Core Project contributors will
  become coauthors of the SPEC document after it is accepted, but before endorsing it,
  in order to help shape it.
<!-- prettier-ignore-end -->

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

Before a proposed SPEC can be accepted, a new SPEC document must be submitted
as a pull request (PR) to the [SPEC repository](https://github.com/scientific-python/specs).
Any community member can submit a new SPEC document.
However, we highly recommended that you first **vet the idea** by doing one or more of the following:

1. discuss the idea in at least one project in the ecosystem,
2. discuss the idea with at least one other member of the ecosystem,
3. discuss the idea on the
   [`specs` discussion forum](https://discuss.scientific-python.org/c/specs/ideas/9),
4. create a minimal, proof of concept prototype.

Each SPEC document should focus on a single key proposal, recommendation, or idea for
coordinating projects in the scientific Python ecosystem.

The first hurdle in the SPEC process is getting a new SPEC document accepted by the Steering Committee.
The Steering Committee will accept the new SPEC document based on the quality of the proposal
and on interest for the proposed SPEC on its
[`specs/ideas` discussion topic](https://discuss.scientific-python.org/c/specs/ideas/9).

The next hurdle is getting Core Projects to endorse the accepted SPEC.
Accepted SPEC documents are marked as `draft documents` until some of
the Core Projects decide to adopt (if applicable) and endorse the SPEC.
During this phase of the process, it is helpful to recruit coauthors
from the Core Projects to help collaboratively develop the SPEC.
Often, this phase of the process will take longer and be more involved
than the the acceptance phase.
All PRs to the SPEC repository will be reviewed by the SCC.
Some SPECs will involve the creation of new projects or implementation
work in existing projects.

The final hurdle is to get projects throughout the ecosystem to adopt the SPEC.
This phase of the process is ill-defined and how effective it will be will
need to be demonstrated.
The hope is that we will attract attention for projects throughout the
ecosystem and they will help us figure out the best way to improve the
process.

Contributors must adhere to our
[Code of Conduct]({{< relref "/about/code_of_conduct.md" >}}).

## New SPEC Document

Use the `quickstart.py` script to create a new SPEC document.
Located at the top-level of the
[SPEC repository](https://github.com/scientific-python/specs),
the script will ask you a few questions and then create a new file
appropriately named with a basic template for you to complete:

Header
: The `Header` section is mostly autofilled by the `quickstart.py` script.
However, you may need to expand or update it.

Description
: The `Description` section captures the general proposal.
A SPEC is accepted based largely on this section and the community interest.
So the focus of a proposed SPEC should be on making a clear and compelling
description of the problem that the SPEC addresses.

Implementation
: If the SPEC is largely documenting already established best practices
that are widely used by the Core Projects, then the `Implementation`
should be relatively straightforward to write.
However, if the SPEC is proposing something new or something not
widely used by the Core Projects already, then the `Implementation`
section often requires an extend period of discussions with the Core
Projects as well as the larger community.
This process takes place after a SPEC is accepted, but before it
is endorsed by any Core Projects.

Notes
: The `Notes` section is optional.

Additional files associated with a SPEC document may be kept in a directory
with the same filename (minus as the `.md` extension) as the SPEC.
For example, files associated with `spec-0000.md` are in `spec-0000`.

For example,

<!-- prettier-ignore-start -->
{{< highlight bash >}}
$ python quickstart.py
Your Name: Jarrod Millman
Your Email Address: millman@berkeley.edu
SPEC number: 0
SPEC title: Minimum Supported Versions
{{< /highlight >}}
<!-- prettier-ignore-end -->

creates the file `spec-0000.md` containing:

<!-- prettier-ignore-start -->
{{< highlight yaml >}}
---
title: "SPEC 0 — Minimum Supported Versions"
date: 2021-01-10
draft: true
author:
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/
endorsed-by:
---

# Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be
used, intended use-cases, and pseudo-code illustrating its use.
-->

# Implementation

<!--
Discuss how this would be implemented.
-->

## Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

## Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

# Notes

<!--
Include a bulleted list of annotated links, comments, and other ancillary
information as needed.
-->

{{< /highlight >}}
<!-- prettier-ignore-end -->

When asked to enter the SPEC number, choose the next available number that
has not yet been used.
Before the SPEC is merged, the Steering Committee may ask you to change the SPEC number so
that it doesn't conflict with another PR.
If so, just rename the file as appropriate and update the SPEC number in the
`title` field of the SPEC header.

The script currently only supports adding one author.
If you need to add additional authors, just edit the text file.

For example, adding a second author the above template requires the following
change to the SPEC header:

<!-- prettier-ignore-start -->
{{< highlight yaml >}}
---
title: "SPEC 0 — Minimum Supported Versions"
date: 2021-01-10
draft: true
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-0-minimum-supported-versions/33
endorsed-by:
---
{{< / highlight >}}
<!-- prettier-ignore-end -->

Leave the `draft` field set to `true` and the `endorsed-by` field empty.
Once the SPEC is in reasonable shape, file a pull request against the
[scientific-python/specs](https://github.com/scientific-python/specs)
repository.
The Steering Committee as well as community members will provide feedback.
They will pay particular attention to ensure the `Description`
section is clear and reasonably complete.
They will also provide advice of how much detail is needed in
the `Implementation` section.

Before the PR is merged, you will be asked to create a new
[discussion](https://discuss.scientific-python.org/c/specs/ideas/9)
(if you haven't already).

## Review and Acceptance

The Steering Committee will consider whether the new idea fits as a SPEC and monitor
subsequent discussion.
If there is sufficient interest, the Steering Committee will convert the discussion to the
[Accepted](https://discuss.scientific-python.org/c/specs/accepted/15)
subcategory and assign it a SPEC number.
At this point, the PR should be updated to ensure the title, file name,
and `discussion` field are correct.
When it is ready, the Steering Committee will merge the PR.
Additional PRs will be made to update or expand the SPEC after it is
accepted.

## Endorsement and Adoption

Once the SPEC is accepted, the hard work begins.
You will need to continue engaging the Core Projects and the larger ecosystem in the
[discussion forum](https://discuss.scientific-python.org/c/specs/accepted/15)
as well as engaging with projects directly.
It will be helpful to recruit additional authors from different projects to
help develop the SPEC and respond to feedback from the ecosystem.
