from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def blog_page(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'blog/blog-page.html', {'page_object': page_object})


def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog-single.html', {'post': post})


def blog_edit(request, pk):
    return render(request, 'blog/blog-edit.html')


def user_posts(request, author_id):
    author = User.objects.get(id=author_id)
    posts = get_list_or_404(Post, author=author_id)
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'blog/user-posts.html', {'page_object': page_object, 'author': author})