from django.db import models
from abstract.models import AbstractModel, AbstractDateLocaleModel


class Country(AbstractModel):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'country'


class CountryI18N(AbstractDateLocaleModel):
    country = models.ForeignKey(Country, related_name='translation', on_delete=models.PROTECT)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'country_i18n'
        unique_together = ['country', 'locale']
