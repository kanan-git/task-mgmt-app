# Generated by Django 4.2 on 2025-01-14 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_todo_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='category',
            new_name='category_of_task',
        ),
    ]
