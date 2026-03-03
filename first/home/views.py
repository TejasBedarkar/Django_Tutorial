from django.shortcuts import render, HttpResponse
from django.template import loader


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
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def services(request):
    return HttpResponse("This is services page")