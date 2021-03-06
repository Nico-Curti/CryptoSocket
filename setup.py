#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import platform
import multiprocessing

try:
  from setuptools import setup
  from setuptools import Extension
  from setuptools import find_packages

except ImportError:
  from distutils.core import setup
  from distutils.core import Extension
  from distutils.core import find_packages

from CryptoSocket.build import get_requires
from CryptoSocket.build import cryptosocket_build_ext
from CryptoSocket.build import read_description

here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
NAME = 'CryptoSocket'
DESCRIPTION = 'Python Wrap for TCP/IP Client Server with RSA cryptography'
URL = 'https://github.com/Nico-Curti/CryptoSocket'
EMAIL = 'nico.curti2@unibo.it'
AUTHOR = 'Nico Curti'
REQUIRES_PYTHON = '>=2.7'
VERSION = None
KEYWORDS = "socket cryptography RSA"

CPP_COMPILER = platform.python_compiler()
README_FILENAME = os.path.join(here, 'README.md')
REQUIREMENTS_FILENAME = os.path.join(here, 'requirements.txt')
VERSION_FILENAME = os.path.join(here, 'CryptoSocket', '__version__.py')

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
  LONG_DESCRIPTION = read_description(README_FILENAME)

except FileNotFoundError:
  LONG_DESCRIPTION = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
  with open(VERSION_FILENAME) as fp:
    exec(fp.read(), about)

else:
  about['__version__'] = VERSION

# parse version variables and add them to command line as definitions
Version = about['__version__'].split('.')

# Set compiler variables

define_args = [ '-DMAJOR={}'.format(Version[0]),
                '-DMINOR={}'.format(Version[1]),
                '-DREVISION={}'.format(Version[2])
              ]


compile_args = [ '-std=c++11', # std
                 '-g0', # disable debug mode
                 '-Wno-unused-function', # disable unused-function warnings
                 '-Wno-narrowing', # disable narrowing conversion warnings
                  # enable common warnings flags
                 '-Wall',
                 '-Wextra',
                 '-Wno-unused-result',
                 '-Wno-unknown-pragmas',
                 '-Wfatal-errors',
                 '-Wpedantic',
                 '-march=native'
               ]

whole_compiler_args = [ *compile_args, *define_args ]


setup(
  name                          = NAME,
  version                       = about['__version__'],
  description                   = DESCRIPTION,
  long_description              = LONG_DESCRIPTION,
  long_description_content_type = 'text/markdown',
  author                        = AUTHOR,
  author_email                  = EMAIL,
  maintainer                    = AUTHOR,
  maintainer_email              = EMAIL,
  python_requires               = REQUIRES_PYTHON,
  install_requires              = get_requires(REQUIREMENTS_FILENAME),
  url                           = URL,
  download_url                  = URL,
  keywords                      = KEYWORDS,
  packages                      = find_packages(include=['CryptoSocket', 'CryptoSocket.*'], exclude=('test', 'testing', 'examples')),
  #include_package_data          = True, # no absolute paths are allowed
  platforms                     = 'any',
  classifiers                   =[
                                   #'License :: OSI Approved :: GPL License',
                                   'Programming Language :: Python',
                                   'Programming Language :: Python :: 3',
                                   'Programming Language :: Python :: 3.6',
                                   'Programming Language :: Python :: Implementation :: CPython',
                                   'Programming Language :: Python :: Implementation :: PyPy'
                                 ],
  license                       = 'MIT',
  cmdclass                      = {'build_ext': cryptosocket_build_ext},
  ext_modules                   = [Extension( name='.'.join(['lib', 'Crypto', 'Decrypter']),
                                              sources=['./CryptoSocket/Crypto/source/decrypter.pyx',
                                                       './cpp/src/Decrypter.cpp'
                                                       ],
                                              include_dirs=[ './cpp/include/', './CryptoSocket/Crypto/include'],
                                              libraries=[],
                                              library_dirs=[
                                                            os.path.join(here, 'lib'),
                                                            os.path.join('usr', 'lib'),
                                                            os.path.join('usr', 'local', 'lib'),
                                              ],  # path to .a or .so file(s)
                                              extra_compile_args = whole_compiler_args,
                                              extra_link_args = [],
                                              language='c++'
                                              ),
                                   Extension( name='.'.join(['lib', 'Crypto', 'Encrypter']),
                                              sources=['./CryptoSocket/Crypto/source/encrypter.pyx',
                                                       './cpp/src/Encrypter.cpp'
                                                       ],
                                              include_dirs=[ './cpp/include/', './CryptoSocket/Crypto/include'],
                                              libraries=[],
                                              library_dirs=[
                                                            os.path.join(here, 'lib'),
                                                            os.path.join('usr', 'lib'),
                                                            os.path.join('usr', 'local', 'lib'),
                                              ],  # path to .a or .so file(s)
                                              extra_compile_args = whole_compiler_args,
                                              extra_link_args = [],
                                              language='c++'
                                              ),
                                   Extension( name='.'.join(['lib', 'Crypto', 'RSA']),
                                              sources=['./CryptoSocket/Crypto/source/rsa.pyx',
                                                       './cpp/src/RSA.cpp'
                                                       ],
                                              include_dirs=[ './cpp/include/', './CryptoSocket/Crypto/include'],
                                              libraries=[],
                                              library_dirs=[
                                                            os.path.join(here, 'lib'),
                                                            os.path.join('usr', 'lib'),
                                                            os.path.join('usr', 'local', 'lib'),
                                              ],  # path to .a or .so file(s)
                                              extra_compile_args = whole_compiler_args,
                                              extra_link_args = [],
                                              language='c++'
                                              ),
  ],
)
