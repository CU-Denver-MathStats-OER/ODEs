#!/usr/bin/env python

from distutils.core import setup

setup(name='utils',
      version='1.0',
      description='utilities for ODEs',
      author='Adam Spiegler, Jonathon Hirschi, Troy Butler',
      author_email='troy.butler@ucdenver.edu',
      url='https://github.com/eecsu/ODEs',
      packages=['utils'],
      install_requires=['matplotlib', 'scipy',
                        'numpy']
      )