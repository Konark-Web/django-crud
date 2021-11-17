from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from .models import Post
from .forms import PostForm, RegistrationForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def signup(request):
    if request.user.is_authenticated:
        return redirect('blog_page')

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('blog_page')

    return render(request, 'registration/registration.html', {'form': form})


def blog_page(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'blog/blog-page.html', {'page_object': page_object})


def blog_new(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form_saved = form.save(commit=False)
            form_saved.author = request.user
            form_saved.save()

            return redirect('blog_single', pk=form_saved.pk)

    return render(request, 'blog/blog-new.html', {'form': form})


def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_edited = request.GET.get('edited')

    post.views = post.views + 1
    post.save()

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
    posts = Post.objects.filter(author=author_id)
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    post_deleted = request.GET.get('deleted')

    return render(request, 'blog/user-posts.html', {'page_object': page_object, 'author': author,
                                                    'post_deleted': post_deleted})
