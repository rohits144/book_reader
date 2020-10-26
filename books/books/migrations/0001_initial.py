# Generated by Django 3.0.7 on 2020-10-26 09:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author_image', models.ImageField(blank=True, upload_to='authors', verbose_name='authors image')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('book_image', models.ImageField(blank=True, upload_to='books', verbose_name='book image')),
                ('isbn_num', models.CharField(blank=True, max_length=30)),
                ('total_pages', models.PositiveIntegerField(blank=True, verbose_name='Total number of pages in book')),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(blank=True, max_length=20)),
                ('language', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('Want to read', 'Not started'), ('Currently reading', 'Reading'), ('Completed reading', 'Completed')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('author_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='books.Author')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('title', 'isbn_num', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('display_pic', models.ImageField(blank=True, upload_to='profiles', verbose_name='profile picture')),
                ('total_books', models.PositiveIntegerField(default=0, verbose_name='Total number of books for user')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages_read', models.PositiveIntegerField(verbose_name='total number of pages read')),
                ('total_books', models.PositiveIntegerField(default=0, verbose_name='total books read')),
                ('progress_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
