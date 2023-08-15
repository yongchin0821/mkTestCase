#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 11:15 AM
# @Author  : Yongchin


from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mkTestCase",
    version="0.0.6",
    author="Yongchin",
    author_email="yongchin39@qq.com",
    license="MIT",
    description="Write test cases like building blocks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["testcase", "automatically generate test cases", "automated test"],
    url="https://github.com/yongchin0821/mkTestCase",
    project_urls={
        "Bug Tracker": "https://github.com/yongchin0821/mkTestCase/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["openpyxl"],
    classifiers=[
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    # pytest looks up the pytest11 entrypoint to discover its plugins
    entry_points={
    },
)
