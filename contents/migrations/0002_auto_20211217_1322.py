# Generated by Django 3.2 on 2021-12-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='submenu',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='submenu',
            unique_together={('menu', 'title')},
        ),
    ]
