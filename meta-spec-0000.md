---
title: "MetaSPEC 0 — Purpose and Process"
date: 2020-12-17
draft: true
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
---

# Description

Scientific Python Ecosystem Coordination documents or SPECs, for short, provide
operational guidelines for projects in the scientific Python ecosystem.
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
SPECs may also propose only certain projects prototype a SPEC before
encouraging other projects to consider adopting the SPEC.

That said, the purpose of the SPEC process is

1. to help unify the ecosystem for users;
2. to provide guidance to projects on technical issues or processes;
3. to document standard APIs, development tools, and community practices; and
4. to serve as a mechanism for ecosystem contributors to discuss shared problems and solutions.

SPECs serve their purpose to the extent that they are discussed and adopted by
several projects—and their authority stems from the extent to which they are.

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

## Glossary

Scientific Python Ecosystem
: The scientific Python ecosystem is a federation of projects that interact
well with one another and that follow similar norms of development,
documentation, testing, and so forth.

SPEC
: A Scientific Python Ecosystem Coordination (SPEC) document provides operational
guidelines for projects in the scientific Python ecosystem.

SSC
: The [SPEC Steering Committee (SSC)]({{< relref "/specs/meta-spec-0001.md" >}})
manages the SPEC documents.

MetaSPEC
: MetaSPECs are special SPECs that are describe the SPEC process.

Core Projects
: The [Core Projects]({{< relref "/specs/meta-spec-0002.md" >}}) are
a small set of mature, community developed project widely used in
scientific research and by other packages in the ecosystem.

A **SPEC** can be

Accepted
: The [SPEC Steering Committee (SSC)]({{< relref "/specs/meta-spec-0001.md" >}})
is responsible for accepting a SPEC.
Accepting a SPEC means that is is assigned a number,
included in the [SPEC listing]({{< relref "/spec_overview.md" >}}),
and linked to a
[`specs` discussion topic](https://discuss.scientific-python.org/c/specs/accepted/15).
It typically is accepted once there is some agreement that the SPEC
describes a useful proposal, recommendation, or idea for coordinating projects.
Often, implementation details will need to be developed and negotiated with
projects and will necessarily develop and evolve after the SPEC is accepted.

Adopted
: Any project in the ecosystem can adopt any SPEC.
Each SPEC describes what adopting it means in its _Ecosystem Adoption_ section.
Every project is responsible for deciding whether they will adopt a SPEC according
to their own governance process.

Endorsed
: The [Core Projects]({{< relref "/specs/meta-spec-0002.md" >}}) can endorse any SPEC.
Endorsements signal to the ecosystem that the core projects not only adopt
the SPEC (when applicable), but that after carefully reviewing the SPEC
that they want to use their reputation in the ecosystem to publicly encourage
other projects to adopt a SPEC.
When applicable, an endorsement also mean that the Core Project provides the
necessary infrastructure required by other projects wishing to adopt the SPEC.

# Implementation

Each SPEC focuses on a single key proposal, recommendation, or idea for
coordinating projects in the scientific Python ecosystem.
A SPEC has a `Description` and an `Implementation` section.
The `Description` section captures the general problem being addressed
and, for this reason, a SPEC is accepted based largely on this section.
The reason the `Description` section carries so much weight is that
the `Implementation` section often requires an extend period of
discussions with the Core Projects as well as the larger community.
Often multiple authors will join a SPEC after it is accepted in
a collaborative effort to develop a community-supported `Implementation`
section.

Any community member can submit a new SPEC.
However, we highly recommended that you **first** do one or more of the following:

1. discuss the idea in at least one project in the ecosystem,
2. discuss the idea with at least one other member of the ecosystem,
3. discuss the idea on the
   [`specs` discussion forum](https://discuss.scientific-python.org/c/specs/ideas/9),
4. create a minimal, proof of concept prototype.

Contributors must adhere to our
[Code of Conduct]({{< relref "/about/code_of_conduct.md" >}}).

## New SPEC

Submitting a new SPEC requires making a pull request to the
[SPEC repository](https://github.com/scientific-python/specs)
with a new SPEC document.

To create a new SPEC document, use the `quickstart.py` script.
Located at the top-level of the
[SPEC repository](https://github.com/scientific-python/specs),
the script will ask you a few questions and then create a new file
appropriately named with a basic template for you to complete.

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
draft: false
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
Before the SPEC is merged, the SSC may ask you to change the SPEC number so
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
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-0-minimum-supported-versions/33
endorsed-by:
---
{{< / highlight >}}
<!-- prettier-ignore-end -->

Leave the `draft` field as is and the `endorsed-by` field empty.

The focus should be on making a clear and compelling description of the
problem that the SPEC addresses.
If the SPEC is largely documenting already established best practices
that are widely used by the Core Projects, then the `Implementation`
should be relatively straightforward to write.
However, if the SPEC is proposing something new or something not
widely used by the Core Projects already, then the `Implementation`
may be difficult to complete.
In this case, it may not be possible to complete the `Core Project Endorsement`
and `Ecosystem Adoption` subsections.

Once the SPEC is in reasonable shape, file a pull request against the
[scientific-python/specs](https://github.com/scientific-python/specs)
repository.
The SSC as well as community members will provide feedback.
They will pay particular attention to ensure the `Description`
section is clear and reasonably complete.
They will also provide advice of how much detail is needed in
the `Implementation` section.

Before the PR is merged, you will be asked to create a new
[discussion](https://discuss.scientific-python.org/c/specs/ideas/9)
(if you haven't already).

## Review and Acceptance

The SSC will consider whether the new idea fits as a SPEC and monitor
subsequent discussion.
If there is sufficient interest, the SSC will convert the discussion to the
[Accepted](https://discuss.scientific-python.org/c/specs/accepted/15)
subcategory and assign it a SPEC number.
At this point, the PR should be updated to ensure the title, file name,
and `discussion` field are correct.
When it is ready, the SSC will merge the PR.
Additional PRs will be made to update or expand the SPEC after it is
accepted.

## Endorsement and Adoption

Once the SPEC is accepted, the hard work begins.
You will need to continue engaging the Core Projects and the larger ecosystem in the
[discussion forum](https://discuss.scientific-python.org/c/specs/accepted/15)
as well as engaging with projects directly.
It will be helpful to recruit additional authors from different projects to
help develop the SPEC and respond to feedback from the ecosystem.
