from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.


def google(request):
    return render(request,"google.html",{})

def success(request):
    return render(request,"success.html",{})


