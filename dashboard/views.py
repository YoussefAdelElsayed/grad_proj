from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Post
from blog.forms import PostForm
from profiles.models import Doctor,Department
from profiles.forms import DepartmentForm, DoctorForm,UserNameForm
from edu.models import Lecture
from edu.forms import LectureForm
from ask.models import Ask
from ask.forms import AnswerAskForm
from .forms import HomeForm,DegreeForm
from .models import Home,Degree
# Create your views here.

@login_required(redirect_field_name='next')
def overview(request):
    posts = Post.objects.all().order_by("-created")
    doctors = Doctor.objects.all()
    lectures =Lecture.objects.all()
    asks =Ask.objects.all()
    departments =Department.objects.all()
    context={
        "title": "Dashboard",
        "posts":posts,
        "doctors":doctors,
        "lectures":lectures,
        "asks":asks,
        "departments":departments,
    }
    return render(request, "dashboard/overview.html",context)


#Post CRUD
@login_required(redirect_field_name='next')
def show_posts(request):
    posts = Post.objects.all().order_by("-created")
    context={
        "title": "الاخبار",
        "posts": posts,
    }
    return render(request, "dashboard/show_posts.html", context)

@login_required(redirect_field_name='next')
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_posts")

    context = {
        "title": f"اضف خبر",
        "form":form,
    }
    return render(request, "dashboard/add_post.html",context)

@login_required(redirect_field_name='next')
def update_post(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    
    if "update_post" in request.POST:
        form = PostForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
            return redirect("show_posts")
    
    if "delete_post" in request.POST:
        post.delete()
        return redirect("show_posts")
    
    context = {
        "title": f"تعديل الخبر",
        "form":form,
        "post":post
        
    }
    return render(request, "dashboard/update_post.html",context)


#Doctor CRUD
@login_required(redirect_field_name='next')
def show_doctors(request):
    doctors = Doctor.objects.all().order_by("-created")
    context = {
        "title": "الاساتذة",
        "doctors": doctors,
    }
    return render(request, "dashboard/show_doctors.html", context)


@login_required(redirect_field_name='next')
def add_doctor(request):
    form = UserCreationForm()
    form2 = DoctorForm()
    if  request.method == "POST":
        form = UserCreationForm(request.POST or None)
        form2 = DoctorForm(request.POST or None, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            form.save()
            newDoctor=form2.save(commit=False)
            newDoctor.user = get_object_or_404(
                User, username=form.cleaned_data['username'])
            newDoctor.save()
        return redirect("show_doctors")
    context = {
        "title": "اضف استاذ",
        "form":form,
        "form2":form2,
        
    }
    return render(request, "dashboard/add_doctor.html", context)

@login_required(redirect_field_name='next')
def update_doctor(request,id):
    doctor = get_object_or_404(Doctor, id=id)
    form = UserNameForm(instance=doctor.user)
    form2 = DoctorForm(instance=doctor)
    if "update_info" in request.POST:
        form = UserNameForm(request.POST or None,request.FILES or None, instance=doctor.user)
        form2 = DoctorForm(request.POST or None,request.FILES or None, instance=doctor)
        
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
    
    if "delete" in request.POST:
        doctor.user.delete()
        return redirect("show_doctors")
    
    context = {
        "title": f"تعديل الاستاذ",
        "doctor": doctor,
        "form":form,
        "form2":form2,
    }
    return render(request, "dashboard/update_doctor.html",context)







#Department CRUD
@login_required(redirect_field_name='next')
def department(request):
    form = DepartmentForm()
    departments = Department.objects.all()
    if "add_department" in request.POST:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()

    elif "delete_department" in request.POST:
        department = Department.objects.get(id=request.POST.get("department_id"))
        department.delete()
        

    context = {
        "title": f"ادارة الاقسام",
        "form":form,
        "departments":departments,
    }
    return render(request, "dashboard/department.html",context)


#Home CRUD
@login_required(redirect_field_name='next')
def edit_home(request):
    home=Home.objects.get(id=1)
    homeform = HomeForm(instance=home)
    degrees = Degree.objects.all()
    if "update_home" in request.POST:
        homeform = HomeForm(request.POST, request.FILES, instance=home)
        if homeform.is_valid():
            homeform.save()
    elif "update_degree" in request.POST:
        degree = Degree.objects.get(id=request.POST.get("id_degrees"))
        degree.Celsius = request.POST.get("degree_value")
        degree.save()
        
    context = {
        "title": f"ادارة الصفحة الرئسية",
        "homeform": homeform,
        "degrees":degrees,
    }
    return render(request, "dashboard/edit_home.html",context)


#ASK CRUD
@login_required(redirect_field_name='next')
def show_asks(request):
    qs = Ask.objects.all().order_by("-created")
    context = {
        "title": f"الاسئلة",
        "qs":qs,
    }
    return render(request, "dashboard/show_asks.html",context)

@login_required(redirect_field_name='next')
def answer_ask(request,id):
    ask = get_object_or_404(Ask, id=id)
    form=AnswerAskForm(instance=ask)
    if "answer_ask" in request.POST:
        form = AnswerAskForm(request.POST, instance=ask)
        if form.is_valid():
            form.save()
            return redirect("show_asks")
    
    if "delete_ask" in request.POST:
        ask.delete()
        return redirect("show_asks")

    context = {
        "title": f"اجاب",
        "ask":ask,
        "form":form,
    }
    return render(request, "dashboard/answer_ask.html",context)



#Lecture CRUD
@login_required(redirect_field_name='next')
def show_lectures(request):
    lectures = Lecture.objects.all().order_by("-created")
    context = {
        "title": f"المحاضرات",
        "lectures": lectures,
    }
    return render(request, "dashboard/show_lectures.html",context)


@login_required(redirect_field_name='next')
def add_lecture(request):
    form = LectureForm()
    if request.method == "POST":
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_lectures")

    context = {
        "title": f"اضف محاضرة",
        "form":form,
    }
    return render(request, "dashboard/add_lecture.html",context)


@login_required(redirect_field_name='next')
def update_lecture(request,id):
    lecture = get_object_or_404(Lecture, id=id)
    form = LectureForm(instance=lecture)
    if "update_lecture" in request.POST:
        form = LectureForm(request.POST or None,request.FILES or None , instance=lecture)
        if form.is_valid():
            form.save()
            return redirect("show_lectures")
    
    if "delete_lecture" in request.POST:
        lecture.delete()
        return redirect("show_lectures")
    
    context = {
        "title": f"تعديل الخبر",
        "form":form,
        "lecture":lecture
        
    }
    return render(request, "dashboard/update_lecture.html",context)



#CURD RESULTS