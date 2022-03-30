import unittest

def Prime_or_not(x):
    flag = False

    if x> 1:
        for i in range(2,x):
            if (x% i) == 0:
                flag = True
                break
    if flag:
        return True
    else:
        return False
class CheckPrimeNumber(unittest.TestCase):
    def test_prime(self):
        result=Prime_or_not(3)
        self.assertTrue(True)

    def test_prime_not(self):
        result=Prime_or_not(10)
        self.assertFalse(False)

if __name__ == "__main__":
        unittest.main()