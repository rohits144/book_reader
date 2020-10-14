from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'book_image', 'total_pages', 'author', 'genre', 'language', 'status']