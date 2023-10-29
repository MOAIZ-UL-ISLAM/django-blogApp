from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    post = Post.objects.all()[:11]
    data = {
        'posts': post
    }
    return render(request, 'blog/index.html', data)

#single post from blog database
def posts(request, url):
    post = Post.objects.get(url=url)
    # print (posts)
    data={
        'post': post
    }
    return render(request, 'blog/post.html', data)
