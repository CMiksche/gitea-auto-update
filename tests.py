'''
Gitea Remote Updater

Copyright 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import functions
import unittest

class Tests(unittest.TestCase):

    def checkSimpleVersion(self):
        self.assertTrue(functions.checkVersion('1.9.1', '1.9.0'))

    def checkTwoIntVersion(self):
        self.assertTrue(functions.checkVersion('1.10.0', '1.9.0'))

    def checkFalseVersion(self):
        self.assertFalse(functions.checkVersion('1.8.0', '1.9.0'))

    def checkSameVersion(self):
        self.assertFalse(functions.checkVersion('1.9.7', '1.9.7'))

if __name__ == '__main__':
    unittest.main()