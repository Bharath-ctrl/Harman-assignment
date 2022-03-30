import unittest

def div(x,y):
    return x/y

class myapp(unittest.TestCase):
    def test_case_div1(self):
        a=12
        b=13
        c=div(a,b)
        self.assertEqual(a/b,c)

if __name__ == "__main__":
    unittest.main()