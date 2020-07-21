# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in promise/__init__.py
from promise import __version__ as version

setup(
	name='promise',
	version=version,
	description='Promantia Manageemnt Information System on ERPNext',
	author='Promantia Business Solutions Pvt. Ltd.',
	author_email='hari.madhavan@promantia.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
