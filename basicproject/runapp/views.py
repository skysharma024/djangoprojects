from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def date(request):
    return render(request,"runapp/first.html")
