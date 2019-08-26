'''
Gitea Auto Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import os
import logging
from update import version, download, build


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

    def initVersionAndBuild(self):
        self.version = version.Version(self.gtSite, self.gtFile)
        self.build = build.Build(self.gtFile, self.sourceDir)

    def getVersionAndTag(self):
        self.currentVersion = self.version.getCurrentVersion()                  # Version from gitea site
        self.githubVersionTag = self.version.getGithubVersionTag(self.apiUrl)   # Get version tag from github and remove first char (v)
        self.githubVersion = self.githubVersionTag[1:]                          # Get version from version tag

    def doUpdate(self):
        if self.buildFromSource:                                                # Should the new version be build from source?
            build.fromSource(self.githubVersionTag)
        else:
            self.download = download.Download(self.tmpDir,
                                              self.githubVersion,
                                              self.githubVersionTag,
                                              self.gtSystem,
                                              self.gtFile)

    def checkAndUpdate(self):
        if version.checkVersion(self.githubVersion, self.currentVersion):        # Check if there is a new version
            logging.info("new version available, stopping service")
            os.system("systemctl stop gitea.service")
            self.doUpdate()
            logging.info("starting gitea.service")
            os.system("systemctl start gitea.service")
            print("update successfully")
        else:
            print("current version is uptodate")
