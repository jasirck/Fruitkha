# Generated by Django 5.0 on 2024-02-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_alter_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='action',
            field=models.CharField(default='allow', max_length=10),
        ),
    ]
