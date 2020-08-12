from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Comment, UserSubscribe
from users.models import User
from django.urls import reverse
from django.db.models import Q
from .form import BookCommentForm, BookGrade
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
            str1 = "/book/"+str(book_detail.id)
            return HttpResponseRedirect(str1)
    else:
        comment_form = BookCommentForm()

        comments = book_detail.comments.all()
        grade_users = book_detail.grade_users
        grade = book_detail.grade * 10
        context = {
            'book_detail': book_detail,
            'comments': comments,
            'comment_form': comment_form,
            'grade': grade,
            'grade_users': grade_users
        }
        return render(request, 'pybook/bookDetail.html', context)


def deleteCommment(request, comment_id, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    comments = Comment.objects.filter(pk=comment_id)
    comments.delete()
    str1 = "/book/"+str(book_detail.id)
    return HttpResponseRedirect(str1)


def like(request, book_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user in comment.like_users.all():
        # 좋아요 취소
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)

    book_detail = get_object_or_404(Book, pk=book_id)
    str1 = "/book/"+str(book_detail.id)
    return HttpResponseRedirect(str1)


def subscribe(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)

    if request.user in book_detail.subscribe_users.all():
        # 구독 취소
        book_detail.subscribe_users.remove(request.user)

    else:
        book_detail.subscribe_users.add(request.user)

    str1 = "/book/"+str(book_detail.id)
    return HttpResponseRedirect(str1)


def grade(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        if request.user in book_detail.grade_users.all():
            b = False
            info = "이미 평점한 책입니다."
            context = {'info': info, 'b': b}
            return render(request, 'users/info.html', context)
        else:
            number = request.POST['number']
            a1 = book_detail.gradeNumber
            a2 = book_detail.grade
            a3 = (float(a2)+float(number))/(float(a1)+1)
            book_detail.gradeNumber = book_detail.gradeNumber+1
            book_detail.grade = a3
            book_detail.grade_users.add(request.user)
            book_detail.save()

            str1 = "/book/"+str(book_detail.id)
            return HttpResponseRedirect(str1)

    str1 = "/book/"+str(book_detail.id)
    return HttpResponseRedirect(str1)
