from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from dashboard.models import Home
from profiles.models import Doctor
from edu.models import Lecture
from .models import Post

# Create your views here.

def home(request):
    info=Home.objects.get(id=1)
    posts = Post.objects.all().order_by("-created")[:3]
    doctors = Doctor.objects.all().order_by("-created")[:10]
    lectures = Lecture.objects.all().order_by("-created")[:3]
    context={
        "title": "معهد السويس لنظم المعلومات الادارية",
        "info":info,
        "posts":posts,
        "doctors":doctors,
        "lectures":lectures,
    }
    return render(request, "blog/home.html",context)


def dean(request):
    context = {
        "title": "كلمة عميد المعهد",
    }
    return render(request, "blog/dean.html",context)


def all_posts(request):
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "title": "الاخبار",
        "posts": page_obj,
    }
    
    
    return render(request, "blog/all_posts.html",context)


def post_details(request,id):
    post = get_object_or_404(Post, id=id)
    context = {
        "title": f"{post.title}",
        "post": post,

    }
    return render(request, "blog/post_details.html",context)