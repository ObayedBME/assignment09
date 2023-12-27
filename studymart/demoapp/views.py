from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_file(request):
    return render(request,'demoapp/add_file.html')
def subtract_file(request):
    return render(request,'demoapp/subtract_file.html')