from rest_framework.serializers import ModelSerializer
from . import models


class TextBlockI18NSerializer(ModelSerializer):
    class Meta:
        model = models.TextBlockMenuI18N
        fields = '__all__'


class TextBlockSerializer(ModelSerializer):
    translations = TextBlockI18NSerializer(many=True, read_only=True)

    class Meta:
        model = models.TextBlock
        fields = '__all__'


class SubMenuI18NSerializer(ModelSerializer):
    class Meta:
        model = models.SubMenuI18N
        fields = '__all__'


class SubMenuSerializer(ModelSerializer):
    translations = SubMenuI18NSerializer(many=True, read_only=True)
    text_blocks = TextBlockSerializer(many=True, read_only=True)

    class Meta:
        model = models.SubMenu
        fields = '__all__'


class MenuI18NSerializer(ModelSerializer):
    class Meta:
        model = models.MenuI18N
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    translations = MenuI18NSerializer(many=True, read_only=True)
    submenus = SubMenuSerializer(many=True, read_only=True)

    class Meta:
        model = models.Menu
        fields = '__all__'
