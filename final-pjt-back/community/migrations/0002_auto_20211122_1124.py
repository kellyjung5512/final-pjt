# Generated by Django 3.2.9 on 2021-11-22 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='movie_title',
        ),
        migrations.RemoveField(
            model_name='community',
            name='rank',
        ),
    ]