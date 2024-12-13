from django.shortcuts import render, redirect
from .forms import CustonRegisterForm
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Profile
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'core/home.html')

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
    
class ProfileUpdate(UpdateView, LoginRequiredMixin):
    model = Profile 
    fields = ['hotel_logo', 'bio', 'address', 'name_hotel']
    success_url = reverse_lazy('profile')

    template_name = 'registration/profile_form.html'
