# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import generics

from .models import SubstanceSurvey
from .serializers import SubstanceSurveySerializer


class SubstanceSurveyAddView(TemplateView):
	template_name = 'survey/substancesurvey_add.html'


class SubstanceSurveyListView(TemplateView):
	template_name = 'survey/substancesurvey_list.html'


class SubstanceSurveyAPIView(generics.ListAPIView):
	queryset = SubstanceSurvey.objects.all()
	serializer_class = SubstanceSurveySerializer


class SubstanceAddAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'survey/substancesurvey_add.html'

    def get(self, request, pk):
        ssv = get_object_or_404(SubstanceSurvey, pk=pk)
        serializer = SubstanceSurveySerializer(ssv)
        return Response({'serializer': serializer, 'ssv': ssv})

    def post(self, request, pk):
        ssv = get_object_or_404(SubstanceSurvey, pk=pk)
        serializer = SubstanceSurveySerializer(ssv, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'ssv': ssv})
        serializer.save()
        return redirect('index')