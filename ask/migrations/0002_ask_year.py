# Generated by Django 4.0.3 on 2022-03-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='year',
            field=models.CharField(blank=True, choices=[('الفرقة الاولة', 'الفرقة الاولة'), ('الفرقة الثانية', 'الفرقة الثانية'), ('الفرقة الثالثة', 'الفرقة الثالثة'), ('الفرقة الرابعة', 'الفرقة الرابعة')], max_length=400, null=True),
        ),
    ]
