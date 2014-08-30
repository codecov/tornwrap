#!/usr/bin/env python
from setuptools import setup

classifiers = ["Development Status :: 4 - Beta",
               "Environment :: Plugins",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: Apache Software License",
               "Topic :: Software Development :: Testing"]

setup(name='tornwrap',
      version="0.0.8",
      description="tornado decorators and basics: @authenticated @ratelimited @validated ErrorHandler",
      long_description=None,
      classifiers=classifiers,
      keywords='tornado tornadoweb decorators wrapper authenticated rate limited validate error handle',
      author='@stevepeak',
      author_email='steve@stevepeak.net',
      url='http://github.com/stevepeak/tornwrap',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=['tornwrap'],
      include_package_data=True,
      zip_safe=True,
      install_requires=["tornado>=4.0.0", "valideer>=0.3.1", "timestring>=1.6.1"],
      entry_points=None)
