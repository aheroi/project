from django.urls import path
from . import views
from .views import ProfileView, ProfileEditView


app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
path("profile/edit/", ProfileEditView.as_view(), name="edit"),
    path('profile/', ProfileView.as_view(), name='profile'),
]
