from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reptile
from .forms import ReptileForm

# Create your views here.
@login_required
def add_reptile(request):
     if request.method == 'POST':
         form = ReptileForm(request.POST, request.FILES)
         if form.is_valid():
             reptile = form.save(commit=False)
             reptile.user = request.user 
             reptile.save()
             return redirect('reptiles:reptile_detail', pk=reptile.pk) 
     else:
         form = ReptileForm()
     return render(request, 'reptiles/add_reptile.html', {'form': form})

def reptile_detail(request, pk):
    reptile = get_object_or_404(Reptile, pk=pk)
    return render(request, 'reptiles/reptile_detail.html', {'reptile': reptile})

def edit_profile(request, pk):
    reptile = get_object_or_404(Reptile, pk=pk)
    if request.method == 'POST':
        form = ReptileForm(request.POST, request.FILES, instance=reptile)
        if form.is_valid():
            form.save()
            return redirect('reptiles:reptile_detail', pk=reptile.pk)
    else:
        form = ReptileForm(instance=reptile)
    return render(request, 'reptiles/edit_reptile.html', {'form': form, 'reptile': reptile})

def reptiles_list(request):
    reptiles = Reptile.objects.all()
    return render(request, 'reptiles/reptiles_list.html', {'reptiles': reptiles})