import unittest

def add(x,y,z):
    return x+y+z
class myapp(unittest.TestCase):
    def test_case_add1(self):
        a=12
        b=13
        c=14
        d=add(a,b,c)
        self.assertEqual(a+b+c,d)

if __name__ == "__main__":
    unittest.main()