from django.shortcuts import render,get_object_or_404
from .models import Year,Lecture
# Create your views here.


def years(request):
    year=Year.objects.all()
    context={
        "title":"الفرقة",
        "years":year,
    }
    
    return render(request, "edu/years.html", context)


def lectures(request,slug):
    lecture = get_object_or_404(Year,slug=slug)
    context = {
        "title": f"{lecture} الفرقة",
        "lectures":lecture,
    }
    return render(request, "edu/lectures.html", context)



def lecture_details(request,slug):
    lecture = get_object_or_404(Lecture, slug=slug)
    context = {
        "title": f"{lecture}",
        "lecture": lecture,
    }
    return render(request, "edu/lecture_details.html", context)


