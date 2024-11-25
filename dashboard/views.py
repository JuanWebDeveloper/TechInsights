from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ManagePost
from blog.models import Post, Category


@login_required
def welcome(request):
    return render(request, 'welcome.html')


@login_required
def list_posts(request):
    posts_list = Post.objects.filter(
        author=request.user).order_by('-created_at')

    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'list_posts.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = ManagePost(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            if not category:
                category, created = Category.objects.get_or_create(
                    name='Sin Categoría')

            Post.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                category=category,
                author=request.user
            )
            return redirect('list_posts')
    else:
        form = ManagePost()

    return render(request, 'create_post.html', {'form': form})
