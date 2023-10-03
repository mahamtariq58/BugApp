from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def myname(request):
    return HttpResponse("<h1> Hello World </h> !")