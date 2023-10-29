from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    post = Post.objects.all()[:11]
    data = {
        'posts': post
    }
    return render(request, 'blog/index.html', data)


def posts(request, url):
    posts = Post.objects.get(url=url)
    # print (posts)
    return render(request, 'blog/posts.html', {'posts': posts})
