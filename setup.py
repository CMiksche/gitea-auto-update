'''
Gitea Auto Updater

Copyright 2018, 2019, 2020, 2021, 2022 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='gitea_auto_update',
    version='2.0.11',
    description='A script which can update gitea to a new version.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/CMiksche/gitea-auto-update',
    author='Christoph Miksche',
    author_email='christoph@miksche.org',
    license='GPLv3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
    ],
    keywords=['gitea', 'update', 'debian', 'linux'],
    python_requires='>=3',
    install_requires=[
        'requests',
        'packaging',
        'fire',
        'configparser'
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['gitea-auto-update=gitea_auto_update.update:main'],
    }
)
