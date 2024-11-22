from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from comments.forms import CommentForm 

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts })

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)  # Make sure to pass data=request.POST
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('posts:page', slug=post.slug) 
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_page.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return redirect('posts:page', slug=post.slug)  # Redirect if not the author

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES, instance=post)  # Use forms.CreatePost
        if form.is_valid():
            form.save()
            return redirect('posts:page', slug=post.slug)
    else:
        form = forms.CreatePost(instance=post)  # Use forms.CreatePost
    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return redirect('posts:page', slug=post.slug)  # Redirect if not the author

    if request.method == 'POST':  # Confirm deletion with POST request
        post.delete()
        return redirect('posts:list')  # Redirect to post list after deletion
    return render(request, 'posts/post_delete.html', {'post': post})