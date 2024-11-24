from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.Register.as_view(), name="register"),
    path('aviso-de-privacidad/', views.aviso_privacidad, name="aviso_privacidad"),
    path('pru/', views.pru, name="pru"),
]