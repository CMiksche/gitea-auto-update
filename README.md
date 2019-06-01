# Gitea Auto Updater

[![Build Status](https://travis-ci.org/CMiksche/gitea-auto-update.svg?branch=master)](https://travis-ci.org/CMiksche/gitea-auto-update)

Script for a automatic update of gitea. Should be run locally on the gitea server. Has options for updating via new binary file or build from source.

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

## Installation

1. Use the following command to install all dependencies.

  ```
  sudo pip install requests packaging
  ```

2. Then clone the git repository.

3. After that, please change the variables in the settings.py file.

4. Enter the command `python updater.py` in your commandline.

5. If you want to schedule your updates, edit your /etc/crontab file.

## Tutorials

* English: http://blog.m5e.de/gitea/update/upgrade/bash/script/2018/11/26/gitea-auto-update-script.html
* German: https://blog.wronnay.net/automatische-gitea-updates/

## Contributors

 - [@Eideen](https://github.com/Eideen)

Thank you for your support!

Interested in contributing to this project? Check out the [Contribution Guidelines](CONTRIBUTING.md).
