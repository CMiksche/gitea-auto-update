'''
Gitea Remote Updater

Copyright 2018, 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
# Gitea Site
gtsite = 'https://your-gitea-instance.com/api/v1/version'
# Gitea GitHub API URL for latest Relase
gtgithubapiurl = 'https://api.github.com/repos/go-gitea/gitea/releases/latest'
# Gitea System
gtsystem = 'linux-amd64'
# Name and Path of gitea file
gtfile = '/usr/local/bin/gitea'
# tmp Name and Path of gitea file
tmpdir  = '/tmp/'
# Build new version from source?
build_from_source = None
# Source directroy
source_dir = '/home/git/go/src/code.gitea.io/gitea'
