---
title: "SPEC 0 — Minimum Supported Versions"
date: 2020-12-17
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Ross Barnowski <rossbar@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-0-minimum-supported-versions/33
endorsed-by:
  - ipython
  - networkx
  - scikit-image
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
3.9  :     2020-10-05,2023-10-05
3.10  :     2021-10-04,2024-10-03
3.11  :     2022-10-24,2025-10-23
3.12  :     2023-10-02,2026-10-01

section numpy
1.21.0  :     2021-06-22,2023-06-22
1.22.0  :     2021-12-31,2023-12-31
1.23.0  :     2022-06-22,2024-06-21
1.24.0  :     2022-12-18,2024-12-17

section scipy
1.10.0  :     2023-01-03,2025-01-02
1.7.0  :     2021-06-20,2023-06-20
1.8.0  :     2022-02-05,2024-02-05
1.9.0  :     2022-07-29,2024-07-28

section matplotlib
3.5.0  :     2021-11-16,2023-11-16
3.6.0  :     2022-09-16,2024-09-15
3.7.0  :     2023-02-13,2025-02-12

section pandas
1.3.0  :     2021-07-02,2023-07-02
1.4.0  :     2022-01-22,2024-01-22
1.5.0  :     2022-09-19,2024-09-18
2.0.0  :     2023-04-03,2025-04-02

section scikit-image
0.19.0  :     2021-12-03,2023-12-03
0.20.0  :     2023-02-28,2025-02-27

section networkx
2.6  :     2021-07-08,2023-07-08
2.7  :     2022-02-28,2024-02-28
2.8  :     2022-04-09,2024-04-08
3.0  :     2023-01-08,2025-01-07
3.1  :     2023-04-04,2025-04-03

section scikit-learn
1.0  :     2021-09-24,2023-09-24
1.1.0  :     2022-05-12,2024-05-11
1.2.0  :     2022-12-08,2024-12-07

section xarray
0.19.0  :     2021-07-23,2023-07-23
0.20.0  :     2021-11-02,2023-11-02
0.21.0  :     2022-01-28,2024-01-28
2022.10.0  :     2022-10-13,2024-10-12
2022.11.0  :     2022-11-04,2024-11-03
2022.12.0  :     2022-12-02,2024-12-01
2022.3.0  :     2022-03-02,2024-03-01
2022.6.0  :     2022-07-22,2024-07-21
2022.9.0  :     2022-09-29,2024-09-28
2023.1.0  :     2023-01-18,2025-01-17
2023.2.0  :     2023-02-07,2025-02-06
2023.3.0  :     2023-03-22,2025-03-21
2023.4.0  :     2023-04-14,2025-04-13
2023.5.0  :     2023-05-19,2025-05-18

section ipython
7.24.0  :     2021-05-28,2023-05-28
7.25.0  :     2021-06-25,2023-06-25
7.26.0  :     2021-08-01,2023-08-01
7.27.0  :     2021-08-27,2023-08-27
7.28.0  :     2021-09-25,2023-09-25
7.29.0  :     2021-10-30,2023-10-30
7.30.0  :     2021-11-26,2023-11-26
7.31.0  :     2022-01-05,2024-01-05
7.32.0  :     2022-02-25,2024-02-25
7.33.0  :     2022-04-29,2024-04-28
7.34.0  :     2022-05-28,2024-05-27
8.0.0  :     2022-01-12,2024-01-12
8.1.0  :     2022-02-25,2024-02-25
8.10.0  :     2023-02-10,2025-02-09
8.11.0  :     2023-02-28,2025-02-27
8.12.0  :     2023-03-30,2025-03-29
8.13.0  :     2023-04-28,2025-04-27
8.2.0  :     2022-03-27,2024-03-26
8.3.0  :     2022-04-29,2024-04-28
8.4.0  :     2022-05-28,2024-05-27
8.5.0  :     2022-09-06,2024-09-05
8.6.0  :     2022-10-30,2024-10-29
8.7.0  :     2022-11-28,2024-11-27
8.8.0  :     2023-01-03,2025-01-02
8.9.0  :     2023-01-27,2025-01-26
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

2023 – Quarter 2 drop support for:

- 28 May 2023 drop ipython 7.24.0 (initially released on May 28, 2021)
- 20 Jun 2023 drop scipy 1.7.0 (initially released on Jun 20, 2021)
- 22 Jun 2023 drop numpy 1.21.0 (initially released on Jun 22, 2021)
- 25 Jun 2023 drop ipython 7.25.0 (initially released on Jun 25, 2021)

2023 – Quarter 3 drop support for:

- 02 Jul 2023 drop pandas 1.3.0 (initially released on Jul 02, 2021)
- 08 Jul 2023 drop networkx 2.6 (initially released on Jul 08, 2021)
- 23 Jul 2023 drop xarray 0.19.0 (initially released on Jul 23, 2021)
- 01 Aug 2023 drop ipython 7.26.0 (initially released on Aug 01, 2021)
- 27 Aug 2023 drop ipython 7.27.0 (initially released on Aug 27, 2021)
- 24 Sep 2023 drop scikit-learn 1.0 (initially released on Sep 24, 2021)
- 25 Sep 2023 drop ipython 7.28.0 (initially released on Sep 25, 2021)

2023 – Quarter 4 drop support for:

- 05 Oct 2023 drop python 3.9 (initially released on Oct 05, 2020)
- 30 Oct 2023 drop ipython 7.29.0 (initially released on Oct 30, 2021)
- 02 Nov 2023 drop xarray 0.20.0 (initially released on Nov 02, 2021)
- 16 Nov 2023 drop matplotlib 3.5.0 (initially released on Nov 16, 2021)
- 26 Nov 2023 drop ipython 7.30.0 (initially released on Nov 26, 2021)
- 03 Dec 2023 drop scikit-image 0.19.0 (initially released on Dec 03, 2021)
- 31 Dec 2023 drop numpy 1.22.0 (initially released on Dec 31, 2021)

2024 – Quarter 1 drop support for:

- 05 Jan 2024 drop ipython 7.31.0 (initially released on Jan 05, 2022)
- 12 Jan 2024 drop ipython 8.0.0 (initially released on Jan 12, 2022)
- 22 Jan 2024 drop pandas 1.4.0 (initially released on Jan 22, 2022)
- 28 Jan 2024 drop xarray 0.21.0 (initially released on Jan 28, 2022)
- 05 Feb 2024 drop scipy 1.8.0 (initially released on Feb 05, 2022)
- 25 Feb 2024 drop ipython 7.32.0 (initially released on Feb 25, 2022)
- 25 Feb 2024 drop ipython 8.1.0 (initially released on Feb 25, 2022)
- 28 Feb 2024 drop networkx 2.7 (initially released on Feb 28, 2022)
- 01 Mar 2024 drop xarray 2022.3.0 (initially released on Mar 02, 2022)
- 26 Mar 2024 drop ipython 8.2.0 (initially released on Mar 27, 2022)

2024 – Quarter 2 drop support for:

- 08 Apr 2024 drop networkx 2.8 (initially released on Apr 09, 2022)
- 28 Apr 2024 drop ipython 7.33.0 (initially released on Apr 29, 2022)
- 28 Apr 2024 drop ipython 8.3.0 (initially released on Apr 29, 2022)
- 11 May 2024 drop scikit-learn 1.1.0 (initially released on May 12, 2022)
- 27 May 2024 drop ipython 7.34.0 (initially released on May 28, 2022)
- 27 May 2024 drop ipython 8.4.0 (initially released on May 28, 2022)
- 21 Jun 2024 drop numpy 1.23.0 (initially released on Jun 22, 2022)

2024 – Quarter 3 drop support for:

- 21 Jul 2024 drop xarray 2022.6.0 (initially released on Jul 22, 2022)
- 28 Jul 2024 drop scipy 1.9.0 (initially released on Jul 29, 2022)
- 05 Sep 2024 drop ipython 8.5.0 (initially released on Sep 06, 2022)
- 15 Sep 2024 drop matplotlib 3.6.0 (initially released on Sep 16, 2022)
- 18 Sep 2024 drop pandas 1.5.0 (initially released on Sep 19, 2022)
- 28 Sep 2024 drop xarray 2022.9.0 (initially released on Sep 29, 2022)

2024 – Quarter 4 drop support for:

- 03 Oct 2024 drop python 3.10 (initially released on Oct 04, 2021)
- 12 Oct 2024 drop xarray 2022.10.0 (initially released on Oct 13, 2022)
- 29 Oct 2024 drop ipython 8.6.0 (initially released on Oct 30, 2022)
- 03 Nov 2024 drop xarray 2022.11.0 (initially released on Nov 04, 2022)
- 27 Nov 2024 drop ipython 8.7.0 (initially released on Nov 28, 2022)
- 01 Dec 2024 drop xarray 2022.12.0 (initially released on Dec 02, 2022)
- 07 Dec 2024 drop scikit-learn 1.2.0 (initially released on Dec 08, 2022)
- 17 Dec 2024 drop numpy 1.24.0 (initially released on Dec 18, 2022)

2025 – Quarter 1 drop support for:

- 02 Jan 2025 drop ipython 8.8.0 (initially released on Jan 03, 2023)
- 02 Jan 2025 drop scipy 1.10.0 (initially released on Jan 03, 2023)
- 07 Jan 2025 drop networkx 3.0 (initially released on Jan 08, 2023)
- 17 Jan 2025 drop xarray 2023.1.0 (initially released on Jan 18, 2023)
- 26 Jan 2025 drop ipython 8.9.0 (initially released on Jan 27, 2023)
- 06 Feb 2025 drop xarray 2023.2.0 (initially released on Feb 07, 2023)
- 09 Feb 2025 drop ipython 8.10.0 (initially released on Feb 10, 2023)
- 12 Feb 2025 drop matplotlib 3.7.0 (initially released on Feb 13, 2023)
- 27 Feb 2025 drop ipython 8.11.0 (initially released on Feb 28, 2023)
- 27 Feb 2025 drop scikit-image 0.20.0 (initially released on Feb 28, 2023)
- 21 Mar 2025 drop xarray 2023.3.0 (initially released on Mar 22, 2023)
- 29 Mar 2025 drop ipython 8.12.0 (initially released on Mar 30, 2023)

2025 – Quarter 2 drop support for:

- 02 Apr 2025 drop pandas 2.0.0 (initially released on Apr 03, 2023)
- 03 Apr 2025 drop networkx 3.1 (initially released on Apr 04, 2023)
- 13 Apr 2025 drop xarray 2023.4.0 (initially released on Apr 14, 2023)
- 27 Apr 2025 drop ipython 8.13.0 (initially released on Apr 28, 2023)
- 18 May 2025 drop xarray 2023.5.0 (initially released on May 19, 2023)

2025 – Quarter 4 drop support for:

- 23 Oct 2025 drop python 3.11 (initially released on Oct 24, 2022)

2026 – Quarter 4 drop support for:

- 01 Oct 2026 drop python 3.12 (initially released on Oct 02, 2023)

## Implementation

<!--
Discuss how this would be implemented.
-->

<!--
### Core Project Endorsement

Discuss what it means for a core project to endorse this SPEC.
-->
<!--

### Ecosystem Adoption

Discuss what it means for a project to adopt this SPEC.
-->

## Notes

- This document builds on [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html), which describes several alternatives including ad hoc version support, all CPython supported versions, default version on Linux distribution, N minor versions of Python, and time window from the X.Y.1 Python release.

- Code to generate support and drop schedule tables:

{{< readcode file="SPEC0_versions.py" lang="python" >}}
