from main_app import views
from django.urls import path
urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
]
