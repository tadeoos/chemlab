from django import forms
from .models import SubstanceSurvey

single_ac_attrs = {"class": "singleinputautocomplete"}
multi_ac_attrs = {"class": "multipleinputautocomplete"}
multi_ac_no_crt_attrs = {"class": "multipleinputautocomplete_nocrt"}


class PrimaryForm(forms.ModelForm):

	# Only special fields (for autocomplete).
	region = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	acquired_from = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	origin = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))

	class Meta:
		model = SubstanceSurvey
		fields = ['region', 'city', 'acquired_from', 'origin', 'date_acquired', 'price']


class SecondaryForm(forms.ModelForm):
	user_code = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	alias = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	substance = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	apperance = forms.CharField(required=False, widget=forms.TextInput(attrs=single_ac_attrs))
	color = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))

	class Meta:
		model = SubstanceSurvey
		fields = ['sample_code', 'user_code', 'contact', 'alias', 'substance', 'apperance', 'color']


class TertiaryForm(forms.ModelForm):
	kinds = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	testmethods = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_attrs))
	detected = forms.CharField(required=False, widget=forms.TextInput(attrs=multi_ac_no_crt_attrs))

	class Meta:
		model = SubstanceSurvey
		fields = ['kinds', 'image', 'observations', 'testmethods', 'detected']

				  