import sys
import calci
import unittest


class calci_test(unittest.TestCase):
    def test_add(self):
        a = 10
        b = 20
        c = calci.add(a, b)
        self.assertEqual(a + b, c)
    #@unittest.skip("skipped now")
    #@unittest.skipIf(sys.platform.startswith("win","no windows please"))
    def test_sub(self):
        a = 10
        b = 20
        c = calci.sub(a, b)
       # self.assertEqual(a - b, c)
        self.assertNotIn()(a,())

    def test_mul(self):
        a = 10
        b = 20
        c = calci.mul(a, b)
        self.assertEqual(a * b, c)

    def test_div(self):
        a = 10
        b = 20
        c = calci.div(a, b)
        self.assertEqual(a / b, c)


if __name__ == "__main__":
    unittest.main()
