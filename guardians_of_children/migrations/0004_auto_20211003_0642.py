# Generated by Django 2.2.5 on 2021-10-03 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guardians_of_children', '0003_auto_20211003_0610'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Video',
            new_name='Videos',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='video',
            new_name='videos',
        ),
    ]
