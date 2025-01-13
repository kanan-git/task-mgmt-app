# IMPORT BUILT-IN LIBRARIES
from django.db import models
from django.contrib.auth.models import User


# TASK CATEGORIES (home, workout, study, hobby, entertaintment, unset, ...)
class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


# TASK TYPE WILL DEFINE IS TASK WILL HAVE MILESTONES (0 > 3 > 15 ...) OR JUST WILL INCOMPLETE/DONE (0 or 1)
class TypeOfTask(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


# MODEL FOR TASK CARD
class Task(models.Model):
    category = models.ManyToManyField(Category)
    todo = models.TextField(max_length=256, null=True, blank=True)
    type_of_task = models.OneToOneField(TypeOfTask, on_delete=models.CASCADE)
    priority_level = models.IntegerField(default=1, blank=True)
    # is_starred = models.BooleanField(default=False) # CHANGE THIS FEATURE'S PLACE TO ANOTHER MODEL, ACCOUNTS WILL HANDLE IT, USER WILL HAVE INTEGER MODEL INSIDE PROFILE CLASS
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id} → Category:{self.category} Type:{self.type_of_task}| Task: {self.todo} • Added:{self.added_time} Updated:{self.updated_time}'
