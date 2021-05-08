from django.urls import path, include
from .views import TaskListViews, TaskDetailViews

urlpatterns = [
    path('', include('authemail.urls'), name='authorization'),
    path('api/todo', TaskListViews.as_view(), name='list_todo'),
    path('api/todo/<int:pk>', TaskDetailViews.as_view(), name='todo'),
]
