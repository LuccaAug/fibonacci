import unittest
from fibonacci import Fibonacci


class MyTestCase(unittest.TestCase):

    def test_negative_value(self):
        f = Fibonacci(-1)
        self.assertRaises(ValueError, f.calcula_fib)

    def test_positive_value(self):
        f = Fibonacci(13)
        self.assertEqual(f.calcula_fib(), 233)

    def test_positive_giant_value(self):
        f = Fibonacci(500)
        self.assertEqual(f.calcula_fib(), 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125)


if __name__ == '__main__':
    unittest.main()
