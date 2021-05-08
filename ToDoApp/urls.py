from django.urls import path
from .views import TaskListViews

urlpatterns = [
    path('api/todo', TaskListViews.as_view(), name='list_todo'),
    path('api/todo/<int:pk>', TaskListViews.as_view(), name='todo'),
]
