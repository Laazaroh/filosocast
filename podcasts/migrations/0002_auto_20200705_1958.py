# Generated by Django 3.0.8 on 2020-07-05 22:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='excerto',
            field=models.TextField(default=models.TextField(), max_length=250),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 22, 58, 25, 651727, tzinfo=utc)),
        ),
    ]
