#!/usr/bin/env python
import os

from setuptools import setup, find_packages

HERE = os.path.dirname(__file__)

setup(
    name="notebook_mapper",
    version="0.0.6",
    description="Jupyter Notebooks + Windows Server mapped drives toolkit.",
    author="James Draper",
    author_email="james.draper@duke.edu",
    license="MIT",
    url="https://github.com/draperjames/notebook_mapper",
    packages=find_packages(),
    platforms=["POSIX", "Windows"],
    provides=["notebook_mapper"],
    keywords="jupyter, notebook, Windows, Mapped Drive, Windows Server",
    long_description=open(os.path.join(HERE, "README.md"), "r").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Systems Administration",
    ],
)
