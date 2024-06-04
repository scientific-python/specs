---
title: "SPEC 7 — Seeding pseudo-random number generation"
date: 2023-04-19
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - Other participants in the discussion <not.yet@named.org>"
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

There is disparity in the APIs libraries provide to seed random number generation.
This SPEC suggests a single, pragmatic API for the ecosystem, taking into account technical and historical factors.
Adopting such a uniform API will simplify the user experience, especially for those who rely on multiple projects.

Specifically, we recommend to:

- Deprecate the use of `RandomState` and `np.random.seed`.
- Standardize usage and interpretation of an `rng` keyword for seeding.

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

(1) they avoid naïve seeding strategies, such as using successive integers, via the underlying [SeedSequence](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawning);
(2) they avoid using global state (from `np.random.mtrand._rand`).

Our recommendation here is a deprecation strategy which does not in _all_ cases adhere to the Hinsen[^hinsen] principle.

The [deprecation strategy](https://github.com/scientific-python/specs/pull/180#issuecomment-1515248009) is:

1. Accept both `rng` and `random_state` keyword arguments.
2. If `rng=None`, handle `random_state` as in legacy behavior (see above), except use a compatible Generator instead of RandomState.
   A DeprecationWarning is raised to warn about a future change in behavior.
3. After <X time>, use only `rng`, seeding with `default_rng(rng)`.
   Raise an error if `random_state` is provided.
4. At a time of the library's choosing, remove any machinery related to `random_state`.

### Impact

The following users will be affected:

1. Those who use `np.random.seed`. The proposal will do away with that global seeding mechanism, meaning that code that relies on it will, after a certain deprecation period, start seeing a different stream of random numbers than before. To ensure that this does not go unnoticed, NumPy will raise a `FutureWarning` when `np.random.seed` is called.

   Such code will, in effect, go from being seeded to being unseeded.
   To avoid that from happening, the code will have to be modified to pass in explicitly an `rng` argument on each function call.

2. Those who do not seed. Their code will, after the deprecation period, use the newly proposed default. Since they were already not requesting repeatable sequences, and since the underlying _distributions_ of pseudo-random numbers did not change, they should be unaffected.

3. Users of `random_state=...`. Support for the `random_state` argument may be dropped eventually, but meanwhile we can provide clear guidance, via deprecation warnings and documentation, on how to migrate to the new `rng` keyword.

[^hinsen]: The Hinsen principle states, loosely, that code should, whether executed now or in the future, return the same result, or raise an error.

### Code

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
