#!/usr/bin/env python
import os
import re
from setuptools import setup, find_packages

__doc__="""
Reusable Newsletter signup application for Django
"""

version = '0.0.1'

setup(name='django-fusionbox-newsletter',
    version=version,
    description='Reusable Newsletter signup application for Django',
    author='Fusionbox programmers',
    author_email='programmers@fusionbox.com',
    keywords='django newsletter',
    long_description=__doc__,
    url='https://github.com/fusionbox/django-fusionbox-newsletter',
    packages=find_packages(),
    namespace_packages=['fusionbox'],
    platforms = "any",
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    install_requires = ['django_fusionbox'],
    requires = ['django_fusionbox'],
)

