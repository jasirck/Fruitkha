# Generated by Django 5.0 on 2024-02-15 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_address_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expect',
            field=models.DateField(default=datetime.datetime(2024, 2, 21, 14, 49, 55, 565381, tzinfo=datetime.timezone.utc)),
        ),
    ]
