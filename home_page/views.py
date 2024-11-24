from django.shortcuts import render
from blog.models import Category


def home_page(request):
    categories = Category.objects.all()
    return render(request, 'home_page.html', {
        'categories': categories})
