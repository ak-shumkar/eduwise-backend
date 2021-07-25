from django.shortcuts import render
from abstract.views import AbstractViewSet
from utils.permissions import IsAdministrator
from . import models, serializers


class InstitutionViewSet(AbstractViewSet):
    queryset = models.Institution.objects.all()
    serializer_class = serializers.InstitutionSerializer
    permission_classes = [IsAdministrator]


class InstitutionI18NViewSet(AbstractViewSet):
    queryset = models.InstitutionI18N.objects.all()
    serializer_class = serializers.InstitutionI18NSerializer
    permission_classes = [IsAdministrator]


class PhotoViewSet(AbstractViewSet):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [IsAdministrator]
