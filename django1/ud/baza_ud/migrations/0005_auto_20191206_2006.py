# Generated by Django 3.0 on 2019-12-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_ud', '0004_auto_20191205_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='pasport_data',
            field=models.CharField(max_length=11, null=True, verbose_name='Паспортные данные'),
        ),
    ]