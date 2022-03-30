import unittest

def add(x,y):
    return x+y

class myapp(unittest.TestCase):
    def test_case_add1(self):
        a=12
        b=13
        c=add(a,b)
        self.assertEqual(a+b,c)
if __name__ == "__main__":
    unittest.main()