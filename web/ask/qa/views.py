# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse("OK %s" % kwargs["num"])
