from flask_restful import reqparse
from datetime import datetime, date, time
from calendar import timegm
import pymongo
import json
import aniso8601
import pytz
import log_resource
NUMBER = "number"
OFFSET = "offset"
DATE_FROM = 'date_from'
DATE_TO = 'date_to'

class LogParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(NUMBER, type=int, default=None)
        parser.add_argument(OFFSET, type=int, default=None)
        parser.add_argument(DATE_FROM, type=log_resource.datetime_from_iso8601, default=None)
        parser.add_argument(DATE_TO, type=log_resource.datetime_from_iso8601, default=None)
        args = parser.parse_args()
        return args