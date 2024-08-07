import contextlib

import numpy as np
import pytest

from transition_to_rng import _transition_to_rng

from scipy._lib._util import check_random_state


@_transition_to_rng("random_state", position_num=1, end_version="1.17.0")
def library_function(arg1, rng=None, arg2=0):
    rng = check_random_state(rng)
    return arg1, rng.random(), arg2


@contextlib.contextmanager
def np_random_seed(seed=0):
    # Save RandomState
    rs = np.random.mtrand._rand

    # Install temporary RandomState
    np.random.mtrand._rand = np.random.RandomState(seed)

    yield

    np.random.mtrand._rand = rs


def test_positional_random_state():
    # doesn't need to warn
    library_function(1, np.random.default_rng(2384924))  # Generators still accepted

    message = "Positional use of"
    if np.random.mtrand._rand._bit_generator._seed_seq is not None:
        library_function(1, None)  # seed not set
    else:
        with pytest.warns(FutureWarning, match=message):
            library_function(1, None)  # seed set

    with pytest.warns(FutureWarning, match=message):
        library_function(1, 1)  # behavior will change

    with pytest.warns(FutureWarning, match=message):
        library_function(1, np.random.RandomState(1))  # will error

    with pytest.warns(FutureWarning, match=message):
        library_function(1, np.random)  # will error


def test_random_state_deprecated():
    message = "keyword argument `random_state` is deprecated"

    with pytest.warns(DeprecationWarning, match=message):
        library_function(1, random_state=None)

    with pytest.warns(DeprecationWarning, match=message):
        library_function(1, random_state=1)


def test_rng_correct_usage():
    library_function(1, rng=None)

    rng = np.random.default_rng(1)
    ref_random = rng.random()

    res = library_function(1, rng=1)
    assert res == (1, ref_random, 0)

    rng = np.random.default_rng(1)
    res = library_function(1, rng, arg2=2)
    assert res == (1, ref_random, 2)


def test_rng_incorrect_usage():
    with pytest.raises(TypeError, match="SeedSequence expects"):
        library_function(1, rng=np.random.RandomState(123))

    with pytest.raises(TypeError, match="multiple values"):
        library_function(1, rng=1, random_state=1)


def test_seeded_vs_unseeded():
    with np_random_seed():
        with pytest.warns(FutureWarning, match="NumPy global RNG"):
            library_function(1)

        # These tests should still pass when the global seed is set,
        # since they provide explicit `random_state` or `rng`
        test_positional_random_state()
        test_random_state_deprecated()
        test_rng_correct_usage()

    # Entirely unseeded, should proceed without warning
    library_function(1)


def test_decorator_no_positional():
    @_transition_to_rng("random_state", end_version="1.17.0")
    def library_function(arg1, *, rng=None, arg2=None):
        rng = check_random_state(rng)
        return arg1, rng.random(), arg2

    message = "keyword argument `random_state` is deprecated"
    with pytest.warns(DeprecationWarning, match=message):
        library_function(1, random_state=3)

    library_function(1, rng=123)


def test_decorator_no_end_version():
    @_transition_to_rng("random_state")
    def library_function(arg1, rng=None, *, arg2=None):
        rng = check_random_state(rng)
        return arg1, rng.random(), arg2

    # no warnings emitted
    library_function(1, rng=np.random.default_rng(235498235))
    library_function(1, random_state=np.random.default_rng(235498235))
    library_function(1, 235498235)
    with np_random_seed():
        library_function(1, None)


if __name__ == "__main__":
    import pytest

    pytest.main(["-W", "error"])
