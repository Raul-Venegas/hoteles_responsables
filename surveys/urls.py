from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.home_surveys, name="home_surveys"),
]