import unittest
from typing import *

from datarepr.core import oxford

__all__ = ["TestOxfordFunction"]


class TestOxfordFunction(unittest.TestCase):
    def test_no_args_at_all(self: Self) -> None:
        self.assertEqual("", oxford())
        self.assertEqual(42, oxford(default=42))
        self.assertEqual("1, 'two', and 3", oxford(1, "two", 3))
        self.assertEqual("1, 'two', and 3", oxford(1, "two", 3, default=42))
        self.assertEqual("1 and 'two'", oxford(1, "two"))
        self.assertEqual("1 or 'two'", oxford(1, "two", conj="or"))


if __name__ == "__main__":
    unittest.main()
