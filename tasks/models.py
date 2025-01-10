from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category = models.CharField(max_length=16)


class Task(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=0)
    todo = models.TextField(max_length=256, null=True, blank=True)
    priority_level = models.IntegerField(default=1)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        summary = str(self.todo[0:16:1])
        return f'→ Category:{self.category} | Task:{summary}'
