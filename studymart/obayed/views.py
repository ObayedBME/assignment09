from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
    return render(request, 'obayed/course.html')

def Data_Science(request):
    Available_course = {'fcourse':['ML','DL','DA','DJ','Py']}
    return render(request, 'obayed/Data_Science.html',Available_course)

def Big_Data(request):
    return render(request, 'obayed/Big_Data.html')

def Data_analytics(request):
    return render(request, 'obayed/Data_analytics.html')

def Deep_Learning(request):
    return render(request,'obayed/deeplearning.html')
