'''
Gitea Auto Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import os
import sys
import logging
import configparser
import fire
import gitea_auto_update.lib.version
import gitea_auto_update.lib.download
import gitea_auto_update.lib.build

class Update:

    def __init__(self, gtSite, gtFile, sourceDir, apiUrl, buildFromSource, tmpDir, gtSystem):
        self.gtSite = gtSite
        self.gtFile = gtFile
        self.sourceDir = sourceDir
        self.apiUrl = apiUrl
        self.buildFromSource = buildFromSource
        self.tmpDir = tmpDir
        self.gtSystem = gtSystem

        self.initVersionAndBuild()
        self.getVersionAndTag()
        self.checkAndUpdate()

    def initVersionAndBuild(self):
        self.version = gitea_auto_update.lib.version.Version(self.gtSite, self.gtFile)
        self.build = gitea_auto_update.lib.build.Build(self.gtFile, self.sourceDir)

    def getVersionAndTag(self):
        self.currentVersion = self.version.getCurrentVersion()                  # Version from gitea site
        self.githubVersionTag = self.version.getGithubVersionTag(self.apiUrl)   # Get version tag from github and remove first char (v)
        self.githubVersion = self.githubVersionTag[1:]                          # Get version from version tag

    def doUpdate(self):
        if self.buildFromSource:                                                # Should the new version be build from source?
            self.build.fromSource(self.githubVersionTag)
        else:
            self.download = gitea_auto_update.lib.download.Download(self.tmpDir,
                                              self.githubVersion,
                                              self.githubVersionTag,
                                              self.gtSystem,
                                              self.gtFile)

    def checkAndUpdate(self):
        if self.version.checkVersion(self.githubVersion, self.currentVersion):        # Check if there is a new version
            logging.info('Update: new version available, stopping service')
            os.system("systemctl stop gitea.service")
            self.doUpdate()
            logging.info('Update: starting gitea.service')
            os.system("systemctl start gitea.service")
            print("update successfully")
        else:
            print("current version is uptodate")

def updater(settings='settings.ini'):
    # Config
    config = configparser.ConfigParser()
    config.read(settings)
    # Create a log file
    logging.basicConfig(filename=config.get('Gitea', 'logFile'), level=logging.DEBUG)
    # Start update
    Update(config.get('Gitea', 'site'),
                  config.get('Gitea', 'file'),
                  config.get('Gitea', 'sourceDir'),
                  config.get('Gitea', 'apiUrl'),
                  config.get('Gitea', 'buildFromSource'),
                  config.get('Gitea', 'tmpDir'),
                  config.get('Gitea', 'system'))


def main():
    if not sys.version_info[0] == 3:
        sys.exit("Sorry, Python 2 is not supported. Please update to Python 3.")
    fire.Fire(updater)


if __name__ == '__main__':
  main()