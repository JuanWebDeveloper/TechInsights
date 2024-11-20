from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Login to login
            return redirect('home_page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
