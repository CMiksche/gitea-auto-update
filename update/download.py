'''
Gitea Auto Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import requests
import os
import logging
from shutil import which    # from whichcraft import which


class Download:

    def __init__(self, tmpDir, githubVersion, githubVersionTag, gtSystem, gtFile):
        if not self.isTool("xz"):
            logging.error("missing dependency: xz")
            quit()

        self.tmpDir = tmpDir
        self.githubVersion = githubVersion
        self.githubVersionTag = githubVersionTag
        self.gtSystem = gtSystem
        self.gtFile = gtFile

        self.downloadGiteaFiles()
        self.checkAndExtract()

    def isTool(name):
        # Function to check if tool is available
        ##Check whether `name` is on PATH and marked as executable.
        return which(name) is not None

    def download(self, url, fileName):
        # Function to download a file
        # open in binary mode
        with open(fileName, "wb") as file:
            # get request
            response = requests.get(url)
            # write to file
            file.write(response.content)

    def downloadGiteaFiles(self):
        # Set download url
        gtDownload = 'https://github.com/go-gitea/gitea/releases/download/' + self.githubVersionTag + '/gitea-' + self.githubVersion + '-' + self.gtSystem + '.xz'
        logging.info('Gitea file: %s', gtDownload)
        shaDownload = gtDownload + '.sha256'
        logging.info('SHA file: %s', shaDownload)

        # Download file
        logging.info("downloading sha256 hashsum")
        self.download(shaDownload, self.tmpDir + 'gitea.xz.sha256')
        logging.info("downloading %s", self.githubVersionTag + 'gitea.xz')
        self.tmpXz = self.tmpDir +'gitea-' + self.githubVersion + '-' + self.gtSystem + '.xz'
        self.download(gtDownload, self.tmpXz)

    def shaCheck(self):
        return os.system("sha256sum -c gitea.xz.sha256 > /dev/null") == 0

    def extractFile(self):
        logging.info("sha ok, extracting file to location")
        # extracting download file
        cmd = "xz -d " + self.tmpXz
        logging.info(cmd)
        os.system(cmd)
        #  moving temp file to gtfile location
        cmd = 'mv ' + self.tmpDir + 'gitea-' + self.githubVersion + '-' + self.gtSystem + ' ' + self.gtFile
        logging.info(cmd)
        os.system(cmd)

    def checkAndExtract(self):
        os.chdir(self.tmpDir)
        if self.shaCheck():
            self.extractFile()
        else:
            logging.error("error: sha256sum failed")
            quit()