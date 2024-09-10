---
title: "SPEC 2 — API Dispatch"
number: 2
date: 2021-12-16
author:
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Aditi Juneja <aditijuneja7@gmail.com>"
discussion:
is-draft: true
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the recommendation.
-->

This SPEC (Scientific Python Ecosystem Coordination) recommendation for API dispatching is designed to enhance interoperability and performance within the scientific Python ecosystem, leveraging the capabilities of [Python `entry_points`](https://packaging.python.org/en/latest/specifications/entry-points/).

This recommendation presents a systematic approach that enables users to redirect function calls to alternative computation backends seamlessly. This flexibility allows users to take advantage of optimized implementations simply by configuring an environment variable or adding an additional keyword argument (more on this later), rather than having to learn a new API's interface, which might not be very "python-user"-friendly. Such adaptability facilitates the integration of hardware-specific optimizations, reimplementations in other programming languages (such as C or Rust), and the utilization of entirely new data structures.

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

A successful prototype implementation of this SPEC is already integrated into [NetworkX](https://github.com/networkx/networkx), embodying its core principles. NetworkX has established a flexible dispatching layer capable of interfacing with multiple computational backends. Currently, this includes backends that facilitate dispatching to [CuGraph](https://github.com/rapidsai/cugraph/tree/branch-24.04/python/nx-cugraph), [GraphBLAS](https://github.com/python-graphblas/graphblas-algorithms), to parallel implementations in [nx-parallel](https://github.com/networkx/nx-parallel) and to the recently added backend [nx-pandas](https://github.com/networkx/nx-pandas).

### Overview : API dispatching in NetworkX

1.  Utilization of Python `entry_point`
    The `entry_point` mechanism serves as a crucial component for backend discovery and integration. By registering backends through the `networkx.backends` `entry_point` in a package's metadata, developers can enable NetworkX to recognize and utilize these backends without requiring explicit imports. Example Registration:

        [project.entry-points."networkx.backends"]
        your_backend_name = "your_dispatcher_class"

2.  Backend Requirements
    To ensure that a backend is compatible with NetworkX, it must adhere to specific structural requirements:

    1. The backend must implement a class that behaves like the `nx.Graph` object, including an attribute `__networkx_backend__` that identifies the backend.

    2. The backend should provide `convert_from_nx` and `convert_to_nx` methods to facilitate the conversion between NetworkX graphs and the backend's graph representation.

3.  Testing the backend
    To ensure that the backend complies with the main NetworkX's API, developers are encouraged to run the NetworkX test suite on their custom backend. Testing Setup:

        NETWORKX_TEST_BACKEND=<your_backend_name>
        pytest --pyargs networkx

4.  Currently, the following ways exist in NetworkX to dispatch a function call to a backend:

    1. Type-based dispatching
       ```py
       H = nx_parallel.ParallelGraph(G)
       nx.betweenness_centrality(H)
       ```
    2. Using a `backend` kwarg
       ```py
       nx.betweenness_centrality(G, backend=”parallel”)
       ```
    3. Environment variable
       ```sh
       export NETWORKX_AUTOMATIC_BACKENDS=parallel && python nx_code.py
       ```
    4. [WIP] Specifying backend as a config parameter (ref. [PR#7485](https://github.com/networkx/networkx/pull/7485))
       ```py
       with nx.config(backend=”parallel”):
           nx.betweenness_centrality(G)
       ```

For more, read the [NetworkX's Backend and Config docs](https://networkx.org/documentation/latest/reference/backends.html)!

### Interesting discussions happening in:

- [`spatch`](https://github.com/scientific-python/spatch) repository
- ["Requirements and discussion of a type dispatcher for the ecosystem"](https://discuss.scientific-python.org/t/requirements-and-discussion-of-a-type-dispatcher-for-the-ecosystem/157) discussion
- [Scientific Python Discourse - SPEC 2](https://discuss.scientific-python.org/t/spec-2-api-dispatch/173)

### Projects developing a Python `entry_points` based backend dispatching:

- networkx : [Backend and Config docs](https://networkx.org/documentation/latest/reference/backends.html)
- scikit-image : [PR#7466](https://github.com/scikit-image/scikit-image/pull/7466)
- scikit-learn : [PR#25535](https://github.com/scikit-learn/scikit-learn/pull/25535)

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
