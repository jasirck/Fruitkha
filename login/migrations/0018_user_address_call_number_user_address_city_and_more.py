# Generated by Django 5.0 on 2024-02-06 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_remove_user_address_address1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_address',
            name='call_number',
            field=models.IntegerField(default=123456789),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='city',
            field=models.CharField(default='calicut', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='house_name',
            field=models.CharField(default='manzil', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='lanmark',
            field=models.CharField(default='thayepeedia', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='name',
            field=models.CharField(default='jasir', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='picode',
            field=models.IntegerField(default=674534),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='post',
            field=models.CharField(default='mayynnur', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='state',
            field=models.CharField(default='kerala', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_address',
            name='user_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to='login.user'),
            preserve_default=False,
        ),
    ]
