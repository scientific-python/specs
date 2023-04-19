---
title: "SPEC 7 — Seeding pseudo-random number generation"
date: 2023-04-19
author:
  - Other participants in the discussion <not.yet@named.org>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
discussion: https://github.com/scipy/scipy/issues/14322
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

There is disparity in the APIs libraries use to seed random number generation.
The goal of this SPEC is suggest a single, pragmatic API for the ecosystem, taking into account technical and historical factors.

### Concepts

- `BitGenerator`: Generates a stream of pseudo-random bits. The default generator in NumPy (`np.random.default_rng`) uses PCG64.
- `Generator`: Derives pseudo-random numbers from the bits produced by a `BitGenerator`.
- `RandomState`: a [legacy object in NumPy](https://numpy.org/doc/stable/reference/random/index.html), similar to `Generator`, that produces random numbers based on the Mersenne Twister.

### Constraints

NumPy, SciPy, scikit-learn, scikit-image, and NetworkX all implement pseudo-random seeding in slightly different ways.
Common keyword arguments include `random_state` and `seed`.
In practice, the seed is unfortunately also often controlled using `np.random.seed`.

## Implementation

<!--
Discuss how this would be implemented.
-->

The new API takes into account legacy behavior in packages such as scikit-learn (see `sklearn.utils.check_random_state`), which works as follows:

1. Because `np.random.seed` is so often used in practice, no seed means
   using the global `RandomState` object, `np.random.mtrand._rand`.
2. (Option a) When a seed is provided, a `RandomState` object is initialized with that seed.
3. (Option b) When a seed is provided, a `Generator` object is initialized with that seed.
4. If an instance of `RandomState` is provided, it is used as-is.
5. If an instance of `Generator` is provided, it is used as-is.

Option a:

Since the `random_state` keyword is so widely established, we recommend continuing its usage, but with the addition of accepting `Generator` instances.

Option b:

Despite the `random_state` keyword being so widely established, we recommend changing its behavior to seed using the new `Generator` interface.
(Very likely an unworkable option, since it will change numerical results.)

Option b(2):

Because the `random_state` keyword is so widely established, and presumes seeding via `RandomState`, we recommend using a new keyword argument, namely `rng`.
If `rng=None`, the global `np.random.seed` behavior is still followed.
Otherwise, a `Generator` is initialized from the given seed.

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
