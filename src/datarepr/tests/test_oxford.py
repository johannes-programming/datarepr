"""Test the oxford function."""

__all__ = ["TestOxfordFunction"]

import unittest
from typing import Self

from datarepr.core import oxford


class TestOxfordFunction(unittest.TestCase):
    """Test the oxford function comprehensively."""

    def test_no_args_at_all(self: Self) -> None:
        """Test oxford with varying numbers of arguments."""
        self.assertEqual("", oxford())
        self.assertEqual(42, oxford(default=42))
        self.assertEqual("1, 'two', and 3", oxford(1, "two", 3))
        self.assertEqual("1, 'two', and 3", oxford(1, "two", 3, default=42))
        self.assertEqual("1 and 'two'", oxford(1, "two"))
        self.assertEqual("1 or 'two'", oxford(1, "two", conj="or"))


if __name__ == "__main__":
    unittest.main()
