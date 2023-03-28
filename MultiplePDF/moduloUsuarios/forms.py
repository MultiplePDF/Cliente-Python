from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    name_user = forms.CharField(max_length=85, required=True)
    email = forms.CharField(max_length=40, required=False)
    user = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = (
            'user',
            'name_user',
            'password',
            'email',

        )