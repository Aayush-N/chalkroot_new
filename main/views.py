from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View, CreateView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *
# Create your views here.

class HomePageView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		board = Board.objects.all()
		context['board_list'] =  board
		return context


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
		create = form.save(commit=False)
		create.added_by = self.request.user
		create.save()
		return HttpResponseRedirect('/list/')
	
	def form_invalid(self,form):
		print(form.errors)
		return HttpResponseRedirect('/add/school')


class SchoolListView(ListView):
	model = School
	template_name = "school_list.html"

	def get_context_data(self, **kwargs):
		print('rating list')
		context = super(SchoolListView, self).get_context_data(**kwargs)
		school_list = School.objects.all()
		rating_list = []
		for school in school_list:
			rating_list.append(school.overall_rating)
		print('-----')
		print(rating_list)
		context['ratings'] = list(set(rating_list))
		return context

def search_view(request):
	context = {}
	schools = School.objects.all()
	form = SearchForm(request.GET)
	if form.is_valid():
		if form.cleaned_data["city"] and form.cleaned_data["name"] and form.cleaned_data["board"] and form.cleaned_data["type"]:
			schools = schools.filter(city__icontains=form.cleaned_data["city"], 
				name__icontains=form.cleaned_data["name"], 
				board__name__icontains=form.cleaned_data["board"],
				category__name__icontains=form.cleaned_data["type"])
		elif form.cleaned_data["city"] and form.cleaned_data["name"] and form.cleaned_data["board"] and not form.cleaned_data["type"]:
			schools = schools.filter(city__icontains=form.cleaned_data["city"], 
				name__icontains=form.cleaned_data["name"], 
				board__name__icontains=form.cleaned_data["board"])
		elif form.cleaned_data["city"] and form.cleaned_data["name"] and not form.cleaned_data["board"] and not form.cleaned_data["type"]:
			schools = schools.filter(city__icontains=form.cleaned_data["city"], 
				name__icontains=form.cleaned_data["name"],)
		else:
			pass
	rating_list = []
	for school in schools:
		rating_list.append(school.overall_rating)
	context['ratings'] = list(set(rating_list))
	context["form"] = form
	context['object_list'] = schools
	context['board'] = Board.objects.all()
	return render(request, "school_list.html",context)


class CompareSchoolView(ListView):
	model = School
	template_name = "compare.html"

	def get_context_data(self, *args, **kwargs):
		context = super(CompareSchoolView, self).get_context_data(**kwargs)
		return context