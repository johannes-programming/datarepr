"""Provide test utilities for the datarepr package."""

__all__ = ["test"]

import unittest


def test() -> unittest.TextTestResult:
    """Run all tests and return the result."""
    suite: unittest.TestSuite
    suite = unittest.TestLoader().discover(start_dir="datarepr.tests")
    return unittest.TextTestRunner().run(suite)
