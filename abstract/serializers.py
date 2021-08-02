from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class AbstractModelSerializer(ModelSerializer):
    image = serializers.FileField
    class Meta:
        model = models.AbstractModel
        fields = '__all__'
        read_only_fields = ['active']
