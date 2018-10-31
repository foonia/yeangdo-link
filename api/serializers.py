from rest_framework import serializers
from analysis.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('birth_date', 'final_education',)
