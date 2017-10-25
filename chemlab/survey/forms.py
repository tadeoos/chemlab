from django import forms
from .models import SubstanceSurvey
from .widgets import MyWidget

class SubstanceSurveyForm(forms.ModelForm):

	kinds = forms.CharField(widget=MyWidget(attrs={"api": "/api/kind/"}))
	testmethods = forms.CharField(widget=MyWidget(attrs={"api": "/api/testmethod/"}))

	class Meta:
		model = SubstanceSurvey
		fields = ['date', 'country', 'city', 'origin', 'origin_code', 'source', 'price', 'alias', 'substance', 'apperance', 'kinds', 'color', 'image', 'observations', 'testmethods']