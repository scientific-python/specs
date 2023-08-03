---
title: "SPEC 0 — Minimum Supported Versions"
date: 2020-12-17
author:
  - "Andreas C. Mueller <andreas.mueller.ml@gmail.com>"
  - "Brigitta Sipőcz <brigitta.sipocz@gmail.com>"
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Madicken Munk <madicken@berkeley.edu>"
  - "Matt Haberland <mhaberla@calpoly.edu>"
  - "Matthias Bussonnier <bussonniermatthias@gmail.com>"
  - "Ralf Gommers <ralf.gommers@gmail.com>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Thomas A Caswell <tcaswell@gmail.com>"
discussion: https://discuss.scientific-python.org/t/spec-0-minimum-supported-versions/33
endorsed-by:
  - ipython
  - networkx
  - numpy
  - scikit-image
  - scipy
---

## Description

This SPEC recommends that all projects across the Scientific Python ecosystem adopt a common time-based policy for dropping support of older Python and core package versions.

All versions refer to feature releases (i.e., Python 3.8.0, NumPy 1.19.0; not Python 3.8.1, NumPy 1.19.2).

Specifically, we recommend that:

1. Support for a given version of Python be dropped **3 years** after its initial release.
2. Support for a given version of other core packages be dropped **2 years** after their initial release.

### Core Project Endorsement

<!--
Briefly discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Briefly discuss what it means for a project to adopt this SPEC.
-->

## Implementation

### Motivation

Limiting the scope of supported dependencies is an effective way for packages to limit maintenance burden.
Combinations of packages need to be tested, which impacts also on continuous integration times and infrastructure upkeep.
Code itself also becomes more complicated when it has to be aware of various combinations of configurations.

Adoption of this SPEC will ensure a consistent support policy across packages, and reduce the need for individual projects to divise similar policies.

Ultimately, reduced maintenance burden frees up developer time, which translates into more features, bugfixes, and optimizations for users.

### Background

In the past, longer support cycles were common.
There were several reasons for this, including the Python 2 / 3 transition, difficulties installing packages, and users needing to use old, operating-system provided versions of Python.
The situation has since improved due to improved installations via binary wheels, virtual environments becoming commonplace, and support for Python 2 being dropped.

### Support Window

{{< mermaid >}}
{{< include-raw "chart.md" >}}
{{< /mermaid >}}

### Drop Schedule

{{< include-md "schedule.md" >}}

## Notes

- This document builds on [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html), which describes several alternatives including ad hoc version support, all CPython supported versions, default version on Linux distribution, N minor versions of Python, and time window from the X.Y.1 Python release.

- Code to generate support and drop schedule tables:

{{< readcode file="SPEC0_versions.py" lang="python" >}}
