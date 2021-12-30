from django.db import models
from django.core.validators import RegexValidator

from smart_selects.db_fields import ChainedForeignKey

from abstract.models import AbstractModel, AbstractDateLocaleModel
from utils.data.countries import COUNTRIES


class Country(models.Model):
    name = models.CharField(max_length=128, choices=COUNTRIES)
    iso_code = models.CharField(unique=True,
                                editable=False,
                                max_length=3,
                                validators=[RegexValidator(regex='^.{3}$',
                                                           message='ISO code has to be of length 3',
                                                           code='no match')])

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class CountryI18N(AbstractDateLocaleModel):
    country = models.ForeignKey(Country,
                                related_name='translations',
                                on_delete=models.PROTECT,
                                verbose_name='Original name')
    name = models.CharField(max_length=64, verbose_name='Translation')

    class Meta:
        db_table = 'country_i18n'
        unique_together = ['country', 'locale']
        verbose_name = 'country translation'


class Province(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, related_name='provinces', on_delete=models.PROTECT)

    class Meta:
        db_table = 'province'
        unique_together = ['name', 'country']

    def __str__(self):
        return self.name


class ProvinceI18N(AbstractDateLocaleModel):
    province = models.ForeignKey(Province,
                                 related_name='translations',
                                 on_delete=models.PROTECT,
                                 verbose_name='Original name')
    name = models.CharField(max_length=64, verbose_name='Translation')

    class Meta:
        db_table = 'province_i18n'
        unique_together = ['province', 'locale']
        verbose_name = 'province translation'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    province = ChainedForeignKey(Province,
                                 chained_field='country',
                                 chained_model_field='country',
                                 blank=True,
                                 null=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'city'
        unique_together = ['name', 'province', 'country']
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class CityI18N(AbstractDateLocaleModel):
    city = models.ForeignKey(City,
                             related_name='translations',
                             on_delete=models.PROTECT,
                             verbose_name='Original name')
    name = models.CharField(max_length=64, verbose_name='Translation')

    class Meta:
        db_table = 'city_i18n'
        unique_together = ['city', 'locale']
        verbose_name = 'city translation'
