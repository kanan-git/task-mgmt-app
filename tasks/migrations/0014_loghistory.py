# Generated by Django 4.2 on 2025-01-27 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0013_task_assigned_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete'), ('error', 'Error'), ('authentication', 'Authentication')], max_length=16)),
                ('event', models.TextField()),
                ('datentime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
