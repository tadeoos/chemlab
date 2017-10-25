from django.conf.urls import url, include
from django.contrib import admin

from survey.views import SubstanceSurveyAddView,\
						 SubstanceSurveyListView,\
						 SubstanceSurveyAPIView,\
						 CountryAPIView,\
						 CityAPIView,\
						 OriginAPIView,\
						 SourceAPIView,\
						 KindAPIView,\
						 TestMethodAPIView,\
						 ApperanceAPIView,\
						 ColorAPIView,\
						 OriginCodeAPIView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', SubstanceSurveyListView.as_view(), name='index'),
	url(r'^add/$', SubstanceSurveyAddView.as_view(), name='add_substance'),
	url(r'^api/substances/$', SubstanceSurveyAPIView.as_view(), 
											  name='substancesurver_list_api'),
	url(r'^api/country/$', CountryAPIView.as_view(), name='api-country'), 
	url(r'^api/city/$', CityAPIView.as_view(), name='api-city'), 
	url(r'^api/origin/$', OriginAPIView.as_view(), name='api-origin'), 
	url(r'^api/source/$', SourceAPIView.as_view(), name='api-source'), 
	url(r'^api/kinds/$', KindAPIView.as_view(), name='api-kinds'), 
	url(r'^api/testmethods/$', TestMethodAPIView.as_view(), name='api-testmethods'), 
	url(r'^api/apperance/$', ApperanceAPIView.as_view(), name='api-apperance'), 
	url(r'^api/color/$', ColorAPIView.as_view(), name='api-color'), 
	url(r'^api/origincode/$', OriginCodeAPIView.as_view(), name='api-origincode'), 

    url(r'^admin/', admin.site.urls),
]
