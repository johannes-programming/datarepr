__all__: list[str] = ["main", "test"]

import sys

from datarepr.tests import test


def main() -> int:
    return int(not test().wasSuccessful())


if __name__ == "__main__":
    sys.exit(main())
