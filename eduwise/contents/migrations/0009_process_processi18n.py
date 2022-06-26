# Generated by Django 3.2 on 2022-01-22 13:01

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_auto_20220122_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'How we work',
                'db_table': 'process',
            },
        ),
        migrations.CreateModel(
            name='ProcessI18N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'),
                                                     ('tr', 'Turkish'), ('kg', 'Kyrgyz')], max_length=2)),
                ('title', models.CharField(max_length=256)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations',
                                           to='contents.process')),
            ],
            options={
                'verbose_name': 'How we work translation',
            },
        ),
    ]
