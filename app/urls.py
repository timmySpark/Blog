from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index,name='index'),
    path('blog/', BlogHome, name='blog'),
]
