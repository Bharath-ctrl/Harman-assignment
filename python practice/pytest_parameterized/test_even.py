import pytest
import even_odd

@pytest.mark.parametrize("a,ans", [(2,True),(4,True),(7,True),(9,True),(10,True),(17,True)])
def test_even(a,ans):
    res=even_odd.ChkEven(a)
    assert res == ans
