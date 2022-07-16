from django.shortcuts import render
import datetime
# Create your views here.
def about(request):
    p=about.objects.all()
    print(p)
    a=datetime.datetime.now()
    return render(request, 'about/index.html',{'title':'udit','date':a})

