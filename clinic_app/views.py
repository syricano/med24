from django.shortcuts import render
from django.http import HttpResponse

def core_app(request):
    return HttpResponse("Hello")