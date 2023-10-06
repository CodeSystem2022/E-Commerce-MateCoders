from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos.')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres letras y números.')
    password2 = forms.CharField(label='Repetir Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=30, required=True, help_text='Requerido. Repita su password.')
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=254, required=True, help_text='Se requiere una dirección de e-mail válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
