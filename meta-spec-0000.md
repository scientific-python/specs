---
title: "MetaSPEC 0 — Purpose and Process"
date: 2020-12-17
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
discussion: https://github.com/scientific-python/specs/discussions/9
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
That said, SPECs only serve a meaningful purpose if they are adopted by several
projects—and their authority largely stems from the extent to which they are.

In practice, this means that SPECs will be tightly integrated with the Core
Projects (see [MetaSPEC 2 — Core Projects]({{< relref
"/specs/meta-spec-0002.md" >}}) for details), but have to remain flexible enough
for projects to implement them according to their own constraints.

## Format

SPECs are UTF-8 encoded text files using
[Markdown](https://www.markdownguide.org/) format and stored in the [SPEC
repository](https://github.com/scientific-python/specs).
The SPEC documents are converted to HTML by code in the [scientific-python.org
repository](https://github.com/scientific-python/scientific-python.org/) using
[Hugo](https://gohugo.io/) and deployed to
[https://scientific-python.org/specs/](https://scientific-python.org/specs/).
Each SPEC has a corresponding
[discussion](https://github.com/scientific-python/specs/discussions/categories/specs)
with the same title, where anyone can comment, ask questions, or vote on
existing comments.

# Implementation

Any community member can propose a new SPEC by making making a pull request to
the [SPEC repository](https://github.com/scientific-python/specs).
However, we highly recommended that the new proposal be discussed
in at least one important project in the ecosystem first.
Often it is helpful also to have drafted a proof of concept implementation
for technical SPECs.

To get feedback from the larger community, we also recommend creating a new
[discussion](https://github.com/scientific-python/specs/discussions/new)—selecting the
[Ideas](https://github.com/scientific-python/specs/discussions/categories/ideas)
category—as early in the process as possible.
The discussion will be linked to the new SPEC using the `discussion`
field in the SPEC header.
Each new discussion should focus on a single key proposal or new idea for
coordinating projects in the scientific Python ecosystem.

Contributors must adhere to our [Code of Conduct]({{< relref
"/about/code_of_conduct.md" >}}).

## New SPECs

Creating a new SPEC requires:

1. making a pull request with a new SPEC document (Markdown file), and
2. starting a related discussion.

To create a new SPEC document, use the `quickstart.py` script.
Located at the top-level of the [SPEC
repository](https://github.com/scientific-python/specs),
the script will ask you a few questions and then create a new file
appropriately named with a basic template for you to complete.

For example,

<!-- prettier-ignore-start -->
{{< highlight bash >}}
$ python quickstart.py
Your Name: Jarrod Millman
Your Email Address: millman@berkeley.edu
SPEC number: 8
SPEC title: Minimum Supported Versions
Discussion number []: 13
{{< /highlight >}}
<!-- prettier-ignore-end -->

creates the file `spec-0008.md` containing:

<!-- prettier-ignore-start -->
{{< highlight yaml >}}
---
title: "SPEC 1 — Minimum Supported Versions"
date: 2021-01-10
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: https://github.com/scientific-python/specs/discussions/13
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
Before the SPEC is merged, the [SSC]({{< relref "/specs/meta-spec-0001.md" >}})
may ask you to change the SPEC number so that it doesn't conflict with another
PR.
If so, just rename the file as appropriate and update the SPEC number in the
`title` field of the SPEC header.

The script currently only supports adding one author.
If you need to add additional authors, just edit the text file.

For example, adding a second author the above template requires the following
change to the SPEC header:

<!-- prettier-ignore-start -->
{{< highlight yaml >}}
---
title: "SPEC 1 — Minimum Supported Versions"
date: 2021-01-10
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
discussion: https://github.com/scientific-python/specs/discussions/13
endorsed-by:
---
{{< / highlight >}}
<!-- prettier-ignore-end -->

While it is recommended that you create a new discussion before creating the PR,
you can also leave the discussion number blank.
Before the PR is merged, you will be asked to verify that you've created a
new discussion and that the `discussion` field is correct.

Once the SPEC is in reasonable shape, file a pull request against the
[scientific-python/specs](https://github.com/scientific-python/specs)
repository.

## Review and Resolution

The SSC (see [MetaSPEC 1 — Governance and Decision Making]({{< relref
"/specs/meta-spec-0001.md" >}}) for details) will consider whether the new idea
fits as a SPEC and monitor subsequent discussion.
If there is sufficient interest, the SSC will convert the discussion to the
[SPEC](https://github.com/scientific-python/specs/discussions/categories/specs)
category and assign it a SPEC number.
When it is ready the SSC will merge the PR.
Additional PRs may be made to update or expand the SPEC.

## Planning SPEC

- SPEC where things are being prototyped, not ready for adoption
- a few Core Projects could test things out

## Core Project Endorsement

Core Projects (see [MetaSPEC 2 — Core Projects]({{< relref
"/specs/meta-spec-0002.md" >}}) for details) monitor SPEC proposals and provide
feedback as early in the process as possible.
They are also encouraged to consider endorsing SPECs to help drive the ecosystem
coordination process forward.

What endorsing a SPEC means exactly may depend on the situation and is
discussed in individual the SPECs.
When appropriate endorsing a SPEC may mean merely that the project has
adopted the SPEC itself and encourages other projects to do so as well.
It may mean, for instance, providing infrastructure necessary for downstream
projects that would like to adopt a SPEC.

Core Projects may discuss whether to endorse a SPEC on their mailing list,
issue tracker, or on a pull request.
Certain SPECs may require Core Projects create their own enhancement
proposals to figure out whether and how to endorse a SPEC.

Regardless, once a Core Project decides to endorse a SPEC, they then add their project
name to the `endorsed-by` field in the SPEC header via a pull request against
the [scientific-python/specs](https://github.com/scientific-python/specs)
repository.

## Ecosystem Adoption

All projects in the ecosystem of scientific Python projects are encouraged to
discuss and adopt SPECs.

The SPEC adoption process may vary be SPEC and is specified in the SPEC.
