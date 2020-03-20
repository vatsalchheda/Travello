from django.shortcuts import render
from .models import Destination
from .models import Blog
# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


def blog(request):
     blogs = Blogs.objects.all()
     return render(request, "dummy.html", {'blogs': blogs})
