# Generated by Django 3.0 on 2019-12-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_ud', '0002_auto_20191205_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_name', models.CharField(max_length=20, null=True, verbose_name='Название должности')),
                ('salary', models.IntegerField(null=True)),
            ],
        ),
    ]
