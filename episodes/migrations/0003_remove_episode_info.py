# Generated by Django 2.1.4 on 2018-12-23 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0002_auto_20181223_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='info',
        ),
    ]
