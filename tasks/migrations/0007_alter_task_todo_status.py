# Generated by Django 4.2 on 2025-01-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_progression_end_task_progression_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='todo_status',
            field=models.IntegerField(choices=[(1, 'Incomplete'), (2, 'Work In Progress'), (3, 'Done')], default=1),
        ),
    ]
