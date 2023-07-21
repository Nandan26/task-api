from django.urls import path
from . import views

urlpatterns = [
    # for delaling with multiple tasks
    path('tasks/', views.TaskReadorCreate.as_view(), name = 'tasklistandcreate'),
    # for individual tasks
    path('tasks/<int:pk>', views.TaskModification.as_view(), name = 'task-crud'),

]