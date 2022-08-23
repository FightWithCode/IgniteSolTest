from django.urls import path
from . import apis

app_name = 'books'

urlpatterns = [
    # APIs Routing
    path('search-book', apis.QueryBook.as_view(), name='search-book')
]
