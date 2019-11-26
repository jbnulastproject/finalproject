from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog

# 홈페이지 함수


def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})

# 디테일 페이지 함수


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

# 포스트페이지 함수


def post(request):
    return render(request, 'blog/post.html')

# 글 생성 함수


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.contents = request.GET['contents']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
