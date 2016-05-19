# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def found(request):
    return HttpResponse("Found!")


def not_found(request):
    return HttpResponseNotFound("Not Found!")
