# Generated by Django 4.2.4 on 2023-08-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(default='pol'),
            preserve_default=False,
        ),
    ]
