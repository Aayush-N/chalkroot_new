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
		return HttpResponseRedirect('/school/')
	
	def form_invalid(self,form):
		print(form.errors)
		return HttpResponseRedirect('/add/school')


class SchoolListView(ListView):
	model = School
	template_name = "school_list.html"

	def get_context_data(self, **kwargs):
		context = super(SchoolListView, self).get_context_data(**kwargs)
		return context

def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        qs = School.objects.search(form.cleaned_data)
    else:
        qs = School.objects.all()
    return render(request, "school_list.html",
            {"form": form, "object_list": qs})

class SearchManager(models.Manager):
    def search(self, **kwargs):
        qs = self.get_query_set()
        if kwargs.get('name', ''):
            qs = qs.filter(name__icontains=kwargs['name'])
        if kwargs.get('city', []):
            qs = qs.filter(city_type=kwargs['city'])
        if kwargs.get('board', []):
            qs = qs.filter(board=kwargs['board'])
        return qs
