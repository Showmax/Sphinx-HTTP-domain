"""Python package setup."""
from __future__ import unicode_literals, with_statement

import io
import os

from setuptools import find_packages, setup

PROJECT_NAME = 'sphinx_http_domain'

#
# Import PIP requirements parser. It is an unpublished interface
# that changed location with PIP version 10.0.0
#
try:
    from pip._internal.download import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.download import PipSession
    from pip.req import parse_requirements


def get_file_contents(filename):
    """Return file contents."""
    file_path = os.path.join(
        os.path.realpath(os.path.dirname(__file__)), filename)

    with io.open(file_path, encoding='utf-8') as fd:
        return fd.read().strip().replace('\r', '')


def get_requirements(requirements):
    """Return an array of requirements."""
    req_path = os.path.join(
        os.path.realpath(os.path.dirname(__file__)), requirements)

    return [str(item.req) for item in
            parse_requirements(req_path, session=PipSession())]


setup(
    name=PROJECT_NAME,
    version=get_file_contents('VERSION'),
    description='Sphinx domain to mark up RESTful web services in ReST',
    long_description=get_file_contents('README.rst'),
    long_description_content_type='text/markdown',
    url='https://github.com/deceze/Sphinx-HTTP-domain/',
    author='David Zentgraf',
    author_email='deceze@gmail.com',
    packages=find_packages(),
    # requires=['Sphinx (>=1.0.7)', 'six (>=1.1.0)'],
    zip_safe=True,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Topic :: Software Development :: Documentation'
    ],
    install_requires=get_requirements('requirements.txt'),
    platforms=['any'],
    license='Software License Agreement (BSD License)',
)
