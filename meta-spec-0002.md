---
title: "MetaSPEC 2 — Core Projects"
date: 2021-01-12
draft: false
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion:
endorsed-by:
---

# Description

The scientific Python ecosystem is a federation of projects
that interact well with one another and that follow similar norms of
development, documentation, testing, and so forth.
This federation is formed around a few "core projects".
These are projects that are depended upon by most of the other projects,
often providing basic data structures, drawing primitives,
or implementations of fundamental algorithms.
Due to their central position in the ecosystem, the policies, practices, and tooling
used by the core projects are widely seen by the ecosystem
and impact many other projects.
In fact, more specialized projects sometimes model themselves on the core packages.

For coordination purposes, we define the Core Projects to be the list
of Projects found in the the `Core Projects` field in the shaded box above.
This MetaSPEC describes the criteria for being a Core Project and
explains how to amend the list in the [implementation section](#implementation) below.

The Core Projects play a special role in the SPEC process.
Each Core Project monitors proposed SPECs and often members of their community
engage in the SPEC design and discussion process.
Moreover, Core Projects may appear in the `endorsed-by` field of a SPEC header.
Having a Core project endorse a SPEC signals to the community that the SPEC has
been vetted by a mature project with a healthy developer review process in-place.
It also allows more specialized projects to easily see
whether the Core Projects they depend on have endorsed a given SPEC.

Since SPECs can be proposed by anyone including members of new or more
specialized projects, having Core Projects consider these proposals
provides a convenient mechanism for projects and individuals
to have greater influence on the Core Projects and larger ecosystem.

# Implementation

Project being on list means

1.  project meets the [criteria](#criteria)
2.  project has agreed to [responsibilities](#responsibilities)

SSC (see [MetaSPEC 1 — Governance and Decision Making]({{< relref
"/specs/meta-spec-0001.md" >}}))
decides if a project is added (possible) or removed (unlikely).

## Criteria

Core Projects are **widely used in scientific research**.
Of course, these tools are often used for other purposes too, and the
scientific Python ecosystem overlaps with the PyData ecosystem---which has a
stronger focus on solving problems in industry.

Core Projects are **widely used in the scientific Python ecosystem**.
They are depended upon by most of the other projects,
often providing basic data structures, drawing primitives,
or implementations of fundamental algorithms.

Core Projects are **developed using shared community practices**.
They have a version control system, a bug tracker, a
code of conduct, a contributors guide, a code review process, a public
roadmap, a documented governance system, an enhancement proposal process,
and regular releases on the [Python Package Index](https://pypi.org/).

Core Projects are **developed in the open by their communities**.
Development takes place in an online forum, and communications are public.
The developers of the project do not all reside at a single institution.

Core Projects are **well documented and well tested**.
They document their APIs, and have inline documentation (most often in
the form of [numpydoc](https://numpydoc.readthedocs.io/) or
[napoleon](https://sphinxcontrib-napoleon.readthedocs.io/)).
They also have a high level of test coverage to ensure that a) the code
does what it is intended to and b) new developers can modify the code without
fear of breaking it.

Core Projects are **open source**.
The 3-clause (also called "modified" or "new") BSD license is by far the most common.

## Responsibilities

- keep project registration information updated
- participate in the SPEC process
- discuss, adopt, and endorse SPECs

## New Core Project

If a project would like to be a Core Project, they should proceed as follows:

1. verify project meets the criteria (above)
2. see if there is interest by creating an issue/discussion?
3. verify the project is willing to take on responsibilities
4. create registration file, file a pull request against the
   [scientific-python/specs](https://github.com/scientific-python/specs)
   repository.

To create your project registration file, change into the
`core-projects` directory and use the `register.py` script.
The script will ask you a few questions and then create a new file
appropriately named with a basic template for you to check and complete.
