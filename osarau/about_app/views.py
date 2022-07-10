from django.shortcuts import render
import datetime
# Create your views here.
def about(request):
    a=datetime.datetime.now()
    return render(request, 'about/index.html',{'title':'udit','date':a})

