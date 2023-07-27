from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_first(request):
    return render(request,'app2_first.html')

def app2_second(request):
    return render(request,'app2_second.html')

def app2_string(request):
    return HttpResponse('<h1><i>This is app2 string response</i></h2>')