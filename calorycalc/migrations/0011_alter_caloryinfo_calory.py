# Generated by Django 4.1 on 2022-11-02 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorycalc', '0010_alter_caloryinfo_calory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloryinfo',
            name='calory',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
