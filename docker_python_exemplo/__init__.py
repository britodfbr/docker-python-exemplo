"""
Principal Module.

Update metadata from version by semver
"""
import toml
import platform

if platform.platform() < '3.6':
    from pathlib2 import Path
else:
    from pathlib import Path


configfile = Path(__file__).parents[1].joinpath("pyproject.toml")
versionfile = Path(__file__).parent.joinpath("version.txt")
a = toml.load(configfile.as_posix())['tool']['poetry']['version']
versionfile.write_text(u'{}\n'.format(a))
__version__ = versionfile.read_text().strip()

if __name__ == '__main__':
    print(__version__)
