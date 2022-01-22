# Generated by Django 3.2 on 2022-01-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_alter_degree_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='other',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fee',
            name='currency',
            field=models.CharField(choices=[('USD', 'US dollar'), ('GBP', 'British pound'), ('CAD', 'Canadian dollar'), ('EUR', 'Euro'), ('CNY', 'Renminbi (Chinese yen)'), ('KRW', 'Korean won'), ('RUB', 'Russian ruble'), ('TRY', 'Turkish lira'), ('KGS', 'Kyrgyz som')], default='USD', max_length=3),
        ),
    ]
