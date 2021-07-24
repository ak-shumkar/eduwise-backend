from abstract.models import AbstractDateLocaleModel
from django.db import models


class Institution(AbstractDateLocaleModel):
    name = models.CharField(max_length=128)
