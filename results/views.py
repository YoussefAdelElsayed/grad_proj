from django.shortcuts import render,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
# Create your views here.

def result(request):
    stu = None
    if request.method == "POST":
        form =StudentForm(request.POST)
        if form.is_valid():
            sitting_number = form['sitting_number'].value()
            try:
                stu = Student.objects.get(sitting_number=sitting_number)
            except Student.DoesNotExist:
                messages.error(request, 'رقم الجلوس غير صحيح')
    else:
        form =StudentForm()
        
    context = {
        "stu":stu,
        "title":"النتائج",
        "form":form,
    }
    return render(request, "results/result.html",context)

