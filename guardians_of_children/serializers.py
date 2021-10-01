from rest_framework import serializers
from .models import Violence

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violence
        fields = "__all__"