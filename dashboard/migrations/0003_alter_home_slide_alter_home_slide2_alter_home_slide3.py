# Generated by Django 4.0.3 on 2022-03-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_degree_celsius_alter_degree_qualifi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='slide',
            field=models.ImageField(height_field='350', upload_to='Home/slide', width_field='700'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slide2',
            field=models.ImageField(height_field='350', upload_to='Home/slide', width_field='700'),
        ),
        migrations.AlterField(
            model_name='home',
            name='slide3',
            field=models.ImageField(height_field='350', upload_to='Home/slide', width_field='700'),
        ),
    ]
