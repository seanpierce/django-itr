# Generated by Django 2.1.4 on 2018-12-17 23:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0004_subscriptionrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionrequest',
            name='token',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
