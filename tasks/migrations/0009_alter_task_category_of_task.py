# Generated by Django 4.2 on 2025-01-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_rename_category_task_category_of_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category_of_task',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.category'),
        ),
    ]
