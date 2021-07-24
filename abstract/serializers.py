from rest_framework.serializers import ModelSerializer
from . import models


class AbstractModelSerializer(ModelSerializer):

    class Meta:
        model = models.AbstractModel
        fields = '__all__'
        read_only_fields = ['active']
