from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models


class TextBlockI18NSerializer(ModelSerializer):
    class Meta:
        model = models.TextBlockMenuI18N
        fields = '__all__'


class TextBlockSerializer(ModelSerializer):
    translations = SerializerMethodField()

    class Meta:
        depth = 1
        model = models.TextBlock
        fields = '__all__'

    @staticmethod
    def get_translations(obj):
        result = dict()
        for translation in obj.translations.all():
            serializer = TextBlockI18NSerializer(translation)

            result.update({translation.locale: serializer.data})
        return result


class SubMenuI18NSerializer(ModelSerializer):
    class Meta:
        model = models.SubMenuI18N
        fields = '__all__'


class SubMenuSerializer(ModelSerializer):
    translations = SerializerMethodField()
    posts = TextBlockSerializer(many=True, read_only=True)

    class Meta:
        model = models.SubMenu
        fields = '__all__'

    @staticmethod
    def get_translations(obj):
        result = dict()
        for translation in obj.translations.all():
            serializer = SubMenuI18NSerializer(translation)

            result.update({translation.locale: serializer.data})
        return result


class MenuI18NSerializer(ModelSerializer):
    class Meta:
        model = models.MenuI18N
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    translations = SerializerMethodField()
    submenus = SubMenuSerializer(many=True, read_only=True)

    class Meta:
        model = models.Menu
        fields = '__all__'

    @staticmethod
    def get_translations(obj):
        result = dict()
        for translation in obj.translations.all():
            serializer = MenuI18NSerializer(translation)

            result.update({translation.locale: serializer.data})
        return result
