from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def list_posts(request):
    return render(request, 'list_posts.html')
