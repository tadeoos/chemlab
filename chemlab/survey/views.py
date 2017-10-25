# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *
from .forms import SubstanceSurveyForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class SubstanceSurveyAddView(TemplateView):
	template_name = 'survey/substancesurvey_add.html'

	def get_context_data(self, **kwargs):
		context = super(SubstanceSurveyAddView, self).get_context_data(**kwargs)
		context['form'] = SubstanceSurveyForm()
		return context


class SubstanceSurveyAPIView(generics.ListAPIView):
	queryset = SubstanceSurvey.objects.all()
	serializer_class = SubstanceSurveySerializer

	def post(self, request, format=None):
		data = request.data
		print(data)
		s = SubstanceSurvey()

		country, crt = Country.objects.get_or_create(name=data.get('country'))
		s.country = country
		if not crt:
			country.save()

		city, crt = City.objects.get_or_create(name=data.get('city'))
		s.city = city
		if not crt:
			city.save()

		origin, crt = Origin.objects.get_or_create(name=data.get('origin'))
		s.origin = origin
		if not crt:
			origin.save()

		source, crt = Source.objects.get_or_create(name=data.get('source'))
		s.source = source
		if not crt:
			source.save()

		apperance, crt = Apperance.objects.get_or_create(name=data.get('apperance'))
		s.apperance = apperance
		if not crt:
			apperance.save()

		origin_code, crt = OriginCode.objects.get_or_create(code=data.get('origin_code'))
		s.origin_code = origin_code
		if not crt:
			apperance.save()

		kinds = data.get('kinds')
		k_l = kinds.split(",")
		for k in k_l:
			kind, crt = Kind.objects.get_or_create(name=k)
			s.kinds.add(kind)

		testmethods = data.get('testmethods')
		t_l = testmethods.split(",")
		for t in t_l:
			testmethod, crt = TestMethod.objects.get_or_create(name=t)
			s.testmethods.add(testmethod)

		colors = data.get('color')
		color_list = colors.split(",")
		for c in color_list:
			color, crt = Color.objects.get_or_create(name=c)
			s.color.add(color)

		s.price = data.get('price')
		s.alias = data.get('alias')
		s.substance = data.get('substance')
		s.image = data.get('image')
		s.observations = data.get('observations')
		s.save()

		return Response("OK")


class SubstanceSurveyListView(TemplateView):
	template_name = 'survey/substancesurvey_list.html'


class CountryAPIView(generics.ListAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer


class CityAPIView(generics.ListAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer


class OriginAPIView(generics.ListAPIView):
	queryset = Origin.objects.all()
	serializer_class = OriginSerializer


class SourceAPIView(generics.ListAPIView):
	queryset = Source.objects.all()
	serializer_class = SourceSerializer


class KindAPIView(generics.ListAPIView):
	queryset = Kind.objects.all()
	serializer_class = KindSerializer
	# authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class TestMethodAPIView(generics.ListAPIView):
	queryset = TestMethod.objects.all()
	serializer_class = TestMethodSerializer


class ApperanceAPIView(generics.ListAPIView):
	queryset = Apperance.objects.all()
	serializer_class = ApperanceSerializer


class ColorAPIView(generics.ListAPIView):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer


class OriginCodeAPIView(generics.ListAPIView):
	queryset = OriginCode.objects.all()
	serializer_class = OriginCodeSerializer
