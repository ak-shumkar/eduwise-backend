from django.db import models


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
    locale = models.CharField(max_length=2, default='en')

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
