#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

with open("readme.md", "r",  encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "allalgorithms",
    packages = ["allalgorithms"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "0.0.0",
    description = "All Algorithms in Python",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://python.allalgorithms.com",
	license='MIT',
    classifiers=(
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
    project_urls={
        'Source': 'https://github.com/abranhe/python-lib',
    },
)
