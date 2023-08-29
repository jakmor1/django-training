from django.shortcuts import render, get_object_or_404

from .models import Category, Post, Author

def post_list_view(request, category_name=None, author_name=None):
    if category_name:
        queryset = Post.objects.filter(category__name=category_name, public=True)
    elif author_name:
        queryset = Post.objects.filter(author__author=author_name, public=True)
    else:
        queryset = Post.objects.filter(public=True)
    context = {
        'object_list': queryset.order_by('-date_publish'),
        'category_list': Category.objects.all(),
        'category_name': category_name,
        'author_list': Author.objects.all(),
    }
    return render(request, 'blog/post_list.html', context)


def post_detail_view(request, post_id):
    context = {
        'object': get_object_or_404(Post, id=post_id),
        'category_list': Category.objects.all(),
        'category_name': None,
    }
    return render(request, 'blog/post_detail.html', context)