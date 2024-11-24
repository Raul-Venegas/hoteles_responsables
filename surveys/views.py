from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.

def home_surveys(request):
    return render(request,'surveys/home_surveys.html')