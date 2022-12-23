from fact import fact
import pytest

def test_fact0():
    assert fact(0) == 1

def test_fact1():
    assert fact(1) == 1

def test_fact2():
    assert fact(2) == 2

def test_fact3():
    assert fact(3) == 6

def test_fact7():
    assert fact(7) == 5040

def test_facta():
    with pytest.raises(TypeError):
        fact('a')