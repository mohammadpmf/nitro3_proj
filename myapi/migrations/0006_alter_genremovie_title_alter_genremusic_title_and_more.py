# Generated by Django 5.0.4 on 2024-04-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_remove_staff_access_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genremovie',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='genremusic',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together={('first_name', 'last_name', 'nick_name')},
        ),
    ]