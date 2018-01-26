# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
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
        if self.request.user.is_staff:
            queryset = SubstanceSurvey.objects.all()
        else:
            sample = self.request.query_params.get('sample', None)
            if sample is not None:
                queryset = SubstanceSurvey.objects.filter(sample_code=sample)
            else:
                queryset = SubstanceSurvey.objects.exclude(user_code__isnull=False)
                
        return queryset

    def post(self, request, format=None):
        data = request.data
        s = SubstanceSurvey.objects.create()
        get_data = data.get('date_acquired')
        if get_data != '':
            s.date_acquired = get_data
        get_data = data.get('price')
        if get_data != '':
            s.price = get_data
        get_data = data.get('sample_code')
        if get_data != '':
            s.sample_code = get_data
        get_data = data.get('image')
        if get_data != '':
            s.image = get_data
        get_data = data.get('observations')
        if get_data != '':
            s.observations = get_data
        get_data = data.get('contact')
        if get_data != '':
            s.contact = get_data

        get_data = data.get('region')
        if get_data != '':
            region, crt = Region.objects.get_or_create(name=get_data)
            if not crt:
                region.save()
            s.region = region

        get_data = data.get('city')
        if get_data != '':
            city, crt = City.objects.get_or_create(name=get_data)
            if not crt:
                city.save()
            s.city = city

        get_data = data.get('acquired_from')
        if get_data != '':
            acquired_from, crt = AcquiredFrom.objects.get_or_create(name=get_data)
            if not crt:
                acquired_from.save()
            s.acquired_from = acquired_from

        get_data = data.get('origin')
        if get_data != '':
            origin, crt = Origin.objects.get_or_create(name=get_data)
            if not crt:
                origin.save()
            s.origin = origin

        get_data = data.get('user_code')
        if get_data != '':
            user_code, crt = UserCode.objects.get_or_create(code=get_data)
            if not crt:
                user_code.save()
            s.user_code = user_code

        get_data = data.get('alias')
        if get_data != '':
            alias, crt = Alias.objects.get_or_create(name=get_data)
            if not crt:
                alias.save()
            s.alias = alias

        get_data = data.get('substance')
        if get_data != '':
            substance, crt = Substance.objects.get_or_create(name=get_data)
            if not crt:
                substance.save()
            s.substance = substance

        get_data = data.get('apperance')
        if get_data != '':
            apperance, crt = Apperance.objects.get_or_create(name=get_data)
            if not crt:
                apperance.save()
            s.apperance = apperance

        get_data = data.get('kinds')
        if get_data != '':
            k_l = get_data.split(",")
            for k in k_l:
                kind, crt = Kind.objects.get_or_create(name=k)
                s.kinds.add(kind)

        get_data = data.get('color')
        if get_data != '':
            color_list = get_data.split(",")
            for c in color_list:
                color, crt = Color.objects.get_or_create(name=c)
                s.color.add(color)

        get_data = data.get('testmethods')
        if get_data != '':
            t_l = get_data.split(",")
            for t in t_l:
                testmethod, crt = TestMethod.objects.get_or_create(name=t)
                s.testmethods.add(testmethod)

        get_data = data.get('detected')
        if get_data != '':
            d_l = get_data.split(",")
            for d in d_l:
                try:
                    dect = Drug.objects.get(name=d)
                    s.detected.add(dect)
                except:
                    pass

        s.save()
        return Response("OK")


class DuplicateSurveyView(TemplateView):
    def get(self, request, uuid, **kwargs):
        ss = get_object_or_404(SubstanceSurvey, uuid=uuid)
        ss.pk = None
        ss.save()
        return HttpResponseRedirect(reverse_lazy('index'))


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
