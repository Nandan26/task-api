from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskReadorCreate.as_view(), name = 'tasklistandcreate'),
    path('tasks/<int:pk>', views.TaskModification.as_view(), name = 'task-crud'),

]