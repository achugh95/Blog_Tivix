# Generated by Django 2.2.5 on 2019-09-14 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20190914_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 15, 7, 3, 703078, tzinfo=utc)),
        ),
    ]
