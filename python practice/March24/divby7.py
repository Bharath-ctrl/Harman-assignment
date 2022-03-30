import unittest

def check_divisibleby7(x):
    if x%7==0:
        return True
    else:
        return False
class CheckDivisible(unittest.TestCase):
    def test_case_check_divisibleby_1(self):
        result=check_divisibleby7(5)
        self.assertFalse(result)

    def test_case_check_divisibleby_2(self):
        result=check_divisibleby7(14)
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()