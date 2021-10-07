# Generated by Django 3.2.7 on 2021-10-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='age_range',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='static/profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='match_radius',
            field=models.CharField(default=0, max_length=7),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
