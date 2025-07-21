---
title: "SPEC Purpose and Process"
date: 2020-12-17
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
---

## Description

The SPEC process is designed to identify areas of shared concern between projects
in the scientific Python ecosystem and to produce collaboratively written,
community adopted guidelines for addressing these.
Such guidelines are known as SPECs: Scientific Python Ecosystem Coordination documents.

Specifically, the purpose of the SPEC process is

1. to help unify the ecosystem for users and developers;
2. to provide guidance to projects on technical issues or processes;
3. to document standard APIs, development tools, and community practices; and
4. to foster ecosystem-wide discussions of common problems and to develop shared solutions.

Projects in the ecosystem have an existing, diverse set of proposal processes
and development constraints.
SPECs complement these: they are a mechanism to encourage shared practices and
improve uniformity of experience across projects.
SPECs may, for example, capture established practices so that new projects can
learn from them; or they may propose a new practice that the authors believe
will benefit the ecosystem as a whole.

Projects decide for themselves whether to adopt any given SPEC—often, this
would be through team consensus.
They may look towards endorsements by [Core Projects](/specs/core-projects) as a signal to help them decide.
A SPEC may not be a good fit for a project, and thus there is no
expectation that all SPECs must be adopted by all projects (in fact, even Core Projects that endorse a SPEC—i.e., signaling that they think it is a good idea—may choose not to adopt it themselves).
Still, SPECs best serve their purpose of communicating cross-project concepts when adopted by numerous projects—and their authority stems from the extent to which they are.

Participants in the SPEC process must adhere to our
[Code of Conduct](https://scientific-python.org/code_of_conduct/).

## What is a SPEC?

A SPEC (Scientific Python Ecosystem Coordination) is a document that captures an idea applicable to multiple projects.
It is the product of discussions with developers across the ecosystem, and captures one of the following types of narratives:

- **Recommendation:** We recommend that you do Y (e.g., [SPEC 8 — Securing the Release Process](https://scientific-python.org/specs/spec-0008/)).
- **Guideline:** Some projects may need to do Y. If you do Y, we recommend that you do it as follows (e.g., [SPEC 1 — Lazy Loading](https://scientific-python.org/specs/spec-0001/)).
- **Advisory:** If you do Y, you should be aware of the following (we don't have any such advisories yet).

{{< admonition important >}}
**What a SPEC is not**

SPECs are _not_ meant to be extensive technical documents that cover a large amount of detail.
They typically _summarize_ an idea, referring to external sources, such as GitHub repositories or websites, for further detail.

If you find yourself wanting to _disseminate information_ across the
ecosystem, it may be better to write a blog post on
https://blog.scientific-python.org or to contribute to an existing
piece of documentation, such as https://learn.scientific-python.org/development/.
A blog post is also a good way to generate initial engagement around an idea that is not yet mature enough, or within scope, to become a SPEC.
{{< /admonition >}}

### Key Terms

Scientific Python Ecosystem
: The **ecosystem** is a loose federation of community developed Python projects
widely used in scientific research that interact well with one another and that
follow similar norms of development, documentation, testing, and so forth.

SPEC Core Projects
: The [Core Projects](/specs/core-projects)
are a small subset of the ecosystem consisting of mature, community developed projects
that are (a) depended upon by most of the other projects and (b) responsible for
reviewing, discussing, implementing, and endorsing SPEC documents.

SPEC Steering Committee
: The [Steering Committee](/specs/steering-committee) leads the SPEC project and
manages the SPEC process including moderating
the [SPECs discussion forum](https://discuss.scientific-python.org/c/specs/),
accepting SPEC documents, and maintaining the SPEC process documents.

SPEC Process
: The SPEC process is outlined in this document and the associated
[SPEC Steering Committee](/specs/steering-committee) and
[SPEC Core Projects](/specs/core-projects) documents.
This process is managed and overseen by the Steering Committee, and functions in collaboration
with the Core Projects, community members, and projects across the ecosystem.

SPEC Document
: A **SPEC document** provides operational guidelines for projects and helps
coordinate the ecosystem to provide a more unified experience for users and developers.
These documents are developed collaboratively with the Core Projects and other interested
ecosystem projects and community members.

### Format

SPECs are UTF-8 encoded text files using
[Markdown](https://www.markdownguide.org/) format and stored in the
[SPEC repository](https://github.com/scientific-python/specs).
The SPEC documents are converted to HTML by code in the
[scientific-python.org repository](https://github.com/scientific-python/scientific-python.org/) using
[Hugo](https://gohugo.io/) and deployed to
[https://scientific-python.org/specs/](https://scientific-python.org/specs/).
Each SPEC has two corresponding discussions: one under [SPECS → Ideas](https://discuss.scientific-python.org/c/specs/ideas), where the SPEC committee discussed its viability, and another under [SPECS → Web Comments](https://discuss.scientific-python.org/c/specs/web-comments), where public comments from https://scientific-python.org/specs are stored.

## Implementation

The Steering Committee manages the SPEC process and will provide guidance to contributors
throughout the process.
In this section, we provide an overview of the main decision points in the SPEC process
and provide guidance for how to get started with a new SPEC proposal.

### Decision Points

A SPEC passes through four decision points over the course of
its development and implementation:
**Accept**, **Publish**, **Endorse**, and **Adopt**.

<!-- prettier-ignore-start -->
```mermaid
graph LR

START[ ]--> |Propose| A[Accept]
A--> |Develop| B[Publish]
B--> |Canvass| C[Endorse]
C--> |Recommend| D[Adopt]

click A callback "Steering Committee Action"
click B callback "Author Action"
click C callback "Core Project Action"
click D callback "Ecosystem Action"

style START fill:#FFFFFF, stroke:#FFFFFF;

```
<!-- prettier-ignore-end -->

The authors start by _proposing_ a SPEC idea, as outlined in [New
SPEC Proposals](#new-spec-proposals)—please read that section carefully before
proposing a new SPEC.

The decision to **accept** (and number) a SPEC is made by the Steering
Committee, once there is agreement that the SPEC concept is
applicable, and it has been confirmed that there are at least two
authors from two different projects interested in working on the new
SPEC and championing it to various projects.
At this point, the authors may submit a first version of the SPEC as a
PR to the [SPEC
repository](https://github.com/scientific-python/specs).
This version may be merged to the main branch whenever the authors
consider it ready, clearly labeled as a draft (see `is-draft` header
field).

In the accepted phase, the authors _develop_ their SPEC, in
consultation with Core Projects and interested community members.
This is done in a collaborative and iterative process, focused on
ensuring that the SPEC is broadly applicable and likely to be widely
adopted.
Once authors consider their SPEC complete, they **publish** it,
removing its draft status.

The author now _canvasses_ their project with the Core Projects, so
they may **endorse** it.
Once a SPEC is endorsed, substantive changes require the approval of
all endorsing Core Projects.

A SPEC is _recommended_ for wide-spread adoption once it is endorsed by
two (or more) Core Projects.
Additional details may be found in [Core Project
documentation](/specs/core-projects).
Individual projects choose to **adopt** the SPEC according to their
own decision-making processes.
Each SPEC describes what adopting it means in its _Ecosystem Adoption_ section.
Ecosystem projects are welcome to adopt a SPEC at any point in the
process, however, it may make sense to wait until a SPEC is endorsed
by several Core Projects to ensure that the SPEC has been vetted and
is deemed stable enough for widespread adoption.
Once a SPEC is endorsed, it may still evolve, but the barrier for
modifying the SPEC will increase substantially (since all endorsing
projects would need to agree to changes).
Projects that adopt a SPEC early should engage in the collaborative
process leading to the SPEC being endorsed by the Core Projects, to
ensure that their use cases are incorporated.

#### Badges

Projects can highlight their adoption of specific SPECs with a SPEC badge.
For example, for SPEC 0, we recommend using

{{< tabs >}}

[[tab]]
name = 'Rendered badge'
content = '''
[![SPEC 0 — Minimum Supported Dependencies](https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038)](https://scientific-python.org/specs/spec-0000/)
'''

[[tab]]
name = 'Markdown'
content = '''

```
[![SPEC 0 — Minimum Supported Dependencies](https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038)](https://scientific-python.org/specs/spec-0000/)
```

'''

[[tab]]
name = 'reStructuredText'
content = '''

```
|SPEC 0 — Minimum Supported Dependencies|

.. |SPEC 0 — Minimum Supported Dependencies| image:: https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038
   :target: https://scientific-python.org/specs/spec-0000/
```

'''

{{< /tabs >}}

Alternatively, you can use one badge to indicate adoption of multiple SPECs.
For example, to indicate adoption of SPECs 0, 1, and 4, we recommend the following

{{< tabs >}}

[[tab]]
name = 'Rendered badge'
content = '''
[![Scientific Python Ecosystem Coordination](https://img.shields.io/badge/SPEC-0,1,4-green?labelColor=%23004811&color=%235CA038)](https://scientific-python.org/specs/)
'''

[[tab]]
name = 'Markdown'
content = '''

```
[![Scientific Python Ecosystem Coordination](https://img.shields.io/badge/SPEC-0,1,4-green?labelColor=%23004811&color=%235CA038)](https://scientific-python.org/specs/)
```

'''

[[tab]]
name = 'reStructuredText'
content = '''

```
|Scientific Python Ecosystem Coordination|

.. |Scientific Python Ecosystem Coordination| image:: https://img.shields.io/badge/SPEC-0,1,4-green?labelColor=%23004811&color=%235CA038
   :target: https://scientific-python.org/specs/
```

'''

{{< /tabs >}}

### New SPEC Proposals

<!-- This is a focused distillation of #decision-points for authors. -->

A good SPEC proposal focuses on a single key recommendation or idea
for coordinating projects in the scientific Python ecosystem, as
discussed under [What is a SPEC?](#what-is-a-spec).

As a SPEC moves through the process, it goes through different states,
as discussed under [Decision Points](#decision-points) and summarized
here.

**Before proposing** a SPEC, we highly recommended that you first **vet
the idea** by doing one or more of the following:

1. Discuss the idea with at least one project in the ecosystem—for example, by posting to project mailing lists or by having a birds-of-a-feather discussion at a community conference like SciPy;
2. discuss the idea with at least one other member of a [Core Project](/specs/core-projects); or
3. if it is a technical idea, create a minimal proof of concept.

**Before submitting** a proposed SPEC:

1. Ensure that the SPEC has at least two authors from two different projects,
   to show cross-project interest.

2. The **idea must be proposed** on the discussion forum under the [`SPECS/Ideas`
   topic](https://discuss.scientific-python.org/c/specs/ideas/9).
   Please list your co-authors.

If the SPEC committee considers the idea suitable for a SPEC, the spec
is **approved** and a number is allocated.

At this point, you should **draft your SPEC document and submit it**
via pull request to the [SPEC repository](https://github.com/scientific-python/specs).

Use the `quickstart.py` script to create the new SPEC document.
Located at the top-level of the [SPEC
repository](https://github.com/scientific-python/specs), the script
will ask you a few questions[^newspec] and then create a new file
appropriately named with a basic template for you to complete (e.g.,
`spec-0000/index.md`).
Leave the `draft` field set to `true` and the `endorsed-by` field empty.
Once the SPEC is in readable shape, file a pull request against the
[SPEC repository](https://github.com/scientific-python/specs).
Let the SPEC committee know when you are ready for your PR to be
merged.
Once they do so, the SPEC will appear in draft form at
<https://scientific-python.org/specs>.

Your job now is to refine the SPEC iteratively and collaboratively
with the community, using follow-up PRs.
You should focus on ensuring that the SPEC is broadly applicable and
likely to be widely adopted.
Once you consider your SPEC complete, **publish** it by making a PR to
remove its draft status.

## Endorsing a SPEC

<!-- This is a focused distillation of #decision-points for Core Projects. -->

[Core Projects](/specs/core-projects) may signal their approval of a SPEC by _endorsing_ it.
This endorsement makes it more likely that other projects will _adopt_ it.
Endorsing a SPEC does _not_, however, mean that a Core Project needs to _adopt_ a SPEC, although it typically would if feasible.
Core Projects use their project-specific discussion and decision making mechanisms to decide whether to endorse a SPEC.

Once a Core Project decides to endorse a SPEC, they add their project
name to the `endorsed-by` field in the SPEC header via a pull request against
the [scientific-python/specs](https://github.com/scientific-python/specs)
repository.

## Notes

[^newspec]:
    The script currently only supports adding one author.
    If you need to add additional authors, just edit the text file.

    Additional files associated with a SPEC document may be kept in the directory
    containing the SPEC.
    For example, files associated with `spec-0000/index.md` are in `spec-0000/`.
