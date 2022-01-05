"import"
import unittest
import math

def my_frexp(input_value):
    'use only integers'
    if not input_value:
        raise TypeError("x cannot be empty")
    if not isinstance(input_value, int):
        raise TypeError("Input should be int")
    return math.frexp(input_value)

class TestFrexpMath(unittest.TestCase):
    "class to test custom frexp function"

    def test_correct_param(self):
        "correct params"
        expected = 0.5, 3
        test_data_x = 4
        self.assertEqual(math.frexp(test_data_x), expected)
        self.assertEqual(my_frexp(test_data_x), expected)

    def test_empty_param(self):
        "empty params"
        with self.assertRaises(TypeError):
            self.assertEqual(my_frexp(None), True)

    def test_missing_param(self):
        "missing params"
        test_data_x = None
        with self.assertRaises(TypeError):
            self.assertEqual(my_frexp(test_data_x), True)

    def test_wrong_param_type(self):
        "wrong params"
        with self.assertRaises(TypeError):
            my_frexp("test")
        with self.assertRaises(TypeError):
            my_frexp([])

if __name__ == '__main__':
    unittest.main()
