# Gitea Remote Updater

Script for a automatic update of gitea. Should be run locally on the gitea server.

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
  sudo pip install requests
  ```

2. Then clone the git repository.

3. After that, please change the variables in the settings.py file.

4. Enter the command `python updater.py` in your commandline.

5. If you want to schedule your updates, edit your /etc/crontab file.
