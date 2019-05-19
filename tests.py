'''
Gitea Remote Updater

Copyright 2019 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import functions
import unittest

class Tests(unittest.TestCase):

    def testSimpleVersion(self):
        self.assertTrue(functions.checkVersion('1.9.1', '1.9.0'))

    def testTwoIntVersion(self):
        self.assertTrue(functions.checkVersion('1.10.0', '1.9.0'))

    def testFalseVersion(self):
        self.assertFalse(functions.checkVersion('1.8.0', '1.9.0'))

    def testSameVersion(self):
        self.assertFalse(functions.checkVersion('1.9.7', '1.9.7'))

    def testInt(self):
        self.assertTrue(functions.checkVersion('9', '8'))

    def testSuffix(self):
        self.assertTrue(functions.checkVersion('1.9.0+dev-264-g8de76b6e6', '1.8.0'))

if __name__ == '__main__':
    unittest.main()