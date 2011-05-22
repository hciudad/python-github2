import _setup

import sys

from nose.tools import assert_equals

import utils


class CommitsQueries(utils.HttpMockTestCase):
    """Test commit querying"""
    def test_list(self):
        commits = self.client.commits.list('JNRowe/misc-overlay')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '37233b357d1a3648434ffda8f569ce96b3bcbf53')

    def test_list_with_branch(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '482f657443df4b701137a3025ae08476cddd2b7d')

    def test_list_with_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay',
                                           file='Makefile')
        assert_equals(len(commits), 31)
        assert_equals(commits[0].id,
                '41bcd985139189763256a8c82b8f0fcbe150eb03')

    def test_list_with_branch_and_file(self):
        commits = self.client.commits.list('JNRowe/misc-overlay', 'gh-pages',
                                           'packages/dev-python.html')
        assert_equals(len(commits), 35)
        assert_equals(commits[0].id,
                '482f657443df4b701137a3025ae08476cddd2b7d')
