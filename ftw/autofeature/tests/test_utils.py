from ftw.autofeature.utils import find_package_by_module
from unittest2 import TestCase


class TestFindPackageByModule(TestCase):

    def test_finds_package_by_a_submodule(self):
        import ftw.autofeature.tests.test_utils
        self.assertEquals(
            u'ftw.autofeature',
            find_package_by_module(ftw.autofeature.tests.test_utils))

    def test_finds_package_by_main_module(self):
        import ftw.autofeature
        self.assertEquals(
            u'ftw.autofeature',
            find_package_by_module(ftw.autofeature))

    def test_returns_None_when_package_not_found(self):
        import os.path
        self.assertEquals(
            None,
            find_package_by_module(os.path))
