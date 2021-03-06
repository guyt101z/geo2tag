import requests
from basic_integration_test import BasicIntegrationTest
import json

TEST_URL = '/instance/user?number=4&offset=0&login=test'
TEST_NOT_VALID_URL = '/instance/user?number=1&offset=0'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
LOGIN = 'login'


def isSorted(L, key):
    tmp = L[0][key]
    for i in L:
        if i[key] < tmp:
            return False
        else:
            tmp = i[key]
    return True


class TestUserListResource(BasicIntegrationTest):

    def testUserListResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        responseText = response.text
        user_list = json.loads(responseText)
        self.assertTrue(isSorted(user_list, LOGIN))
        response = requests.get(self.getUrl(TEST_NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
