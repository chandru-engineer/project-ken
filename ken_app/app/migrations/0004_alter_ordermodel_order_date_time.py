# Generated by Django 3.2.15 on 2022-09-02 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_ordermodel_order_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 3, 2, 6, 12, 171164)),
        ),
    ]
