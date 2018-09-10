from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r"^$", views.HomePageView.as_view(), name='HomePageView'),
	url(r"^school/?P<school>\w+", views.SchoolView.as_view(), name='SchoolView'),
]
