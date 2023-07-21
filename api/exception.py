from rest_framework.exceptions import APIException


class CustomException(APIException):
    '''
    Custome exception if object is not found
    '''
    status_code = 400
    default_detail = 'A custom exception has occurred.'

    def __init__(self, detail=None, code=None):
        if detail is not None:
            self.detail = detail
        
        else:
            self.detail = self.default_detail

        if code is not None:
            self.status_code = code