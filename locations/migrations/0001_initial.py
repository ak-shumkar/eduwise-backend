# Generated by Django 3.2 on 2021-12-15 11:55

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
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='provinces', to='locations.country')),
            ],
            options={
                'db_table': 'province',
                'unique_together': {('name', 'country')},
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='locations.province')),
            ],
            options={
                'verbose_name_plural': 'cities',
                'db_table': 'city',
                'unique_together': {('name', 'province')},
            },
        ),
        migrations.CreateModel(
            name='ProvinceI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locale', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('tr', 'Turkish'), ('kg', 'Kyrgyz')], max_length=2)),
                ('name', models.CharField(max_length=64, verbose_name='Translation')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='translations', to='locations.province', verbose_name='Original name')),
            ],
            options={
                'verbose_name': 'province translation',
                'db_table': 'province_i18n',
                'unique_together': {('province', 'locale')},
            },
        ),
        migrations.CreateModel(
            name='CountryI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locale', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('tr', 'Turkish'), ('kg', 'Kyrgyz')], max_length=2)),
                ('name', models.CharField(max_length=64, verbose_name='Translation')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='translations', to='locations.country', verbose_name='Original name')),
            ],
            options={
                'verbose_name': 'country translation',
                'db_table': 'country_i18n',
                'unique_together': {('country', 'locale')},
            },
        ),
        migrations.CreateModel(
            name='CityI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locale', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('tr', 'Turkish'), ('kg', 'Kyrgyz')], max_length=2)),
                ('name', models.CharField(max_length=64, verbose_name='Translation')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='translations', to='locations.city', verbose_name='Original name')),
            ],
            options={
                'verbose_name': 'city translation',
                'db_table': 'city_i18n',
                'unique_together': {('city', 'locale')},
            },
        ),
    ]