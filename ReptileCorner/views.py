from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

def home(request):
    # return HttpResponse("Hello World!")
    posts = Post.objects.all().order_by('-date')[:5]
    return render(request, 'home.html', { 'posts': posts })

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')