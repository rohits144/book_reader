# Generated by Django 3.1.2 on 2020-10-14 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author_image', models.ImageField(blank=True, height_field=100, upload_to='image/', verbose_name='authors image', width_field=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_pic', models.ImageField(blank=True, height_field=100, upload_to='image/', verbose_name='profile picture', width_field=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('book_image', models.ImageField(blank=True, height_field=100, upload_to='image/', verbose_name='book image', width_field=100)),
                ('total_pages', models.PositiveIntegerField(blank=True, verbose_name='Total number of pages in book')),
                ('genre', models.CharField(blank=True, max_length=20)),
                ('language', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('Want to read', 'Not started'), ('Currently reading', 'Reading'), ('Completed reading', 'Completed')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
