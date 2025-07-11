import setuptools
from pathlib import Path

setuptools.setup(
    name='kwasipdf',
    version=1.0,
    long_description=Path('READMD.md').read_text(),
    packages=setuptools.find_packages(exclude=['tests', 'data'])
)
