from django import forms

from .models import *
from django.contrib.auth import get_user_model

class SchoolCreateForm(forms.ModelForm):
	class Meta:
		User = get_user_model()
		model = School
		fields = ('__all__')
		exclude = ('added_by', 'overall_rating')