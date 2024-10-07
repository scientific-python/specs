---
title: "SPEC 10 — Changelog"
number: 10
date: 2024-06-03
author:
  - "Inessa Pawson <inessapawson@gmail.com>"
discussion: https://discuss.scientific-python.org/t/
endorsed-by:
---

## Description

SPEC 10 provides guidelines and best practices for maintaining a changelog file
for libraries in the Scientific Python ecosystem.

### Core Project Endorsement

<!--
Briefly discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

The endorsement of this SPEC signifies your project's support for the guidelines
laid out in the document.

## Implementation

Keeping a clear, organized, and human-readable record of notable changes for each
version of a Python library is essential for the project’s maintenance and sustainability.
It promotes transparency and trust between the project’s leadership team, developers, and users.

### What Is a Changelog?

A changelog is a file which contains a curated list of
notable changes for each version of a project.

### Guiding Principles

- Changelogs are meant for humans, not machines.
- Every version should have an entry.
- Group similar types of changes together.
- Make versions and sections linkable.
- List the most recent version first.
- Display the release date for each version.
- Indicate the type of release: minor, patch, pre-, ...
- Give credit to contributors. It’s a good idea to include contributions that are rarely
  captured by version control systems, e.g., issue and PR triage, thoughtful feedback via comments,
  community support work, etc.
- Automate the release process to the fullest extent while adhering to the guiding principles
  mentioned above.

### Types of Changes

- **New features**: Updates that expand/improve the existing features
- **Changed**: Could be further categorized as Removed, Deprecated, and Changed
- **Fixed**: Bug fixes and security patches, could be grouped separately
- **Documentation**: Updates and improvements to the library documentation
- **Infrastructure**: Updates related to the library infrastructure and tooling
- **Maintenance**: Internal updates that do not impact users directly

### Standard Changelog Format

There is not one standard changelog format.

ADD EXAMPLES

### Naming the Changelog File

CHANGELOG, CHANGES, HISTORY, NEWS, or RELEASES are widely accepted names for changelog files.

### GitHub Releases

GitHub offers a lot of flexibility in terms of creating release documentation.

The most common approaches are:

**1. Auto-Generated Release Notes:**

GitHub's "Auto-Generate Release Notes" feature allows automatically generate release notes that
include a list of merged pull requests, a list of contributors to the release, and a link to a
full changelog (if created).

You can also customize your automated release notes, using labels to create custom categories to
organize pull requests you want to include and exclude certain labels and users (e.g., bots) from
appearing in the output.

This approach is adopted by ADD PROJECTS

**2. Changelog-First Strategy:**

Maintaining a detailed changelog file that is referenced in the GitHub release notes.

This approach is adopted by ADD PROJECTS

**3. Combined Approach:**

Use auto-generated GitHub release notes alongside a manually maintained changelog. This provides
both details (from the automated notes) and curated insights (from the changelog). To direct users
to the curated changelog for additional information, include a note (e.g.,
"Also see changelog for more details") on top of the generated text.

This approach is adopted by ADD PROJECTS

The selected approach often depends on a project's size, the community's needs, and the maintainers'
resources and personal preferences.

For more info about releasing projects on GitHub,
refer to: https://docs.github.com/en/repositories/releasing-projects-on-github

### Automation

TO DO

### Editing a Changelog

It is generally acceptable to edit a changelog for the following reasons:

- maintaining accuracy of the records about the changes in each release (e.g.,
  adding essential information that was left out when the initial changelog was published)
- improving clarity and readability of the change log. Try to avoid nitpicking when
  making edits to the changelog.

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
