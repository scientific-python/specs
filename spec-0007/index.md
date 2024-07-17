---
title: "SPEC 7 — Seeding pseudo-random number generation"
date: 2023-04-19
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Sebastian Berg <sebastianb@nvidia.com>"
  - "Pamphile Roy <roy.pamphile@gmail.com>"
  - "Matt Haberland <mhaberla@calpoly.edu>"
  - Other participants in the discussion <not.yet@named.org>"
discussion: https://github.com/scipy/scipy/issues/14322
endorsed-by:
---

## Description

Currently, libraries across the ecosystem provide various APIs for seeding random number generation.
This SPEC suggests a unified, pragmatic API, taking into account technical and historical factors.
Adopting such a uniform API will simplify the user experience, especially for those who rely on multiple projects.

We recommend:

- avoiding the use of global state and legacy bitstream generators, and
- standardizing the usage and interpretation of an `rng` keyword for seeding.

We suggest implementing these principles by:

- deprecating the use of `numpy.random.seed` to control the random state,
- deprecating the use of `random_state`/`seed` arguments in favor of a consistent `rng` argument, and
- using `numpy.random.default_rng` to validate the `rng` argument and instantiate a `Generator`.

### Scope

This is intended as a recommendation to all libraries that allow users to control the
state of a NumPy random number generator. It is specifically targeted toward functions
that allow use of `numpy.random.seed` to control the random state and accept
`RandomState` instances via an argument with a name other than `rng`, but the ideas
are more broadly applicable. Use of random number generators other than those provided
by NumPy are not considered at this time, but may be addressed in a future version.

### Concepts

- `BitGenerator`: Generates a stream of pseudo-random bits. The default generator in NumPy (`numpy.random.default_rng`) uses PCG64.
- `Generator`: Derives pseudo-random numbers from the bits produced by a `BitGenerator`.
- `RandomState`: a [legacy object in NumPy](https://numpy.org/doc/stable/reference/random/index.html), similar to `Generator`, that produces random numbers based on the Mersenne Twister.

### Constraints

NumPy, SciPy, scikit-learn, scikit-image, and NetworkX all implement pseudo-random seeding in slightly different ways.
Common keyword arguments include `random_state` and `seed`.
In practice, the seed is unfortunately also often controlled using `numpy.random.seed`.

## Implementation

Legacy behavior in packages such as scikit-learn (`sklearn.utils.check_random_state`) typically handle `None` (use the global seed state), an int (convert to `RandomState`), or `RandomState` object.

Two strong motivations for moving over to `Generator`s are:

(1) they avoid naïve seeding strategies, such as using successive integers, via the underlying [SeedSequence](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawning);
(2) they avoid using global state (from `numpy.random.mtrand._rand`).

Our recommendation here is a deprecation strategy which does not in _all_ cases adhere to the Hinsen[^hinsen] principle.

The [deprecation strategy](https://github.com/scientific-python/specs/pull/180#issuecomment-1515248009) is:

1. Accept both `rng` and `random_state`/`seed` keyword arguments.
2. If both are specified, raise an error.
3. If neither is specified and `np.random.seed` has been used to set the seed, emit a `FutureWarning` about the upcoming change in behavior.
4. If `random_state`/`seed` is passed by keyword or by position, treat it as before, but:

- Emit a `DeprecationWarning` if passed by keyword, warning about the deprecation of keyword `random_state` in favor of `rng`.
- Emit a `FutureWarning` if passed by position, warning about the change in behavior of the positional argument.

5. If `rng` is passed by keyword, standardize it using `numpy.random.default_rng`.
6. After the deprecation period, use only `rng`, validated with `numpy.random.default_rng`.
   Raise an error if `random_state`/`seed` is provided.

   By now, the function signature, with type annotations, could look like this:

   ```python
   from collections.abc import Sequence
   import numpy as np


   SeedLike = int | np.integer | Sequence[int] | np.random.SeedSequence
   RNGLike = np.random.Generator | np.random.BitGenerator


   def my_func(rng: RNGLike | SeedLike | None = None):
       """My function summary.

       Parameters
       ----------
       rng : `numpy.random.Generator`, optional
           Pseudorandom number generator state. When `rng` is None, a new
           `numpy.random.Generator` is created using entropy from the
           operating system. Types other than `numpy.random.Generator` are
           passed to `numpy.random.default_rng` to instantiate a `Generator`.
       """
       rng = np.random.default_rng(rng)

       ...

   ```

   Also note the suggested language for the `rng` parameter docstring, which encourages the user to pass a `Generator` or None, but allows for other types accepted by `numpy.random.default_rng` (captured by the type annotation).

### Impact

There are three classes of users, which will be affected to varying degrees.

1. Those who do not attempt to control the random state.
   Their code will immediately switch from using the unseeded global `RandomState` to using an unseeded `Generator`.
   Since the underlying _distributions_ of pseudo-random numbers will not change, these users will be relatively unaffected.

2. Users of `random_state`/`seed` arguments.
   Support for these arguments will be dropped eventually, but during the deprecation period, we can provide clear guidance, via warnings and documentation, on how to migrate to the new `rng` keyword.

3. Those who use `numpy.random.seed`.
   The proposal will do away with that global seeding mechanism, meaning that code that relies on it would, after the deprecation period, go from being seeded to being unseeded.
   To ensure that this does not go unnoticed, libraries that allowed for control of the random state via `numpy.random.seed` should raise a `FutureWarning` if `np.random.seed` has been called. (See Code below for an example.)
   In response, users must switch from using `numpy.random.seed` to passing the `rng` argument explicitly to all functions that accept it.

[^hinsen]: The Hinsen principle states, loosely, that code should, whether executed now or in the future, return the same result, or raise an error.

### Code

As an example, consider how a SciPy function would transition from a `random_state` parameter to an `rng` parameter using a decorator.

{{< include-code "transition_to_rng.py" "python" >}}

### Core Project Endorsement

Endorsement of this SPEC means that a project intends to:

- avoid the use of global state and legacy bitstream generators, and
- standardize the usage and interpretation of an `rng` keyword for seeding.

### Ecosystem Adoption

To adopt this SPEC, a project should:

- deprecate the use of `numpy.random.seed` to control the random state,
- deprecate the use of `random_state`/`seed` arguments in favor of an `rng` argument in all functions that require random number generation, and
- use `numpy.random.default_rng` to validate the `rng` argument and instantiate a `Generator`.

## Notes
