from django.db import models
from abstract.models import AbstractModel, AbstractDateLocaleModel
from django.core.validators import RegexValidator


class Country(AbstractModel):
    name = models.CharField(max_length=64)
    iso_code = models.CharField(unique=True,
                                default='NON',  # TODO Remove
                                max_length=3,
                                validators=[RegexValidator(regex='^.{3}$',
                                                           message='ISO code has to be of length 3',
                                                           code='no match')])

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return f"{self.name}"


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


class Province(AbstractModel):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, related_name='provinces', on_delete=models.PROTECT)

    class Meta:
        db_table = 'province'
        unique_together = ['name', 'country']

    def __str__(self):
        return f"{self.name}, {self.country.name}"


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


class City(AbstractModel):
    name = models.CharField(max_length=64)
    province = models.ForeignKey(Province, related_name='cities', on_delete=models.PROTECT)

    class Meta:
        db_table = 'city'
        unique_together = ['name', 'province']
        verbose_name_plural = 'cities'

    def __str__(self):
        return f"{self.name}, {self.province.name}, {self.province.country.name}"


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
