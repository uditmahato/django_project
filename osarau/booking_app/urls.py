from django.urls import path
from booking_app import views

urlpatterns = [
    path('book',views.book)
]
