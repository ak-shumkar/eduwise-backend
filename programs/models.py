from abstract.models import AbstractDateModel, AbstractDateLocaleModel, AbstractModel
from django.db import models
from users.models import User


class ProgramType(AbstractDateModel):
    """ Types like BS, MS, PHD etc."""
    name = models.CharField(max_length=128)


class ProgramTypeI18N(AbstractDateLocaleModel):
    """ Program Type translation"""
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
    overview = models.TextField()
    title = models.CharField(max_length=128)
    link = models.URLField(null=True, blank=True)
    institution = models.ForeignKey('institutions.Institution', on_delete=models.PROTECT, related_name='programs')
    term = models.ForeignKey(Term, on_delete=models.PROTECT, related_name='programs')


class ProgramI18N(AbstractDateLocaleModel):
    """ Program translation """
    program = models.ForeignKey(Program, on_delete=models.PROTECT, related_name='translations')
    overview = models.TextField()
    title = models.CharField(max_length=128)


class Fee(AbstractDateModel):
    """ Fees for tuition, dormitory etc"""
    description = models.TextField()
    tuition = models.IntegerField()
    housing = models.IntegerField()
    other = models.IntegerField()
    program = models.OneToOneField(Program, related_name='fee', on_delete=models.PROTECT)


class Application(AbstractDateModel):
    """ Applications for programs """
    user = models.ForeignKey(User, related_name='applications', on_delete=models.PROTECT)
    program = models.ForeignKey(Program, related_name='applications', on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'program']
