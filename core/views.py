from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,template_name='core/index.html')

def about(request):
    return render(request,template_name='core/aboutus.html')

def services(request):
    return render(request,template_name='core/services.html')

def contact(request):
    return render(request,template_name='core/contact.html')

def error_404_handler(request,exception):
    return render(request,template_name='404.html',status=404)