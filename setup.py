# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split(' ')

setup(
	name='file extractor',
	version=1.0,
	description='Extract file',
	author='VinayPrabhu',
	author_email='vinay335csprabhu@gmail.com',
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
