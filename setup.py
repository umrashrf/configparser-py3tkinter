#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = ['Click>=6.0',]

setup_requirements = ['pytest-runner',]

test_requirements = ['pytest',]

setup(
    name='configparser-py3tkinter',
    author="Umair Ashraf",
    author_email='umrashrf@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=requirements,
    include_package_data=True,
    keywords='',
    packages=find_packages(include=['configparser-py3tkinter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/umrashrf/configparser-py3tkinter',
    version='0.1.0',
    zip_safe=False,
)
