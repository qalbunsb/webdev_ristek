from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField, UserCreationForm
from .models import *

class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='email',
        widget=forms.TextInput(
            attrs={'class' : 'form-control','autofocus': True, 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class' : 'form-control','autocomplete': 'current-password', 'placeholder': 'Password'}),
    )

class MyUserCreationForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control'
        }

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Profile
        fields = ('full_name',)