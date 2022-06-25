from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractActiveModel(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractLocaleModel(models.Model):
    class Locale(models.TextChoices):
        ENGLISH = 'en', _('English')
        RUSSIAN = 'ru', _('Russian')
        TURKISH = 'tr', _('Turkish')
        KYRGYZ = 'kg', _('Kyrgyz')
    locale = models.CharField(max_length=2, choices=Locale.choices)

    class Meta:
        abstract = True


class AbstractDateLocaleModel(AbstractDateModel, AbstractLocaleModel):
    class Meta:
        abstract = True


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
