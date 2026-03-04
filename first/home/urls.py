from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    # link to details page in all_members.html and create details view and details.html page
    path('about/details/<int:id>', views.details, name='details'),
    path("services", views.services, name="services"),
]
