from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class CustonRegisterForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'last_name', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        
        return password1
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name_hotel', 'address', 'bio', 'hotel_logo']
        widgets = {
            'name_hotel': forms.TextInput(attrs={
                'class': 'form-control ps-5 custom-input',
                'placeholder': 'Nombre del hotel',
                'style': 'height: 45px; border-radius: 10px; background-color: #f8fafc; color: #0d0c22;',
                'autocomplete': 'off',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control ps-5 custom-input',
                'placeholder': 'Ubicación',
                'style': 'height: 45px; border-radius: 10px; background-color: #f8fafc; color: #0d0c22;',
                'autocomplete': 'off',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control ps-5 custom-input',
                'placeholder': 'Cuéntanos sobre tu hotel',
                'rows': 4,
                'style': 'border-radius: 10px; background-color: #f8fafc; color: #0d0c22;',
            }),
            'hotel_logo': forms.ClearableFileInput(attrs={
                'class': 'form-control custom-input',
                'style': 'height: 45px; border-radius: 10px;',
            }),
        }
