# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in chdnext_greek_support/__init__.py
from chdnext_greek_support import __version__ as version

setup(
	name='chdnext_greek_support',
	version=version,
	description='ChD Computers erpnext Greek support',
	author='ChD Computers',
	author_email='chdcomputers@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
