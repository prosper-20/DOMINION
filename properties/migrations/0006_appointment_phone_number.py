# Generated by Django 4.2.4 on 2023-08-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_property_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(default=234555, max_length=11),
            preserve_default=False,
        ),
    ]
