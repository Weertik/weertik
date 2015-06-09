# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token_auth',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 22, 15, 51, 429062, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
