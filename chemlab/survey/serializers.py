from rest_framework import serializers
from .models import *


class SubstanceSurveySerializer(serializers.ModelSerializer):
	image = serializers.CharField(source='get_image_url')
	detected = serializers.ListField(source='get_detected')
	class Meta:
		model = SubstanceSurvey
		fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Region
		fields = ('text', 'value')


class CitySerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = City
		fields = ('text', 'value')


class AcquiredFromSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = AcquiredFrom
		fields = ('text', 'value')


class OriginSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Origin
		fields = ('text', 'value')


class UserCodeSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	code = serializers.CharField(source='pk')
	class Meta:
		model = UserCode
		fields = ('text', 'code')


class AliasSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Alias
		fields = ('text', 'value')


class SubstanceSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='pk')
	value = serializers.CharField(source='pk')
	class Meta:
		model = Substance
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


class DrugSerializer(serializers.ModelSerializer):
	text = serializers.CharField(source='name')
	value = serializers.CharField(source='name')
	class Meta:
		model = Drug
		fields = ('text', 'value')
