from django.shortcuts import render
from blog.models import Category, Post


def home_page(request):
    categories = Category.objects.exclude(name='Sin Categoría')
    posts = Post.objects.all().order_by('-created_at')[:3]
    return render(request, 'home_page.html', {
        'categories': categories,
        'posts': posts})
