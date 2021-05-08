from rest_framework import serializers
from .models import Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'PeriodOfTime')


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('User',)
