import pytest
from docker_python_exemplo import __version__, versionfile
try:
    from pathlib2 import Path
except ImportError:
    from pathlib import Path

import re


def test_version_file():
    assert versionfile.is_file()


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (__version__, True),
        ('1.0', False),
        ('111.1.1', True),
        ('0.111111.1', True),
        ('0.0.111111', True),
        ('0.0.1-alpha.11111', True),
        # ('0.0.1-a0', False),
        # ('0.0.1-0', False),
    ],
)
def test_versions(entrance, expected):
    reg = re.compile(r'\d+(\.\d+){2}(-\w+\.\d+)?', flags=re.I)
    assert bool(reg.search(entrance)) == expected
