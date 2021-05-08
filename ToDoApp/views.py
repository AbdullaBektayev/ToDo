from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TaskListViews(APIView):

    def get(self, request):
        tasks = Task.objects.filter(User=request.user)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskDetailViews(APIView):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
