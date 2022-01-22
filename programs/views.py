from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from abstract.views import AbstractViewSet
from utils.permissions import IsAdministrator, IsStudentOrAgent, ReadOnlyOrAdmin
from . import models, serializers
from .filters import ProgramFilters


class DegreeViewSet(AbstractViewSet):
    model = models.Degree
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer
    permission_classes = [ReadOnlyOrAdmin]


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
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = (SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ['title']
    filterset_class = ProgramFilters


class FeeViewSet(AbstractViewSet):
    model = models.Fee
    queryset = models.Fee.objects.all()
    serializer_class = serializers.FeeSerializer
    permission_classes = [ReadOnlyOrAdmin]


class ApplicationViewSet(AbstractViewSet):
    model = models.Application
    queryset = models.Application.objects.all()
    post_serializer_class = serializers.ApplicationSerializer
    list_serializer_class = serializers.ApplicationDetailSerializer
    permission_classes = [IsStudentOrAgent]

    def get_queryset(self):
        """ If user is not admin, return the applications only belonging to current user """
        qs = self.queryset
        user = self.request.user
        if user is not None:
            if user.is_agent or user.is_student:
                qs = qs.filter(user=user)
            return qs
        return None
