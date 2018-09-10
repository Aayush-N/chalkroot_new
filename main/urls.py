from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r"^$", views.HomePageView.as_view(), name='HomePageView'),
	url(r'^school/(?P<sid>[\w\-]+)$', views.SchoolView.as_view(), name='SchoolView'),
	url(r"^add/school/", views.SchoolCreateView.as_view(), name="create_school"),
]
