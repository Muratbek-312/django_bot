from rest_framework import serializers
from .models import Stadup


class StadupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadup
        fields = ('id', 'user_name', 'done', 'todo', 'problems', 'publication')