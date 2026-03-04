from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Home


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