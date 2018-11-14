from rest_framework import serializers
from analysis.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'age', 'sex', 'address', 'desired_salary',)
