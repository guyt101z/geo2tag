#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from flask import Flask
from werkzeug.exceptions import BadRequest
from point_resource_parsers import PointResourceParsers

URL = '/testservice/point/552833515c0dd1178d37f7bb/'
BAD_URL = '/testservice/point/point_id/'
LAT = 55.24
JSON = u"{'а': 'б', 'в': 'г'}"
ALT = 1.34
LON = 3.54
_LAT = 'lat'
_LON = 'lon'
_ALT = 'alt'
_JSON = 'json'
_CHANNEL_ID = u'канал_ид'
CORRECT_ARGS = {_LAT: LAT, _JSON: JSON, _LON: LON, _ALT: ALT}
INCORRECT_ARGS = {_LAT: True, _JSON: JSON, _ALT: [1, 2, 3]}

app = Flask(__name__)


class test_GT_1318_Point_Parser(TestCase):

    def test_GT_1318_Point_Parser(self):

        with app.test_request_context(
                BAD_URL,
                data=INCORRECT_ARGS,
                method='PUT'
        ):
            with self.assertRaises(BadRequest):
                args = PointResourceParsers.parsePutParameters()

        with app.test_request_context(URL, data=CORRECT_ARGS, method='PUT'):
            args = PointResourceParsers.parsePutParameters()
            self.assertEqual(args[_LAT], LAT)
            self.assertEqual(args[_JSON], JSON)
            self.assertEqual(args[_LON], LON)
            self.assertEqual(args[_ALT], ALT)
