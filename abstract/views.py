from rest_framework.viewsets import ModelViewSet
from utils import responses
from django.db import models


class AbstractViewSet(ModelViewSet):
    model = models.Model
    post_serializer_class = None
    list_serializer_class = None

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve'] and self.list_serializer_class:
            return self.list_serializer_class
        if self.post_serializer_class:
            return self.post_serializer_class

        return self.serializer_class

    def get_queryset(self):
        if hasattr(self.model, 'active'):
            return self.model.objects.filter(active=True)
        return self.model.objects.all()

    def destroy(self, request, *args, **kwargs):
        """ Set current record inactive rather than permanently remove it from database """
        instance = self.get_object()
        if hasattr(instance, 'active'):
            setattr(instance, 'active', False)
            instance.save()
            return responses.no_content()
        else:
            return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if hasattr(self.model, 'owner') and request.user:
            data['owner'] = request.user.id
        if hasattr(self.model, 'user') and request.user:
            data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        # Here I do not understand why active is set to False although it its default value if True TODO
        if hasattr(instance, 'active'):
            setattr(instance, 'active', True)
        return responses.created(serializer.data)
