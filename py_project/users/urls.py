from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.userlogin),
    url(r'^logout/$', views.userlogout),
    url(r'^join/$', views.userlogout),
]
