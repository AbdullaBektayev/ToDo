from django.db import models
from django.utils import timezone
from authemail.models import EmailUserManager, EmailAbstractUser
from django.contrib.auth import get_user_model


class User(EmailAbstractUser):
    objects = EmailUserManager()


class Task(models.Model):
    User = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
    )
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Done = models.BooleanField(default=False)
    PeriodOfTime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
