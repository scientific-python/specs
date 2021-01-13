---
title: "MetaSPEC 2 — Adopted By Field"
date: 2021-01-12
draft: false
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: 
adopted-by:
---

# Description

The Adopted By (AB) projects, informally defined, are a loose
federation of projects that interact well with one another and that follow
similar norms of development, documentation, testing, and so forth.
More concretely, the AB projects are the projects that may appear in the
``adopted-by`` field of a SPEC header.
And all AB projects are included in the ``adopted-by`` field of this MetaSPEC.

## AB Projects

### ✓ **are used in scientific research**

The AB projects focus on packages with a scientific research purpose.
Of course, these tools are often used for other purposes too, and the SPE
overlaps with the PyData ecosystem---which has a stronger focus on solving
problems in industry.

### ✓ **are mature Python packages**

AB projects have a version control system, a bug tracker, a
code of conduct, a contributors guide, a code review process, a public
roadmap, a documented governance system, an enhancement proposal process,
and regular releases on the [Python Package Index](https://pypi.org/).

### ✓ **are developed in the open by their communities**

SPE packages are developed by their communities.  Development takes place in an
online forum, and communications are public.  The developers of the project do
not all reside at a single institution.

### ✓ **are well documented**

Packages must document their APIs, and have inline documentation (most often in
the form of [numpydoc](https://numpydoc.readthedocs.io/) or
[napoleon](https://sphinxcontrib-napoleon.readthedocs.io/)).

### ✓ **are well tested**

Packages should have a high level of test coverage to ensure that a) the code
does what it is intended to and b) new developers can modify the code without
fear of breaking it.

### ✓ **are released with a liberal license**

The About by packages have liberal open source licenses.
The 3-clause (also called "modified" or "new") BSD license is by far the most common.
Whatever license is chosen should adhere to the [Open Source
Definition](https://opensource.org/osd-annotated).

### ✓ **Use common data exchange mechanisms**

Unless a package itself provides data exchange, it should support standard
mechanisms for data exchange.
Array data, e.g., should support NumPy or similar.
This ensures that core packages can "talk" to one another.


# Implementation

To register a project make a pull request to the
[SPEC repository](https://github.com/scientific-python/specs).

## Register a New Project

To create your project registration file, change into the
``meta-spec-0002`` directory and use the ``register.py`` script.
The script will ask you a few questions and then create a new file
appropriately named with a basic template for you to complete.

For example,

{{< highlight bash >}}
$ python register.py
Project Name: NetworkX
What name is it register under on https://pypi.org/project/: networkx
Discussion number [optional]:
{{< /highlight >}}

creates the file ``networkx.md`` containing:

{{< highlight markdown >}}
---
project-name: "NetworkX"
date: 2021-01-12
draft: false
discussion: https://github.com/scientific-python/specs/discussions/6
---

# Use in scientific research

<!--
Briefly describe how this project is used in scientific research.
-->
{{< /highlight >}}

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
