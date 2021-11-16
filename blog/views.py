from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from .models import Post
from .forms import PostForm

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
    post_edited = request.GET.get('edited')
    return render(request, 'blog/blog-single.html', {'post': post, 'post_edited': post_edited})


def blog_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user.id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return redirect(f'{reverse("blog_single", args=(post.pk,))}?edited=true')

    return render(request, 'blog/blog-edit.html', {'form': form, 'post': post})


def blog_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user.id)
    post.delete()

    return redirect(f'{reverse("user_posts", args=(post.author.id,))}?deleted=true')


def user_posts(request, author_id):
    author = User.objects.get(id=author_id)
    posts = get_list_or_404(Post, author=author_id)
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    post_deleted = request.GET.get('deleted')

    return render(request, 'blog/user-posts.html', {'page_object': page_object, 'author': author,
                                                    'post_deleted': post_deleted})
