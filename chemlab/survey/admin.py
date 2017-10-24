# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(SubstanceSurvey)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Origin)
admin.site.register(OriginCode)
admin.site.register(Source)
admin.site.register(Apperance)
admin.site.register(Kind)
admin.site.register(TestMethod)