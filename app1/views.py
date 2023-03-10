from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mounika(request):
    return HttpResponse('<h1>my name is mounikasir!<h1>')
