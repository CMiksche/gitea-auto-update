'''
Gitea Auto Updater

Copyright 2019, 2020 The Gitea-Auto-Update Authors
All rights reserved.

License: GNU General Public License
'''
import unittest
import gitea_auto_update.lib.version

VERSION = gitea_auto_update.lib.version


class TestVersion(unittest.TestCase):
    """Test the version class"""

    def test_simple_version(self):
        """1.9.1 should be newer than 1.9.0"""
        self.assertTrue(VERSION.check_version('1.9.1', '1.9.0'))

    def test_two_int_version(self):
        """1.10.0 should be newer than 1.9.0"""
        self.assertTrue(VERSION.check_version('1.10.0', '1.9.0'))

    def test_false_version(self):
        """1.8.0 should be older than 1.9.0"""
        self.assertFalse(VERSION.check_version('1.8.0', '1.9.0'))

    def test_same_version(self):
        """1.9.7 should be the same as 1.9.7"""
        self.assertFalse(VERSION.check_version('1.9.7', '1.9.7'))

    def test_int(self):
        """9 should be newer than 8"""
        self.assertTrue(VERSION.check_version('9', '8'))

    def test_suffix(self):
        """1.9.0+dev-264-g8de76b6e6 should be newer than 1.8.0"""
        self.assertTrue(VERSION.check_version('1.9.0+dev-264-g8de76b6e6', '1.8.0'))

    def test_parse_file_version(self):
        """It should get the version from a string"""
        string = 'Gitea version 1.8.1 built with go1.12.2 : bindata, sqlite, sqlite_unlock_notify'
        self.assertEqual(
            VERSION.parse_file_version(string),
            '1.8.1'
        )


if __name__ == '__main__':
    unittest.main()
