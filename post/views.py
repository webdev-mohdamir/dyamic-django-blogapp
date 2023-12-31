from django.shortcuts import render
from .postdata import posts as allPost


def index(request):
    return render(request, "index.html", {"allPost": allPost})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def post(request, slug):
    return render(request, "post.html", {"allPost": allPost, "slug": slug})
