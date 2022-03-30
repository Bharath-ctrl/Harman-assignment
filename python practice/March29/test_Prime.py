import Prime
import pytest

@pytest.mark.parametrize("a,b",[(3,False),(4,False),(1,False),(5,False),(20,False),(50,False)])
def test_Prime(a,b):
    res=Prime.prime(a)
    assert not res == b