
from django.http import HttpResponse
from django.shortcuts import render
from blog import models


def hello_somebody(request):
    return HttpResponse('<h1>Hello!</h1>')


def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post' : post})