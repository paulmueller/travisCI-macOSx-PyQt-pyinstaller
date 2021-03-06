#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists, dirname, realpath
from setuptools import setup, find_packages
import sys

author = u"Paul Müller"
authors = [author]
description = 'Minimal setup for building PyQt apps for MacOSx on travisCI'
name = 'fooqt'
year = "2018"


sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
try:
    from _version import version  # @UnresolvedImport
except:
    version = "unknown"

setup(
    name=name,
    author=author,
    author_email='dev@craban.de',
    url='https://github.com/paulmueller/travisCI-macOSx-PyQt-pyinstaller',
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    # Qt5 regularly drops support for older osx versions, so you might
    # want to use an older version of PyQt5. See also:
    # http://doc.qt.io/QtForDeviceCreation/qtee-changelog.html#boot-to-qt-5-9-6
    # For instance, to support osx 10.10, use:
    # install_requires=["pyqt5<5.10"],
    install_requires=["pyqt5"],
    license="MIT",
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    keywords=["foo-bar"],
    setup_requires=['pytest-runner'],
    tests_require=["pytest", "pytest-qt"],
    entry_points={"gui_scripts" : ['fooqt = fooqt.__main__:main']},
    platforms=['ALL'],
    )
