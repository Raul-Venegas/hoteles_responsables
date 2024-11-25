from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.home_surveys, name="home_surveys"),
    path('natural/', views.natural, name="natural"),
    path('natural_encuesta/', views.natural_survey, name="natural_survey"),
    path('socio-cultural/', views.socio_cultural, name="socio-cultural"),
    path('socio-cultural_encuesta/', views.socio_cultural_survey, name="socio-cultural_survey"),
    path('economico/', views.economico, name="economico"),
    path('economico_encuesta/', views.economico_survey, name="economico_survey"),
]