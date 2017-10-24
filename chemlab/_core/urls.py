from django.conf.urls import url, include
from django.contrib import admin

from survey.views import SubstanceSurveyAddView,\
						 SubstanceSurveyListView,\
						 SubstanceSurveyAPIView,\
						 SubstanceAddAPI

urlpatterns = [
	url(r'^$', SubstanceSurveyListView.as_view(), name='index'),
	url(r'^$', SubstanceSurveyAddView.as_view(), name='add_substance'),
	url(r'^api/substances/$', SubstanceSurveyAPIView.as_view(), 
											  name='substancesurver_list_api'),
	url(r'^api/substances/add', SubstanceAddAPI.as_view(), 
											  name='substancesurver_add_api'),

    url(r'^admin/', admin.site.urls),
]
