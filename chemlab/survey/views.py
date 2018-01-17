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
from .forms import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


@method_decorator(staff_member_required, name='dispatch')
class SubstanceSurveyAddView(TemplateView):
    template_name = 'survey/substancesurvey_add.html'

    def get_context_data(self, **kwargs):
        context = super(SubstanceSurveyAddView, self).get_context_data(**kwargs)
        context['primary_form'] = PrimaryForm()
        context['secondary_form'] = SecondaryForm()
        context['tertiary_form'] = TertiaryForm()
        return context


class SubstanceSurveyAPIView(generics.ListAPIView):
    serializer_class = SubstanceSurveySerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        if user is None:
            queryset = SubstanceSurvey.objects.exclude(user_code__isnull=False)
        else:
            queryset = SubstanceSurvey.objects.filter(user_code=user)
        return queryset

    def post(self, request, format=None):
        data = request.data
        s = SubstanceSurvey()

        region, crt = Region.objects.get_or_create(name=data.get('region'))
        s.region = region
        if not crt:
            region.save()

        city, crt = City.objects.get_or_create(name=data.get('city'))
        s.city = city
        if not crt:
            city.save()

        acquired_from, crt = AcquiredFrom.objects.get_or_create(name=data.get('acquired_from'))
        s.acquired_from = acquired_from
        if not crt:
            acquired_from.save()

        origin, crt = Origin.objects.get_or_create(name=data.get('origin'))
        s.origin = origin
        if not crt:
            origin.save()

        s.date_acquired = data.get('date_acquired')
        s.price = data.get('price')
        s.sample_code = data.get('sample_code')

        user_code, crt = UserCode.objects.get_or_create(code=data.get('user_code'))
        s.user_code = user_code
        if not crt:
            user_code.save()

        s.contact = data.get('contact')

        alias, crt = Alias.objects.get_or_create(name=data.get('alias'))
        s.alias = alias
        if not crt:
            alias.save()

        substance, crt = Substance.objects.get_or_create(name=data.get('substance'))
        s.substance = substance
        if not crt:
            substance.save()

        apperance, crt = Apperance.objects.get_or_create(name=data.get('apperance'))
        s.apperance = apperance
        if not crt:
            apperance.save()

        kinds = data.get('kinds')
        k_l = kinds.split(",")
        for k in k_l:
            kind, crt = Kind.objects.get_or_create(name=k)
            s.kinds.add(kind)

        colors = data.get('color')
        color_list = colors.split(",")
        for c in color_list:
            color, crt = Color.objects.get_or_create(name=c)
            s.color.add(color)

        s.image = data.get('image')
        s.observations = data.get('observations')

        testmethods = data.get('testmethods')
        t_l = testmethods.split(",")
        for t in t_l:
            testmethod, crt = TestMethod.objects.get_or_create(name=t)
            s.testmethods.add(testmethod)

        detected = data.get('detected')
        d_l = detected.split(",")
        for d in d_l:
            try:
                dect = Drug.objects.get(name=d)
                s.detected.add(dect)
            except:
                pass

        s.save()

        return Response("OK")


class SubstanceSurveyListView(TemplateView):
    template_name = 'survey/substancesurvey_list.html'


class RegionAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AcquiredFromAPIView(generics.ListAPIView):
    queryset = AcquiredFrom.objects.all()
    serializer_class = AcquiredFromSerializer


class OriginAPIView(generics.ListAPIView):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer


class UserCodeAPIView(generics.ListAPIView):
    queryset = UserCode.objects.all()
    serializer_class = UserCodeSerializer


class AliasAPIView(generics.ListAPIView):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


class SubstanceAPIView(generics.ListAPIView):
    queryset = Substance.objects.all()
    serializer_class = SubstanceSerializer


class ApperanceAPIView(generics.ListAPIView):
    queryset = Apperance.objects.all()
    serializer_class = ApperanceSerializer


class KindAPIView(generics.ListAPIView):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class ColorAPIView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TestMethodAPIView(generics.ListAPIView):
    queryset = TestMethod.objects.all()
    serializer_class = TestMethodSerializer

class DetectedAPIView(generics.ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
