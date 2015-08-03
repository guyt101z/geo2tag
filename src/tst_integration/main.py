import unittest
import sys
from test_tests_page import Test_tests_page
from test_PointListGet import TestPointListGet
from basic_integration_test import BasicIntegrationTest
from test_testplugin import TestTestPlugin
from basic_integration_test import BasicIntegrationTest
from test_status_request import TestStatusRequest
from test_delete_service_name import TestServiceDeleteRequest
from test_get_service_name import TestServiceGetRequest
from test_get_request import TestServiceListGetRequest
from test_put_service_name import TestServicePutRequest
from test_post_request import TestServiceListPostRequest
from test_service_name_get import TestServiceNameGetRequest
from test_get_channel_by_id import TestChannelGetRequest
from test_channel_service_get import TestChannelServiceGetRequest
from test_GT_1283_channels_service_post import TestChannelServicePostRequest
from test_channel_service_delete import ChannelResourceDelete
from test_channel_service_put import ChannelResourcePut
from test_instance_log import TestInstanceLogRequest
from test_point_resource_get import TestPointGetRequest
from test_debug_info_resource import TestDebugInfoResource
from test_logout_resource import TestLogoutResource
from test_GT_1320_point_resource_put import PointResourcePut
from test_delete_point_by_id import TestPointResourceDelete
from test_point_list_resource_post import TestPointListPostRequest
from test_GT_1386 import Test_GT_1386
from test_debug_login_resource import TestDebugLoginResource
from test_get_rout_map import TestRoutMap

def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicIntegrationTest.parametrize(TestTestPlugin, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestPointListGet, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(Test_tests_page, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestChannelGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestStatusRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceDeleteRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServicePutRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceListGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceListPostRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestChannelServiceGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceNameGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestChannelServicePostRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(ChannelResourceDelete, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(ChannelResourcePut, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestInstanceLogRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestPointGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestDebugInfoResource, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestLogoutResource, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(PointResourcePut, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestPointResourceDelete, param=host))    
    suite.addTest(BasicIntegrationTest.parametrize(TestPointListPostRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(Test_GT_1386, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestDebugLoginResource, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestRoutMap, param=host))
    returnCode = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(returnCode)

if __name__ == '__main__':
    host = sys.argv[1]
    main(host)
