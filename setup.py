#
# OxRSE setuptools script
#
# This file is part of the Oxford RSE Python Template project.
#  Copyright (c) 2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the OxRSE
#  software package.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the oxrse module.

    The easiest way would be to just ``import oxrse``, but note that this may
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple _version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('oxrse'))
    from _version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='oxrse',

    # Version
    version=get_version(),

    description='An example Python project.',

    long_description=get_readme(),

    license='BSD 3-clause license',

    # author='',

    # author_email='',

    maintainer='Michael Clerx',

    maintainer_email='michael.clerx@cs.ox.ac.uk',

    url='https://github.com/OxfordRSE/template-project-python',

    # Packages to include
    packages=find_packages(include=('oxrse', 'oxrse.*')),

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy',
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
        ],
    },
)
