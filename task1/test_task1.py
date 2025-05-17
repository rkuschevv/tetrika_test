import unittest

from .solution import strict


class TestStrictDecorator(unittest.TestCase):
    def test_valid_types(self):
        @strict
        def test_func(a: int, b: str) -> str:
            return str(a) + b

        result = test_func(42, "test")
        self.assertEqual(result, "42test")

    def test_invalid_argument_type(self):
        @strict
        def test_func(a: int, b: str) -> str:
            return str(a) + b

        with self.assertRaises(TypeError) as context:
            test_func(8.6, "тест")
        self.assertIn("должен быть типа int", str(context.exception))

    def test_invalid_return_type(self):
        @strict
        def test_func(a: int, b: int) -> str:
            return a + b

        with self.assertRaises(TypeError) as context:
            test_func(-4, 6)
        self.assertIn("must be of type str", str(context.exception))

    def test_multiple_arguments(self):
        @strict
        def test_func(a: int, b: str, c: float) -> str:
            return str(a) + b + str(c)

        result = test_func(1, "test", 3.14)
        self.assertEqual(result, "1test3.14")

    def test_sum_two_function(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        result = sum_two(40, 2)
        self.assertEqual(result, 42)


if __name__ == "__main__":
    unittest.main()
