from django.shortcuts import render
from .models import Destination
from .models import Blogs
# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


def blog(request):
    blogs = Blogs.objects.all()
    return render(request, "blog.html", {'blogs': blogs})


def blogindex(request):
    blogs = Blogs.objects.all()
    return render(request, "index1.html", {'blogs': blogs})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
