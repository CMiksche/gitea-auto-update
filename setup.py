import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='gitea_auto_update',
      version='2.0.5',
      description='A script which can update gitea to a new version.',
      long_description=long_description,
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