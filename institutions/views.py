from abstract.views import AbstractViewSet
from utils.permissions import IsAdministrator
from . import models, serializers


class InstitutionViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE universities """
    model = models.Institution
    queryset = models.Institution.objects.all()
    post_serializer_class = serializers.InstitutionSerializer
    list_serializer_class = serializers.InstitutionDetailSerializer
    permission_classes = [IsAdministrator]


class InstitutionI18NViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE universities translations """
    model = models.InstitutionI18N
    queryset = models.InstitutionI18N.objects.all()
    serializer_class = serializers.InstitutionI18NSerializer
    permission_classes = [IsAdministrator]


class PhotoViewSet(AbstractViewSet):
    """ CREATE, GET, UPDATE, DELETE universities gallery """
    model = models.Photo
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [IsAdministrator]
