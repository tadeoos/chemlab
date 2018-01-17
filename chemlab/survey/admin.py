# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


def duplicate_survey(modeladmin, request, queryset):
	for o in queryset:
		o.pk = None
		o.save()

admin.site.site_title = 'ChemLab - Restricted Zone'
admin.site.site_header = 'ChemLab - Restricted Zone'
admin.site.index_title = 'Site administration'
duplicate_survey.short_description = "Duplicate selected surveys"


class SurveyAdmin(admin.ModelAdmin):
    actions = [duplicate_survey]


admin.site.register(SubstanceSurvey, SurveyAdmin)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Origin)
admin.site.register(OriginCode)
admin.site.register(Source)
admin.site.register(Apperance)
admin.site.register(Kind)
admin.site.register(TestMethod)
admin.site.register(Drug)
admin.site.register(UserCode)
admin.site.register(AcquiredFrom)
admin.site.register(Alias)
admin.site.register(Substance)
admin.site.register(Color)
admin.site.register(Region)
