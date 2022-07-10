from django.urls import path
from about_app import views

urlpatterns = [
    path('about',views.about),
]
