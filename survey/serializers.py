from rest_framework import serializers

from survey.models import Survey


class SurveySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Survey.objects.create(**validated_data)

