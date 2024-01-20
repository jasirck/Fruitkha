# Generated by Django 5.0 on 2024-01-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin', '0005_alter_myadmincategory_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myadmincategory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='myvariant',
            name='id',
        ),
        migrations.AlterField(
            model_name='myadmincategory',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='myvariant',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]