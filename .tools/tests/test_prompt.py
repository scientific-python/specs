from contextlib import contextmanager

from tools import prompt
import builtins


@contextmanager
def yield_input(s):
    system_input = builtins.input

    def input(*args, **kwargs):
        return input.returnvals.pop(0)

    if isinstance(s, (list, tuple)):
        input.returnvals = list(s)
    else:
        input.returnvals = [s]

    builtins.input = input

    yield

    builtins.input = system_input


def test_validate_int():
    with yield_input(['foo', '1.5', 1]):
        val = prompt(
            'Please input integer',
            validate=lambda x: int(x)
        )
        assert val == 1


def test_validate_str():
    with yield_input(['hello', 'world', 'scikit-something']):
        val = prompt(
            'Input scikit name',
            validate=lambda x: x if x.startswith('scikit') else None
        )
        assert val == 'scikit-something'


def test_default_value():
    with yield_input(''):
        val = prompt(
            'Enter optional string',
            default='default-answer'
        )
        assert val == 'default-answer'


def test_default_value_after_bad_input():
    with yield_input(['asd', '']):
        val = prompt(
            'Enter scikit name',
            validate=lambda x: x if x.startswith('scikit') else None,
            default='scikit-something'
        )
        assert val == 'scikit-something'


def test_default_not_validated():
    with yield_input(''):
        val = prompt(
            'Enter a number',
            validate=lambda x: int(x),
            default='hello'
        )
        assert val == 'hello'
