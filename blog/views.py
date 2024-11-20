from django.shortcuts import render


def blog(request):
    return render(request, 'blog.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')
