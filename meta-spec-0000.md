---
title: "MetaSPEC 0 — Purpose and Process"
date: 2020-12-17T19:53:08-08:00
draft: false
author: 'Jarrod Millman <millman@berkeley.edu>'
spec_status: Draft
spec_type: meta
summary: |
  The Scientific Python Ecosystem Coordination (SPEC) mechanism
  is used to recommend project policies, coding conventions,
  and standard tooling.
---

{{< notice note >}}
This SPEC is an example of a MetaSPEC (i.e., a SPEC about SPECs).
{{< /notice >}} 

# Description

A Scientific Python Ecosystem Coordination (SPEC) document is a mechanism for
recommending project policies, coding conventions, and standard tooling for
coordinating projects in the scientific Python ecosystem.
A SPEC should provide a concise technical specification of the feature and a
rationale for the feature.
The SPEC author is responsible for building consensus within the community and
documenting dissenting opinions.

SPECs are UTF-8 encoded text files using
[Markdown](https://www.markdownguide.org/) format.
We use [Hugo](https://gohugo.io/) to convert SPECs to HTML for viewing on the
web [^2].
Please see the [spec-template]({{< ref "/specs/spec-template.md" >}})
file and for more information.
Because the SPECs are maintained as text files in a versioned
repository, their revision history is the historical record of the
feature proposal[^1].

The SPEC process begins with a new idea for coordinating projects in the
scientific Python ecosystem.  It is highly recommended that a single SPEC
contain a single key proposal or new idea.  The more focused the SPEC, the more
successful it tends to be.

Each SPEC has one or more authors who write the SPEC, shepherd the discussions
in the appropriate forums, and build community support for the idea.
The SPEC author must first attempt to ascertain whether the
idea is suitable for a SPEC.

Ideas often come from developers of projects in the ecosystem.
In these cases, the idea should be discussed in those projects first.

# Implementation

Before submitting a new proposal, the SPEC author (there may be multiple authors)
must start a discussion briefly explaining the basic idea:
     
  https://github.com/scientific-python/specs/discussions/new

If there is interest the SPEC author will be requested to draft a proposed SPEC.

- quickstart tool


<!--

The proposal should be submitted as a draft SPEC via a `GitHub pull
request`_ to the ``doc/nxeps`` directory with the name ``nxep-<n>.rst``
where ``<n>`` is an appropriately assigned four-digit number (e.g.,
``spec-0000.rst``). The draft must use the :doc:`nxep-template` file.

-->


## Review and Resolution

Once you create a PR, the SPEC Steering Committee will do some basic checks on your PR.

At the earliest convenience, the PR should be merged (regardless of
whether it is accepted during discussion).  Additional PRs may be made
by the Author to update or expand the SPEC, or by maintainers to set
its status, discussion URL, etc.

### SPEC Status

Every SPEC is assigned a status, which is either ``draft``, ``accepted``, or ``withdrawn``.

#### How a SPEC becomes Accepted

#### How a SPEC becomes Withdrawn

# Discussion

# Notes

[^1]: This historical record is available by the normal git commands for
    retrieving older revisions, and can also be browsed on
    [GitHub](https://github.com/scientific-python/specs).

[^2]: The URL for viewing SPECs on the web is
    <https://scientific-python.org/specs/>
