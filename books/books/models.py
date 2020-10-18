from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
logger = logging.getLogger()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_pic = models.ImageField(upload_to='profiles', verbose_name='profile picture', blank=True)

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
    author_image = models.ImageField(upload_to='image/', verbose_name='authors image', width_field=100, height_field=100, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    book_image = models.ImageField(upload_to='image/', verbose_name='book image', width_field=100, height_field=100, blank=True)
    total_pages = models.PositiveIntegerField(verbose_name='Total number of pages in book', editable=True, blank=True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_author', null=True, blank=True)
    genre = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=100, choices=(('Want to read', 'Not started'), ('Currently reading', 'Reading'), ('Completed reading', 'Completed')))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)