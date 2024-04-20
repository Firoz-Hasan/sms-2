from rest_framework.response import Response
from rest_framework import status

class ResponseData:
    @staticmethod
    def success(code, message, data='None'):
        return {
            "code": code,
            "message": message,
            "data": data,
        }

    @staticmethod
    def error(code, message):
        return {
            "code": code,
            "message": message,
        }
