from django.urls import path, include
from .views import TaskListViews, TaskDetailViews, TaskCompletedViews

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
