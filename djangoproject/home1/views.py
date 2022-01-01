from django.shortcuts import render
from django.http import HttpResponse
from subprocess import check_output

def index(request):
    return HttpResponse("This is the home page.")

def list(request):
    return HttpResponse("this is a list")

def ipconfig(request):
    text = check_output(['ipconfig'])
    return HttpResponse(text)

def cpu_usage(request):
    text = check_output(["wmic", "cpu", "get", "loadpercentage"])
    return HttpResponse(text)