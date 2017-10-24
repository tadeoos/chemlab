from rest_framework import serializers
from .models import SubstanceSurvey


class SubstanceSurveySerializer(serializers.ModelSerializer):
	added = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	class Meta:
		model = SubstanceSurvey
		fields = '__all__'