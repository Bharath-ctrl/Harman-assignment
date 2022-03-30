import sys
import calci
import unittest


class calci_test(unittest.TestCase):

    def setUp(self):
        self.a=10
        self.b=20
        print("Setup called")
    def tearDown(self):
        self.a=0
        self.b=0
        print("teardown called")
    def test_add(self):
        # a = 10
        # b = 20
        c = calci.add(self.a,self.b)
        self.assertEqual(self.a + self.b, c)
    #@unittest.skip("skipped now")
    #@unittest.skipIf(sys.platform.startswith("win","no windows please"))
    def test_sub(self):
        a = 10
        b = 20
        c = calci.sub(self.a,self.b)
        self.assertEqual(self.a - self.b, c)
       #  self.assertNotIn()(a,())

    def test_mul(self):
        a = 10
        b = 20
        c = calci.mul(self.a,self.b)
        self.assertEqual(self.a * self.b, c)

    def test_div(self):
        a = 10
        b = 20
        c = calci.div(self.a,self.b)
        self.assertEqual(self.a / self.b, c)


if __name__ == "__main__":
    unittest.main()
