# Generated by Django 3.2.5 on 2021-07-24 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='CountryI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locale', models.CharField(default='en', max_length=2)),
                ('name', models.CharField(max_length=64)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='translation', to='locations.country')),
            ],
            options={
                'db_table': 'country_i18n',
                'unique_together': {('country', 'locale')},
            },
        ),
    ]
