from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app3_first(request):
    return render(request,'app3_first.html')

def app3_second(request):
    return render(request,'app3_second.html')

def app3_string(request):
    return HttpResponse('<h2><i>This is App3 string response</i></h2>')