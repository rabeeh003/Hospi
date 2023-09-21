from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('doctor/', views.doctor,name="doctor"),
    path('booking/', views.booking,name="booking"),
    path('department/', views.department,name="department"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
]
