from django.shortcuts import render, redirect
from .forms import SignInForm


def blog(request):
    return render(request, 'blog.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Login to login
            return redirect('home_page')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def signup(request):
    return render(request, 'signup.html')
