from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^workshopschedule', views.workshopschedule, name='workshopschedule'),
]