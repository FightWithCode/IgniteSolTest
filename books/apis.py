from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Bookshelves, BookAuthors, BookLanguage, BookShelf, BookSubject, Subject, Language, Format
from django.core.paginator import Paginator


class QueryBook(APIView):
    def get(self, request):
        response = {}
        try:
            # Getting all the filter parameters
            mime_type = request.query_params.get('mime')
            
            # Language and book are integers thus converting using int() with try block to make it none it it is invalid
            try:
                language = int(request.query_params.get('language'))
            except:
                language = None
            try:
                book_id = int(request.query_params.get('book_id'))
            except:
                book_id = None
            title = request.query_params.get('title')

            # Filtering books with given laguage and mime_type
            book_id_list = []
            if language:
                book_id_list = BookLanguage.objects.filter(language_id=language).values_list('book_id', flat=True)
            if mime_type:
                mime_type_filter = Format.objects.filter(mime_type__icontains=mime_type).values_list('book_id', flat=True)
                book_id_list = list(set(book_id_list) | set(mime_type_filter))
            queryset = Book.objects.filter(id__in=book_id_list)

            # Filtering books on basis of title once the language and mime filter is done
            if title and queryset:
                queryset.filter(title__icontains=title)
            else:
                queryset = Book.objects.filter(title__icontains=title)
            # Fitering based on the bookd_id
            if book_id:
                queryset = queryset.filter(id=book_id)
            
            # Making required object for the seach results with descending order of popularity
            data = []
            for i in queryset.order_by('-download_count'):
                temp_dict = {}
                temp_dict['title'] = i.title
                temp_dict['download_count'] = i.download_count
                # Get details and if author not found or any error occures continue to next book
                try:
                    book_author_obj = BookAuthors.objects.filter(book_id=i.id)[0]  # Getting first author only for now
                    author_obj = Author.objects.get(id=book_author_obj.author_id)
                    temp_dict['author'] = {
                        'name': author_obj.name,
                        'birth': author_obj.birth_year,
                        'death': author_obj.death_year,
                    }
                    temp_dict['genere'] = 'Not sure which table has genre'
                    languages = []
                    for book_lan in BookLanguage.objects.filter(book_id=i.id):
                        lan_obj = Language.objects.get(id=book_lan.language_id)
                        languages.append(lan_obj.code)
                    temp_dict['languages'] = languages
                    subjects = []
                    for book_sub in BookSubject.objects.filter(book_id=i.id):
                        sub_obj = Subject.objects.get(id=book_sub.subject_id)
                        subjects.append(sub_obj.name)
                    temp_dict['subjects'] = subjects

                    shelves = []
                    for book_sh in Bookshelves.objects.filter(book_id=i.id):
                        sh_obj = BookShelf.objects.get(id=book_sh.bookshelf_id)
                        shelves.append(sh_obj.name)
                    temp_dict['shelves'] = shelves

                    links = []
                    for link in Format.objects.filter(book_id=i.id):
                        links.append(link.url)
                    temp_dict['links'] = links
                except Exception as e:
                    pass
                data.append(temp_dict)
            response = data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response['msg'] = 'error'
            response['error'] = str(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

