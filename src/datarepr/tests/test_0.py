"""Test the datarepr function."""

__all__ = ["TestDatareprFunction"]

import unittest
from typing import Any, Self

from datarepr.core import datarepr


class TestDatareprFunction(unittest.TestCase):
    """Test the datarepr function comprehensively."""

    def test_combination_of_all(self: Self) -> None:
        """Test a complex combination of types and structures."""
        expected: str
        result: str
        result = datarepr(
            "complex_function",
            [1, 2],
            {3: 4},
            a=5,
            b=[6, 7],
            c={"key": "value"},
        )
        expected = (
            "complex_function([1, 2], {3: 4}, a=5,"
            " b=[6, 7], c={'key': 'value'})"
        )
        self.assertEqual(result, expected)

    def test_empty_args_kwargs(self: Self) -> None:
        """Test when only the name is provided and no args or kwargs."""
        result: str
        result = datarepr("test_function")
        self.assertEqual(result, "test_function()")

    def test_empty_name(self: Self) -> None:
        """Test with an empty name."""
        result: str
        result = datarepr("", 1, 2, a=3)
        self.assertEqual(result, "(1, 2, a=3)")

    def test_keyword_args_only(self: Self) -> None:
        """Test with keyword arguments only."""
        result: str
        result = datarepr("test_function", a=1, b=2, c=3)
        self.assertEqual(result, "test_function(a=1, b=2, c=3)")

    def test_keyword_args_only_1(self: Self) -> None:
        """Test with string keyword arguments."""
        result: str
        result = datarepr("test_function", x="x", y="y")
        self.assertEqual(result, "test_function(x='x', y='y')")

    def test_large_number_of_args(self: Self) -> None:
        """Test with a large number of arguments."""
        args: range
        expected: str
        result: str
        args = range(100)
        result = datarepr("test_function", *args)
        expected = "test_function(" + ", ".join(map(str, args)) + ")"
        self.assertEqual(result, expected)

    def test_mixed_args(self: Self) -> None:
        """Test with both positional and keyword arguments."""
        result: str
        result = datarepr("test_function", 1, 2, a=3, b=4)
        self.assertEqual(result, "test_function(1, 2, a=3, b=4)")

    def test_mixed_args_1(self: Self) -> None:
        """Test with string positional and int keyword arguments."""
        result: str
        result = datarepr("test_function", "x", "y", z=5)
        self.assertEqual(result, "test_function('x', 'y', z=5)")

    def test_name_as_non_string(self: Self) -> None:
        """Test with the 'name' parameter as a non-string type."""
        result: str
        result = datarepr(123, "arg1")
        self.assertEqual(result, "123('arg1')")
        result = datarepr(None, "arg1")
        self.assertEqual(result, "None('arg1')")

    def test_no_args_at_all(self: Self) -> None:
        """Test with no arguments, not even the name."""
        args: Any
        args = ()
        with self.assertRaises(TypeError):
            # Raise TypeError: missing required 'name' argument.
            datarepr(*args)

    def test_positional_args_only(self: Self) -> None:
        """Test with positional arguments only."""
        result: str
        result = datarepr("test_function", 1, 2, 3)
        self.assertEqual(result, "test_function(1, 2, 3)")

    def test_positional_args_only_1(self: Self) -> None:
        """Test with string positional arguments."""
        result: str
        result = datarepr("test_function", "a", "b", "c")
        self.assertEqual(result, "test_function('a', 'b', 'c')")

    def test_special_characters(self: Self) -> None:
        """Test with special characters in arguments."""
        result: str
        result = datarepr("test_function", "a\nb", "\t", key="val\nue")
        self.assertEqual(
            result, "test_function('a\\nb', '\\t', key='val\\nue')"
        )

    def test_various_types(self: Self) -> None:
        """Test with various types of arguments."""
        result: str
        result = datarepr("test_function", 1, 2.0, True, None)
        self.assertEqual(result, "test_function(1, 2.0, True, None)")
        result = datarepr("test_function", [1, 2], {3, 4}, {"key": "value"})
        self.assertEqual(
            result, "test_function([1, 2], {3, 4}, {'key': 'value'})"
        )
        result = datarepr("test_function", [1, 2], {3, 4}, {"key": "value"})
        self.assertEqual(
            result, "test_function([1, 2], {3, 4}, {'key': 'value'})"
        )


if __name__ == "__main__":
    unittest.main()
