# Generated by Django 3.2 on 2022-01-18 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_institution_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('season', models.DateField()),
                ('application_deadline', models.DateField()),
                ('program_start', models.DateField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deadlines', to='institutions.institution')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
