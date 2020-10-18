from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book, Profile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'book_image', 'total_pages', 'author', 'genre', 'language', 'status']


class UpdateDp(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_pic']