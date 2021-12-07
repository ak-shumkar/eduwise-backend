from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from utils.permissions import ReadOnlyOrAdmin


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
