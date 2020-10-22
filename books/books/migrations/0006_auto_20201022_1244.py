# Generated by Django 3.1.2 on 2020-10-22 12:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_auto_20201022_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_num',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'isbn_num', 'user')},
        ),
    ]
