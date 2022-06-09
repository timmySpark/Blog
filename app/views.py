from django.shortcuts import render
from app.models import *

# Create your views here.


def Index(request):
    template_name = 'index.html'
    category = Category.objects.all()
    featured_post = Blog.objects.all()[:3]
    recent_post = Blog.objects.all().order_by('-created_at')[4:7]
    side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]
    popular_post = Blog.objects.all().order_by('-created_at')[17]
    most_read_post = Blog.objects.all().order_by('-created_at')[18:22]
    hot_stuff = Blog.objects.all().order_by('?')[0]
    top_of_the_week = Blog.objects.all().order_by('-created_at')[23:26]
    context = {
        'category' : category,
        'featured_post' : featured_post,
        'recent_post': recent_post,
        'side_recent_post':side_recent_post,
        'side_popular_post': side_popular_post,
        'popular_post':popular_post,
        'most_read_post':most_read_post,
        'hot_stuff':hot_stuff,
        'top_of_the_week':top_of_the_week

    }
    return render(request, template_name,context)

def BlogHome(request):
    template_name = 'blog.html'
    return render(request, template_name)
