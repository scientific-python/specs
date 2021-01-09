---
title: MetaSPEC 1 — Governance and Decision Making
date: 2021-01-06T09:11:39-08:00
draft: false
author:
  - 'Jarrod Millman <millman@berkeley.edu>'
  - 'Stéfan van der Walt <stefanv@berkeley.edu>'
spec_status: Draft
summary: |
  Governance and decision making for the Scientific Python Ecosystem Coordination (SPEC) process.
---

# Description

Scientific Python Ecosystem Coordination documents or SPECs, for short, provide operational guidelines for projects in the Scientific Python ecosystem.  Their goal is to coordinate the ecosystem and to provide a more unified experience for users.

Projects in the ecosystem have an existing, diverse set of proposal processes and development constraints.  SPECs, therefore, are not meant to be prescriptive: rather, they are a mechanism to encourage shared practices and improve uniformity of experience.  SPECs may, for example, capture established practices so that new projects can learn from them; or they may propose a new practice that the authors believe will benefit the ecosystem as a whole.

Projects decide for themselves whether to adopt any given SPEC—often, this would be through team consensus.  A SPECs may not be a good fit for every single project, and thus there is no expectation that all SPECs must be adopted by all projects.  That said, SPECs only serve a meaningful purpose if they are adopted by several projects—and their authority largely stems from the extent to which they are.

In practice, this means that SPECs will be tightly integrated with core projects, but remain flexible enough for projects to implement them according to their own constraints.

## Steering Committee

The initial SPEC Steering Committee (SSC) is composed of representatives from the NumPy, SciPy, Matplotlib, pandas, statsmodels, scikit-image, scikit-learn, and NetworkX projects as well as two general community members.

As mentioned above, the steering project does not decide which SPECs are adopted—that choice resides with individual projects.  They do, however, have control over whether SPECs are accepted in the first place.

The SSC will:

- Maintain and approve SPECs, including SPECs related to the SPEC
  process (MetaSPECs);
- serve as a communication channel to and from their projects; and
- accept new projects into the SSC.

## Contributors

Any community member can propose a new SPEC by making a pull request to the [SPEC repository](https://github.com/scientific-python/specs).  However, we recommend first discussing ideas in the [online forum](https://github.com/scientific-python/specs/discussions/categories/ideas).

Contributors should read our [Code of Conduct]({{< ref
"/about/code_of_conduct.md" >}}).

# Implementation

## Decision making and communication

The SSC makes decisions through group consensus and, in the very rare instance where no consensus can be reached, by two-thirds majority vote of those available to cast a vote within ten days.

Communication within the SSC takes place via the email group at ...  SSC members are expected to be aware of conversations on this list to lean validity to consensus seeking and voting.

## Membership

There are no term limits to the SPEC Steering Committee (SSC)—projects may replace their representatives at will, or choose not to participate.  New projects are invited by the SSC.

## MetaSPECs

Alterations to MetaSPECs have to be approved by the SSC.

## Enhancement Proposals and SPECs 

For projects with an existing enhancement proposal process in place, we recommend creating a new proposal to list the SPECs adopted along with links to project discussions leading to adoption.

Once a project adopts a SPEC, they should add their project name to the `spec_adopted_by` field in the SPEC header.

- email list

  - specs@python.org ?
    - https://mail.python.org/mailman3/lists/?count=200
  - specs@groups.io ?

# Discussion

# Notes
