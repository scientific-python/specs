---
title: "SPEC Core Projects"
hide_meta: true
draft: true
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion:
endorsed-by:
---

## Description

Core Projects are depended upon by most of the other projects,
and often provide basic data structures, drawing primitives,
or implementations of fundamental algorithms.
Due to their central position in the ecosystem, the policies, practices, and tooling
used by the Core Projects are widely seen by the ecosystem
and impact many other projects.
The [Steering Committee]({{< relref "/specs/steering-committee" >}}) maintains the list of
Core Projects.

Core Projects endorse SPEC documents.
During the endorsement stage of the SPEC process, Core Project contributors
propose, discuss, and review SPEC documents with the goal of developing
a coherent implementation plan suitable for all the Core Projects.
Often SPECs are coauthored by contributors from several Core Projects as well
as other community members (e.g., contributors to other ecosystem projects).

### Core Projects

{{< page_gallery pages="." link=internal >}}

## Implementation

Core Projects are involved at all stages of the SPEC process.
They work collaboratively to develop draft SPECs so that they can be endorsed.

### What are the characteristics of a Core Project?

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

### How does a Core Project endorse a SPEC?

Core Projects use their project-specific discussion and decision making mechanisms to decide whether to support a SPEC.
Certain SPECs may, for example, require Core Projects to create their _own_ enhancement
proposals to expand on implementation details.

Once a Core Project decides to endorse a SPEC, they add their project
name to the `endorsed-by` field in the SPEC header via a pull request against
the [scientific-python/specs](https://github.com/scientific-python/specs)
repository.

### How many Core Projects should there be?

This is up to the Steering Committee.
But it is expected that the list of Core Projects will remain small and will not change rapidly.
During the endorsement stage of the SPEC process, contributors to the Core Projects are supposed
to achieve a shared agreement on how to implement the SPEC.
When adding new Core Projects, the Steering Committee should ensure that doing so will
only make it easier for the the Core Projects to achieve consensus.

### How do you add a project?

If the Steering Committee decides to admit a new Core Project and the project agrees, then
the project creates a registration file and files a pull request against the
[scientific-python/specs](https://github.com/scientific-python/specs) repository.

To create your project registration file, change into the
`core-projects` directory and use the `register.py` script.
The script will ask you a few questions and then create a new file
appropriately named with a basic template for you to check and complete.

### How do you remove a project?

If a Core Project no longer wishes to participate or if the Steering Committee decides to remove
a Core Project, then the project registration file should be deleted, the project
should be removed from the gallery above, and all occurrence of that Core Project
in the `endorsed-by` field of a SPEC header should be deleted.
