from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Task(models.Model):
    User = models.ForeignKey(models=get_user_model())
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Done = models.BooleanField(default=False)
    PeriodOfTime = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
