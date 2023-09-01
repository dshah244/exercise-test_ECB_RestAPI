#!/usr/bin/env python
import os
from setuptools import setup, find_packages
import sys

_source_code_dir = '.'
__version__ = 1.0

sys.path.insert(0, _source_code_dir)

# -----------------------------------------------------------------------------


def _pkg_deps(list_of_deps):
    assert isinstance(list_of_deps, list), 'must be a list not {0}'\
                                           .format(type(list_of_deps))
    if len(list_of_deps) == 0:
        return 'Package :: Dependencies :: EMPTY_LIST_OF_DEPENDENCIES'
    else:
        return 'Package :: Dependencies :: {0}'\
               .format(' -- '.join(list_of_deps))
# -----------------------------------------------------------------------------


PKG_DEPENDENCIES = [
    'pytest',
	'tavern',
    'flask',
]

setup(
    # ===========================================================================
    # general information
    # ===========================================================================
    name='pt_m'.replace('_', '-'),
    version=__version__,
    description='PT_M',
    # ===========================================================================
    # package information
    # ===========================================================================
    package_dir={'': _source_code_dir},
    packages=find_packages(_source_code_dir),
    scripts=[],
    # ===========================================================================
    # installation
    # ===========================================================================
    zip_safe=False,
    install_requires=PKG_DEPENDENCIES,
    # ===========================================================================
    # meta data
    # ===========================================================================

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Test Engineers',
        'Operating System :: any',
        'Programming Language :: Python :: > 3.5',
    ],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', 'pt_m'.replace('_', '-')),
            'version': ('setup.py', '{0}'.format(__version__)),
            'release': ('setup.py', '{0}'.format(__version__)),
            'warning_is_error': ('setup.py', True),
        }
    },
)
