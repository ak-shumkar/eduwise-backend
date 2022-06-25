# Generated by Django 3.2 on 2022-01-07 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('website', models.URLField(blank=True, null=True)),
                ('about', models.TextField(default='')),
                ('address', models.CharField(default='', max_length=128)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='institutions',
                                           to='locations.city')),
            ],
            options={
                'db_table': 'institution',
            },
        ),
        migrations.CreateModel(
            name='InstitutionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos',
                                                  to='institutions.institution')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
        migrations.CreateModel(
            name='InstitutionTypeI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                                       related_name='translations', to='institutions.institutiontype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='institution',
            name='institution_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='institutions',
                                    to='institutions.institutiontype'),
        ),
        migrations.CreateModel(
            name='InstitutionI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locale', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'),
                                                     ('tr', 'Turkish'), ('kg', 'Kyrgyz')], max_length=2)),
                ('name', models.CharField(max_length=128)),
                ('about', models.TextField(default='')),
                ('address', models.CharField(default='', max_length=128)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                                  related_name='translations', to='institutions.institution')),
            ],
            options={
                'db_table': 'institution_i18n',
                'unique_together': {('locale', 'institution')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='institution',
            unique_together={('name', 'city')},
        ),
    ]
