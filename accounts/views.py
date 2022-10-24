from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy


from .forms import CustomUserCreationForm, UserEditForm
# Create your views here.


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["email"]} registered successfully.')
            # return redirect('website:website_index')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'You are already logged in as <b>{request.user.username}</b> '))
        return redirect('website:website_index')

    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'User {user.username} logged successfully')
            return redirect('website:website_index')
        else:
            messages.warning(request, f'User {username} could not authenticate, check credential')

    return render(request, 'accounts/login.html', context={'username': username})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('accounts:login')


class ProfileView(LoginRequiredMixin, DetailView):
    context_object_name = "current_user"
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user
