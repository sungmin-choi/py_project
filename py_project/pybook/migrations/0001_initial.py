# Generated by Django 3.0.8 on 2020-08-09 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=15)),
                ('grade', models.FloatField(default=0)),
                ('gradeNumber', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('author_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('area', models.CharField(blank=True, max_length=15)),
                ('subscribe_users', models.ManyToManyField(related_name='subscribe_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user_books', models.ManyToManyField(related_name='book_posts', to='pybook.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
                ('comment_textfield', models.TextField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pybook.Book')),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
