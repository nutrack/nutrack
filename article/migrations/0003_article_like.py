# Generated by Django 4.1 on 2022-10-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_remove_article_like_remove_article_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
    ]