---
title: "SPEC 13 — Recommended targets and naming conventions"
number: 13
date: 2024-06-05
author:
  - "Pamphile Roy <roy.pamphile@gmail.com>"
  - "Matthias Bussonnier <bussonniermatthias@gmail.com>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-13-recommended-targets-and-naming-conventions
endorsed-by:
---

## Description

For consistency and decreased cognitive load across the ecosystem, this SPEC
recommends naming conventions around various project aspects--such as project
structure, repository layout, folder names, task runner and `pyproject.toml`
targets name.

From a cursory survey in the Scientific Python ecosystem, we discover some
frustration from contributors and maintainer when moving from one project to
another and believe that consistency will make it both easier for existing
maintainer to contribute to project as well a decrease the confusion of new
developers when contributing or creating new projects.

There seem to be a strong consensus with preference for `docs` in favor of
`docs`, and a preference for `tests` in favor of `test`.

We will note though that the _extra_ optional dependencies on PyPI seem to favor
`test` (present on 7573 packages) vs `tests` (2362 times).

## Implementation

For the tie being we will not pronounce ourselves on the optional extra
`extra` dependency for `pyproject.toml`.

For other targets and folders we recommend that:

- Targets related to testing be named `tests` (and not `test`). For example
  `spin tests`, `python dev.py tests`, `nox -s tests`.
- Folders containing tests be names `tests`.
- Targets related to documentations be named `docs` (and not `doc`). For example
  `spin docs`, `make docs`, `tox -s docs`.
- That the documentation `extra` optional dependency be named `docs` (and not
  doc), so that docs dependencies can be installed with `pip install .[docs]`
- Use lowercase.

It is appropriate to have the singular aliases to ease transition, but the
plurals should always be the default.

## Notes

![Vote from ecosystem maintainers at the 2024 Scientific Python Ecosystem Summit in Seattle](./ecosystem_voting.jpg)
