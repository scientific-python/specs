import contextlib

import numpy as np
import pytest

from transition_to_rng import _transition_to_rng, library_function


@contextlib.contextmanager
def np_random_seed(seed=0):
    # Save RandomState
    rs = np.random.mtrand._rand

    # Install temporary RandomState
    np.random.mtrand._rand = np.random.RandomState(seed)

    yield

    np.random.mtrand._rand = rs


def test_seeded_vs_unseeded():
    with np_random_seed():
        with pytest.warns(FutureWarning, match="NumPy global RNG"):
            library_function(1)

        # These behaviors should not change when the global seed is set,
        # since they provide explicit `random_state` or `rng`
        test_positional_random_state()
        test_random_state_deprecated()
        test_rng_correct_usage()

    # Entirely unseeded, should proceed without warning
    library_function(1)


def test_positional_random_state():
    # doesn't need to warn
    library_function(1, None)  # seed not set
    library_function(1, np.random.default_rng(2384924))  # Generators still accepted

    with pytest.warns(FutureWarning, match="Positional use of"):
        library_function(1, 1)  # behavior will change

        # will raise error in the future
        library_function(1, np.random.RandomState(1))
        library_function(1, np.random)


def test_random_state_deprecated():
    with pytest.warns(
        DeprecationWarning, match="keyword argument `random_state` is deprecated"
    ):
        library_function(1, random_state=None)
        library_function(1, random_state=1)


def test_rng_correct_usage():
    library_function(1, rng=None)

    assert library_function(1, rng=1) == library_function(1, rng=1)
    assert library_function(1, rng=np.random.default_rng(123)) == library_function(
        1, rng=np.random.default_rng(123)
    )


def test_rng_incorrect_usage():
    with pytest.raises(TypeError, match="SeedSequence expects"):
        library_function(1, rng=np.random.RandomState(123))

    with pytest.raises(TypeError, match="multiple values"):
        library_function(1, rng=1, random_state=1)


@_transition_to_rng("random_state", end_version="1.17.0")
# previously, the signature of the function was
#   library_function(arg1, random_state=None, arg2=None):
def random_function(arg1, *, rng=None, arg2=None):
    if isinstance(rng, (np.random.Generator, np.random.RandomState)):
        rng = rng.random()
    print((arg1, rng, arg2))


def test_decorator_no_positional():
    with pytest.warns(
        DeprecationWarning, match="keyword argument `random_state` is deprecated"
    ):
        random_function(1, random_state=3)

    random_function(1, rng=123)


if __name__ == "__main__":
    import pytest

    pytest.main(["-W", "error"])
