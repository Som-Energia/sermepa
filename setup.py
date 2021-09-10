#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
A client to submit payment orders to the Sermepa service.
"""

from setuptools import setup, find_packages

with open("README.md") as readme:
    longdesc = readme.read()


setup(
    name='sermepa',
    version='1.0.3',
    description = __doc__.strip(),
    author='GISCE Enginyeria',
    author_email='devel@gisce.net',
    url='http://www.gisce.net',
    license='General Public Licence 2 or later',
    long_description=longdesc,
    long_description_content_type='text/markdown',
    provides=['sermepa'],
    test_suite='sermepa',
    install_requires=[
        'pyDes',
        'simplejson',
        ],
    test_require=[
        'requests',
        ],
    packages=find_packages(),
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Topic :: Office/Business :: Financial',
        'Operating System :: OS Independent',
    ],
)
# vim: et sw=4 ts=4
