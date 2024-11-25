from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.

def home_surveys(request):
    return render(request,'surveys/home_surveys.html')

def natural(request):
    return render(request,'surveys/natural.html')

@login_required
def natural_survey(request):
    return render(request,'surveys/natural_survey.html')

def socio_cultural(request):
    return render(request,'surveys/socio-cultural.html')

@login_required
def socio_cultural_survey(request):
    return render(request,'surveys/socio_cultural_survey.html')

def economico(request):
    return render(request,'surveys/economico.html')

@login_required
def economico_survey(request):
    return render(request,'surveys/economico_survey.html')