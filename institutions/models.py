from abstract.models import AbstractDateModel, AbstractDateLocaleModel
from django.db import models


class Institution(AbstractDateModel):
    name = models.CharField(max_length=128)
    website = models.URLField(blank=True, null=True)
    about = models.TextField(default='')
    address = models.CharField(max_length=128, default='')
    city = models.ForeignKey('locations.City', related_name='institutions', on_delete=models.PROTECT)

    class Meta:
        db_table = 'institution'


class InstitutionI18N(AbstractDateLocaleModel):
    name = models.CharField(max_length=128)
    about = models.TextField(default='')
    address = models.CharField(max_length=128, default='')
    institution = models.ForeignKey(Institution, related_name='translations', on_delete=models.PROTECT)

    class Meta:
        db_table = 'institution_i18n'
        unique_together = ['locale', 'institution']


class Photo(AbstractDateModel):
    name = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    institution = models.ForeignKey(Institution, related_name='photos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'photo'
