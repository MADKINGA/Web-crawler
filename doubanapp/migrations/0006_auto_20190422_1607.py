# Generated by Django 2.1.7 on 2019-04-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubanapp', '0005_auto_20190422_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db',
            name='detail',
            field=models.CharField(default='', max_length=200),
        ),
    ]
