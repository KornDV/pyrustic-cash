#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])

from setuptools import setup
from setuptools_rust import Binding, RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyrustic-cash",
    version="0.1",
    author="Dima Korneev",
    author_email="korteam7@gmail.com",
    description="Calculates position in accounts",
    long_description="Adjust exist positions in different accaunts with pending transaction and trades",
    long_description_content_type="text/markdown",
    url="https://github.com/KornDV/pyrustic-cash",
    rust_extensions=[RustExtension(
        ".pyrustic_cash.pyrustic_cash",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["pyrustic_cash"],
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
        ],
    zip_safe=False,
)
