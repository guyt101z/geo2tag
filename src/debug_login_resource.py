from flask_restful import reqparse
from flask_restful import Resource
from config_reader import getDebugUsers
from user_routines import logUserIn

ID = "_id"


def parseId():
    parser = reqparse.RequestParser()
    parser.add_argument(ID, type=unicode, default=None)
    args = parser.parse_args()
    return args


class DebugLoginResource(Resource):

    def get(self):
        parser_dict = parseId()
        usersList = getDebugUsers()
        _id = parser_dict[ID]
        if _id in usersList:
            logUserIn(_id)
            return('')
        else:
            return ('Credentials are incorrect', 401)
