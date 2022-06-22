from django.shortcuts import redirect, render,get_object_or_404
from app.models import *
from app.forms import *

# Create your views here.


def Index(request):
    template_name = 'index.html'
    featured_post = Blog.objects.all()[:3]
    recent_post = Blog.objects.all().order_by('-created_at')[4:7]
    popular_post = Blog.objects.all().order_by('-created_at')[17]
    most_read_post = Blog.objects.all().order_by('-created_at')[18:22]
    hot_stuff = Blog.objects.all().order_by('?')[0]
    top_of_the_week = Blog.objects.all().order_by('-created_at')[23:26]
    context = {
        'featured_post' : featured_post,
        'recent_post': recent_post,
        'popular_post':popular_post,
        'most_read_post':most_read_post,
        'hot_stuff':hot_stuff,
        'top_of_the_week':top_of_the_week

    }
    return render(request, template_name,context)

def BlogHome(request,slug):
    template_name = 'blog.html'
    category = get_object_or_404(Category,slug=slug)
    post = Blog.objects.filter(category__slug=slug)

    context = {
        'post': post,
        'cat' : category,

    }

    return render(request, template_name,context)


def PostDetail(request,slug):
    template_name = 'article.html'
    post = get_object_or_404(Blog,slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.save()
            return redirect('/')

    postComment = Comment.objects.filter(post=post)
    context = {
        'post':post,
        'form':form,
        'postComment':postComment
    }
    return render(request, template_name,context)    

