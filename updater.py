'''
Gitea Remote Updater

Copyright 2018 Christoph Daniel Miksche
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

# Version from gitea site
current_version = requests.get(settings.gtsite).json()['version']

# Get version tag from github and remove first char (v)
github_version_tag = requests.get(settings.gtgithubapiurl).json()['tag_name']

# Get version from version tag
github_version = github_version_tag[1:]

# Check if there is a new version
if github_version > current_version:

    # Stop systemd service
    os.system("systemctl stop gitea.service")

    # Set download url
    gtdownload = 'https://github.com/go-gitea/gitea/releases/download/'+github_version_tag+'/gitea-'+github_version+'-'+settings.gtsystem

    # Download file
    download(gtdownload, settings.gtfile)

    # Start systemd service
    os.system("systemctl start gitea.service")
