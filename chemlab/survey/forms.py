from django import forms
from .models import SubstanceSurvey


class SubstanceSurveyForm(forms.ModelForm):

	single_ac_attrs = {"class": "singleinputautocomplete"}
	multi_ac_attrs = {"class": "multipleinputautocomplete"}

	country = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	origin = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	origin_code = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	source = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	apperance = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))

	color = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	kinds = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	testmethods = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))

	class Meta:
		model = SubstanceSurvey
		fields = ['country', 'city', 'origin', 'origin_code', 'source',
				  'price', 'alias', 'substance', 'apperance', 'kinds',
				  'color', 'image', 'observations', 'testmethods']