# Generated by Django 3.2 on 2021-12-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20211217_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='textblock',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='textblockmenui18n',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
