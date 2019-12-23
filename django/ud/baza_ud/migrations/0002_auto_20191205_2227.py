# Generated by Django 3.0 on 2019-12-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_ud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddField(
            model_name='staff',
            name='address',
            field=models.CharField(max_length=20, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='staff',
            name='middle_name',
            field=models.CharField(max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone_num',
            field=models.CharField(max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя'),
        ),
    ]
