from rest_framework import serializers
from . import models

class ParaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Para
        fields = '__all__'
        read_only_fields = ('created_at','updated_at')