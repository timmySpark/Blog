from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *


urlpatterns = [
    path('', Index,name='index'),
    path('blog/category/<str:slug>', BlogHome, name='Blog'),
    path('blog-details/<str:slug>', PostDetail, name='post-details'),
    path('blog/search', PostSearch, name='search-result'),
    path('blog/404',Page_404, name='page404'),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)