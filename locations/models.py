from django.db import models
from abstract.models import AbstractModel, AbstractDateLocaleModel
from django.core.validators import RegexValidator


class Country(AbstractModel):
    name = models.CharField(max_length=64)
    iso_code = models.CharField(unique=True, max_length=3, validators=[RegexValidator(regex='^.{3}$', message='ISO code has to be of length 3', code='no match')])

    class Meta:
        db_table = 'country'


class CountryI18N(AbstractDateLocaleModel):
    country = models.ForeignKey(Country, related_name='translations', on_delete=models.PROTECT)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'country_i18n'
        unique_together = ['country', 'locale']


class Province(AbstractModel):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, related_name='provinces', on_delete=models.PROTECT)

    class Meta:
        db_table = 'province'
        unique_together = ['name', 'country']


class ProvinceI18N(AbstractDateLocaleModel):
    province = models.ForeignKey(Province, related_name='translations', on_delete=models.PROTECT)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'province_i18n'
        unique_together = ['province', 'locale']


class City(AbstractModel):
    name = models.CharField(max_length=64)
    province = models.ForeignKey(Province, related_name='cities', on_delete=models.PROTECT)

    class Meta:
        db_table = 'city'
        unique_together = ['name', 'province']


class CityI18N(AbstractDateLocaleModel):
    city = models.ForeignKey(City, related_name='translations', on_delete=models.PROTECT)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'city_i18n'
        unique_together = ['city', 'locale']
