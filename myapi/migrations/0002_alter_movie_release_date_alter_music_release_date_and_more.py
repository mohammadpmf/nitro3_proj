# Generated by Django 5.0.4 on 2024-04-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='end_release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='start_release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]