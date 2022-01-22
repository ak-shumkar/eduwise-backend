# Generated by Django 3.2 on 2022-01-22 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_auto_20220122_0943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterModelOptions(
            name='facultyi18n',
            options={'verbose_name': 'faculty translation'},
        ),
        migrations.AddField(
            model_name='facultyi18n',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='programs.faculty'),
            preserve_default=False,
        ),
    ]
