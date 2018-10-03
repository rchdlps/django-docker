from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})
