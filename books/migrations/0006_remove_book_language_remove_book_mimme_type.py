# Generated by Django 4.1 on 2022-08-23 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_language_book_mimme_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='book',
            name='mimme_type',
        ),
    ]
