from django import forms
from .models import SubstanceSurvey


class SubstanceSurveyForm(forms.ModelForm):

	single_ac_attrs = {"class": "singleinputautocomplete"}
	multi_ac_attrs = {"class": "multipleinputautocomplete"}
	multi_ac_no_crt_attrs = {"class": "multipleinputautocomplete_nocrt"}

	# Only special fields (for autocomplete).
	region = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	acquired_from = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	origin = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	user_code = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	alias = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	substance = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	apperance = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	color = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	kinds = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	testmethods = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	detected = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_no_crt_attrs))

	class Meta:
		model = SubstanceSurvey
		fields = ['region', 'city', 'acquired_from', 'origin', 'date_acquired', 'price', 
				  'sample_code', 'user_code', 'contact', 'alias', 'substance', 'apperance',
				  'kinds', 'color', 'image', 'observations', 'testmethods', 'detected']
