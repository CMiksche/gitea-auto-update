# Gitea Auto Update

[![Build Status](https://cloud.drone.io/api/badges/CMiksche/gitea-auto-update/status.svg)](https://cloud.drone.io/CMiksche/gitea-auto-update)
[![PyPI version](https://badge.fury.io/py/gitea-auto-update.svg)](https://badge.fury.io/py/gitea-auto-update)
[![Downloads](https://pepy.tech/badge/gitea-auto-update)](https://pepy.tech/project/gitea-auto-update)
![GitHub](https://img.shields.io/github/license/cmiksche/gitea-auto-update?style=flat)
[![Twitter Follow](https://img.shields.io/twitter/follow/cmiksche?style=social)](https://twitter.com/cmiksche)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/106336578279256330?domain=https%3A%2F%2Fmastodon.social&style=social)](https://mastodon.social/@cmiksche)

Script for an automatic update of gitea. Should be run locally on the gitea server. Has options for updating via new binary file or build from source.

## Want to update more?

> If you want to update Gitea and other software (like Drone, Caddy, Podman, Python, Zitadel and Kanboard), you should check out [Autoupdate](https://chapati.systems/autoupdate/).
>
> This new tool of mine was built as a single binary with a config file and tested on multiple Linux systems.

## Procedure
* Get Gitea Version from the Gitea CLI and if that fails from the Gitea API
* Get latest Release via GitHub API
* Check if there is a newer Version
* If there is a newer Version:
    * If binary file was selected:
        * Download new version
        * Check sha256
        * Overwrite old version
    * If build from source is active:
        * Checkout new release branch
        * Build binary
        * Overwrite old binary


## General Information
License: GNU General Public License

Author: Christoph Daniel Miksche (m5e.de)

Uses python version 3


## Dependencies
Ensure `pip3`, `setuptools`, `xz-utils` and `wheel` dependencies are installed on the system you are running this script in. (Most Linux OS like Ubuntu or Debian come with these pre-installed)

## Installation

Create a settings.ini file on your system. Example:

  ````
[Gitea]
site=https://your-gitea-instance.com/api/v1/version
apiUrl=https://api.github.com/repos/go-gitea/gitea/releases/latest
system=linux-amd64
file=/usr/local/bin/gitea
tmpDir=/tmp/
buildFromSource=
sourceDir=
logFile=update.log
  ````

Use the following command to install gitea-auto-update.

  ```
  sudo pip3 install gitea-auto-update
  ```

Enter the command `gitea-auto-update --settings=/path/to/settings.ini` in your commandline.

If you want to schedule your updates, edit your /etc/crontab file.

## Tutorials

* English: http://blog.m5e.de/gitea/update/upgrade/bash/script/2018/11/26/gitea-auto-update-script.html
* German: https://blog.wronnay.net/automatische-gitea-updates/

## Development

The following instructions help you for developing.

* Check out the [Contribution Guidelines](CONTRIBUTING.md).
* Clone this git repo
* Install pipenv: `pip install pipenv`
* Install all dependencies: `pipenv install`
* Install git pre-commit hooks (for pylint and gitlint) with `pre-commit install`
* You can run the tests with `python -m unittest`
* After pushing, you should check the build status which currently checks the tests, pylint and the commit message format.

### Notes

The following steps are automatically executed via pre-commit hooks.

* You can run pylint with `pylint gitea_auto_update`
* After changes and commit, you can check if your commit message follows the contribution guidelines with `gitlint`. If there is a problem, gitlint will show you a error message.

## Contributors

See https://github.com/CMiksche/gitea-auto-update/graphs/contributors

Thank you for your support!

Interested in contributing to this project? Check out the [Contribution Guidelines](CONTRIBUTING.md).
