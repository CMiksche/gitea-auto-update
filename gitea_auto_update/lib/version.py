'''
Gitea Auto Updater

Copyright 2018, 2019, 2020 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import os
import logging
from packaging import version
import requests


def get_github_version_tag(api_url):
    """Get the version from github"""
    version_tag = requests.get(api_url).json()['tag_name']
    logging.info('Version: github_version_tag = %s', version_tag)
    return version_tag


def parse_file_version(string):
    """Get the version from a file"""
    return string.split(" ")[2]


def check_version(new_version, old_version):
    """Function to check if there is a new version"""
    return version.parse(new_version) > version.parse(old_version)


class Version:
    """Class to get and check the gitea version"""

    def __init__(self, gt_site, gt_file):
        self.gt_site = gt_site
        self.gt_file = gt_file

    def get_version_from_file(self):
        """Read the version from the gitea file"""
        version_string = os.popen(self.gt_file + " -v").read()
        return parse_file_version(version_string)

    def get_current_version(self):
        """Function to get the current version"""
        try:
            # Try to get the version from the file
            current_version = self.get_version_from_file()
        except IOError:
            # Get the version via the web api if the file does fail
            try:
                current_version = requests.get(self.gt_site).json()['version']
                if current_version.status_code != 200:
                    raise RuntimeError("Could not download version.") from None
            except RuntimeError:
                # To allow installation, return a default version of "0.0.0".
                current_version = "0.0.0"
        finally:
            logging.info('Version: current_version = %s', current_version)
        return current_version
