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
