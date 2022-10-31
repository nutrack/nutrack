# Generated by Django 4.1 on 2022-10-31 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', max_length=100, null=True)),
                ('calories', models.IntegerField(blank=True, default=0, null=True)),
                ('protein', models.IntegerField(blank=True, default=0, null=True)),
                ('fat', models.IntegerField(blank=True, default=0, null=True)),
                ('carbs', models.IntegerField(blank=True, default=0, null=True)),
                ('is_food', models.BooleanField(default=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('rater', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
