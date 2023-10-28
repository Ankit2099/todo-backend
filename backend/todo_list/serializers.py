from rest_framework import serializers
from .models import task


class taskSerializer(serializers.Serializer):
    class Meta:
        model = task
        fields = "__all__"
