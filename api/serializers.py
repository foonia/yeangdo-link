from rest_framework import serializers
from analysis.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'age', 'sex', 'address', 'desired_occupation1', 'final_education', 'desired_salary',)
