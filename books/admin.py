from django.contrib import admin
from .models import Author, Book, BookAuthors, Language, BookLanguage, Subject, Bookshelves, BookShelf, Format


admin.site.register(Author)
admin.site.register(BookShelf)
admin.site.register(Book)
admin.site.register(BookAuthors)
admin.site.register(Language)
admin.site.register(BookLanguage)
admin.site.register(Subject)
admin.site.register(Bookshelves)
admin.site.register(Format)
