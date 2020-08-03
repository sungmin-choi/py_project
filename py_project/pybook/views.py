from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Comment
from django.db.models import Q
from .form import BookCommentForm
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


def bookDetail(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(book_id=book_id)

    if request.method == 'POST':
        comment_form = BookCommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        comment_form.instance.book_id = book_id

        if comment_form.is_valid():
            comment_form.save()

    else:
        comment_form = BookCommentForm()
        comments = book_detail.comments.all()
        print(comments)
        context = {
            'book_detail': book_detail,
            'comments': comments,
            'comment_form': comment_form
        }
        return render(request, 'pybook/bookDetail.html', context)
