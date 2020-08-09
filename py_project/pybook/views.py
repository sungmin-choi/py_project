from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Comment, UserDetail
from django.urls import reverse
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
        print(request.post)
        comment_form = BookCommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        comment_form.instance.book_id = book_id

        if comment_form.is_valid():
            comment_form.save()
            comment_form = BookCommentForm()
            comments = book_detail.comments.all()
            grade = book_detail.grade * 10
            context = {
                'book_detail': book_detail,
                'comments': comments,
                'comment_form': comment_form,
                'grade': grade
            }
            return render(request, 'pybook/bookDetail.html', context)
    else:
        comment_form = BookCommentForm()
        comments = book_detail.comments.all()
        grade = book_detail.grade * 10
        context = {
            'book_detail': book_detail,
            'comments': comments,
            'comment_form': comment_form,
            'grade': grade
        }
        return render(request, 'pybook/bookDetail.html', context)


def deleteCommment(request, comment_id, book_id):
    comments = Comment.objects.filter(pk=comment_id)
    comments.delete()
    book_detail = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(book_id=book_id)
    comment_form = BookCommentForm()
    comments = book_detail.comments.all()
    grade = book_detail.grade * 10
    context = {
        'book_detail': book_detail,
        'comments': comments,
        'comment_form': comment_form,
        'grade': grade
    }
    return render(request, 'pybook/bookDetail.html', context)


def like(request, book_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user in comment.like_users.all():
        # 좋아요 취소
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)

    book_detail = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(book_id=book_id)
    comment_form = BookCommentForm()
    comments = book_detail.comments.all()
    grade = book_detail.grade * 10
    context = {
        'book_detail': book_detail,
        'comments': comments,
        'comment_form': comment_form,
        'grade': grade
    }
    return render(request, 'pybook/bookDetail.html', context)


def subscribe(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    if request.user in book_detail.subscribe_users.all():
        # 구독 취소
        book_detail.subscribe_users.remove(request.user)

    else:
        book_detail.subscribe_users.add(request.user)

    comments = Comment.objects.filter(book_id=book_id)
    comment_form = BookCommentForm()
    comments = book_detail.comments.all()
    grade = book_detail.grade * 10
    context = {
        'book_detail': book_detail,
        'comments': comments,
        'comment_form': comment_form,
        'grade': grade
    }
    return render(request, 'pybook/bookDetail.html', context)
