'''
Gitea Auto Updater

Copyright 2018, 2019, 2020 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import os


def build_from_source(tag, gt_file, source_dir):
    """Function to build the new version from source"""
    os.chdir(source_dir)
    os.system("git checkout main")
    os.system("git pull")
    os.system("git checkout " + tag)
    os.system('TAGS="bindata sqlite sqlite_unlock_notify" make generate build')
    os.system("cp gitea " + gt_file)
    os.system("rm -f gitea")
