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

   Also note the suggested language for the `rng` parameter docstring, which encourages the user to pass a `Generator` or None, but allows for other types accepted by `numpy.random.default_rng`.

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

```python
import numpy as np
import functools
import warnings

def _transition_to_rng(old_name, position_num=None, dep_version=None):
    """ Example decorator to transition from old PRNG usage to new `rng` behavior

    Suppose the decorator is applied to a function that used to accept parameter
    `old_name='random_state'` either by keyword or as a positional argument at
    `position_name=1`. At the time of application, the name of the argument in the
    function signature is manually changed to the new name, `rng`.

    - If the function is called with both `random_state` and `rng`, the decorator
      raises an error.
    - If `random_state` is provided as a keyword argument, the decorator passes
      `random_state` to the function's `rng` argument as a keyword, but the decorator
      will emit a `DeprecationWarning` about the deprecation of keyword `random_state`.
    - If `random_state` is provided as a positional argument, the decorator passes
      `random_state` to the function's `rng` argument by position, but the decorator
      will emit a `FutureWarning` about the changing behavior of the argument.
    - If `rng` is provided as a keyword argument, the decorator validates `rng` using
      `numpy.random.default_rng` before passing it to the function.
    - If neither `random_state` nor `rng` is provided, the decorator checks whether
      `np.random.seed` has been used to set the global seed. If so, it emits a
      `FutureWarning` against use of `numpy.random.seed`. Either way, the decorator
      calls the function without explicitly passing the `rng` argument.

    To avoid warnings, a user must pass `rng` as a keyword or pass a `Generator`
    object or `None` by position.

    After the deprecation period, the decorator can be removed, and the function
    can begin to validate the `rng` argument by calling `np.random.default_rng(rng)`
    internally.

    Parameters
    ----------
    old_name : str
        The old name of the PRNG argument (e.g. `seed` or `random_state`).
    position_num : int, optional
        The (0-indexed) position of the old PRNG argument (if accepted by position).
        Maintainers are welcome to eliminate this argument and use, for example,
        `inspect`, if preferred.
    dep_version : str, optional
        The full version number of the library in which warnings about use of the
        old PRNG argument begin to be emitted. The version in which the behavior
        will change is assumed to be two versions later.

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
            
            # Can only specify PRNG one of the three ways
            if int(as_old_kwarg) + int(as_new_kwarg) + int(as_pos_arg) > 1:
                message = (f"{fun.__name__}() got multiple values for "
                           f"argument now known as `{new_name}`")
                raise TypeError(message)

            if as_old_kwarg:  # warn about deprecated use of old kwarg
                kwargs[new_name] = kwargs.pop(old_name)
                if dep_version:
                    message = (f"Use of keyword argument `{old_name}` is "
                               f"deprecated and replaced by `{new_name}`.  "
                               f"Support for `{old_name}` will be removed "
                               f"in SciPy {end_version}. Use keyword `{new_name}` "
                               "to silence this warning.")
                    warnings.warn(message, DeprecationWarning, stacklevel=2)

            elif as_pos_arg and dep_version:
                # Warn about changing meaning of positional arg

                # Note that this decorator does not deprecate positional use of the
                # argument; it only warns that the behavior will change in the future.
                # Simultaneously transitioning to keyword-only use is another option.

                message = (f"Positional use of `{new_name}` (formerly known as "
                           f"`{old_name}`) is still allowed, but the behavior is "
                           "changing: the argument will be validated using "
                           "`np.random.default_rng` beginning in SciPy {end_version} "
                           f"Ensure that `np.random.default_rng(rng)` returns "
                           "successfully to silence this warning.")
                warnings.warn(message, FutureWarning, stacklevel=2)

            elif as_new_kwarg:  # no warnings; this is the preferred use
                # After the removal of the decorator, validation with
                # np.random.default_rng will be done inside the decorated function
                kwargs[new_name] = np.random.default_rng(kwargs[new_name])

            elif np.random.mtrand._rand._bit_generator._seed_seq is None:
                # Emit FutureWarning if `np.random.seed` was used and no PRNG was passed
                message = ("The NumPy global rng was seeded by calling "
                           f"`np.random.seed`. Beginning in {end_version}, this "
                           "function will no longer use the global rng. It will "
                           "instead use the `rng` argument, if provided, or create "
                           "a new `Generator` using `np.random.default_rng()`.")
                warnings.warn(message, FutureWarning, stacklevel=2)

            return fun(*args, **kwargs)
        return wrapper
    return decorator


# Example usage of _prepare_rng decorator
@_transition_to_rng("random_state", 1, "1.15.0")
# previously, the signature of the function was
#   library_function(arg1, random_state=None, arg2=None):
def library_function(arg1, rng=None, arg2=None):
    if isinstance(rng, (np.random.Generator, np.random.RandomState)):
        rng = rng.random()
    print((arg1, rng, arg2))

```
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


