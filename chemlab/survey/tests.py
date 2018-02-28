# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient

from .models import SubstanceSurvey, Color, Region, Drug


class TestSubstanceSurveyAPIView(TestCase):
    client = APIClient()
    sample_data = {
        'date_acquired': '2018-02-02',
        'price': '10',
        'sample_code': 'SAMPLECODE',
        'image': '',
        'observations': 'sth is wrong with the color',
        'contact': '700-000-000',
        'region': 'Poland',
        'city': 'Warsaw',
        'acquired_from': 'Some weird dude',
        'origin': 'Unknown',
        'user_code': 'TEST_USER_CODE111',
        'alias': '?',
        'substance': '',
        'apperance': '',
        'kinds': '',
        'color': 'yellow,green,white',
        'testmethods': 'test_method1, test_method2',
        'detected': 'coco,molly,friends',
    }

    def test_post_method_creates_an_object(self):
        # ensure there are no below objects in db
        self.assertEqual(len(SubstanceSurvey.objects.all()), 0)
        self.assertEqual(len(Region.objects.all()), 0)
        self.assertEqual(len(Color.objects.all()), 0)
        # run `post` method
        self.client.post('/api/substances/', self.sample_data, format='json')
        # ensure that objects were created
        self.assertEqual(len(Region.objects.all()), 1)
        self.assertEqual(len(Color.objects.all()), 3)
        self.assertEqual(len(SubstanceSurvey.objects.all()), 1)

    def test_post_does_not_create_new_drugs(self):
        self.assertEqual(len(SubstanceSurvey.objects.all()), 0)
        number_of_drugs_before = len(Drug.objects.all())
        self.client.post('/api/substances/', self.sample_data, format='json')
        self.assertEqual(len(SubstanceSurvey.objects.all()), 1)
        self.assertEqual(number_of_drugs_before, len(Drug.objects.all()))
