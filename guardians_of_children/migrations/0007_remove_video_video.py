# Generated by Django 2.2.5 on 2021-10-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guardians_of_children', '0006_auto_20211003_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
    ]
