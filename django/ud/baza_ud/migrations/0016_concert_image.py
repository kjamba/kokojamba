# Generated by Django 3.0.1 on 2019-12-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_ud', '0015_auto_20191223_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение'),
        ),
    ]
