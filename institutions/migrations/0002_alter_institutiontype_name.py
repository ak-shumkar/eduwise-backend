# Generated by Django 3.2.5 on 2021-09-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutiontype',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]