from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .form import JoinForm

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
    current_user = request.user
    context = {"email": current_user.email}
    return render(request, 'users/userDetail.html', context)


def change_password(request):
    b = False
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            b = True
            info = "변경성공"
            context = {'info': info, 'b': b}
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'users/info.html', context)
        else:
            b = False
            info = "비밀번호가 맞지않습니다"
            context = {'info': info, 'b': b}
            return render(request, 'users/info.html', context)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })
