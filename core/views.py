from django.shortcuts import render, redirect
from .forms import CustonRegisterForm, ProfileForm
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from surveys.models import Applied_solutions

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
    form_class = ProfileForm
    success_url = reverse_lazy('core:perfil')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class EcoHotels(View):
    def get(self, request):
        users_with_profiles = User.objects.select_related('profile').filter(
            profile__isnull=False,
            profile__name_hotel__isnull=False,
            profile__address__isnull=False,
        ).exclude(
            profile__name_hotel='',
            profile__address='',
        )

        for user in users_with_profiles:

            solutions_natural = Applied_solutions.objects.filter(
                user_id=user.pk,
                solution__survey_id = 1
            )

            solutions_naturalApplied = Applied_solutions.objects.filter(
                user_id=user.pk,
                solution__survey_id = 1,
                applied=True
            )

            if len(solutions_naturalApplied) > 0:
                percentage_natural = (len(solutions_naturalApplied)/len(solutions_natural)) * 100
            else:
                percentage_natural = 0

            solutions_socio = Applied_solutions.objects.filter(
                user_id=user.pk,
                solution__survey_id = 2
            )

            solutions_socioApplied = Applied_solutions.objects.filter(
                user_id=user.pk,
                solution__survey_id = 2,
                applied=True
            )

            if len(solutions_socioApplied) > 0:
                percentage_socio = (len(solutions_socioApplied)/len(solutions_socio)) * 100
            else:
                percentage_socio = 0

            solutions_eco = Applied_solutions.objects.filter(
                user_id=user.pk,
                solution__survey_id = 3
            )

            solutions_ecoApplied = Applied_solutions.objects.filter(
                user_id=user.pk,
                solution__survey_id = 3,
                applied=True
            )

            if len(solutions_ecoApplied) > 0:
                percentage_eco = (len(solutions_ecoApplied)/len(solutions_eco)) * 100
            else:
                percentage_eco = 0

            user.percentage_natural = percentage_natural
            user.percentage_socio = percentage_socio
            user.percentage_eco = percentage_eco


        context = {
            'users_with_profiles': users_with_profiles,
        }
        return render(request, 'core/listEcoHotels.html', context)