# Generated by Django 4.0.3 on 2022-04-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_result_delete_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='rating',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
