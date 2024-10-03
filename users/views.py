from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form })