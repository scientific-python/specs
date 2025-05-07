---
title: "SPEC 7 — Seeding Pseudo-Random Number Generation"
number: 7
date: 2023-04-19
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Sebastian Berg <sebastianb@nvidia.com>"
  - "Pamphile Roy <roy.pamphile@gmail.com>"
  - "Matt Haberland <mhaberla@calpoly.edu>"
endorsed-by:
  - ipython
  - numpy
  - scikit-image
  - scipy
---

## Description

Currently, libraries across the ecosystem provide various APIs for seeding pseudo-random number generation.
This SPEC suggests a unified, pragmatic API, taking into account technical and historical factors.
Adopting such a uniform API will simplify the user experience, especially for those who rely on multiple projects.

We recommend:

- standardizing the usage and interpretation of an `rng` keyword for seeding, and
- avoiding the use of global state and legacy bitstream generators.

We suggest implementing these principles by:

- deprecating uses of an existing seed argument (commonly `random_state` or `seed`) in favor of a consistent `rng` argument,
- using `numpy.random.default_rng` to normalize the `rng` argument and instantiate a `Generator`[^no-RandomState], and
- deprecating the use of `numpy.random.seed` to control the random state.

We are primarily concerned with API uniformity, but also encourage libraries to move towards using [NumPy pseudo-random `Generator`s](https://numpy.org/doc/stable/reference/random/generator.html) because:

1. `Generator`s avoid problems associated with naïve seeding (e.g., using successive integers), via its [SeedSequence](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawning) mechanism;
2. their use avoids relying on global state—which can make code execution harder to track, and may cause problems in parallel processing scenarios.

[^no-RandomState]:
    Note that in NumPy versions prior to 2.2.0, `numpy.random.default_rng` does not accept instances of `RandomState`.
    In more recent versions, `numpy.random.default_rng` will convert `RandomState` instances to `Generator`s, which may not behave identically even with identical method calls.
    That said, neither `np.random.seed` nor `np.random.RandomState` _themselves_ are deprecated, so they may still be used directly in some contexts (e.g. by developers for generating unit test data).

### Scope

This is intended as a recommendation to all libraries that allow users to control the state of a NumPy random number generator.
It is specifically targeted toward functions that currently accept random number seeds using an argument other than `rng`, rely on the particular behavior of `RandomState` methods, or allow `numpy.random.seed` to control the random state, but the ideas are more broadly applicable.
Random number generators other than those provided by NumPy could also be accommodated by an `rng` keyword, but that is beyond the scope of this SPEC.

### Concepts

- `BitGenerator`: Generates a stream of pseudo-random bits. The default generator in NumPy (`numpy.random.default_rng`) uses PCG64.
- `Generator`: Derives pseudo-random numbers from the bits produced by a `BitGenerator`.
- `RandomState`: a [legacy object in NumPy](https://numpy.org/doc/stable/reference/random/index.html), similar to `Generator`, that produces random numbers based on the Mersenne Twister.

### Constraints

NumPy, SciPy, scikit-learn, scikit-image, and NetworkX all implement pseudo-random seeding in slightly different ways.
Common keyword arguments include `random_state` and `seed`.
In practice, the seed is also often controllable using `numpy.random.seed`.

### Core Project Endorsement

Endorsement of this SPEC means that a project considers the standardization and interpretation of the `rng` keyword, as well as avoiding use of global state and legacy bitstream generators, good ideas that are worth implemented widely.

### Ecosystem Adoption

To adopt this SPEC, a project should:

- deprecate the use of `random_state`/`seed` arguments in favor of an `rng` argument in all functions where users need to control pseudo-random number generation,
- use `numpy.random.default_rng` to normalize the `rng` argument and instantiate a `Generator`, and
- deprecate the use of `numpy.random.seed` to control the random state.

#### Badges

Projects can highlight their adoption of this SPEC by including a SPEC badge.
{{< spec_badge number="7" title="Seeding pseudo-random number generation" >}}
To indicate adoption of multiple SPECS with one badge, see [this](../purpose-and-process/#badges).

## Implementation

Legacy behavior in packages such as scikit-learn (`sklearn.utils.check_random_state`) typically handle `None` (use the global seed state), an int (convert to `RandomState`), or `RandomState` object.

Our recommendation here is a deprecation strategy which does not in _all_ cases adhere to the Hinsen principle[^hinsen],
although it could very nearly do so by enforcing the use of `rng` as a keyword argument.

[^hinsen]: The Hinsen principle states, loosely, that code should, whether executed now or in the future, return the same result, or raise an error.

The [deprecation strategy](https://github.com/scientific-python/specs/pull/180#issuecomment-1515248009) is as follows.

**Initially**, accept both `rng` and the existing `random_state`/`seed`/`...` keyword arguments.

- If both are specified by the user, raise an error.
- If `rng` is passed by keyword, normalize it with `np.random.default_rng()` and use it to generate random numbers as needed.
- If `random_state`/`seed`/`...` is specified (by keyword or position, if allowed), preserve existing behavior.

**After `rng` becomes available** in all releases within the support window suggested by SPEC 0, emit warnings as follows:

- If neither `rng` nor `random_state`/`seed`/`...` is specified and `np.random.seed` has been used to set the seed, emit a `FutureWarning` about the upcoming change in behavior.
- If `random_state`/`seed`/`...` is passed by keyword or by position, treat it as before, but:

  - Emit a `DeprecationWarning` if passed by keyword, warning about the deprecation of keyword `random_state` in favor of `rng`.
  - Emit a `FutureWarning` if passed by position, warning about the change in behavior of the positional argument.

**After the deprecation period**, accept only `rng`, raising an error if `random_state`/`seed`/`...` is provided.

By now, the function signature, with type annotations, could look like this:

```python
from collections.abc import Sequence
import numpy as np


SeedLike = int | np.integer | Sequence[int] | np.random.SeedSequence
RNGLike = np.random.Generator | np.random.BitGenerator


def my_func(*, rng: RNGLike | SeedLike | None = None):
    """My function summary.

    Parameters
    ----------
    rng : `numpy.random.Generator`, optional
        Pseudorandom number generator state. When `rng` is None, a new
        `numpy.random.Generator` is created using entropy from the
        operating system. Types other than `numpy.random.Generator` are
        passed to `numpy.random.default_rng` to instantiate a ``Generator``.
    """
    rng = np.random.default_rng(rng)

    ...

```

Also note the suggested language for the `rng` parameter docstring, which encourages the user to pass a `Generator` or `None`, but allows for other types accepted by `numpy.random.default_rng` (captured by the type annotation).

### Impact

There are three classes of users, which will be affected to varying degrees.

1. Those who do not attempt to control the random state.
   Their code will switch from using the unseeded global `RandomState` to using an unseeded `Generator`.
   Since the underlying _distributions_ of pseudo-random numbers will not change, these users should be largely unaffected.
   While _technically_ this change does not adhere to the Hinsen principle, its impact should be minimal.

2. Users of `random_state`/`seed` arguments.
   Support for these arguments will be dropped eventually, but during the deprecation period, we can provide clear guidance, via warnings and documentation, on how to migrate to the new `rng` keyword.

3. Those who use `numpy.random.seed`.
   The proposal will do away with that global seeding mechanism, meaning that code that relies on it would, after the deprecation period, go from being seeded to being unseeded.
   To ensure that this does not go unnoticed, libraries that allowed for control of the random state via `numpy.random.seed` should raise a `FutureWarning` if `np.random.seed` has been called. (See [Code](#code) below for an example.)
   To fully adhere to the Hinsen principle, these warnings should instead be raised as errors.
   In response, users will have to switch from using `numpy.random.seed` to passing the `rng` argument explicitly to all functions that accept it.

### Code

As an example, consider how a SciPy function would transition from a `random_state` parameter to an `rng` parameter using a decorator.

{{< include-code "transition_to_rng.py" "python" >}}

## Notes
