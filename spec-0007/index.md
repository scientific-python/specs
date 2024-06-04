---
title: "SPEC 7 — Seeding pseudo-random number generation"
date: 2023-04-19
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Sebastian Berg <sebastianb@nvidia.com>"
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

1. Those who use `np.random.seed`. The proposal will do away with that global seeding mechanism, meaning that code that relies on it will, after a certain deprecation period, start seeing a different stream of random numbers than before. To ensure that this does not go unnoticed, the library will raise a `FutureWarning` if `np.random.seed` was called earlier.

   Such code will, in effect, go from being seeded to being unseeded.
   To avoid that from happening, the code will have to be modified to pass in explicitly an `rng` argument on each function call.

2. Those who do not seed. Their code will, after the deprecation period, use the newly proposed default. Since they were already not requesting repeatable sequences, and since the underlying _distributions_ of pseudo-random numbers did not change, they should be unaffected.

3. Users of `random_state=...`. Support for the `random_state` argument may be dropped eventually, but meanwhile we can provide clear guidance, via deprecation warnings and documentation, on how to migrate to the new `rng` keyword.

[^hinsen]: The Hinsen principle states, loosely, that code should, whether executed now or in the future, return the same result, or raise an error.

### Code

For example, SciPy may implement this with the following decorator to support both names.
This is implemented using:
1. A `check_random_state` function which normalizes the either old or new input to a `Generator` or `RandomState` object.
   This function only gives a `FutureWarning` when users (probably) NumPy's global legacy `RandomState`.  As noted in point 1. above.
2. A decorator to deal with the rename changes.  In future versions this will deprecate the old keyword.  At this time, it will ensure that the documentation and auto-completion only shows the new parameter name.
   Delaying the deprecation ensures that downstream users can switch to `rng=` on all supported SciPy versions when the deprecation happens.

```python
_NoValue = object()  # singleton to indicate not explicitly passed


def check_random_state(seed=_NoValue, rng=_NoValue):
    if rng is not _NoValue and seed is not _NoValue:
        raise TypeError("cannot pass both `rng=` and `random_state=` at the same time.")
    if rng is not _NoValue:
        return np.random.default_rng(rng)

    if seed is _NoValue:
        # If the user passed nothing, we have to reach into NumPy here:
        # 1. If np.random.seed(None) was called (or never called), then we can
        #    just use the default_rng (the result is random anyway).
        # 2. If it was called, we must return the global random state object
        #    and warn about future ignoring of seed!
        if np.random.mtrand._rand._bit_generator._seed_seq is not None:
            # The user did not seed, so no need to warn.
            return np.random.default_rng()
        warnings.warn(
            "The NumPy global rng was seeded in call to np.random.seed() "
            "in the future this function will ignore this seed and return "
            "random values as if a new `np.random.default_rng()` was created.",
            FutureWarning, stacklevel=5)
        return np.random.mtrand._rand
    if seed is None or seed is np.random:
        return np.random.mtrand._rand
    if isinstance(seed, (numbers.Integral, np.integer)):
        return np.random.RandomState(seed)
    if isinstance(seed, (np.random.RandomState, np.random.Generator)):
        return seed

    raise ValueError(f"'{seed}' cannot be used to seed a numpy.random.RandomState"
                     " instance")


def _prepare_rng(old_name, dep_version=None):
    new_name = "rng"

    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            if old_name in kwargs:
                if dep_version:
                    end_version = dep_version.split('.')
                    end_version[1] = str(int(end_version[1]) + 2)
                    end_version = '.'.join(end_version)
                    message = (f"Use of keyword argument `{old_name}` is "
                               f"deprecated and replaced by `{new_name}`.  "
                               f"Support for `{old_name}` will be removed "
                               f"in SciPy {end_version}.")
                    warnings.warn(message, DeprecationWarning, stacklevel=2)
                if new_name in kwargs:
                    message = (f"{fun.__name__}() got multiple values for "
                               f"argument now known as `{new_name}`")
                    raise TypeError(message)

            kwargs[new_name] = check_random_state(
                kwargs.pop(old_name, _NoValue),
                rng=kwargs.pop(new_name, _NoValue)
            )
            return fun(*args, **kwargs)
        return wrapper
    return decorator


@_prepare_rng("random_state")
def library_function(/, rng=None):
    # The decorated library function takes an `rng` argument which is
    # guaranteed to be a either a Generator or a RandomState.
    # `random_state=` is supported input (the old can be customized).
    assert isinstance(rng, (np.random.Generator, np.random.RandomState))
```

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
