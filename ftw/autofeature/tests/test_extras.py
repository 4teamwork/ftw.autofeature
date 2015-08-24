from ftw.autofeature.testing import ZCML_LAYER
from unittest2 import TestCase


ZCML = '''
<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:zcml="http://namespaces.zope.org/zcml"
    xmlns:autofeature="http://namespaces.zope.org/autofeature"
    package="ftw.autofeature.tests">
{}
</configure>
'''


class TestExtrasFeaturesAreAutomaticallyRegistered(TestCase):
    layer = ZCML_LAYER

    def test_zcml_feature_registered_when_using_utility(self):
        test_feature_name = 'ftw.autofeature:tests'
        self.assert_feature_not_provided(test_feature_name)

        self.layer.load_zcml_string(ZCML.format(
            '<include package="ftw.autofeature" file="meta.zcml" />'))
        self.assert_feature_not_provided(test_feature_name)

        self.layer.load_zcml_string(ZCML.format(
            '<autofeature:extras />'))
        self.assert_feature_provided(test_feature_name)

    def assert_feature_provided(self, feature_name):
        context = self.layer._get_configuration_context()
        self.assertTrue(
            context.hasFeature(feature_name),
            'The feature {} should now be registered.'.format(feature_name))

    def assert_feature_not_provided(self, feature_name):
        context = self.layer._get_configuration_context()
        self.assertFalse(
            context.hasFeature(feature_name),
            'The feature {} should NOT be registered.'.format(feature_name))
