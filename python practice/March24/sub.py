import unittest

def sub(x,y):
    return x-y

class myapp(unittest.TestCase):
    def test_case_sub1(self):
        a=12
        b=13
        c=sub(a,b)
        self.assertEqual(a-b,c)

if __name__ == "__main__":
    unittest.main()