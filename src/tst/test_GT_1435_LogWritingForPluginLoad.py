from unittest import TestCase
import pymongo
import os
from bson import objectid
from flask import Flask
from flask.ext.restful import Api
import sys
sys.path.append('../')
from plugins import enablePlugin
from db_model import getDbName, getDbObject
from log import writeInstanceLog

app = Flask(__name__)
api = Api(app)

db = getDbObject(getDbName())

PLUGIN_TEST_PLUGIN = 'test_plugin'
PLUGIN_FAIL_PLUGIN = 'test_plugin_for_fail'
FIELD_USERID = 'user_id'
LOG_USERID = 'system'
COLLECTION_LOG = 'log'
FIELD_MESSAGE = 'message'
ID = '_id'

MESSAGE_LOAD_DONE = 'Plugin ' + PLUGIN_TEST_PLUGIN + ' successfully loaded'
MESSAGE_LOAD_FAIL = 'Error occurred while loading the plugin ' + PLUGIN_FAIL_PLUGIN
FILLER = 'filler'

class TestLogWritingForPluginLoad(TestCase):
    def setUp(self):
        for i in range(10):
            writeInstanceLog(FILLER, FILLER)
        homeDir = os.getcwd()
        if os.getcwd().find('/var/www') != -1:
            homeDir = '/var/www/geomongo/'
            os.chdir(homeDir)
        else:
            if os.getcwd().find('src/tst') != -1:
                os.chdir('..')
        print os.getcwd()
    def testLogWritingForPluginLoadDone(self):
        enablePlugin(api, PLUGIN_TEST_PLUGIN)
        last_log_document = db[COLLECTION_LOG].find().sort({ID, pymongo.DESCENDING}).limit(1)
        print last_log_document
        self.assertNotEqual(last_log_document[0][FIELD_MESSAGE].find(MESSAGE_LOAD_DONE), -1)
        self.assertEqual(last_log_document[0][FIELD_USERID], LOG_USERID)
    def testLogWritingForPluginLoadFail(self):
        enablePlugin(api, PLUGIN_FAIL_PLUGIN)
        last_log_document = db[COLLECTION_LOG].find().sort({ID, pymongo.DESCENDING}).limit(1)
        print last_log_document
        self.assertNotEqual(last_log_document[0][FIELD_MESSAGE].find(MESSAGE_LOAD_FAIL), -1)
        self.assertEqual(last_log_document[0][FIELD_USERID], LOG_USERID)


