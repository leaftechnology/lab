# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in lab/__init__.py
from lab import __version__ as version

setup(
	name='lab',
	version=version,
	description='My Lab',
	author='sammish',
	author_email='sammish.thundiyil@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
