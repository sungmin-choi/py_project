from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^search/$', views.search),
    url(r'^book/(?P<book_id>.+)/$', views.bookDetail, name="book"),
    path('delete/<int:book_id>/<int:comment_id>', views.deleteCommment),
    path('like/<int:book_id>/<int:comment_id>', views.like),
    path('subscribe/<int:book_id>', views.subscribe),
]
