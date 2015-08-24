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
        context = self.layer._get_configuration_context()

        test_feature_name = 'ftw.autofeature:tests'

        self.assertFalse(
            context.hasFeature(test_feature_name),
            'Did not expect feature ftw.testing:tests to be already registerd. ')

        self.layer.load_zcml_string(ZCML.format(
            '<include package="ftw.autofeature" file="meta.zcml" />'))
        self.assertFalse(
            context.hasFeature(test_feature_name),
            'Did not expect feature ftw.testing:tests to be already registerd. ')

        self.layer.load_zcml_string(ZCML.format(
            '<autofeature:extras />'))
        self.assertTrue(
            context.hasFeature(test_feature_name),
            'The feature ftw.testing:tests should now be registered.')
