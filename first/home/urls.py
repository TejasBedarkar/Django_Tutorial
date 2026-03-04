from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    # link to details page in all_members.html and create details view and details.html page
    path('about/details/<int:id>', views.details, name='details'),
    path("services", views.services, name="services"),
    
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("logout", views.logout_view, name="logout"),
    
]
