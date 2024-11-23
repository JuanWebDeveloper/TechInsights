from django.shortcuts import render, redirect
from .forms import ManagePost


def welcome(request):
    return render(request, 'welcome.html')


def list_posts(request):
    return render(request, 'list_posts.html')


def create_post(request):
    if request.method == 'POST':
        form = ManagePost(request.POST)
        if form.is_valid():
            redirect('list_posts')
    else:
        form = ManagePost()
        return render(request, 'create_post.html', {'form': form})
