---
title: "SPEC 0 — Minimum Supported Versions"
date: 2020-12-17
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-0-minimum-supported-versions/33
endorsed-by:
---

## Description

This SPEC recommends that all projects across the Scientific Python ecosystem adopt a common time-based policy for dropping support of older Python and core package versions.

All versions refer to feature releases (i.e., Python 3.8.0, NumPy 1.19.0; not Python 3.8.1, NumPy 1.19.2).

Specifically, we recommend that:

1. Support for a given version of Python be dropped **3 years** after its initial release.
2. Support for a given version of other core packages be dropped **2 years** after their initial release.

We illustrate this SPEC with release dates of NumPy, SciPy, and Matplotlib.

<!-- prettier-ignore-start -->
{{<mermaid>}}
gantt
dateFormat  YYYY-MM-DD
axisFormat  %m / %Y
title Support Window

section Python
3.8  :     py38, 2019-10-14,2022-10-13
3.9  :     py39, 2020-10-05,2023-10-05
3.1  :     py31, 2021-10-04,2024-10-03

section NumPy
1.2  :     np12, 2021-01-30,2023-01-30
1.21  :     np121, 2021-06-22,2023-06-22
1.22  :     np122, 2021-12-31,2023-12-31
1.23  :     np123, 2022-06-22,2024-06-21

section SciPy
1.6  :     sp16, 2020-12-31,2022-12-31
1.7  :     sp17, 2021-06-20,2023-06-20
1.8  :     sp18, 2022-02-05,2024-02-05
1.9  :     sp19, 2022-06-29,2024-06-28

section Matplotlib
3.4  :     mpl34, 2021-03-26,2023-03-26
3.5  :     mpl35, 2021-11-15,2023-11-15

{{</mermaid>}}
<!-- prettier-ignore-end -->

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

### Drop Schedule

    On Oct 13, 2022 drop support for Python 3.8 (initially released on Oct 14, 2019)
    On Dec 31, 2022 drop support for SciPy 1.6 (initially released on Dec 31, 2020)
    On Jan 30, 2023 drop support for NumPy 1.2 (initially released on Jan 30, 2021)
    On Mar 26, 2023 drop support for Matplotlib 3.4 (initially released on Mar 26, 2021)
    On Jun 20, 2023 drop support for SciPy 1.7 (initially released on Jun 20, 2021)
    On Jun 22, 2023 drop support for NumPy 1.21 (initially released on Jun 22, 2021)
    On Oct 05, 2023 drop support for Python 3.9 (initially released on Oct 05, 2020)
    On Nov 15, 2023 drop support for Matplotlib 3.5 (initially released on Nov 15, 2021)
    On Dec 31, 2023 drop support for NumPy 1.22 (initially released on Dec 31, 2021)
    On Feb 05, 2024 drop support for SciPy 1.8 (initially released on Feb 05, 2022)
    On Jun 21, 2024 drop support for NumPy 1.23 (initially released on Jun 22, 2022)
    On Jun 28, 2024 drop support for SciPy 1.9 (initially released on Jun 29, 2022)
    On Oct 03, 2024 drop support for Python 3.1 (initially released on Oct 04, 2021)

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

- This document builds on [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html), which describes several alternatives including ad hoc version support, all CPython supported versions, default version on Linux distribution, N minor versions of Python, and time window from the X.Y.1 Python release.

- Code to generate support and drop schedule tables:

{{< readcode file="versions.py" lang="python" >}}
