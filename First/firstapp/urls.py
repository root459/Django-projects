from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('',views.index,name='home' ),
    path('aboutus',views.aboutus,name="aboutus"),
    path('contactus',views.contactus,name="contactus")
]