# Generated by Django 5.2.2 on 2025-06-08 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktodo', '0005_alter_task_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasktodo.tasktype'),
        ),
    ]
