# -*- coding: utf-8 -*-

import pytest

from cirr.skeleton import fib

__author__ = "LaurenÈ›iu Andronache"
__copyright__ = "LaurenÈ›iu Andronache"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
