import unittest
from .binary_to_decimal_conversion import binary_to_decimal_converter


class TestBinaryToDecimal(unittest.TestCase):

    def binary_to_decimal_0(self):
        dec = binary_to_decimal_converter(0)
        self.assertEqual(dec, 0)

    def binary_to_decimal_1(self):
        dec = binary_to_decimal_converter(1)
        self.assertEqual(dec, 1)

    def binary_to_decimal_10(self):
        dec = binary_to_decimal_converter(10)
        self.assertEqual(dec, 2)

    def test_binary_to_decimal_with_string(self):
        with self.assertRaises(TypeError):
            dec = binary_to_decimal_converter("hello")


if __name__ == '__main__':
    unittest.main()
