# Generated by Django 4.1.1 on 2022-09-10 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_rename_title_todo_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='finished',
            field=models.BooleanField(default=True),
        ),
    ]
