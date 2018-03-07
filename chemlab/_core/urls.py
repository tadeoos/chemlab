from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from survey.views import (
    SubstanceSurveyAddView,
    SubstanceSurveyListView,
    SubstanceSurveyAPIView,
    RegionAPIView,
    CityAPIView,
    AcquiredFromAPIView,
    OriginAPIView,
    UserCodeAPIView,
    AliasAPIView,
    SubstanceAPIView,
    KindAPIView,
    ColorAPIView,
    TestMethodAPIView,
    ApperanceAPIView,
    DetectedAPIView,
    DuplicateSurveyView
)

from static_page.views import StaticPageView


urlpatterns = [
    url(r'^$', SubstanceSurveyListView.as_view(), name='index'),
    url(r'^add/$', SubstanceSurveyAddView.as_view(), name='add_substance'),
    url(r'^api/substances/$', SubstanceSurveyAPIView.as_view(), name='substancesurver_api'),
    url(r'^api/region/$', RegionAPIView.as_view(), name='api-region'),
    url(r'^api/city/$', CityAPIView.as_view(), name='api-city'),
    url(r'^api/acquired_from/$', AcquiredFromAPIView.as_view(), name='api-acquired-from'),
    url(r'^api/origin/$', OriginAPIView.as_view(), name='api-origin'),
    url(r'^api/user_code/$', UserCodeAPIView.as_view(), name='api-user-code'),
    url(r'^api/alias/$', AliasAPIView.as_view(), name='api-alias'),
    url(r'^api/substance/$', SubstanceAPIView.as_view(), name='api-substance'),
    url(r'^api/kinds/$', KindAPIView.as_view(), name='api-kinds'),
    url(r'^api/color/$', ColorAPIView.as_view(), name='api-color'),
    url(r'^api/testmethods/$', TestMethodAPIView.as_view(), name='api-testmethods'),
    url(r'^api/apperance/$', ApperanceAPIView.as_view(), name='api-apperance'),
    url(r'^api/detected/$', DetectedAPIView.as_view(), name='api-detected'),
    url(r'^duplicate/(?P<uuid>[\w\d-]+)/$', DuplicateSurveyView.as_view(), name='duplicate-survey'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[-\w\d]+)/$', StaticPageView.as_view(), name="static-page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
