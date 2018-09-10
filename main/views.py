from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View, CreateView
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from .models import *
from .forms import *
# Create your views here.

class HomePageView(TemplateView):
	template_name = "home.html"


class SchoolView(TemplateView):
	template_name = "school.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SchoolView, self).get_context_data(**kwargs)
		school_id = kwargs.get('sid', None)
		school_details = School.objects.get(sid=school_id)
		context['school'] =  school_details
		return context


class SchoolCreateView(CreateView):
	model = School
	template_name = "school_create.html"

	success_url = reverse_lazy("school")
	error_url = reverse_lazy('school_create')
	form_class = SchoolCreateForm

	def get_context_data(self, *args, **kwargs):
		context = super(SchoolCreateView, self).get_context_data(*args, **kwargs)
		return context
	
	def form_valid(self, form):
		create = forms.save(commit=False)
		create.added_by = self.request.user
		create.save()
		return HttpResponseRedirect('/school/')
	
	def form_invalid(self,form):
		print(form.errors)
		return HttpResponseRedirect('/add/school')