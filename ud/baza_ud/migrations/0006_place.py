# Generated by Django 3.0 on 2019-12-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_ud', '0005_auto_20191206_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='Название')),
                ('address', models.CharField(max_length=20, null=True, verbose_name='Адрес')),
                ('capacity', models.PositiveIntegerField(verbose_name='Вместимость')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоимость аренды')),
            ],
            options={
                'verbose_name': 'Площадка',
                'verbose_name_plural': 'Площадки',
            },
        ),
    ]