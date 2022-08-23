from django.db import models


class Author(models.Model):
    birth_year = models.IntegerField()
    death_year = models.IntegerField()
    name = models.CharField(max_length=128)


class Book(models.Model):
    download_count = models.IntegerField(default=0)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField()

    def __str__(self):
        return self.title


class BookAuthors(models.Model):
    book_id = models.IntegerField()
    author_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_authors'


class Bookshelves(models.Model):
    book_id = models.IntegerField()
    bookshelf_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_bookshelves'


class BookLanguage(models.Model):
    book_id = models.IntegerField()
    language_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_languages'


class BookSubject(models.Model):
    book_id = models.IntegerField()
    subject_id = models.IntegerField()

    class Meta:
        db_table = 'books_book_subjects'


class BookShelf(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'books_bookshelf'


class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book_id = models.IntegerField()

    class Meta:
        db_table = 'books_format'

class Language(models.Model):
    code = models.CharField(max_length=4)
    
    class Meta:
        db_table = 'books_language'
    
    def __str__(self):
        return self.code


class Subject(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'books_subject'

# from books.models import Book, Language, Format, BookLanguage
# for i in Book.objects.all():
#     try:
#         l = Format.objects.get(book_id=i.id)
#         # for j in l:
#         #     lan = Language.objects.get(id=l.language_id)
#         #     i.language = lan.code
#         #     i.save()
#     except Exception as e:
#         print(e)