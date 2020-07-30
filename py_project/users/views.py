from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.
def userlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            print("성공")
            login(request, myuser)
            return redirect('/')
        else:
            print("실패")
    return render(request, 'users/login.html')


def userlogout(request):
    logout(request)
    return redirect('/')
