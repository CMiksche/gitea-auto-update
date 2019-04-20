'''
Gitea Remote Updater

Copyright 2018 Christoph Daniel Miksche
All rights reserved.

License: GNU General Public License
'''
import settings
import requests
import os
import functions

# Version from gitea site
current_version = requests.get(settings.gtsite).json()['version']

# Get version tag from github and remove first char (v)
github_version_tag = requests.get(settings.gtgithubapiurl).json()['tag_name']

# Get version from version tag
github_version = github_version_tag[1:]

# Check if there is a new version
if functions.checkVersion(github_version, current_version):

    # Stop systemd service
    os.system("systemctl stop gitea.service")

    # Should the new version be build from source?
    if settings.build_from_source:

        functions.buildFromSource(github_version_tag)

    else:

        # Set download url
        gtdownload = 'https://github.com/go-gitea/gitea/releases/download/'+github_version_tag+'/gitea-'+github_version+'-'+settings.gtsystem

        # Download file
        functions.download(gtdownload, settings.gtfile)

    # Start systemd service
    os.system("systemctl start gitea.service")
