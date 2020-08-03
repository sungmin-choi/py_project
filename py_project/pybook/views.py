from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
import json

# Create your views here.


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'pybook/index.html', context)


def search(request):
    searching = request.GET.get('searching')
    books = Book.objects.all().filter(Q(name__contains=searching)
                                      | Q(author__contains=searching))
    context = {'books': books, 'searching': searching}
    return render(request, 'pybook/search.html', context)


def bookDetail(request, id):
    return render(request, 'pybook/bookDetail.html')
