# Generated by Django 4.1 on 2022-10-28 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorycalc', '0002_alter_caloryinfo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloryinfo',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 28, 15, 0, 43, 291304)),
        ),
    ]
