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
operational guidelines for projects in the Scientific Python ecosystem.
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

In practice, this means that SPECs will be tightly integrated with core
projects, but remain flexible enough for projects to implement them according
to their own constraints.

## Format

SPECs are UTF-8 encoded text files using
[Markdown](https://www.markdownguide.org/) format.
We use [Hugo](https://gohugo.io/) to convert SPECs to HTML for viewing on the
web [^2].
Because the SPECs are maintained as text files in a versioned
repository, their revision history is the historical record of the
feature proposal[^1].

# Implementation

Any community member can propose a new SPEC by making making a pull request to
the [SPEC repository](https://github.com/scientific-python/specs).
However, we highly recommended that new proposals should first be discussed
in at least one important project in the ecosystem.
Often it is helpful to have also drafted a proof of concept implementation
for technical SPECS.

We also recommend creating a new
[discussion](https://github.com/scientific-python/specs/discussions/new) and
selecting the
[Ideas](https://github.com/scientific-python/specs/discussions/categories/ideas)
category as early in the process as possible.
The discussion will be linked to the new SPEC using the ``discussion``
field in the SPEC header.

Focus on a single key proposal or new idea for coordinating projects in
the scientific Python ecosystem.

Contributors must adhere to our [Code of Conduct]({{< relref
"/about/code_of_conduct.md" >}}).

## Create PR

Use the ``quickstart.py`` script to create the PR.
This script is located at the top-level of the [SPEC
repository](https://github.com/scientific-python/specs).
The script will ask you a few questions and then create new file
appropriately named with a basic template for you to complete.

For example,

{{< highlight bash >}}
$ python quickstart.py
Enter your name: Jarrod Millman
Enter your email address: millman@berkeley.edu
Enter the SPEC number: 1
Enter the SPEC title: Minimum Supported Versions
Enter the discussion number: 13
{{< / highlight >}}

creates the file ``spec-0001.md`` containing

{{< highlight markdown >}}
---
title: "SPEC 1 — Minimum Supported Versions"
date: 2021-01-10
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: https://github.com/scientific-python/specs/discussions/13
adopted-by:
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
Discuss how this would be implemented by projects.
-->

# Notes

<!--
Include a bulleted list of annotated links, comments, and other ancillary
information as needed.
-->
{{< / highlight >}}
<!--

The proposal should be submitted as a draft SPEC via a `GitHub pull
request`_ to the ``doc/nxeps`` directory with the name ``nxep-<n>.rst``
where ``<n>`` is an appropriately assigned four-digit number (e.g.,
``spec-0000.rst``). The draft must use the :doc:`nxep-template` file.

-->

When asked to enter the SPEC number, choose the next available number that
has not yet been used.
Before the PR is merged, the SCC may ask you to change the SPEC number so that
it doesn't conflict with another PR.
If so, just rename the file as appropriate and update the SPEC number in the
``title`` field of the SPEC header.

The script currently only supports adding one author.
If you need to add additional authors, just edit the text file.

For example, adding a second author the above template requires the following
change to the SPEC header:

{{< highlight markdown >}}
---
title: "SPEC 1 — Minimum Supported Versions"
date: 2021-01-10
draft: false
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
discussion: https://github.com/scientific-python/specs/discussions/13
adopted-by:
---
{{< / highlight >}}

While it is recommended that you create a new discussion before creating the PR,
you can just make up a number when asked to enter the discussion number.
Before the PR is merged, you will be asked to verify that you've created a
new discussion and that the ``discussion`` field is correct.

## Review and Resolution

The SCC (see [MetaSPEC 1 — Governance and Decision Making]({{< relref
"/specs/meta-spec-0001.md" >}}) for details) will consider the new idea and
monitor the discussion.
If there is interest, the SCC will convert the discussion to the
[SPEC](https://github.com/scientific-python/specs/discussions/categories/specs)
category and assign it a SPEC number.
When it is ready the SCC will merge the PR.
Additional PRs may be made to update or expand the SPEC.

## Enhancement Proposals and SPECs

For projects with an existing enhancement proposal process in place, we
recommend creating a new proposal to list the SPECs adopted along with links to
project discussions leading to adoption.

Once a project adopts a SPEC, they should add their project name to the
``adopted-by`` field in the SPEC header.

<!--
### SPEC Status

Every SPEC is assigned a status, which is either ``draft``, ``accepted``, or ``withdrawn``.

#### How a SPEC becomes Accepted

#### How a SPEC becomes Withdrawn
-->

# Notes

[^1]: This historical record is available by the normal git commands for
    retrieving older revisions, and can also be browsed on
    [GitHub](https://github.com/scientific-python/specs).

[^2]: The URL for viewing SPECs on the web is
    <https://scientific-python.org/specs/>
