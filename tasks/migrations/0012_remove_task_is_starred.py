# Generated by Django 4.2 on 2025-01-19 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_task_todo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_starred',
        ),
    ]
