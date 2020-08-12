from django.db import models
from users.models import User

# Create your models here.


class Book(models.Model):
    objects = models.Manager()
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=15)
    grade = models.FloatField(default=0)
    gradeNumber = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    author_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    area = models.CharField(max_length=15, blank=True)
    subscribe_users = models.ManyToManyField(
        User, related_name='subscribe_posts', blank=True)
    grade_users = models.ManyToManyField(
        User, related_name='User_posts', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    comment_textfield = models.TextField()
    like_users = models.ManyToManyField(
        User, related_name='like_posts', blank=True)

    def __str__(self):
        return (self.author.email if self.author else "무명") + "의 댓글"

    class Meta:
        ordering = ['-id']


class UserSubscribe(models.Model):
    email = models.EmailField(unique=True)
    user_books = models.ManyToManyField(
        Book, related_name='book_posts')

    def __str__(self):
        return self.email
