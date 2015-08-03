import unittest
import sys
sys.path.append('../')
from db_model import getDbObject
from main import app
from plugins import isPluginEnabled

TEST_PLUGIN_NAME = 'test_plugin'
TEST_PLUGIN_NAME_NOT_VALID = 'test_plugin_not_valid_name'

class TestPlugins(unittest.TestCase):
    def testIsPluginEnabled(self):
        RESULT = isPluginEnabled(TEST_PLUGIN_NAME, app)
        self.assertTrue(RESULT is True)
        RESULT = isPluginEnabled(TEST_PLUGIN_NAME_NOT_VALID, app)
        self.assertTrue(RESULT is False)
