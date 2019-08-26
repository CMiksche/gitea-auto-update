from setuptools import setup

setup(name='gitea_auto_update',
      version='2.0.0',
      description='A script which can update gitea to a new version.',
      url='https://github.com/CMiksche/gitea-auto-update',
      author='Christoph Miksche',
      author_email='christoph@miksche.org',
      license='GPLv3',
      classifiers=[
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: Unix",
      ],
      keywords=['gitea', 'update', 'debian', 'linux'],
      install_requires=[
            'requests',
            'packaging',
            'fire'
      ],
      packages=['update'],
      entry_points={
          'console_scripts': ['gitea-auto-update=update.__init__:main'],
      }
      )