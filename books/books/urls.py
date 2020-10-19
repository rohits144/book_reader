from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from .views import index_view, register, profile, add_book, upload_dp, add_progress, books_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('add_book/', add_book, name='add_book'),
    path('upload_dp/', upload_dp, name='upload_dp'),
    path('add_progress/', add_progress, name='add_progress'),
    path('book_list/', books_list_view, name='book_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
