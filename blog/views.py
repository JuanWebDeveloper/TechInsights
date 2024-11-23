from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def blog(request):
    return render(request, 'blog.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=User.objects.get(
                email=email).username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create a new user with the cleaned data from the form
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Save the user to the database
            user.save()
            # Log the user in
            login(request, user)
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
