# Generated by Django 4.0.3 on 2022-03-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
