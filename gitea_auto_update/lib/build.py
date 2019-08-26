'''
Gitea Auto Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import os

class Build:

    def __init__(self, gtFile, sourceDir):
        self.gtFile = gtFile
        self.sourceDir = sourceDir

    def fromSource(self, tag):
        # Function to build the new version from source
        os.chdir(self.sourceDir)
        os.system("git checkout master")
        os.system("git pull")
        os.system("git checkout " + tag)
        os.system('TAGS="bindata sqlite sqlite_unlock_notify" make generate build')
        os.system("mv gitea " + self.gtFile)