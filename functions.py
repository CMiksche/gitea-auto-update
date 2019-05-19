'''
Gitea Remote Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import settings
import requests
import os

# Function to download a file
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)

# Function to build the new version from source
def buildFromSource(tag):
    # Change to source dir
    os.chdir(settings.source_dir)
    # Checkout master
    os.system("git checkout master")
    # Update
    os.system("git pull")
    # Checkout relase branch
    os.system("git checkout "+tag)
    # Build from source
    os.system('TAGS="bindata sqlite sqlite_unlock_notify" make generate build')
    # Move binary
    os.system("mv gitea "+settings.gtfile)

# Function to check if there is a new version
def checkVersion(new_version, old_version):

    from packaging import version

    return version.parse(new_version) > version.parse(old_version)

# Function to check if tool is available
def is_tool(name):
    ##Check whether `name` is on PATH and marked as executable.

    # from whichcraft import which
    from shutil import which

    return which(name) is not None
