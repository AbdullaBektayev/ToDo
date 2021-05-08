from celery.result import AsyncResult
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, User
from .serializers import TaskListSerializer, TaskDetailSerializer
from .tasks import send_mail_of_done

class TaskListViews(APIView):

    def get(self, request):
        tasks = Task.objects.filter(User=request.user)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskCompletedViews(APIView):

    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        user = User.objects.get(pk=task.User.pk)
        email = user.email
        task_name = task.Name
        celery_task = send_mail_of_done.delay(
            email=email,
            task_name=task_name
        )
        result = AsyncResult(celery_task.id, app=send_mail_of_done)
        message = result.get()
        if 'error' in message:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(message, status=status.HTTP_200_OK)


class TaskDetailViews(APIView):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        task_object = Task.objects.get(pk=pk)
        serializer = TaskDetailSerializer(
            task_object,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            Task.objects.get(pk=pk).delete()
            return Response(
                {
                    'message': 'Task was deleted successfully!'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as exp:
            Response(
                {
                    'message': 'Cannot delete task',
                    'Exception': exp,
                },
                status=status.HTTP_400_BAD_REQUEST
            )
