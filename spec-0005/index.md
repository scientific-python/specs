---
title: "SPEC 5 — CI Best Practices"
date: 2022-09-22
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Marta Iborra <martaiborra24@gmail.com>"
  - "Ryan May <rmay@ucar.edu>"
  - "Brigitta Sipőcz <brigitta.sipocz@gmail.com>"
discussion: https://discuss.scientific-python.org/t/spec-5-ci-best-practices/507
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

## Implementation

<!--
Discuss how this would be implemented.
-->

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->

- Recommend that CI running against PRs be expected to pass--if it fails, it should be important

- Schedule regular runs of CI against nightlies/pre-releases

  - Good for other checks that don't need to run on every PR
  - Could use for pins
  - Can use labels to trigger additional runs of "exotic" jobs
  - Can open an issue on failure rather than hiding in a UI somewhere--helps give notifications
  - Generate a badge for the workflow, that can be collected into a dashboard

- GitHub actions security concerns
  - Need to trust action creators
  - Pin to hash vs. version/tag?
  -
