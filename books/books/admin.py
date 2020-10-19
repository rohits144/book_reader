from django.contrib import admin
from .models import Author, Book, Profile, Progress


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    pass