'''
Gitea Auto Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import logging
import configparser
import fire
import update

def updater(settings='settings.ini'):
    # Config
    config = configparser.ConfigParser()
    config.read(settings)
    # Create a log file
    logging.basicConfig(filename=config.get('Gitea', 'logFile'), level=logging.DEBUG)
    # Start update
    update.Update(config.get('Gitea', 'site'),
                  config.get('Gitea', 'file'),
                  config.get('Gitea', 'sourceDir'),
                  config.get('Gitea', 'apiUrl'),
                  config.get('Gitea', 'buildFromSource'),
                  config.get('Gitea', 'tmpDir'),
                  config.get('Gitea', 'system'))

def main():
    fire.Fire(updater)

if __name__ == '__main__':
  main()