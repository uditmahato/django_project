from django.shortcuts import render

from main_app.models import Todo

# Create your views here.
def home(request):
    Todo_list=Todo.objects.all()
    return render(request,'index.html',{"todos":Todo_list})

def add(request):
    if request.method=="GET":
        return render(request,'add.html')
    else:
        title=request.POST.get('title')
        description=request.POST.get('description')
        Todo.objects.create(title=title,description=description)
        return home(request)


