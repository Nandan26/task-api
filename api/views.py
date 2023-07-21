from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer
from .exception import CustomException
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .custom_response import CustomResponse




class TaskReadorCreate(APIView):
    '''
    Handling single/multiple objects
    '''
    def get(self, request, *args, **kwargs):
        task_objects = Task.objects.all()
        serializer = TaskSerializer(task_objects, many = True)
        
        return CustomResponse(serializer.data, all_data = True)

    def post(self, request, *args, **kwargs):
        
        if isinstance(request.data, list):
            serializer = TaskCreateSerializer(data=request.data, many=True)
        else:
            serializer = TaskCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
        
    
    def delete(self, request, *args, **kwargs):
        for data in request.data:
            task = Task.objects.filter(id=data['id'])
            task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskModification(APIView):
    '''
    For Perticular object mentioned in url
    '''
    def get(self, request, pk):

        try:
            task_object = Task.objects.get(pk = pk)

        except Task.DoesNotExist:
            raise CustomException(detail='There is no task at that id', code = 404)
        
        serializer = TaskSerializer(task_object)

        return Response(serializer.data) 

    def delete(self, request, pk=None):
        task = Task.objects.filter(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk=None):

        try:
            task_object = Task.objects.get(pk = pk)

        except Task.DoesNotExist:
            raise CustomException(detail='There is no task at that id', code = 404)
        
        data = {
            'title': request.data.get('title') or task_object.title, 
            'is_completed': request.data.get('is_completed') or task_object.is_completed
        }

        serializer = TaskSerializer(instance = task_object, data=data, partial = True)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







