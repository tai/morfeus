from setuptools import setup

setup(name='morfeus',
      version='0.2',
      description='Library to control moRFeus mixer/signal generator',
      url='http://github.com/tai/morfeus',
      author='Taisuke Yamada',
      author_email='tai.nospam@nospam.rakugaki.org',
      license='MIT',
      packages=['morfeus'],
      scripts = ['bin/morfeus'],
      zip_safe=False)
