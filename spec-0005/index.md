---
title: "SPEC 5 — CI Best Practices"
date: 2022-09-22
author:
  - "Tim Head <betatim@gmail.com>"
  - "Marta Iborra <martaiborra24@gmail.com>"
  - "Ryan May <rmay@ucar.edu>"
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Brigitta Sipőcz <brigitta.sipocz@gmail.com>"
discussion: https://discuss.scientific-python.org/t/spec-5-ci-best-practices/507
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the recommendation.
-->

### Core Project Endorsement

<!--
Briefly discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Briefly discuss what it means for a project to adopt this SPEC.
-->

## Implementation

<!--
Discuss how this would be implemented.
Explain the general need and the advantages of this specific recommendation.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

### Build nightly wheels

By building and uploading wheel for your project you make it easier for projects
that depend on you to test against your latest changes. They can then report problems
they find.

There are a few steps to implementing this for your project:

1. Get access to the area that nightly wheels are uploaded to
2. Setup a CI step that builds wheels for your project
3. Setup a CI step that uploads wheels to https://anaconda.org/scientific-python-nightly-wheels/

For step (1) contact XXX. Deposit the token you get as a [secret on your repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets) named `UPLOAD_TOKEN`.

The work for step (2) depends on your project. You are probably already doing this for your
releases. The new thing to add is that building wheels is run on a schedule every night or
once a week.

For step (3) there is a GitHub Action that you can use. You can find the action at
https://github.com/scientific-python/upload-nightly-action. To use it in your "build wheels
workflow" add the following lines as an additional step:

```
- name: Upload wheel
  uses: scientific-python/upload-nightly-action@main
  with:
    artifacts_path: dist/
    anaconda_nightly_upload_token: ${{ secrets.UPLOAD_TOKEN }}
```

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
