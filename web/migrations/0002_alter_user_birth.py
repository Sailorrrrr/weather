# Generated by Django 3.2.5 on 2022-03-03 07:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(10000000)]),
        ),
    ]
