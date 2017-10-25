# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import generics

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


class SubstanceSurveyListView(TemplateView):
	template_name = 'survey/substancesurvey_list.html'


class SubstanceSurveyAPIView(generics.ListAPIView):
	queryset = SubstanceSurvey.objects.all()
	serializer_class = SubstanceSurveySerializer


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
	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)



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
