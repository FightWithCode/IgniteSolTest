from django.shortcuts import render
from books.models import Language

def index(request):
    context = {
        'languages': Language.objects.all()
    }

    return render(request, 'index.html', context)
