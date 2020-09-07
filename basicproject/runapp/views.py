from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def date(request):
    return HttpResponse("<h1>Hello sir the time is  "+str(datetime.datetime.now()))
