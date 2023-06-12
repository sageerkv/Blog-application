from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>remove', DeletePostView.as_view(), name="delete_post"),
    
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('password_change/', views.password_change, name="password_change"),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name="password_reset_confirm"),
]