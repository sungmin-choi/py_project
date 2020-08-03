from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.userlogin),
    url(r'^logout/$', views.userlogout),
    url(r'^join/$', views.userjoin),
    url(r'^me/$', views.userDetail),
    url(r'^change_password/$', views.change_password),
    url(r'^example/$', views.example),
]
