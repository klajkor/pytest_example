# ###
# Another solution for importing from parent directory:
#
# import sys
# from pathlib import Path # if you haven't already done so
# file = Path(__file__).resolve()
# parent, root = file.parent, file.parents[1]
# sys.path.append(str(root))
#
# # Additionally remove the current file's directory from sys.path
# try:
#     sys.path.remove(str(parent))
# except ValueError:  # Already removed
#     pass
#

import pytest
from pytest_example import hello


@pytest.fixture
def bob():
    return {"name": "Bob"}


def test_hello(bob):
    assert hello(bob) == "Hi, Bob"
