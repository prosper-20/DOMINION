# Generated by Django 4.2.4 on 2023-08-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
