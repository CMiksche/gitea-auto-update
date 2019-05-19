# Gitea Remote Updater

Script for a automatic update of gitea. Should be run locally on the gitea server. Has options for updating via new binary file or build from source.

## Procedure
* Get Gitea Version via Gitea API
* Get latest Relase via GitHub API
* Check if there is a newer Version
* If true
    * Download new version, overwrite old version

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
