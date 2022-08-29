#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])

from setuptools import setup
from setuptools_rust import Binding, RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyrustic_cash",
    version="0.0.1",
    author="Dima Korneev",
    author_email="korteam7@gmail.com",
    description="Calculates position in accounts",
    long_description="Adjust exist positions in different accaunts with pending transaction and trades",
    long_description_content_type="text/markdown",
    url="https://github.com/KornDV/pyrustic-cash",
    install_requires=[],
    rust_extensions=[RustExtension(
        ".pyrustic_cash.pyrustic_cash",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["pyrustic_cash"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    zip_safe=False,
    python_requires='>=3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fib-number = pyrustic_cash.cmd.fib_numb:fib_numb',
        ],
    },
)
