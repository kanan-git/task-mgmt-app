# REFERENCE: https://medium.com/@ahmalopers703/getting-started-with-django-rest-api-for-beginners-9c121a2ce0d3

from django.contrib.auth.models import User
from django.db import models

from rest_framework import serializers

from .models import Task, Category, TypeOfTask


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTask
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    # PRIORITY_OPTIONS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)]
    # STATUS_OPTIONS = [(1,'1 → Incomplete'), (2,'2 → Work In Progress'), (3,'3 → Done')]
    category_of_task = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, required=True)
    type_of_task = serializers.PrimaryKeyRelatedField(queryset=TypeOfTask.objects.all, required=True)
    todo = serializers.CharField(max_length=256, required=False)
    priority_level = serializers.ChoiceField(choices=Task.PRIORITY_OPTIONS, default=1)
    todo_status = serializers.ChoiceField(choices=Task.STATUS_OPTIONS, default=1)
    progression_start = serializers.IntegerField(default=0)
    progression_end = serializers.IntegerField(default=1)
    added_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Task
        fields = ('__all__')
    def create(self, validated_data):
        return Task.objects.create(**validated_data) # kwargs=validated_data
    def update(self, instance, validated_data):
        instance.category_of_task = validated_data.get('category_of_task', instance.category_of_task)
        instance.type_of_task = validated_data.get('type_of_task', instance.type_of_task)
        instance.todo = validated_data.get('todo', instance.todo)
        instance.priority_level = validated_data.get('priority_level', instance.priority_level)
        instance.todo_status = validated_data.get('todo_status', instance.todo_status)
        instance.progression_start = validated_data.get('progression_start', instance.progression_start)
        instance.progression_end = validated_data.get('progression_end', instance.progression_end)
        # instance.added_time = validated_data.get('added_time', instance.added_time)
        # instance.updated_time = validated_data.get('updated_time', instance.updated_time)
        # instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
        instance.save()
        return instance
