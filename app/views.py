from django.shortcuts import render

# Create your views here.


def Index(request):
    template_name = 'index.html'
    return render(request, template_name)

def BlogHome(request):
    template_name = 'blog.html'
    return render(request, template_name)
