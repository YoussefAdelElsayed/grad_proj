# Generated by Django 4.0.3 on 2022-03-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_alter_ask_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
