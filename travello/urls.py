from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogindex.html', views.blogindex, name='blogindex'),
    path('blog.html', views.blog, name='blog')
]
    