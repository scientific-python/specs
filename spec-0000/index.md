---
title: "SPEC 0 — Minimum Supported Dependencies"
number: 0
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
endorsed-by:
  - ipython
  - matplotlib
  - networkx
  - numpy
  - scikit-image
  - scipy
  - xarray
  - zarr
---

## Description

This SPEC recommends that all projects across the Scientific Python ecosystem adopt a common time-based policy for dropping dependencies. From the perspective of this SPEC, the dependencies in question are core packages as well as older Python versions.

All versions refer to feature releases (i.e., Python 3.8.0, NumPy 1.19.0; not Python 3.8.1, NumPy 1.19.2).

Specifically, we recommend that:

1. Support for Python versions be dropped **3 years** after their initial release.
2. Support for core package dependencies be dropped **2 years** after their initial release.

{{< admonition note >}}
Core packages may or may not decide to provide bug fix releases during the full 2 year period after release.
Therefore, projects may occasionally want to drop support for core package dependencies earlier than recommended by this SPEC.
For instance, if a newer minimum version of a core package is needed by a project due to a critical bug fix,
which is not backported to older versions.
{{< /admonition >}}

### Core Project Endorsement

<!--
Briefly discuss what it means for a core project to endorse this SPEC.
-->

Core project endorsing this SPEC means that those projects encourage all projects across the Scientific Python ecosystem
to limit how long they support older Python versions and older dependency versions.
A core project endorsing this SPEC does **not** imply that that project will provide bug-fix releases for two full years after a release.

### Ecosystem Adoption

<!--
Briefly discuss what it means for a project to adopt this SPEC.
-->

#### Badges

Projects can highlight their adoption of this SPEC by including a SPEC badge.
{{< spec_badge number="0" title="Minimum Supported Dependencies" >}}
To indicate adoption of multiple SPECS with one badge, see [this](../purpose-and-process/#badges).

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

```mermaid
{{< include-raw "chart.md" >}}
```

### Drop Schedule

Below is an auto generated schedule with recommended dates for dropping support. We suggest that the next release in a given quarter is
considered as the one removing support for a given item.

You may want to delay the removal of support of an older Python version until your package fully works on the newly released Python, thus keeping the number of supported minor versions of Python the same for your package.

{{< include-md "schedule.md" >}}

### Automatically updating dependencies

To help projects stay compliant with this spec, we additionally provide a `schedule.json` file that can be used by CI systems to deterime new version boundaries. The structure of the file is as follows:

```json
[
  {
    "start_date": "iso8601_timestamp",
    "packages": {
      "package_name": "version"
    }
  }
]
```

All information in the json file is in a string format that should be easy to use. The date is the first timestamp of the relevant quarter. Thus a workflow for using this file could be:

1. fetch `schedule.json`
2. determine maximum date that is smaller than current date
3. update packages listed with new minimum versions

You can obtain the new versions you should set by using this `jq` expression:

```sh

jq 'map(select(.start_date |fromdateiso8601 |tonumber  < now))| sort_by("start_date") | reverse | .[0].packages ' schedule.json

```

If you use a package manager like pixi you could update the dependencies with a bash script like this:

```sh

curl -Ls -o schedule.json https://raw.githubusercontent.com/scientific-python/specs/main/spec-0000/schedule.json
for line in $(jq 'map(select(.start_date |fromdateiso8601 |tonumber  < now))| sort_by("start_date") | reverse | .[0].packages | to_entries | map(.key + ":" + .value)[]' --raw-output schedule.json); do
	package=$(echo "$line" | cut -d ':' -f 1)
	version=$(echo "$line" | cut -d ':' -f 2)
	pixi add "$package>=$version"

done

```

## Notes

- This document builds on [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html), which describes several alternatives including ad hoc version support, all CPython supported versions, default version on Linux distribution, N minor versions of Python, and time window from the X.Y.1 Python release.

- Code to generate support and drop schedule tables:

{{< include-code "SPEC0_versions.py" "python" >}}
