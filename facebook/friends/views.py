from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("""
#     <!DOCTYPE html>
#     <head>
#         <title>Home Page </title>
#     </head>
#     <body>
#         <h1>Welcome to our Page</h1>
#         <p>World is scamming you ,Be alert</p>
#     </body>
#     </html>
#     """) 

def home(request):
    return render(request,'home.html')
def about(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <head>
        <title>About Page </title>
    </head>
    <body>
        <h1>We are kitabcorner</h1>
        <p>Leading book company</p>
    </body>
    </html>
    """) 