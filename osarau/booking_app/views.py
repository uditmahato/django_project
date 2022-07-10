from django.shortcuts import render

# Create your views here.
def book(request):
    return render(request, 'book/index.html')
