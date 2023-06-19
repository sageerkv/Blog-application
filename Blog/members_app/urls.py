from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
from .views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register')
]