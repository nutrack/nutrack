# Generated by Django 4.1 on 2022-10-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='exactdate',
            field=models.DateField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='exactmonth',
            field=models.DateField(default=0),
        ),
    ]