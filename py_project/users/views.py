from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from pybook.models import UserSubscribe
from .models import User
from pybook.models import Book
from django.contrib.auth.forms import UserCreationForm
from .form import JoinForm
from django.contrib.auth.hashers import check_password

# Create your views here.


def userlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            return redirect('/')
    return render(request, 'users/login.html')


def userlogout(request):
    logout(request)
    return redirect('/')


def userjoin(request):
    b = False
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            us = UserSubscribe.objects.create(email=request.POST['email'])
            us.save()
            form.save()
            b = True
            info = "가입성공"
            context = {'info': info, 'b': b}
            return render(request, 'users/info.html', context)
        else:
            b = False
            info = "이메일이 존재하거나 혹은 비밀번호 잘못입력 하셨습니다"
            context = {'info': info, 'b': b}
            return render(request, 'users/info.html', context)
    elif request.method == "GET":
        form = JoinForm()
        return render(request, 'users/join.html', {'form': form})


def userDetail(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'users/userDetail.html', context)


def change_password(request):
    b = False
    if request.method == 'POST':
        current_password = request.POST.get("OriginPassword")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("setPassword1")
            password_confirm = request.POST.get("setPassword2")
            if new_password == password_confirm:
                b = True
                info = "변경성공"
                context = {'info': info, 'b': b}
                user.set_password(new_password)
                user.save()
                return render(request, 'users/info.html', context)
            else:
                b = False
                info = "새로운 비밀번호가 맞지않습니다"
                context = {'info': info, 'b': b}
                return render(request, 'users/info.html', context)
        else:
            b = False
            info = "기존 비밀번호가 맞지않습니다"
            context = {'info': info, 'b': b}
            return render(request, 'users/info.html', context)

    else:
        return render(request, 'users/change_password.html')


def example(request):
    return render(request, 'users/example.html')
