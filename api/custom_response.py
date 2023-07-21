from rest_framework.response import Response
from rest_framework.serializers import Serializer

class CustomResponse(Response):
    def __init__(self, data=None, **kwargs):
        # Check if data is a list (POST request) and exclude unnecessary fields
        if isinstance(data, list):
            if kwargs.get('all_data') == True:
                data = list(data)
                kwargs.pop('all_data')
            data = {'tasks': data}
        super().__init__(data, **kwargs)