from ftw.autofeature.utils import find_extras_by_package
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


class TestGetExtrasByPackage(TestCase):

    def test_returns_a_dict_with_extras(self):
        extras = find_extras_by_package(u'ftw.autofeature')
        self.assertEquals(dict, type(extras),
                          'Excpected find_extras_by_package result to be a dict.' )

        self.assertIn(u'tests', extras,
                      'Expected key "tests" to be in ftw.autofeature\'s extras.')

    def test_dependencies_are_listed_in_each_extras(self):
        self.assertIn('ftw.testing',
                      find_extras_by_package(u'ftw.autofeature')['tests'])
