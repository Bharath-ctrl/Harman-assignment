import unittest

def mul(x,y):
    return x*y

class myapp(unittest.TestCase):
    def test_case_mul1(self):
        a=12
        b=13
        c=mul(a,b)
        self.assertEqual(a*b,c)

if __name__ == "__main__":
    unittest.main()