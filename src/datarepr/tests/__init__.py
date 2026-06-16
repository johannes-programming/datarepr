import unittest

__all__ = ["test"]


def test() -> unittest.TextTestResult:
    suite: unittest.TestSuite
    suite = unittest.TestLoader().discover(start_dir="datarepr.tests")
    return unittest.TextTestRunner().run(suite)
