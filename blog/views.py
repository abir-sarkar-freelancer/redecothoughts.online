from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category
# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-date_published')[:6]
    context = {'posts': posts}
    return render(
        request,
        'blog/home.html',
        context,
    )


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(
        request,
        'blog/category_list.html',
        context,
    )


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    posts_list = Post.objects.filter(category=category)
    paginator = Paginator(
        posts_list,
        6,
    )
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_detail.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    query = request.GET.get('q')
    posts = []

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'posts': posts,
    }

    return render(request, 'blog/search.html', context)
