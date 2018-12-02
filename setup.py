# -*- coding: utf-8-unix -*-
#
# for user:
# python setup.py install
#
# for maintainer:
# python setup.py sdist upload -r https://test.pypi.org/legacy/
# python setup.py sdist upload
#

from setuptools import setup

# use README.md for long_description
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='morfeus',
      version='0.3',
      description='Library to control moRFeus mixer/signal generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/tai/morfeus',
      author='Taisuke Yamada',
      author_email='tai.nospam@nospam.rakugaki.org',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Communications :: Ham Radio",
          "Topic :: System :: Hardware :: Hardware Drivers",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Telecommunications Industry"
      ],
      packages=['morfeus'],
      scripts = ['bin/morfeus'],
      install_requires=['hidapi', 'argparse'],
      zip_safe=False)
