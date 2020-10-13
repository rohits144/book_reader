from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_pic = models.ImageField(verbose_name='profile picture', width_field=100, height_field=100, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    author_image = models.ImageField(verbose_name='authors image', width_field=100, height_field=100, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=30)
    book_image = models.ImageField(verbose_name='book image', width_field=100, height_field=100, blank=True)
    total_pages = models.PositiveIntegerField(verbose_name='Total number of pages in book', editable=True, blank=True,)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=100, choices=(('Want to read', 'Not started'), ('Currently reading', 'Reading'), ('Completed reading', 'Completed')))