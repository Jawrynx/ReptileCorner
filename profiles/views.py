from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages

from django.contrib.auth.models import User
from posts.models import Post

@login_required
def profile(request, username): 
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-date') 
    context = {
        'user': user, 
        'posts': posts
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profiles:profile', username=request.user.username) 
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'profiles/edit_profile.html', context)