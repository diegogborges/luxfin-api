from rest_framework import serializers
from due.models import Due, Due_Definition


class DueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Due


class DueDefinitionSerializer(serializers.ModelSerializer):
    due = DueSerializer()

    class Meta:
        fields = '__all__'
        model = Due_Definition

