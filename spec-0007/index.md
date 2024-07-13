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

- deprecating the use of `RandomState` and `numpy.random.seed`,
- accepting an `rng` argument in all functions that require random number generation, and
- using `numpy.random.default_rng` to validate the `rng` argument and instantiate a `Generator`.

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
2. If `rng=None`, handle `random_state`/`seed` as in legacy behavior (see above), except use a compatible Generator instead of RandomState.
   A DeprecationWarning is raised to warn about a future change in behavior.
3. After <X time>, use only `rng` validated with `numpy.random.default_rng`.
   Raise an error if `random_state`/`seed` is provided.
4. At a time of the library's choosing, remove any machinery related to `random_state`/`seed`.

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

   Also note the suggested language for the `rng` parameter docstring, which encourages the user to pass a `Generator` or None, but allows for other types accepted by `numpy.random.default_rng`.

### Impact

The following users will be affected:

1. Those who use `numpy.random.seed`. 
   The proposal will do away with that global seeding mechanism, meaning that code that relies on it will, after a certain deprecation period, start seeing a different stream of random numbers than before.
   To ensure that this does not go unnoticed, the library should raise a `FutureWarning` if `np.random.seed` has been called. (See Code below for an example.)

   Such code will, in effect, go from being seeded to being unseeded. 
   To prevent this, users must switch from using `numpy.random.seed` to passing the `rng` argument explicitly to all functions that accept it.

2. Those who do not seed. Their code will, after the deprecation period, use the newly proposed default. Since they were already not requesting repeatable sequences, and since the underlying _distributions_ of pseudo-random numbers did not change, they should be unaffected.

3. Users of `random_state`/`seed` arguments. 
   Support for these arguments will be dropped eventually, but during the deprecation period, we can provide clear guidance, via warnings and documentation, on how to migrate to the new `rng` keyword.

[^hinsen]: The Hinsen principle states, loosely, that code should, whether executed now or in the future, return the same result, or raise an error.

### Code

As an example, consider how a SciPy function would transition from a `seed` parameter to the `rng` keyword using a decorator.
This is implemented using:

1. A `check_random_state` function which normalizes either old (`seed`) or new (`rng`) input to a `Generator` object.
   If `np.random.seed()` was called, and neither `seed` nor `rng` is given, a `FutureWarning` is raised to let the user know that they _tried_ to set the seed but that it had no effect.
2. A decorator to handle renaming the `seed` keyword to `rng`.
   At a given future version, the decorator deprecates the keyword-only parameter `seed`; for now, it provides the new `rng` keyword, so users can start switching in preparation.
   It changes the documentation and auto-completion to only advertise the new `rng` parameter.

```python
import numpy as np
import functools
import numbers
import warnings

_NoValue = object()  # singleton to indicate not explicitly passed

# Should this specify the version number in which the behavior will change?
def _check_random_state(seed=_NoValue, rng=_NoValue):
    """ PRNG validator during deprecation period
    
    Accepts inputs specified via old `seed` (or `random_state`) arguments
    or new `rng` argument and returns appropriate PRNG.
    
    Once the removal of `seed`/`random_state` argument is executed,
    this function may be removed, and `numpy.random.default_rng` may be
    used to validate the `rng` argument.
    
    Parameters
    ----------
    seed : <insert long list of objects here>
        Input specified via old `seed` (or `random_state`) argument
    rng :  <insert long list of objects here>
        Input specified via old `seed` (or `random_state`) argument
    Returns
    -------
    prng : NumPy `Generator` or `RandomState`
        Pseudo-random number generator
    """
    if rng is not _NoValue and seed is not _NoValue:
        raise TypeError("Cannot pass both `rng` and `seed` (or `random_state`).")
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
                     " instance.")


def _prepare_rng(old_name, position_num=None, dep_version=None):
    """ Example decorator to deprecate old PRNG usage

    Parameters
    ----------
    old_name : str
        The old name of the PRNG argument (e.g. `seed` or `random_state`).
    position_num : int, optional
        The (0-indexed) position of the old PRNG argument (if accepted by position).
        Maintainers are welcome to eliminate this argument and use, for example,
        `inspect`, if preferred.
    dep_version : str, optional
        The full version number of the library in which positional and kwarg use
        of the old PRNG argument was deprecated. If specified, `DeprecationWarning`s
        will be emitted.

    """
    new_name = "rng"

    if dep_version:
        end_version = dep_version.split('.')
        end_version[1] = str(int(end_version[1]) + 2)
        end_version = '.'.join(end_version)

    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            # Determine how PRNG was passed
            as_old_kwarg = old_name in kwargs
            as_new_kwarg = new_name in kwargs
            as_pos_arg = position_num is not None and len(args) >= position_num + 1
            
            # Can only specify PRNG one way
            if int(as_old_kwarg) + int(as_new_kwarg) + int(as_pos_arg) > 1:
                message = (f"{fun.__name__}() got multiple values for "
                           f"argument now known as `{new_name}`")
                raise TypeError(message)
            
            if as_old_kwarg:  # warn about deprecated use of old kwarg
                kwargs[new_name] = _check_random_state(seed=kwargs.pop(old_name))
                if dep_version:
                    message = (f"Use of keyword argument `{old_name}` is "
                               f"deprecated and replaced by `{new_name}`.  "
                               f"Support for `{old_name}` will be removed "
                               f"in SciPy {end_version}.")
                    warnings.warn(message, DeprecationWarning, stacklevel=2)

            elif as_pos_arg:  # warn about deprecated positional use
                # Not required for adoption of this SPEC; feel free to remove
                args = list(args)
                args[position_num] = _check_random_state(seed=args[position_num])
                if dep_version:
                    message = (f"Positional use of argument `{old_name}` and "
                               "those that follow is deprecated and will cause "
                               f"an error in SciPy {end_version}. Replace these "
                               f"with keyword arguments, and use `{new_name}` "
                               f"instead of `{old_name}`.")
                    warnings.warn(message, DeprecationWarning, stacklevel=2)

            elif as_new_kwarg:  # no warnings; this is the preferred use
                kwargs[new_name] = _check_random_state(rng=kwargs[new_name])

            else:  # will emit FutureWarning if `np.random.seed` was used
                kwargs[new_name] = _check_random_state()

            return fun(*args, **kwargs)
        return wrapper
    return decorator


# Example usage of _prepare_rng decorator
@_prepare_rng("random_state", 1, "1.15.0")
def library_function(arg1, rng=None, arg2=None):
    # The decorated library function accepts an `rng` argument, but the user
    # can also pass a `random_state` argument (as specified by `old_name`) or
    # a positional argument (with position specified by `position_name`). In
    # any case, the argument passed to `library_function` will be either a
    # Generator or a RandomState after validation by the decorator.
    assert isinstance(rng, (np.random.Generator, np.random.RandomState))
    print((arg1, rng.random(), arg2))
```

### Core Project Endorsement

Endorsement of this SPEC means that a project intends to:

- avoid the use of global state and legacy bitstream generators, and
- standardize the usage and interpretation of an `rng` keyword for seeding.

### Ecosystem Adoption

To adot this SPEC, a project should:

- deprecate the use of `RandomState` and `numpy.random.seed`,
- accept an `rng` argument in all functions that require random number generation, and
- use `numpy.random.default_rng` to validate the `rng` argument and instantiate a `Generator`.

## Notes


