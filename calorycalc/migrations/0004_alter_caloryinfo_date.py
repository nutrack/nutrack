# Generated by Django 4.1 on 2022-10-28 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorycalc', '0003_alter_caloryinfo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloryinfo',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 28, 15, 1, 43, 889032)),
        ),
    ]