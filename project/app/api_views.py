from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from . import models
from . import serializers


class Para(generics.ListCreateAPIView):
    queryset = models.Para.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ParaSerializer

class Paramodi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Para.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ParaSerializer

    def get_object(self):
        return get_object_or_404(models.Para, pk=self.kwargs['para_id'])
