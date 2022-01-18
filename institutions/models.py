from django.db import models

from abstract.models import AbstractDateModel, AbstractDateLocaleModel, AbstractModel


class InstitutionType(AbstractModel):
    """ University, College etc"""
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class InstitutionTypeI18N(AbstractModel):
    """ Institution type translations """
    name = models.CharField(max_length=128)
    institution_type = models.ForeignKey(InstitutionType, related_name='translations', on_delete=models.PROTECT)


class Institution(AbstractDateModel):
    """ Institution item """
    name = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    image = models.ImageField('University profile image', upload_to='institutions', null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    about = models.TextField(default='')
    address = models.CharField(max_length=128, default='')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # Relations
    city = models.ForeignKey('locations.City', related_name='institutions', on_delete=models.PROTECT)
    institution_type = models.ForeignKey(InstitutionType, related_name='institutions', on_delete=models.PROTECT)

    class Meta:
        db_table = 'institution'
        unique_together = ['name', 'city']

    def __str__(self):
        return self.name + ", " + self.city.name


class InstitutionI18N(AbstractDateLocaleModel):
    """ Institution item translations """
    name = models.CharField(max_length=128)
    about = models.TextField(default='')
    address = models.CharField(max_length=128, default='')
    institution = models.ForeignKey(Institution, related_name='translations', on_delete=models.PROTECT)

    class Meta:
        db_table = 'institution_i18n'
        unique_together = ['locale', 'institution']


class Photo(AbstractDateModel):
    """ Institution photos """
    name = models.CharField(blank=True, null=True, max_length=64)
    image = models.ImageField(upload_to='images')
    institution = models.ForeignKey(Institution, related_name='photos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'photo'
