
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index_view, register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
