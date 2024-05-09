from setuptools import setup, find_packages
import os

# Importing version from the version module
version = {}
with open(os.path.join("src", "version.py")) as fp:
    exec(fp.read(), version)

setup(
    name='lib-version',
    version=version['__version__'],
    packages=find_packages()
)