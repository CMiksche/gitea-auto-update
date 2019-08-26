'''
Gitea Auto Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
from packaging import version
import os
import requests
import logging

class Version:

    def __init__(self, gtSite, gtFile):
        self.gtSite = gtSite
        self.gtFile = gtFile

    def checkVersion(self, newVersion, oldVersion):
        # Function to check if there is a new version
        return version.parse(newVersion) > version.parse(oldVersion)

    def parseFileVersion(self, string):
        return string.split(" ")[2]

    def getVersionFromFile(self):
        versionString = os.popen(self.gtFile + " -v").read()
        return self.parseFileVersion(versionString)

    def getCurrentVersion(self):
        # Function to get the current version
        try:
            # Try to get the version from the file
            currentVersion = self.getVersionFromFile()
        except:
            # Get the version via the web api if the file does fail
            currentVersion = requests.get(self.gtSite).json()['version']
            if currentVersion.status_code != 200:
                currentVersion = self.getVersionFromFile()
        finally:
            logging.info('Version: current_version = %s', currentVersion)
            return currentVersion

    def getGithubVersionTag(self, apiUrl):
        versionTag = requests.get(apiUrl).json()['tag_name']
        logging.info('Version: github_version_tag = %s', versionTag)
        return versionTag