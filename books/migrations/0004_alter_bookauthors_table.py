# Generated by Django 4.1 on 2022-08-23 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_dowload_count_book_download_count'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookauthors',
            table='books_book_authors',
        ),
    ]
