from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Post, Category


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    # ИСПРАВЛЕНО: 10 → 5
    paginator = Paginator(post_list, 5)  # ← Измените эту строку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        ),
        pk=pk
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_list = category.post_set.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
