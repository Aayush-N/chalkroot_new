from django import forms

from .models import *
from django.contrib.auth import get_user_model

class SchoolCreateForm(forms.ModelForm):
	class Meta:
		User = get_user_model()
		model = School
		exclude = ('added_by', 'overall_rating')

class SearchForm(forms.ModelForm):
	class Meta:
		model = School
		exclude = ('added_by','sid','contact_number','website','photos','admission_info',)