# Generated by Django 3.2.5 on 2022-01-06 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todosite', '0005_auto_20211219_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='check',
        ),
    ]
