from django.shortcuts import render
import datetime
from about_app.models import about_t
# Create your views here.
def about(request):
    # p=about_t.objects.filter(first_name='udit')
    # print(p)
    p=about_t.objects.all()
    print('**********************')
    for a in p:
        print(a.first_name)
    a=datetime.datetime.now()
    return render(request, 'about/index.html',{'title':'udit','date':a})

