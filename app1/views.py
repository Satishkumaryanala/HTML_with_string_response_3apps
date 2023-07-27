from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(request):
    return render(request,'app1_first.html')

def app1_second(request):
    return render(request,'app1_second.html')

def app1_string(request):
    return HttpResponse('<h1><i>This is app1 string response</i></h1>')