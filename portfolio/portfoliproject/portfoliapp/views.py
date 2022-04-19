from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def project(request):
    return  render(request,'projects.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')