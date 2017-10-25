from rest_framework import serializers
from .models import *


class SubstanceSurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubstanceSurvey
		fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Country
		fields = ('text', 'value')

class CitySerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = City
		fields = ('text', 'value')


class OriginSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Origin
		fields = ('text', 'value')


class SourceSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Source
		fields = ('text', 'value')


class KindSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Kind
		fields = ('text', 'value')


class TestMethodSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = TestMethod
		fields = ('text', 'value')


class ApperanceSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Apperance
		fields = ('text', 'value')


class ColorSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Color
		fields = ('text', 'value')


class OriginCodeSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = OriginCode
		fields = ('text', 'value')
