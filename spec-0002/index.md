---
title: "SPEC 2 — API Dispatch"
number: 2
date: 2021-12-16
author:
  - "Jarrod Millman <millman@berkeley.edu>"
discussion:
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the recommendation.
-->

We propose mechanisms for wholesale reimplementations of library functions.
This would allow groups outside of, say, `networkx` to (a) provide new
functions to replace parts of `networkx`, or (b) provide data structures
that can pass through NetworkX's existing computational pipelines.

This SPEC focuses on the rationale for these mechanisms, and provides
links to implementations related technical discussions.

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

A successful prototype implementation of this SPEC (at least in spirit) is already
available [inside NetworkX](https://networkx.org/documentation/latest/reference/utils.html#backends).

NetworkX has developed a dispatching layer which can plug into multiple backends.
Currently we have backends which can dispatch to
[CuGraph](https://github.com/rapidsai/cugraph/tree/branch-24.04/python/nx-cugraph),
[GraphBLAS](https://github.com/python-graphblas/graphblas-algorithms) and a
[joblib bpacked parallel
implementation](https://github.com/networkx/nx-parallel) of algorithms in
NetworkX.

One of the goals here is to provide drop in replacement for old code written with NetworkX. Users
should be able to set a config option/env variable and dispatch their code to different backends.
These backends could be hardware specific ones, reimplementations in other languages (hello rust!) or
using a totally new data structure (GraphBLAS in the case of NetworkX).

On the NetworkX side we are still ironing out more details, and we are still missing out on a detailed
spec (or SPEC). I think other projects in the scientific python ecosystem could also benefit from some
kind of dispatching along these lines. There is some progress towards creating an [engine API in
scikit-learn](https://github.com/scikit-learn/scikit-learn/pull/25535) which follows similar rational.

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
