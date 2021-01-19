---
title: "MetaSPEC 2 — Core Projects"
date: 2021-01-12
draft: false
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: 
adopted-by:
---

# Description

The Scientific Python Ecosystem (SPE), informally defined, is a loose
federation of projects that interact well with one another and that follow
similar norms of development, documentation, testing, and so forth.

- historically a loosely defined collection on core projects helped ensure
  this worked

  - these core projects provide the foundational data structures, libraries,
    and tools depended on by many other projects in the ecosystem.

  - this means policies, practices, and tooling used by the core projects
    is widely seen by the community and impacts most other projects

  - for instance, docstring standard, nep 29, etc...

  - best practice have sometimes originated from the core and sometimes new
    practices originated outside the core, but even then these new best practices
    enjoy wider circulation once the core projects adopt and informally promote
    these new ideas

- SPECs aim, in part, to facilitate and formalize this process of both
  top-down and bottom-up coordination

  - the list of core projects can be found listed under the ``Core Projects``
    field in the header above.
  
  - the core projects are the projects that may appear in the
  ``adopted-by`` field of a SPEC header.

  - having the core projects adopting a SPEC signals to the community
    that this is a vetted and widely used standard, process, or ...

  - it also provides a mechanism for new project to become widely
    known and used.  by contributing a SPEC here smaller projects
    can ensure that the core projects are made aware of new ideas
    and can discuss adopting new ideas.

- this metaspec describes what the characteristics of the core projects are,
  and how that list can be amended

## Core Project Characteristics

### ✓ **widely used in scientific research**

The core projects focus on packages with a scientific research purpose.
Of course, these tools are often used for other purposes too, and the SPE
overlaps with the PyData ecosystem---which has a stronger focus on solving
problems in industry.

### ✓ **developed using shared community practices**

Core projects have a version control system, a bug tracker, a
code of conduct, a contributors guide, a code review process, a public
roadmap, a documented governance system, an enhancement proposal process,
and regular releases on the [Python Package Index](https://pypi.org/).

### ✓ **developed in the open by their communities**

SPE packages are developed by their communities.  Development takes place in an
online forum, and communications are public.  The developers of the project do
not all reside at a single institution.

### ✓ **well documented and well tested**

Packages document their APIs, and have inline documentation (most often in
the form of [numpydoc](https://numpydoc.readthedocs.io/) or
[napoleon](https://sphinxcontrib-napoleon.readthedocs.io/)).
Packages also have a high level of test coverage to ensure that a) the code
does what it is intended to and b) new developers can modify the code without
fear of breaking it.

### ✓ **released with a liberal license**

The core packages have liberal open source licenses.
The 3-clause (also called "modified" or "new") BSD license is by far the most common.
Whatever license is chosen should adhere to the [Open Source
Definition](https://opensource.org/osd-annotated).

### ✓ **able to work together**

Unless a package itself provides data exchange, it should support standard
mechanisms for data exchange.
Array data, e.g., should support NumPy or similar.
This ensures that core packages can "talk" to one another.


# Implementation

To register a project make a pull request to the
[SPEC repository](https://github.com/scientific-python/specs).

## Register a New Project

To create your project registration file, change into the
``projects`` directory and use the ``register.py`` script.
The script will ask you a few questions and then create a new file
appropriately named with a basic template for you to complete.

Once the registration file is in reasonable shape, file a pull request against the
[scientific-python/specs](https://github.com/scientific-python/specs)
repository.

## Review and Resolution

The SSC (see [MetaSPEC 1 — Governance and Decision Making]({{< relref
"/specs/meta-spec-0001.md" >}}) for details) will review the PR and
may ask you to clarify or correct a few things.
When it is ready the SSC will merge the PR.
Additional PRs may be made to update or expand the registration file.

Once a project is registered as a SPE, they are required to do the following:

- keep their project registration information updated
- participate in the SPEC process
- discuss and adopt SPECs that make sense for them

<!--
May need explain this more.  They need to make a PR.  The PR should explicitly demonstrate with links that they meet all these requirements.
-->

# Notes

<!--
Include a bulleted list of annotated links, comments, and other ancillary
information as needed.
-->
