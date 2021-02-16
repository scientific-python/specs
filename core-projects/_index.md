---
title: "SPEC Core Projects"
date: 2021-01-12
draft: true
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion:
endorsed-by:
---

# Description

The scientific Python ecosystem is formed around a few "core projects".
These are projects that are depended upon by most of the other projects,
often providing basic data structures, drawing primitives,
or implementations of fundamental algorithms.
Due to their central position in the ecosystem, the policies, practices, and tooling
used by the core projects are widely seen by the ecosystem
and impact many other projects.
In fact, more specialized projects sometimes model themselves on the core packages.

## Core Projects

{{< page_gallery pages="." link=internal >}}

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

The [Steering Committee]({{< relref "/specs/steering-committee" >}}) maintains the list of
Core Projects.

## What are the characteristics of a Core Project?

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
the form of the [numpydoc docstring standard](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).
They also have a high level of test coverage to ensure that a) the code
does what it is intended to and b) new developers can modify the code without
fear of breaking it.

Core Projects are **open source**.
The 3-clause (also called "modified" or "new") BSD license is by far the most common.

## What are the responsibilities of being a Core Project?

- keep project registration information updated
- participate in the SPEC process
- discuss, adopt, and endorse SPECs

## How does a Core Project endorse a SPEC?

Core Projects may discuss whether to endorse a SPEC on their mailing list,
issue tracker, or on a pull request.
Certain SPECs may require Core Projects create their own enhancement
proposals to figure out whether and how to endorse a SPEC.

Once a Core Project decides to endorse a SPEC, they add their project
name to the `endorsed-by` field in the SPEC header via a pull request against
the [scientific-python/specs](https://github.com/scientific-python/specs)
repository.

## How many Core Projects should there be?

This is up to the Steering Committee.
But it is expected that the list of Core Projects will not rapidly change.

## How do you add a project?

If the Steering Committee decides to admit a new Core Project and the project agrees, then
the project create registration file, file a pull request against the
[scientific-python/specs](https://github.com/scientific-python/specs) repository.

To create your project registration file, change into the
`core-projects` directory and use the `register.py` script.
The script will ask you a few questions and then create a new file
appropriately named with a basic template for you to check and complete.

The Steering Committee should also update the gallery above.

## How do you remove a member?

If a Core Project no longer wishes to participate or if the Steering Committee decides to remove
a Core Project, then the project registration file should be deleted, the project
should be removed from the gallery above, and all occurrence of that Core Project
in the `endorsed-by` field of a SPEC header should be deleted.
