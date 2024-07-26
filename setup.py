#! /usr/bin/env python
#
# Copyright (C) 2022 Kacper Sokol <kacper@xmlx.dev>
# License: MIT

import re
from pathlib import Path
from setuptools import find_packages, setup

def dependencies_from_file(file_path):
    required = []
    with open(file_path) as f:
        for l in f.readlines():
            l_c = l.strip()
            # Get not empty lines and ones that do not start with Python
            # comment "#" (preceded by any number of white spaces)
            if l_c and not l_c.startswith('#'):
                required.append(l_c)
    return required

def get_dependency_version(dependency, list_of_dependencies):
    matched_dependencies = []

    reformatted_dependency = dependency.lower().strip()
    for dep in list_of_dependencies:
        dependency_version = re.split('~=|==|!=|<=|>=|<|>|===', dep)
        if dependency_version[0].lower().strip() == reformatted_dependency:
            matched_dependencies.append(dep)

    if not matched_dependencies:
        raise NameError(f'{dependency} dependency could not be found in the '
                        'list of dependencies.')

    return matched_dependencies

def get_version():
    """Retrieves package version."""
    version = [
        line
        for line in Path('xml_book/__init__.py').read_text().split('\n')
        if '__version__' in line
    ]
    assert len(version) == 1, 'Only one version assignment expected.'
    version = version[0].split(' = ')[-1].strip("'")
    return version

DISTNAME = 'XML-Book-Code'
PACKAGE_NAME = 'xml_book'
VERSION = get_version()
DESCRIPTION = ('A Python library implementing a collection of modules used by '
               'the eXplainable Machine Learning book')
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Kacper Sokol'
MAINTAINER_EMAIL = 'kacper@xmlx.dev'
URL = 'https://github.com/xmlx-dev/xml-book-code/'
DOWNLOAD_URL = 'https://github.com/xmlx-dev/xml-book-code/releases'
# DOWNLOAD_URL = f'https://pypi.org/project/{DISTNAME}/#files'
LICENSE = 'MIT'
PACKAGES = find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests'])
INSTALL_REQUIRES = dependencies_from_file('requirements.txt')
# Python 3.7 and up but not commited to Python 4 support yet
PYTHON_REQUIRES = '~=3.7'
INCLUDE_PACKAGE_DATA = True
#ZIP_SAFE = False

def setup_package():
    metadata = dict(name=DISTNAME,
                    maintainer=MAINTAINER,
                    maintainer_email=MAINTAINER_EMAIL,
                    description=DESCRIPTION,
                    license=LICENSE,
                    url=URL,
                    download_url=DOWNLOAD_URL,
                    version=VERSION,
                    install_requires=INSTALL_REQUIRES,
                    long_description=LONG_DESCRIPTION,
                    include_package_data=INCLUDE_PACKAGE_DATA,
                    python_requires=PYTHON_REQUIRES,
                    # zip_safe=ZIP_SAFE,
                    packages=PACKAGES)

    setup(**metadata)

if __name__ == '__main__':
    setup_package()
