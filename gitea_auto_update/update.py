'''
Gitea Auto Updater

Copyright 2018, 2019, 2020 The Gitea-Auto-Update Authors
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
    """
    Main class to update gitea
    """

    def __init__(self,
                 config):
        self.config = config

        # Get version tag from github and remove first char (v)
        self.github_version_tag = gitea_auto_update.lib.version.get_github_version_tag(
            config.get('Gitea', 'apiUrl')
        )
        # Get version from version tag
        self.github_version = self.github_version_tag[1:]

        self.check_and_update()

    def do_update(self):
        """Execute the update"""

        # Should the new version be build from source?
        if self.config.get('Gitea', 'buildFromSource'):
            gitea_auto_update.lib.build.build_from_source(
                self.github_version_tag,
                self.config.get('Gitea', 'file'),
                self.config.get('Gitea', 'sourceDir')
            )
        else:
            gitea_auto_update.lib.download.Download(
                self.config.get('Gitea', 'tmpDir'),
                self.github_version_tag,
                self.config.get('Gitea', 'system'),
                self.config.get('Gitea', 'file')
            )

    def check_and_update(self):
        """Check if a update is possible and do it if it is"""
        # Version from gitea site
        version = gitea_auto_update.lib.version.Version(
            self.config.get('Gitea', 'site'),
            self.config.get('Gitea', 'file')
        )
        current_version = version.get_current_version()
        # Check if there is a new version
        if gitea_auto_update.lib.version.check_version(self.github_version, current_version):
            logging.info('Update: new version available, stopping service')
            os.system("systemctl stop gitea.service")
            self.do_update()
            logging.info('Update: starting gitea.service')
            os.system("systemctl start gitea.service")
            print("update successfully")
        else:
            print("current version is uptodate")


def updater(settings='settings.ini'):
    """Get the config and set logging"""
    # Config
    config = configparser.ConfigParser()
    config.read(settings)
    # Create a log file
    logging.basicConfig(filename=config.get('Gitea', 'logFile'), level=logging.DEBUG)
    # Start update
    Update(config)


def main():
    """Main func"""
    if not sys.version_info[0] == 3:
        sys.exit("Sorry, Python 2 is not supported. Please update to Python 3.")
    fire.Fire(updater)


if __name__ == '__main__':
    main()
