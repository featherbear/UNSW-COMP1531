from fibonacci import fib_sequence
from vals import vals


def test_fib():
    for val in vals:
        assert(fib_sequence(val) == vals[val])
