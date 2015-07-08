from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import deletePointById, getPointById, updatePoint
from point_does_not_exist import PointDoesNotExist
from point_resource_parsers import PointResourceParsers

class PointResource(Resource):
    def get(self, serviceName, pointId):
        try:
            newPoint = getPointById(serviceName, pointId)
        except PointDoesNotExist as e:
            return e.getReturnObject()
        return newPoint
        
    def post(self):
        pass
    def put(self, serviceName, pointId):
        args = PointResourceParsers.parsePutParameters()
        try:
            updatePoint(serviceName, pointId, args)
        except PointDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200
        
    def delete(self, serviceName, pointId):
        try:
            deletePointById(serviceName, pointId) 
        except PointDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200