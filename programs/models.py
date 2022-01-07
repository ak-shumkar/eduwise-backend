from abstract.models import AbstractDateModel, AbstractDateLocaleModel, AbstractModel
from django.db import models
from users.models import User


class Degree(AbstractDateModel):
    """ Degrees like BS, MS, PHD etc."""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class DegreeI18N(AbstractDateLocaleModel):
    """ Degree translation"""
    name = models.CharField(max_length=128)


class Term(AbstractDateModel):
    """ Program start season like Winter 2022, Spring 2023"""
    season = models.CharField(max_length=32)
    year = models.IntegerField()

    class Meta:
        unique_together = ['season', 'year']


class TermI18N(AbstractDateLocaleModel):
    """ Term translation """
    season = models.CharField(max_length=32)
    term = models.ForeignKey(Term, related_name='translations', on_delete=models.PROTECT)


class Program(AbstractDateModel):
    """ Program """
    overview = models.TextField('Description')
    title = models.CharField(max_length=128)
    website = models.URLField('Link to program details', null=True, blank=True)
    duration = models.IntegerField('Study duration in month(s)', default=0)
    start = models.DateField('Start date', blank=True, null=True)
    end = models.DateField('End date', blank=True, null=True)
    deadline = models.DateField('Application deadline', blank=True, null=True)
    # Relations
    institution = models.ForeignKey('institutions.Institution',
                                    on_delete=models.PROTECT,
                                    related_name='programs')
    degree = models.OneToOneField(Degree, on_delete=models.PROTECT, related_name='degree', null=True, blank=True)

    def __str__(self):
        return self.title


class ProgramI18N(AbstractDateLocaleModel):
    """ Program translation """
    program = models.ForeignKey(Program, on_delete=models.PROTECT, related_name='translations')
    overview = models.TextField()
    title = models.CharField(max_length=128)


class Fee(AbstractDateModel):
    """ Fees for tuition, dormitory etc"""
    CURRENCIES = [
        ('USD', 'US dollar')
    ]
    description = models.TextField(default="")
    tuition = models.IntegerField(default=0)
    housing = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='USD')
    program = models.OneToOneField(Program, related_name='fee', on_delete=models.PROTECT)


class Application(AbstractDateModel):
    """ Applications for programs """
    user = models.ForeignKey(User, related_name='applications', on_delete=models.PROTECT)
    program = models.ForeignKey(Program, related_name='applications', on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'program']
