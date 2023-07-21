from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    '''
    For GET requests
    '''
    class Meta:
        model = Task
        fields = '__all__'

class TaskCreateSerializer(serializers.ModelSerializer):
    '''
    For POST requests
    '''
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = {
            'id': instance.id
        }
        return representation