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

Legacy behavior in packages such as scikit-learn (`sklearn.utils.check_random_state`) typically handle `None` (use the global seed state), an int (convert to `RandomState`), or `RandomState` object.

Two strong motivations for moving over to `Generator`s are:

(1) it avoids naïve seeding strategies, such as using successive integers, via the underlying [SeedSequence](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawning);
(2) it avoids using global state for seeding.

Our recommendation here is a deprecation strategy which does not in _all_ cases adhere to the Hinsen[^hinsen] principle. Specifically, behavior will change over a long period of time in the case where no seed is specified. I.e., the output of `library_func()` will change, since the underlying PRNG used will be different.

The [deprecation strategy](https://github.com/scientific-python/specs/pull/180#issuecomment-1515248009) is:

1. Accept both `rng` and `random_state` keyword arguments.
2. If `rng=None`, handle `random_state` as in legacy behavior (see above), except use a compatible Generator instead of RandomState.
   A DeprecationWarning is raised to warn about a future change in behavior.
3. After <X time>, use only `rng`, seeding with `default_rng(rng)`.
   Raise an error if `random_state` is provided.
4. At a time of the lirbrary's choosing, remove any machinery related to `random_state`.

[^hinsen]: The Hinsen principle states, loosely, that code should, whether executed now or in the future, return the same result, or raise an error.

TODO: Add example `check_random_state` implementation.

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
