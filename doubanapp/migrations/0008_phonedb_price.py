# Generated by Django 2.1.7 on 2019-04-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubanapp', '0007_auto_20190422_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonedb',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
    ]
