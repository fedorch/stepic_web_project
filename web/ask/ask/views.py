# from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.


def not_found(request):
    return HttpResponseNotFound("Not Found!")
