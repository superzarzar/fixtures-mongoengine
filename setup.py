#!/usr/bin/env python
from setuptools import setup

setup(name='fixtures_mongoengine',
      version='1.3.1',
      description='MongoEngine Fixtures.',
      author='Vitaly Nikitin',
      author_email='alaris.nik@gmail.com',
      url='https://github.com/coderfly/fixtures-mongoengine/',
      download_url='https://github.com/coderfly/fixtures-mongoengine/tarball/1.3.1',
      install_requires=['six', 'mongoengine>=0.8.6'],
      packages=['fixtures_mongoengine'],
      keywords=['testing', 'fixtures', 'mongoengine']
      )
