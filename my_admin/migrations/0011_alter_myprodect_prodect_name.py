# Generated by Django 5.0 on 2024-01-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin', '0010_alter_unlist_prodect_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprodect',
            name='prodect_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
