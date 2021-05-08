from django.urls import path, include
from .views import TaskListViews, TaskDetailViews, TaskCompletedViews
from ToDo.swagger import urlpatterns as swagger_url

urlpatterns = [
    path('', include('authemail.urls'), name='authorization'),
    path('api/todo', TaskListViews.as_view(), name='list_todo'),
    path('api/todo/<int:pk>', TaskDetailViews.as_view(), name='todo'),
    path(
        'api/todo/<int:pk>/execute',
        TaskCompletedViews.as_view(),
        name='task_completed'
    )
]

urlpatterns += swagger_url
