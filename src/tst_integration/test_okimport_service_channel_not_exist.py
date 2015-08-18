import unittest
import requests
import json
from basic_integration_test import BasicIntegrationTest

VALID_TEST_URL = 'instance/plugin/ok_import/service/testservice/job'
INVALID_TEST_URL = 'instance/plugin/ok_import/service/not_testservice/job'
VALID_RESPONSE_CODE = 200
INVALID_RESPONSE_CODE = 404
INVALID_SERVICE_TEXT = 'Service not found'
INVALID_CHANNEL_TEXT = 'Channel does not exist'
PARAM_CHANNEL_NAME = 'channelName'
DATA_ARR = ['channelName', 'openDataUrl', 'showObjectUrl', 'showImageUrl']
TEST_VAL_PREFIX = 'test_val_'
CHANNEL_NAME = 'testchannel'
DATA = {
    DATA_ARR[0]: CHANNEL_NAME,
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[2]: TEST_VAL_PREFIX + DATA_ARR[2],
    DATA_ARR[3]: TEST_VAL_PREFIX + DATA_ARR[3]
}

class Test_OKImportJob_not_exist(BasicIntegrationTest):
    def test_OKImportJob_GET_POST_VALID_INVALID_SERVICE(self):
        #Srevice POST
        #VALID
        response = requests.post(self.getUrl(VALID_TEST_URL),data = DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertNotEquals(responseText, 'None')
        #INVALID
        response = requests.post(self.getUrl(INVALID_TEST_URL),data = DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
        self.assertEquals(responseText, INVALID_SERVICE_TEXT)
        #Service GET
        #VALID
        response = requests.get(self.getUrl(VALID_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertNotEquals(responseText,'[]')
        #INVALID
        response = requests.get(self.getUrl(INVALID_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
        self.assertEquals(responseText, INVALID_SERVICE_TEXT)
    def test_OKImportJob_POST_VALID_INVALID_CHANNEL(self):
        #Channel POST
        #INVALID
        DATA[PARAM_CHANNEL_NAME] = 'notchannel'
        response = requests.post(self.getUrl(VALID_TEST_URL),data = DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
        self.assertEquals(responseText, INVALID_CHANNEL_TEXT)