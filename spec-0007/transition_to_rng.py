import numpy as np
import functools
import warnings


def _transition_to_rng(old_name, *, position_num=None, end_version):
    """Example decorator to transition from old PRNG usage to new `rng` behavior

    Suppose the decorator is applied to a function that used to accept parameter
    `old_name='random_state'` either by keyword or as a positional argument at
    `position_name=1`. At the time of application, the name of the argument in the
    function signature is manually changed to the new name, `rng`. If positional
    use was allowed before, this is not changed.*

    - If the function is called with both `random_state` and `rng`, the decorator
      raises an error.
    - If `random_state` is provided as a keyword argument, the decorator passes
      `random_state` to the function's `rng` argument as a keyword, but the decorator
      will emit a `DeprecationWarning` about the deprecation of keyword `random_state`.
    - If `random_state` is provided as a positional argument, the decorator passes
      `random_state` to the function's `rng` argument by position, but the decorator
      will emit a `FutureWarning` about the changing interpretation of the argument.
    - If `rng` is provided as a keyword argument, the decorator validates `rng` using
      `numpy.random.default_rng` before passing it to the function.
    - If neither `random_state` nor `rng` is provided, the decorator checks whether
      `np.random.seed` has been used to set the global seed. If so, it emits a
      `FutureWarning`, noting that usage of `numpy.random.seed` will eventually have
      no effect. Either way, the decorator calls the function without explicitly
      passing the `rng` argument.

    To avoid warnings, a user must pass `rng` as a keyword.

    After the deprecation period, the decorator can be removed, and the function
    can simply validate the `rng` argument by calling `np.random.default_rng(rng)`.

    * A `FutureWarning` is emitted when the PRNG argument is used by
      position. It indicates that the "Hinsen principle" (same
      code yielding different results in two versions of the software)
      will be violated, unless positional use is deprecated. Specifically:

      - If `None` is passed by position, the function will change from being
        seeded to being unseeded.
      - If an integer is passed by position, the random stream will change.

      We suggest that projects consider deprecating positional use of
      `random_state`/`rng` (i.e., change their function signatures to
      ``def my_func(..., *, rng=None)``); that might not make sense
      for all projects, so this SPEC does not make that
      recommendation, neither does this decorator enforce it.

    Parameters
    ----------
    old_name : str
        The old name of the PRNG argument (e.g. `seed` or `random_state`).
    position_num : int, optional
        The (0-indexed) position of the old PRNG argument (if accepted by position).
        Maintainers are welcome to eliminate this argument and use, for example,
        `inspect`, if preferred.
    end_version : str, optional
        The full version number of the library when the behavior described in
        `DeprecationWarning`s and `FutureWarning`s will take effect.

    """
    NEW_NAME = "rng"

    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            # Determine how PRNG was passed
            as_old_kwarg = old_name in kwargs
            as_new_kwarg = NEW_NAME in kwargs
            as_pos_arg = position_num is not None and len(args) >= position_num + 1

            # Can only specify PRNG one of the three ways
            if int(as_old_kwarg) + int(as_new_kwarg) + int(as_pos_arg) > 1:
                message = (
                    f"{fun.__name__}() got multiple values for "
                    f"argument now known as `{NEW_NAME}`"
                )
                raise TypeError(message)

            cmn_msg = (
                " To silence this warning and ensure consistent behavior in "
                f"SciPy {end_version}, control the RNG using argument "
                f"`{NEW_NAME}`. Arguments passed to keyword `{NEW_NAME}` will "
                "be validated by `np.random.default_rng`, so the behavior "
                "corresponding with a given value may change compared to use "
                f"of `{old_name}`. For example, "
                "1) `None` results in unpredictable random numbers, "
                "2) an integer results in a different stream of random numbers, "
                "(with the same distribution), and "
                "3) `np.random` or `RandomState` instances result in an error. "
                "See the documentation of `default_rng` for more information."
            )

            # Check whether global random state has been set
            global_seed_set = np.random.mtrand._rand._bit_generator._seed_seq is None

            if as_old_kwarg:  # warn about deprecated use of old kwarg
                kwargs[NEW_NAME] = kwargs.pop(old_name)
                message = (
                    f"Use of keyword argument `{old_name}` is "
                    f"deprecated and replaced by `{NEW_NAME}`.  "
                    f"Support for `{old_name}` will be removed "
                    f"in SciPy {end_version}."
                ) + cmn_msg
                warnings.warn(message, DeprecationWarning, stacklevel=2)

            elif as_pos_arg:
                # Warn about changing meaning of positional arg

                # Note that this decorator does not deprecate positional use of the
                # argument; it only warns that the behavior will change in the future.
                # Simultaneously transitioning to keyword-only use is another option.

                message = (
                    f"Positional use of `{NEW_NAME}` (formerly known as "
                    f"`{old_name}`) is still allowed, but the behavior is "
                    "changing: the argument will be validated using "
                    f"`np.random.default_rng` beginning in SciPy {end_version}."
                ) + cmn_msg
                warnings.warn(message, FutureWarning, stacklevel=2)

            elif as_new_kwarg:  # no warnings; this is the preferred use
                # After the removal of the decorator, validation with
                # np.random.default_rng will be done inside the decorated function
                kwargs[NEW_NAME] = np.random.default_rng(kwargs[NEW_NAME])

            elif global_seed_set:
                # Emit FutureWarning if `np.random.seed` was used and no PRNG was passed
                message = (
                    "The NumPy global RNG was seeded by calling "
                    f"`np.random.seed`. Beginning in {end_version}, this "
                    "function will no longer use the global RNG."
                ) + cmn_msg
                warnings.warn(message, FutureWarning, stacklevel=2)

            return fun(*args, **kwargs)

        return wrapper

    return decorator


# Example usage of _prepare_rng decorator
@_transition_to_rng("random_state", position_num=1, end_version="1.17.0")
# previously, the signature of the function was
#   library_function(arg1, random_state=None, arg2=None):
def library_function(arg1, rng=None, arg2=None):
    if isinstance(rng, (np.random.Generator, np.random.RandomState)):
        rng = rng.random()
    print((arg1, rng, arg2))
