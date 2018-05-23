from __future__ import unicode_literals, with_statement

from distutils.core import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='sphinx-http-domain',
    version='0.3',
    description='Sphinx domain to mark up RESTful web services in ReST',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/deceze/Sphinx-HTTP-domain/',
    author='David Zentgraf',
    author_email='deceze@gmail.com',
    packages=['sphinx_http_domain'],
    requires=['Sphinx (>=1.0.7)', 'six (>=1.1.0)'],
    zip_safe=True,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Topic :: Software Development :: Documentation'],
)
