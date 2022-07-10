
from django.contrib import admin
from django.urls import path,include
from friends import views 
urlpatterns = [
    path('home/', views.home),
    path('about/',views.about)
]
