from django.db import models

# Create your models here.


class Book(models.Model):
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=15)
    grade = models.IntegerField(default=0)
    date = models.DateField()
    like = models.IntegerField(default=0)
    description = models.TextField()
    area = models.CharField(max_length=15)
