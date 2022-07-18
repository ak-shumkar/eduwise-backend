from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class AbstractModelSerializer(ModelSerializer):
    image = serializers.FileField

    class Meta:
        model = models.AbstractModel
        fields = '__all__'
        read_only_fields = ['active']


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `_fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        _fields = self.context['request'].query_params.get('_fields')
        if _fields:
            fields = _fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
