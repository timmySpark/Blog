from django.shortcuts import render

# Create your views here.

def BlogHome(request):
    template_name = 'blog.html'
    return render(request, template_name)
