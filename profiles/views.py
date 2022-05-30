from django.shortcuts import render
from .models import Department
# Create your views here.


def doctors(request):
    departments=Department.objects.all()
    context={
        "title":"هيئة التدريس",
        "departments":departments,
    }
    return render(request, "profiles/doctors.html",context)
