from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustonRegisterForm
from django.views import View
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request,'core/home.html')

@login_required
def pru(request):
    return render(request,'core/pru.html')

def aviso_privacidad(request):
    return render(request,'core/aviso_privacidad.html')

class Register(View):
    def get(self, request):
        return render(request,'registration/register.html')
    
    def post(self, request):
        user_creation_form = CustonRegisterForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username = user_creation_form.cleaned_data["username"], password = user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
        
        return render(request, 'registration/register.html', {'form': user_creation_form})