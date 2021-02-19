from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^awards', views.awards, name='awards'),
]
