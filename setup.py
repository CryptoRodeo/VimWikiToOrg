#!/usr/bin/env python

from os import walk
from os.path import join, relpath

from setuptools import find_packages, setup


version = "1.2.0"

entry_points = {
    'console_scripts': [
        'vimwki_to_org = vimwiki_to_org.__main__:main'
    ]
}

README = open('README.md', encoding='utf-8').read()

description = README

setup(
    name='vimwiki_to_org',
    version=version,
    url='https://github.com/CryptoRodeo/VimWikiToOrg',
    author='Bryan Ramos',
    author_email='bryan.ramos@hey.com',
    description="Converts vimwiki files to org mode",
    project_urls={
        'Source': 'https://github.com/CryptoRodeo/VimWikiToOrg',
        'Tracker': 'https://github.com/CryptoRodeo/VimWikiToOrg/issues',
    },
    keywords='vimwiki orgmode convert',
    license='GPLv3',
    long_description=description,
    packages=find_packages(),
    entry_points=entry_points,
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    ],
    test_suite='vimwiki_to_org.tests',
)
