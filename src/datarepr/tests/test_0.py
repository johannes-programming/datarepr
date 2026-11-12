"""Test the datarepr function."""

__all__ = ["TestDatareprFunction"]

import enum
import io
import tomllib
import unittest
from collections.abc import Sequence
from functools import cached_property
from pathlib import Path
from typing import Any, Self, cast

from datarepr.core import datarepr


class Lazy(enum.Enum):
    lazy = None

    @cached_property
    def data(self: Self) -> dict[str, Any]:
        file: Path
        stream: io.BufferedReader
        file = Path(__file__).parent / "testdata.toml"
        with file.open("rb") as stream:
            return tomllib.load(stream)

    @cached_property
    def test_0(self: Self) -> dict[str, Any]:
        return cast(dict[str, Any], self.lazy.data["test_0"])


class TestDatareprFunction(unittest.TestCase):
    """Test the datarepr function comprehensively."""

    def go_valid(
        self: Self,
        name: str,
        /,
        *,
        solution: str,
        args: Sequence[Any],
        kwargs: Any = (),
    ) -> None:
        """Test the datarepr function with valid parameters."""
        result: str
        with self.subTest(name):
            result = datarepr(*args, **dict(kwargs))
            self.assertEqual(result, solution)

    def test_0(self: Self) -> None:
        """Test the testdata."""
        for x, y in Lazy.lazy.test_0.items():
            self.go_valid(x, **y)

    def test_combination_of_all(self: Self) -> None:
        """Test a complex combination of types and structures."""
        result: str
        solution: str
        result = datarepr(
            "complex_function",
            [1, 2],
            {3: 4},
            a=5,
            b=[6, 7],
            c={"key": "value"},
        )
        solution = (
            "complex_function([1, 2], {3: 4}, a=5,"
            " b=[6, 7], c={'key': 'value'})"
        )
        self.assertEqual(result, solution)

    def test_name_as_non_string(self: Self) -> None:
        """Test with the 'name' parameter as a non-string type."""
        result: str
        result = datarepr(None, "arg1")
        self.assertEqual(result, "None('arg1')")

    def test_no_args_at_all(self: Self) -> None:
        """Test with no arguments, not even the name."""
        args: Any
        args = ()
        with self.assertRaises(TypeError):
            # Raise TypeError: missing required 'name' argument.
            datarepr(*args)

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
