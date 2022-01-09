# Generated by Django 3.2.5 on 2022-01-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todosite', '0006_remove_task_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]