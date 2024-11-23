from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ManagePost


@login_required
def welcome(request):
    return render(request, 'welcome.html')


@login_required
def list_posts(request):
    return render(request, 'list_posts.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = ManagePost(request.POST)
        if form.is_valid():
            # Logic for saving the post
            redirect('list_posts')
    else:
        form = ManagePost()

    return render(request, 'create_post.html', {'form': form})
