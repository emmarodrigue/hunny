# Generated by Django 3.2.7 on 2021-11-11 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunny_app', '0003_auto_20211104_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='children_preference',
        ),
    ]
