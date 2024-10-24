from rest_framework import serializers
from api.models import Film, Worklist


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class WorklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklist
        fields = "__all__"