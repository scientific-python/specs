import numpy as np
import functools
import warnings


def _transition_to_rng(old_name, *, position_num=None, end_version=None):
    """Example decorator to transition from old PRNG usage to new `rng` behavior

    Suppose the decorator is applied to a function that used to accept parameter
    `old_name='random_state'` either by keyword or as a positional argument at
    `position_num=1`. At the time of application, the name of the argument in the
    function signature is manually changed to the new name, `rng`. If positional
    use was allowed before, this is not changed.*

    - If the function is called with both `random_state` and `rng`, the decorator
      raises an error.
    - If `random_state` is provided as a keyword argument, the decorator passes
      `random_state` to the function's `rng` argument as a keyword. If `end_version`
      is specified, the decorator will emit a `DeprecationWarning` about the
      deprecation of keyword `random_state`.
    - If `random_state` is provided as a positional argument, the decorator passes
      `random_state` to the function's `rng` argument by position. If `end_version`
      is specified, the decorator will emit a `FutureWarning` about the changing
      interpretation of the argument.
    - If `rng` is provided as a keyword argument, the decorator validates `rng` using
      `numpy.random.default_rng` before passing it to the function.
    - If `end_version` is specified and neither `random_state` nor `rng` is provided
      by the user, the decorator checks whether `np.random.seed` has been used to set
      the global seed. If so, it emits a `FutureWarning`, noting that usage of
      `numpy.random.seed` will eventually have no effect. Either way, the decorator
      calls the function without explicitly passing the `rng` argument.

    If `end_version` is specified, a user must pass `rng` as a keyword to avoid warnings.

    After the deprecation period, the decorator can be removed, and the function
    can simply validate the `rng` argument by calling `np.random.default_rng(rng)`.

    * A `FutureWarning` is emitted when the PRNG argument is used by
      position. It indicates that the "Hinsen principle" (same
      code yielding different results in two versions of the software)
      will be violated, unless positional use is deprecated. Specifically:

      - If `None` is passed by position and `np.random.seed` has been used,
        the function will change from being seeded to being unseeded.
      - If an integer is passed by position, the random stream will change.
      - If `np.random` or an instance of `RandomState` is passed by position,
        an error will be raised.

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
        `DeprecationWarning`s and `FutureWarning`s will take effect. If left
        unspecified, no warnings will be emitted by the decorator.

    """
    NEW_NAME = "rng"

    cmn_msg = (
        "To silence this warning and ensure consistent behavior in SciPy "
        f"{end_version}, control the RNG using argument `{NEW_NAME}`. Arguments passed "
        f"to keyword `{NEW_NAME}` will be validated by `np.random.default_rng`, so the "
        "behavior corresponding with a given value may change compared to use of "
        f"`{old_name}`. For example, "
        "1) `None` will result in unpredictable random numbers, "
        "2) an integer will result in a different stream of random numbers, (with the "
        "same distribution), and "
        "3) `np.random` or `RandomState` instances will result in an error. "
        "See the documentation of `default_rng` for more information."
    )

    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            # Determine how PRNG was passed
            as_old_kwarg = old_name in kwargs
            as_new_kwarg = NEW_NAME in kwargs
            as_pos_arg = position_num is not None and len(args) >= position_num + 1
            emit_warning = end_version is not None

            # Can only specify PRNG one of the three ways
            if int(as_old_kwarg) + int(as_new_kwarg) + int(as_pos_arg) > 1:
                message = (
                    f"{fun.__name__}() got multiple values for "
                    f"argument now known as `{NEW_NAME}`"
                )
                raise TypeError(message)

            # Check whether global random state has been set
            global_seed_set = np.random.mtrand._rand._bit_generator._seed_seq is None

            if as_old_kwarg:  # warn about deprecated use of old kwarg
                kwargs[NEW_NAME] = kwargs.pop(old_name)
                if emit_warning:
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

                arg = args[position_num]
                # If the argument is None and the global seed wasn't set, or if the
                # argument is one of a few new classes, the user will not notice change
                # in behavior.
                ok_classes = (
                    np.random.Generator,
                    np.random.SeedSequence,
                    np.random.BitGenerator,
                )
                if (arg is None and not global_seed_set) or isinstance(arg, ok_classes):
                    pass
                elif emit_warning:
                    message = (
                        f"Positional use of `{NEW_NAME}` (formerly known as "
                        f"`{old_name}`) is still allowed, but the behavior is "
                        "changing: the argument will be normalized using "
                        f"`np.random.default_rng` beginning in SciPy {end_version}, "
                        "and the resulting `Generator` will be used to generate "
                        "random numbers."
                    ) + cmn_msg
                    warnings.warn(message, FutureWarning, stacklevel=2)

            elif as_new_kwarg:  # no warnings; this is the preferred use
                # After the removal of the decorator, normalized with
                # np.random.default_rng will be done inside the decorated function
                kwargs[NEW_NAME] = np.random.default_rng(kwargs[NEW_NAME])

            elif global_seed_set and emit_warning:
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


# Example usage of _prepare_rng decorator.

# Suppose a library uses a custom random state normalisation function, such as
from scipy._lib._util import check_random_state

# https://github.com/scipy/scipy/blob/94532e74b902b569bfad504866cb53720c5f4f31/scipy/_lib/_util.py#L253


# Suppose a function `library_function` is defined as:
def library_function(arg1, random_state=None, arg2=0):
    random_state = check_random_state(random_state)
    return random_state.random() * arg1 + arg2


# We apply the decorator and change the function signature at the same time.
# The use of `random_state` throughout the function may be replaced with `rng`,
# or the variable may be defined as `random_state = rng`.
@_transition_to_rng("random_state", position_num=1)
def library_function(arg1, rng=None, arg2=0):
    rng = check_random_state(rng)
    return rng.random() * arg1 + arg2


# After `rng` is available in all releases within the support window suggested by
# SPEC 0, we pass the `end_version` param to the decorator to emit warnings.
@_transition_to_rng("random_state", position_num=1, end_version="1.17.0")
def library_function(arg1, rng=None, arg2=0):
    rng = check_random_state(rng)
    return rng.random() * arg1 + arg2


# At the end of the deprecation period, remove the decorator, and  normalize
# `rng` with` np.random.default_rng`.
def library_function(arg1, rng=None, arg2=0):
    rng = np.random.default_rng(rng)
    return rng.random() * arg1 + arg2
