from setuptools import setup, find_packages
import os

version = {}
with open(os.path.join("src", "version.py")) as fp:
    exec(fp.read(), version)

setup(
    name='lib-version',
    version=version['__version__'],
    packages=find_packages(),
    description='A library to manage and track versions of software components'
)
