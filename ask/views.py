from django.shortcuts import render
from django.contrib import messages
from .models import Ask
from .forms import AskForm
# Create your views here.
def ask(request):
    asks = Ask.objects.filter(show=True)
    if request.method=="POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            messages.success(
                request, f'تهانينا {name} لقد تم وصول رسالتك/ي   بنجاح.')
            form = AskForm()
            
    else:
        form = AskForm()
    
    context={
        "title": "اسأل",
        "form":form,
        "asks":asks,
        
    }
    return render(request,"ask/ask.html",context)