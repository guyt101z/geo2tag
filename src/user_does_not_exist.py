from base_geo2tag_exception import BaseGeo2TagException

class UserDoesNotExist(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "User does not exist"
        return ERROR, 404
