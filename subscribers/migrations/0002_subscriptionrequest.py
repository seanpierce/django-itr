# Generated by Django 2.1.4 on 2018-12-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
