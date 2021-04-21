#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      
      name='example-test',
      version='0.0.1',
      url="https://github.com/lucienne1986/Python-Projects",
      author="Lucienne Micallef",
      author_email="lucienne1986@gmail.com",
      description='Say hello',
      long_description=long_description,
      long_description_content_type="text/markdown",
      py_modules=["example-test"],
      package_dir={'':'src'},
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      packages=setuptools.find_packages(where="src"),
      python_requires=">=3.6",
           
      )