from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('index/', views.index, name='index'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('password_change/', views.password_change, name="password_change"),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name="password_reset_confirm"),
]