from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.home_surveys, name="home_surveys"),
    path('natural/', views.natural, name="natural"),
    path('natural_encuesta/', views.Natural_survey.as_view(), name="natural_survey"),
    path('socio-cultural/', views.socio_cultural, name="socio-cultural"),
    path('socio-cultural_encuesta/', views.Socio_cultural_survey.as_view(), name="socio-cultural_survey"),
    path('economico/', views.economico, name="economico"),
    path('economico_encuesta/', views.Economico_survey.as_view(), name="economico_survey"),
    path('puntos/', views.Score_obtained.as_view(), name="score_obtained"),
    path('soluciones/', views.Solutions_view.as_view(), name="solutions"),
]