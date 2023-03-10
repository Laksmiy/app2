from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pavan(request):
    return HttpResponse('<h1>my name is pavan</h1>')


