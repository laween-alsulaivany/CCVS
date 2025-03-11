"""
This file is used to install the package.
The reason we install the package is to give it access to the system path.
This is necessary because the package is not in the system path by default.

please do not modify this but run it at least once to install the package.
"""


from setuptools import setup, find_packages

setup(
    name="CCVS",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
