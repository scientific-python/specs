---
title: "SPEC 4 — Nightly Wheels"
date: 2022-09-05
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Matthew Feickert <matthew.feickert@cern.ch>"
  - "Olivier Grisel <olivier.grisel@ensta.org>"
discussion: https://discuss.scientific-python.org/t/spec-4-nightly-wheels/474
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

This SPEC recommends that projects test against nightly wheels of several
widely-used projects in the Scientific Python ecosystem.

There are two main motivations for this recommendation:

1. Testing against nightly wheels will help identify when changes to the main branch
   of the widely-used projects break downstream projects.
2. By using the nightly wheels projects will not have to build packages from source,
   which can be difficult and time consumming.

## Implementation

<!--
Discuss how this would be implemented.
-->

We recommend that projects add a cron job to test against the nightly wheels and
when errors are encountered to automatically open an issue in their project so they
can investigate.

The nightly wheels can be found [here](https://anaconda.org/scientific-python-nightly-wheels/).

We have a GitHub action to upload new nightly wheels and remove old ones:
https://github.com/scientific-python/upload-nightly-action

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
