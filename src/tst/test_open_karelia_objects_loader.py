#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
from open_karelia_objects_loader import OpenKareliaObjectsLoader

class Test_GT_1509_open_karelia_objects_loader(TestCase):
    def test_GT_1509_open_karelia_objects_loader(self):
    	obj = OpenKareliaObjectsLoader('http://geomongo/instance/service?number=1&offset=0')
    	data = obj.load()
    	self.assertNotEquals(data, None)
    	self.assertNotEquals(data, '')