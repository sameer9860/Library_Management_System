from django.shortcuts import render
from .models import Book
from .utils import best_first_search


# Create your views here.

def index(request):
    query = request.GET.get('q')
    results = []
    if query:
        books = Book.objects.all()
        results = best_first_search(query, books)
    
    return render(request, 'app/index.html', {'results': results, 'query': query})