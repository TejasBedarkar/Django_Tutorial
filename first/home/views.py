from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Home

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    context = {
        'variable1': "this is sent",
        'variable2': "this is also sent",
    }
    return render(request, 'index.html', context)
    
def about(request):
    # return HttpResponse("This is about page")
    
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    
    #to see data on web page
  mymembers = Home.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))  

# Add link to details page in all_members.html and create details view and details.html page
def details(request, id):
  mymember = Home.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request)) 
    

def services(request):
    return HttpResponse("This is services page")

def home(request):
  mymembers = Home.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


# For Authentication
def register_view(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request, user)
      return redirect("dashboard")
  else:
    initial_data = {
      'username': '',
      'password1': '',
      'password2': ''
    }
    form = UserCreationForm(initial=initial_data)
    
  return render(request, 'auth/register.html', {'form': form})



                        
def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user=form.get_user()
      login(request, user)
      return redirect("dashboard")
  else:
    initial_data = {
      'username': '',
      'password': ''
    }
    form = AuthenticationForm(initial=initial_data)
    
  return render(request, 'auth/login.html', {'form': form})





def dashboard_view(request):
  return render(request, 'dashboard.html')







def logout_view(request):
  logout(request)
  return redirect("login")