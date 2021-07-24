from django.db import models
from abstract.models import AbstractModel, AbstractDateLocaleModel


class Country(AbstractModel):
    name = models.CharField(max_length=64)

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