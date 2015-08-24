from ftw.autofeature.testing import ZCML_LAYER
from ftw.autofeature.tests.helpers import capture_streams
from StringIO import StringIO
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


class TestDumpRegisteredFeatures(TestCase):
    layer = ZCML_LAYER

    def test_dumps_registered_features(self):
        output = StringIO()
        with capture_streams(output):
            self.load_zcml('<include package="ftw.autofeature" file="meta.zcml" />',
                           '<autofeature:extras />',
                           '<autofeature:dump />')

        self.assertMultiLineEqual(
            'Currently registered ZCML features (by autofeature:dump):\n'
            '-  ftw.autofeature:example\n'
            '-  ftw.autofeature:example:tests\n'
            '-  ftw.autofeature:tests\n'
            '-  ftw.autofeature:tests:example\n',
            output.getvalue())

    def load_zcml(self, *lines):
        self.layer.load_zcml_string(ZCML.format('\n'.join(lines)))
