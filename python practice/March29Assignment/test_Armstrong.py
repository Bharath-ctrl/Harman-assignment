import pytest
import Armstrong

@pytest.mark.parametrize("a,ans", [(2,True),(4,True),(7,True),(9,True),(10,True),(17,True)])
def test_even(a,ans):
    res=Armstrong.ChkArm(a)
    assert res == ans
