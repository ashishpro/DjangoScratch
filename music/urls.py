from django.urls import include
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^main/', views.index, name='index')
]