# import Calculator
# import pytest
#
#
# @pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
# @pytest.mark.skip(reason="nothing")
# def test_add2no(a,b,c):
#     result=Calculator.add2no(a,b)
#     assert result == c
#
# @pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
# def test_sub2no(a,b,c):
#     result= Calculator.sub2no(a,b)
#     assert result == c
#
# @pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,6),(8,2,10)])
# def test_mul2no(a,b,c):
#     result= Calculator.mul2no(a,b)
#     assert result == c
#
# @pytest.mark.xfail
# @pytest.mark.parametrize('a,b,c',[(3,2,1),(5,1,8),(8,2,10)])
# def test_div2no(a,b,c):
#     result = Calculator.div2no(a,b)
#     assert result == c

import Calculator
import pytest

@pytest.mark.parametrize('a,b,c',[(3,2,5),(6,3,9),(1,2,3)])

@pytest.mark.skip(reason="nothing")
def test_add2no(a,b,c):

    result=Calculator.add2no(a,b)
    assert result == c

@pytest.mark.parametrize('a,b,c',[(2,5,6,),(20,10,30),(7,8,6)])
def test_sub2no(a,b,c):

    result= Calculator.sub2no(a,b)
    assert result == c

@pytest.mark.parametrize('a,b,c',[(2,5,6,),(20,10,30),(7,8,6)])
def test_mul2no(a,b,c):

    result= Calculator.mul2no(a,b)
    assert result == c
@pytest.mark.xfail
@pytest.mark.parametrize('a,b,c',[(2,5,6,),(20,10,30),(7,8,6)])
def test_div2no(a,b,c):

    result= Calculator.div2no(a,b)
    assert result == c