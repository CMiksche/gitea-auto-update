'''
Gitea Auto Updater

Copyright 2018, 2019, 2020 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import os
import sys
import logging
from shutil import which    # from whichcraft import which
import requests


def is_tool(name):
    """Function to check if tool is available"""
    # Check whether `name` is on PATH and marked as executable.
    return which(name) is not None


def download(url, file_name):
    """Function to download a file"""
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


def sha_check():
    """Check sha for gitea file"""
    sha_path = 'gitea.xz.sha256'
    if os.path.exists(sha_path):
        return os.system("sha256sum -c "+sha_path+" > /dev/null") == 0
    # return true because we don't have a sha file to check
    return True


class Download:
    """Class for downloading gitea"""

    def __init__(self, tmp_dir, github_version_tag, gt_system, gt_file):
        if not is_tool("xz"):
            logging.error('Download: missing dependency: xz')
            sys.exit()

        self.tmp_dir = tmp_dir
        self.github_version_tag = github_version_tag
        self.github_version = self.github_version_tag[1:]
        self.gt_system = gt_system
        self.gt_file = gt_file

        self.download_gitea_files()
        self.check_and_extract()

    def download_gitea_files(self):
        """Download gitea files"""
        # Set download url
        gt_download = 'https://github.com/go-gitea/gitea/releases/download/' \
                      + self.github_version_tag + '/gitea-' + self.github_version \
                      + '-' + self.gt_system + '.xz'
        logging.info('Download: Gitea file: %s', gt_download)
        sha_download = gt_download + '.sha256'
        logging.info('Download: SHA file: %s', sha_download)

        # Download file
        logging.info('Download: downloading sha256 hashsum')
        download(sha_download, self.tmp_dir + 'gitea.xz.sha256')
        logging.info('Download: downloading %s', self.github_version_tag + 'gitea.xz')
        self.tmp_xz = self.tmp_dir + 'gitea-' + self.github_version + '-' + self.gt_system + '.xz'
        download(gt_download, self.tmp_xz)

    def extract_file(self):
        """Extract gitea file"""
        logging.info('Download: sha ok, extracting file to location')
        # extracting download file
        cmd = "xz -d " + self.tmp_xz
        os.system(cmd)
        #  copying temp file to gtfile location.
        #  Copying preserves SELinux permissions, see issue #22
        cmd = 'cp ' + self.tmp_dir + 'gitea-' + self.github_version \
              + '-' + self.gt_system + ' ' + self.gt_file
        os.system(cmd)
        # cleaning up tmp file
        cmd = 'rm -f ' + self.tmp_dir + 'gitea-' + self.github_version + '-' + self.gt_system
        os.system(cmd)
        cmd = 'chmod +x ' + self.gt_file
        os.system(cmd)

    def check_and_extract(self):
        """Check file and extract"""
        os.chdir(self.tmp_dir)
        if sha_check():
            self.extract_file()
        else:
            logging.error('Download: error: sha256sum failed')
            sys.exit()
