# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .forms import PrimaryForm, SecondaryForm, TertiaryForm
from .models import (
    SubstanceSurvey,
    Region,
    City,
    AcquiredFrom,
    Origin,
    UserCode,
    Alias,
    Substance,
    Apperance,
    Kind,
    Color,
    TestMethod,
    Drug,
)
from .serializers import (
    SubstanceSurveySerializer,
    RegionSerializer,
    CitySerializer,
    AcquiredFromSerializer,
    OriginSerializer,
    UserCodeSerializer,
    AliasSerializer,
    SubstanceSerializer,
    ApperanceSerializer,
    KindSerializer,
    ColorSerializer,
    TestMethodSerializer,
    DrugSerializer,
)


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

        SURVEY_ONLY_FIELDS = (
            'date_acquired',
            'price',
            'sample_code',
            'image',
            'observations',
            'contact'
        )
        SURVEY_FOREIGN_FIELDS = (
            ('region', Region, 'name'),
            ('city', City, 'name'),
            ('acquired_from', AcquiredFrom, 'name'),
            ('origin', Origin, 'name'),
            ('user_code', UserCode, 'code'),
            ('alias', Alias, 'name'),
            ('substance', Substance, 'name'),
            ('apperance', Apperance, 'name')
        )
        SURVEY_M2M_FIELDS = (
            ('kinds', Kind),
            ('color', Color),
            ('testmethods', TestMethod)
        )

        for field in SURVEY_ONLY_FIELDS:
            value = data.get(field, '')
            if value:
                setattr(s, field, value)

        for atr, model, arg_name in SURVEY_FOREIGN_FIELDS:
            get_data = data.get(atr)
            if get_data != '':
                obj, crt = model.objects.get_or_create(**{arg_name: get_data})
                if not crt:
                    obj.save()
                setattr(s, atr, obj)

        for attr, model in SURVEY_M2M_FIELDS:
            get_data = data.get(attr)
            if get_data:
                data_split = get_data.split(",")
                for el in data_split:
                    add_el, crt = model.objects.get_or_create(name=el)
                field = getattr(s, attr)
                field.add(add_el)

        get_data = data.get('detected')
        if get_data:
            d_l = get_data.split(",")
            for d in d_l:
                try:
                    dect = Drug.objects.get(name=d)
                    s.detected.add(dect)
                except Drug.DoesNotExist:
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
