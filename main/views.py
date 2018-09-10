from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"


class SchoolView(TemplateView):
    template_name = "school.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SchoolView, self).get_context_data(**kwargs)
        school_id = kwargs.get('school', None)
        school_details = School.objects.get(sid=school_id)
        context['school'] =  school_details
        return context
