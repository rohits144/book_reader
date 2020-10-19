from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from datetime import datetime

logger = logging.getLogger()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    display_pic = models.ImageField(upload_to='profiles', verbose_name='profile picture', blank=True)
    total_books = models.PositiveIntegerField(verbose_name='Total number of books for user', editable=True, default=0)
    curr_no_books = models.PositiveIntegerField(verbose_name='Number of books Currently reading', editable=True, default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, display_pic='profiles/dpp.jpg')
    instance.profile.save()
    logger.info("Profile saved successfully for {}".format(instance.username))


class Author(models.Model):
    name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='authors', verbose_name='authors image', blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    book_image = models.ImageField(upload_to='books', verbose_name='book image', blank=True)
    isbn_num = models.CharField(max_length=30, blank=True)
    total_pages = models.PositiveIntegerField(verbose_name='Total number of pages in book', editable=True, blank=True)
    author = models.CharField(max_length=100)
    author_obj = models.ForeignKey(Author, on_delete=models.DO_NOTHING, blank=True, null=True)
    genre = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=100, choices=(
    ('Want to read', 'Not started'), ('Currently reading', 'Reading'), ('Completed reading', 'Completed')))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.book_image == "":
            self.book_image = "books/b1.jpg"
        super(Book, self).save(*args, **kwargs)


@receiver(post_save, sender=Book)
def create_author(sender, instance, created, **kwargs):
    if created:
        if len(Author.objects.filter(name__iexact=instance.author)) > 0:
            logger.info("Author already exist, No need to create again")
            instance.author_obj = Author.objects.get(name__iexact=instance.author)
            instance.save()
        else:
            obj = Author.objects.create(name=instance.author, author_image='profiles/dpp.jpg')
            instance.author_obj = obj
            instance.save()
    logger.info("Author created successfully for {}".format(instance.author))


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    pages_read = models.PositiveIntegerField(verbose_name='total number of pages read', editable=True, blank=False)
    progress_date = models.DateTimeField(blank=False, null=False, default=datetime.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + "'s " + self.book.title + "'s " + "Progress"
