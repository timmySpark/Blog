from .models import *

def blog_renderer(request):
    category = Category.objects.all()
    side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]

    return {
        'category' : category,
        'side_recent_post':side_recent_post,
        'side_popular_post': side_popular_post,

    }