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

<!-- prettier-ignore-start -->
{{<mermaid>}}
gantt
dateFormat  YYYY-MM-DD
axisFormat  %m / %Y
title Support Window


section python
3.8  :     2019-10-14,2022-10-13
3.9  :     2020-10-05,2023-10-05
3.10  :     2021-10-04,2024-10-03

section numpy
1.20.0  :     2021-01-30,2023-01-30
1.21.0  :     2021-06-22,2023-06-22
1.22.0  :     2021-12-31,2023-12-31
1.23.0  :     2022-06-22,2024-06-21

section scipy
1.6.0  :     2020-12-31,2022-12-31
1.7.0  :     2021-06-20,2023-06-20
1.8.0  :     2022-02-05,2024-02-05
1.9.0  :     2022-07-29,2024-07-28

section matplotlib
3.4.0  :     2021-03-26,2023-03-26
3.5.0  :     2021-11-16,2023-11-16

section pandas
1.2.0  :     2020-12-26,2022-12-26
1.3.0  :     2021-07-02,2023-07-02
1.4.0  :     2022-01-22,2024-01-22

section scikit-image
0.18.0  :     2020-12-15,2022-12-15
0.19.0  :     2021-12-03,2023-12-03

section networkx
2.6  :     2021-07-08,2023-07-08
2.7  :     2022-02-28,2024-02-28
2.8  :     2022-04-09,2024-04-08

section scikit-learn
0.24.0  :     2020-12-22,2022-12-22
1.0  :     2021-09-24,2023-09-24
1.1.0  :     2022-05-12,2024-05-11
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

    On Oct 13, 2022 drop support for python 3.8 (initially released on Oct 14, 2019)
    On Dec 15, 2022 drop support for scikit-image 0.18.0 (initially released on Dec 15, 2020)
    On Dec 22, 2022 drop support for scikit-learn 0.24.0 (initially released on Dec 22, 2020)
    On Dec 26, 2022 drop support for pandas 1.2.0 (initially released on Dec 26, 2020)
    On Dec 31, 2022 drop support for scipy 1.6.0 (initially released on Dec 31, 2020)
    On Jan 30, 2023 drop support for numpy 1.20.0 (initially released on Jan 30, 2021)
    On Mar 26, 2023 drop support for matplotlib 3.4.0 (initially released on Mar 26, 2021)
    On Jun 20, 2023 drop support for scipy 1.7.0 (initially released on Jun 20, 2021)
    On Jun 22, 2023 drop support for numpy 1.21.0 (initially released on Jun 22, 2021)
    On Jul 02, 2023 drop support for pandas 1.3.0 (initially released on Jul 02, 2021)
    On Jul 08, 2023 drop support for networkx 2.6 (initially released on Jul 08, 2021)
    On Sep 24, 2023 drop support for scikit-learn 1.0 (initially released on Sep 24, 2021)
    On Oct 05, 2023 drop support for python 3.9 (initially released on Oct 05, 2020)
    On Nov 16, 2023 drop support for matplotlib 3.5.0 (initially released on Nov 16, 2021)
    On Dec 03, 2023 drop support for scikit-image 0.19.0 (initially released on Dec 03, 2021)
    On Dec 31, 2023 drop support for numpy 1.22.0 (initially released on Dec 31, 2021)
    On Jan 22, 2024 drop support for pandas 1.4.0 (initially released on Jan 22, 2022)
    On Feb 05, 2024 drop support for scipy 1.8.0 (initially released on Feb 05, 2022)
    On Feb 28, 2024 drop support for networkx 2.7 (initially released on Feb 28, 2022)
    On Apr 08, 2024 drop support for networkx 2.8 (initially released on Apr 09, 2022)
    On May 11, 2024 drop support for scikit-learn 1.1.0 (initially released on May 12, 2022)
    On Jun 21, 2024 drop support for numpy 1.23.0 (initially released on Jun 22, 2022)
    On Jul 28, 2024 drop support for scipy 1.9.0 (initially released on Jul 29, 2022)
    On Oct 03, 2024 drop support for python 3.10 (initially released on Oct 04, 2021)

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
