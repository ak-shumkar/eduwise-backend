from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from eduwise.utils.permissions import ReadOnlyOrAdmin


class MenuViewSet(ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [ReadOnlyOrAdmin]


class TextBlockViewSet(ModelViewSet):
    queryset = models.TextBlock.objects.all()
    serializer_class = serializers.TextBlockSerializer
    permission_classes = [ReadOnlyOrAdmin]


class SubMenuViewSet(ModelViewSet):
    queryset = models.SubMenu.objects.all()
    serializer_class = serializers.SubMenuSerializer
    permission_classes = [ReadOnlyOrAdmin]


class NewsViewSet(ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [ReadOnlyOrAdmin]


class ProcessViewSet(ModelViewSet):
    queryset = models.Process.objects.all()
    serializer_class = serializers.ProcessSerializer
    permission_classes = [ReadOnlyOrAdmin]
