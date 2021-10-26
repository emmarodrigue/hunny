# Generated by Django 3.2.7 on 2021-10-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunny_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age_range',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='match_radius',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('NB', 'Nonbinary')], max_length=2, null=True),
        ),
    ]
