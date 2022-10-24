from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.Field(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Username'
    }))
    # first_name = forms.Field(widget=forms.TextInput(attrs={
    #     'class': 'form-control form-control-user', 'placeholder': 'First Name'
    # }))
    # last_name = forms.Field(widget=forms.TextInput(attrs={
    #     'class': 'form-control form-control-user', 'placeholder': 'Last Name'
    # }))
    email = forms.Field(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'E-mail'
    }))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Password'
    }), label='Password')
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Confirm password'
    }), label='Confirm password')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
