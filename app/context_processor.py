from .models import *

def blog_renderer(request):
    category = Category.objects.all()
    counts = []
    for c in category:
        category_count = Blog.objects.filter(category=c).count()
        counts.append(category_count)

    category_count = zip(category,counts)    
    side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]

    return {
        'category' : category,
        'cat_count':category_count,
        'side_recent_post':side_recent_post,
        'side_popular_post': side_popular_post,
        'counts':counts,
    }