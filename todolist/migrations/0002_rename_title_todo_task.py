# Generated by Django 4.1.1 on 2022-09-10 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='task',
        ),
    ]
