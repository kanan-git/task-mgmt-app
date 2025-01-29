from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
