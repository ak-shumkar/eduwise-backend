from abstract.models import AbstractDateModel, AbstractDateLocaleModel, AbstractModel
from django.db import models


class ProgramType(AbstractDateModel):
    name = models.CharField(max_length=128)


class ProgramTypeI18N(AbstractDateLocaleModel):
    name = models.CharField(max_length=128)


class Term(AbstractDateModel):
    season = models.CharField(max_length=32)
    year = models.IntegerField()


class TermI18N(AbstractDateLocaleModel):
    season = models.CharField(max_length=32)
    term = models.ForeignKey(Term, related_name='translations', on_delete=models.PROTECT)


class Program(AbstractDateModel):
    overview = models.TextField()
    title = models.CharField(max_length=128)
    link = models.URLField(null=True, blank=True)
    institution = models.ForeignKey('institutions.Institution', on_delete=models.PROTECT, related_name='programs')
    term = models.ForeignKey(Term, on_delete=models.PROTECT, related_name='programs')
