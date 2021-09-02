from abstract.views import AbstractViewSet
from utils.permissions import IsAdministrator
from . import models, serializers


class ProgramTypeViewSet(AbstractViewSet):
    model = models.ProgramType
    queryset = models.ProgramType.objects.all()
    post_serializer_class = serializers.ProgramTypeSerializer
    list_serializer_class = serializers.ProgramTypeDetailSerializer
    permission_classes = [IsAdministrator]


class ProgramTypeI18NViewSet(AbstractViewSet):
    model = models.ProgramTypeI18N
    queryset = models.ProgramType.objects.all()
    serializer_class = serializers.ProgramTypeI18NSerializer
    permission_classes = [IsAdministrator]


class TermViewSet(AbstractViewSet):
    model = models.Term
    queryset = models.Term.objects.all()
    post_serializer_class = serializers.TermSerializer
    list_serializer_class = serializers.TermDetailSerializer
    permission_classes = [IsAdministrator]


class TermI18NViewSet(AbstractViewSet):
    model = models.TermI18N
    queryset = models.TermI18N.objects.all()
    serializer_class = serializers.TermI18NSerializer
    permission_classes = [IsAdministrator]


class ProgramViewSet(AbstractViewSet):
    model = models.Program
    queryset = models.Program.objects.all()
    serializer_class = serializers.ProgramSerializer
    permission_classes = [IsAdministrator]


class ProgramI18NViewSet(AbstractViewSet):
    model = models.ProgramTypeI18N
    queryset = models.ProgramI18N.objects.all()
    serializer_class = serializers.ProgramI18NSerializer
    permission_classes = [IsAdministrator]
